from json import dumps
from pyramid.httpexceptions import HTTPError
from pyramid.request import Response


class JSONError(HTTPError):
    """
    Error Response
    Implement with:
        # TODO doublecheck import
        from errors import JSONError
        config.add_view(JSONError, context=HTTPError)
    """

    _error_status_codes = {
        400: {'message': 'Bad Request'},
        401: {'message': 'Unauthorized'},
        402: {'message': 'Payment Required'},
        403: {'message': 'Forbidden'},
        404: {'message': 'Not Found'},
        405: {'message': 'Method Not Allowed'},
        406: {'message': 'Not Acceptable'},
        407: {'message': 'Proxy Authentication Required'},
        408: {'message': 'Request Timeout'},
        409: {'message': 'Conflict'},
        410: {'message': 'Gone'},
        411: {'message': 'Length Required'},
        412: {'message': 'Precondition Failed'},
        413: {'message': 'Request Entity Too Large'},
        414: {'message': 'Request-URI Too Long'},
        415: {'message': 'Unsupported Media Type'},
        416: {'message': 'Request Range Not Satisfiable'},
        417: {'message': 'Expectation Failed'},
        422: {'message': 'Unprocessable Entity'},
        423: {'message': 'Locked'},
        424: {'message': 'Failed Dependency'},
        500: {'message': 'Internal Server Error'},
        501: {'message': 'Not Implemented'},
        502: {'message': 'Bad Gateway'},
        503: {'message': 'Service Unavailable'},
        504: {'message': 'Gateway Timeout'},
        505: {'message': 'HTTP Version Not Supported'},
        507: {'message': 'Insufficient Storage'}
        }

    def __init__(self, exc, req):
        self.exc = exc
        self.req = req
        super(RestError, self).__init__()

    # TODO: pass in environ and start_request as in super()__call__()?
    #       and use prepare?
    def __call__(self):
        if self.req.exception.code not in self._error_status_codes:
            # TODO: make sure we have adequate handling? or allow a 500?
            #super(RestError,self).__call__(self.req.environ, self.req???)
            raise self.exc
        response_dict = {
            'code': self.exc.code,
            'message': self.exc.explanation
        }
        response = Response(dumps(response_dict))
        response.status_int = self.exc.code
        return response
