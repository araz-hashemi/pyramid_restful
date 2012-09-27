try:
    import simplejson as json
except ImportError:
    import json

from pyramid.renderers import JSONP as JSONPBase


class JSONP(JSONPBase):

    def __call__(self, info):
        def _render(value, system):
            request = system['request']
            context = system['context']

            if request.response.status_int == 200:
                value['status'] = {'code': 200, 'message': 'OK'}
            else:
                value = {'status': value}

            default = self._make_default(request)
            val = self.serializer(value, default=default, **self.kw)
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
