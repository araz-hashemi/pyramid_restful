try:
    import simplejson as json
except ImportError:
    import json

from pyramid.renderers import JSONP as JSONPBase


class JSONP(JSONPBase):
    """Wrap jsonp responses with parameterized callback.
    """

    def __call__(self, info):
        def _render(value, system):
            request = system['request']

            # Here we forcibly set the HTTP response status code to 200
            # regardless of the actual response code, which will be returned
            # in the 'status' field of the JSON dictionary that is returned.
            # For a comprehensive explanation of why we do this, see the
            # Guardian's article on their JSONP API design:
            #
            # http://www.guardian.co.uk/info/developer-blog/2012/jul/16/
            # http-status-codes-jsonp
            #
            if request.response.status_int == 200:
                value['status'] = {'code': 200, 'message': 'OK'}
            else:
                # the error class renders the code/message here
                value = {'status': value}

            val = json.dumps(value)
            callback = request.GET.get(self.param_name)

            if callback is None:
                ct = 'application/json'
                body = val
            else:
                ct = 'application/javascript'
                body = '%s(%s)' % (callback, val)
                request.response.status_int = 200
            response = request.response
            if response.content_type == response.default_content_type:
                response.content_type = ct
            return body
        return _render
