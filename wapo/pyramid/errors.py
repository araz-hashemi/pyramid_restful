"""Class to transform vanilla HTTP exceptions into JSON dictionaries.

Copyright 2012 WaPo Labs

[License]

Author: Brian Neumann <brian@wapolabs.com>
        Sean McBride <sean@wapolabs.com>
        Daniel Li <daniel@wapolabs.com>

This class transforms vanilla HTTP exceptions thrown by Pyramid into JSON
dictionaries that include information on the exceptions, such as a status
code and human-readable error message.  We created this class in order to
keep all of Trove API's responses as JSON dictionaries, even in the case
of HTTP exceptions.

"""

from json import dumps

from pyramid.httpexceptions import HTTPError
from pyramid.request import Response


class JSONError(HTTPError):
    """Class to transform vanilla HTTP exceptions into JSON dictionaries.

    This class transforms vanilla HTTP exceptions thrown by Pyramid into JSON
    dictionaries that include information on the exceptions, such as a status
    code and human-readable error message.  We created this class in order to
    keep all of Trove API's responses as JSON dictionaries, even in the case
    of HTTP exceptions.

    For more information on how Pyramid organizes HTTP exceptions, see the
    Pyramid narrative documentation:

        http://docs.pylonsproject.org/projects/pyramid/en/latest/api/
        httpexceptions.html

    """

    def __init__(self, exception, request):
        self.exc = exception
        self.request = request

        super(JSONError, self).__init__()

    def __call__(self):
        if not isinstance(self.request.exception, HTTPError):
            raise self.exc

        self.request.response.status_int = self.exc.code

        response_dict = {
            'code': self.exc.code,
            'message': self.exc.detail or self.exc.explanation
            }

        return response_dict
