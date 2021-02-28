#!/usr/bin/env python

from twisted.internet import reactor
from twisted.python import log
from twisted.scripts.twistd import run

from . import settings
from .server import setup

# This variable is used as an application handler by twistd
application = setup()


def heartbeat():
    log.msg('heartbeat')
    reactor.callLater(60, heartbeat)


if settings.DEBUG:
    reactor.callLater(0, heartbeat)

# Load all services from service_repository module.
try:
    import service_repository  # @UnusedImport
except ImportError:
    print("***** Is service_repository missing? Add service_repository module to your python path!")

run()
