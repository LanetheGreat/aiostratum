def setup(setup_event=None):
    try:
        from twisted.internet import epollreactor
        epollreactor.install()
    except ImportError:
        print('Failed to install epoll reactor, default reactor will be used instead.')

    try:
        from . import settings
    except ImportError:
        print('***** Is config.py missing? Maybe you want to copy and customize the top portion on settings.py?')

    from twisted.application import service
    application = service.Application('aiostratum-server')

    if settings.ENABLE_EXAMPLE_SERVICE:
        from . import example_service  # @UnusedImport

    if setup_event is None:
        setup_finalize(None, application)
    else:
        setup_event.addCallback(setup_finalize, application)

    return application


def setup_finalize(event, application):
    import OpenSSL.SSL
    from twisted.application import internet
    from twisted.internet import reactor, ssl
    from twisted.python import log
    from twisted.web.server import Site

    from . import http_transport
    from . import irc
    from . import socket_transport
    from . import websocket_transport
    from . import settings
    from .services import ServiceEventHandler

    try:
        from . import signature
        signing_key = signature.load_privkey_pem(settings.SIGNING_KEY)
    except Exception:
        print("Loading of signing key '%s' failed, protocol messages cannot be signed." % settings.SIGNING_KEY)
        signing_key = None

    # Attach HTTPS Poll Transport service to application
    try:
        sslContext = ssl.DefaultOpenSSLContextFactory(settings.SSL_PRIVKEY, settings.SSL_CACERT)
    except OpenSSL.SSL.Error:
        sslContext = None
        print('Cannot initiate SSL context, are SSL_PRIVKEY or SSL_CACERT missing?')
        print('This will skip all SSL-based transports.')

    # Set up thread pool size for service threads
    reactor.suggestThreadPoolSize(settings.THREAD_POOL_SIZE)

    if settings.LISTEN_SOCKET_TRANSPORT:
        # Attach Socket Transport service to application
        socket = internet.TCPServer(
            settings.LISTEN_SOCKET_TRANSPORT,
            socket_transport.SocketTransportFactory(
                debug=settings.DEBUG,
                signing_key=signing_key,
                signing_id=settings.SIGNING_ID,
                event_handler=ServiceEventHandler,
                tcp_proxy_protocol_enable=settings.TCP_PROXY_PROTOCOL,
            )
        )
        socket.setServiceParent(application)

    # Build the HTTP interface
    httpsite = Site(
        http_transport.Root(
            debug=settings.DEBUG,
            signing_key=signing_key,
            signing_id=settings.SIGNING_ID,
            event_handler=ServiceEventHandler,
        )
    )
    httpsite.sessionFactory = http_transport.HttpSession

    if settings.LISTEN_HTTP_TRANSPORT:
        # Attach HTTP Poll Transport service to application
        http = internet.TCPServer(settings.LISTEN_HTTP_TRANSPORT, httpsite)
        http.setServiceParent(application)

    if settings.LISTEN_HTTPS_TRANSPORT and sslContext:
        https = internet.SSLServer(settings.LISTEN_HTTPS_TRANSPORT, httpsite, contextFactory=sslContext)
        https.setServiceParent(application)

    if settings.LISTEN_WS_TRANSPORT:
        from autobahn.twisted.websocket import listenWS
        log.msg('Starting WS transport on %d' % settings.LISTEN_WS_TRANSPORT)
        ws = websocket_transport.WebsocketTransportFactory(
            settings.LISTEN_WS_TRANSPORT,
            debug=settings.DEBUG,
            signing_key=signing_key,
            signing_id=settings.SIGNING_ID,
            event_handler=ServiceEventHandler,
        )
        listenWS(ws)

    if settings.LISTEN_WSS_TRANSPORT and sslContext:
        log.msg('Starting WSS transport on %d' % settings.LISTEN_WSS_TRANSPORT)
        wss = websocket_transport.WebsocketTransportFactory(
            settings.LISTEN_WSS_TRANSPORT,
            is_secure=True,
            debug=settings.DEBUG,
            signing_key=signing_key,
            signing_id=settings.SIGNING_ID,
            event_handler=ServiceEventHandler,
        )
        listenWS(wss, contextFactory=sslContext)

    if settings.IRC_NICK:
        reactor.connectTCP(
            settings.IRC_SERVER,
            settings.IRC_PORT,
            irc.IrcLurkerFactory(
                settings.IRC_ROOM,
                settings.IRC_NICK,
                settings.IRC_HOSTNAME,
            )
        )

    return event


if __name__ == '__main__':
    print("This is not executable script. Try 'twistd -ny launcher.tac instead!")
