from twisted.internet import defer

from .exceptions import MethodNotFoundException
from .services import wrap_result_object


class GenericEventHandler:

    def _handle_event(self, msg_method, msg_params, connection_ref):
        return defer.maybeDeferred(wrap_result_object, self.handle_event(msg_method, msg_params, connection_ref))

    def handle_event(self, msg_method, msg_params, connection_ref):
        '''In most cases you'll only need to overload this method.'''
        print('Other side called method', msg_method, 'with params', msg_params)
        raise MethodNotFoundException("Method '%s' not implemented" % msg_method)
