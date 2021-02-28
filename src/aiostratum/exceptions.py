class StratumException(Exception):
    pass


class ProtocolException(StratumException):
    pass


class TransportException(StratumException):
    pass


class ServiceException(StratumException):
    code = -2


class UnauthorizedException(ServiceException):
    pass


class SignatureException(ServiceException):
    code = -21


class PubsubException(ServiceException):
    pass


class AlreadySubscribedException(PubsubException):
    pass


class IrcClientException(StratumException):
    pass


class SigningNotAvailableException(SignatureException):
    code = -21


class UnknownSignatureIdException(SignatureException):
    code = -22


class UnknownSignatureAlgorithmException(SignatureException):
    code = -22


class SignatureVerificationFailedException(SignatureException):
    code = -23


class MissingServiceTypeException(ServiceException):
    code = -2


class MissingServiceVendorException(ServiceException):
    code = -2


class MissingServiceIsDefaultException(ServiceException):
    code = -2


class DefaultServiceAlreadyExistException(ServiceException):
    code = -2


class ServiceNotFoundException(ServiceException):
    code = -2


class MethodNotFoundException(ServiceException):
    code = -3


class FeeRequiredException(ServiceException):
    code = -10


class TimeoutServiceException(ServiceException):
    pass


class RemoteServiceException(StratumException):
    pass
