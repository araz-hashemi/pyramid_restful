import logging
from pyramid.httpexceptions import HTTPError
from pyramid.view import view_config

log = logging.getLogger(__name__)

class RestError(HTTPError):
    """
    Error Response
    """
    
    status_codes = {
        400:'Bad Request',
        401:'Unauthorized',
        402:'Payment Required',
        403:'Forbidden',
        404:'Not Found',
        405:'Method Not Allowed',
        406:'Not Acceptable',
        407:'Proxy Authentication Required',
        408:'Request Timeout',
        409:'Conflict',
        410:'Gone',
        411:'Length Required',
        412:'Precondition Failed',
        413:'Request Entity Too Large',
        414:'Request-URI Too Long',
        415:'Unsupported Media Type',
        416:'Request Range Not Satisfiable',
        417:'Expectation Failed',
        422:'Unprocessable Entity',
        423:'Locked',
        424:'Failed Dependency',
        500:'Internal Server Error',
        501:'Not Implemented',
        502:'Bad Gatewate',
        503:'Service Unavailable',
        504:'Gateway Timeout',
        505:'HTTP Version Not Supported',
        507:'Insufficient Storage'
        }
                     
    # SPM - This may need to be an __init__
    def __call__(self, status, message=None, sub_code=None, body_template=None):
        if status not in allowed_codes:
            raise ValueError, 'status code not permitted'
        
        self.status = status
        self.title = status_codes.get('status')
        self.explanation = message
        self.sub_code = code
        self.body_template = body_template

    def prepare(self, environ):
        """
        Prepares the response for being called as a WSGI application \
        (see pyramid.interfaces)
        """
        #TODO:
        #self.app_iter = [???]
        #self.body = ???
        pass