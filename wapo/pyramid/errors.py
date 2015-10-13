"""Class to handle transformations of HTTP exceptions into JSON dictionaries.

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

import logging

from pyramid.httpexceptions import HTTPException
from pyramid.httpexceptions import HTTPInternalServerError

log = logging.getLogger(__name__)


class JSONError(object):
    """View to render vanilla Pyramid HTTP exceptions as JSON dicts.

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
        self._exception = exception
        self._request = request

    def __call__(self):
        if not isinstance(self._exception, HTTPException):
            log.exception(self._exception)
            self._exception = HTTPInternalServerError()

        self._request.response.status_int = self._exception.code

        response_dict = {
            'code': self._exception.code,
            'message': self._exception.detail or self._exception.explanation,
        }

        return response_dict
