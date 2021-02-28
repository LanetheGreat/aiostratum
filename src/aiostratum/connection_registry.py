import weakref
from twisted.internet import reactor

from .services import GenericService


class RegistryMeta(type):

    def __iter__(cls):  # @NoSelf
        yield from cls._connections.keyrefs()


class ConnectionRegistry(metaclass=RegistryMeta):
    _connections = weakref.WeakKeyDictionary()

    @classmethod
    def add_connection(cls, conn):
        cls._connections[conn] = True

    @classmethod
    def remove_connection(cls, conn):
        try:
            del cls._connections[conn]
        except Exception:
            print('Warning: Cannot remove connection from ConnectionRegistry')

    @classmethod
    def get_session(cls, conn):
        if isinstance(conn, weakref.ref):
            conn = conn()

        if isinstance(conn, GenericService):
            conn = conn.connection_ref()

        if conn is None:
            return None

        return conn.get_session()


def dump_connections():
    for x in ConnectionRegistry:
        conn = x()
        conn.transport.write('cus')
        print('!!!', conn)
    reactor.callLater(5, dump_connections)


reactor.callLater(0, dump_connections)
