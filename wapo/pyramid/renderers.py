import logging

try:
    import simplejson as json
except ImportError:
    import json

from pyramid.renderers import JSONP as JSONPBase


log = logging.getLogger(__name__)

def printlog(msg):
    log.debug('\n[0;34m%s[0m' % repr(msg))


class JSONP(JSONPBase):

    def __call__(self, info):
        def _render(value, system):
            request = system['request']
            context = system['context']

            default = self._make_default(request)
            val = self.serializer(value, default=default, **self.kw)
            callback = request.GET.get(self.param_name)

            printlog(value)

            if callback is None:
                ct = 'application/json'
                body = val
            else:

                # --- Begin Trove API customizations ---

                val_obj = json.loads(val)
                if request.response.status_int == 200:
                    val_obj = {
                        'status': {'code': 200, 'message': 'OK'},
                        'value': val_obj,
                        }
                else:
                    val_obj = {'status': val_obj}
                val = json.dumps(val_obj)
                request.response.status_int = 200

                # --- End Trove API customizations ---

                ct = 'application/javascript'
                body = '%s(%s)' % (callback, val)
            response = request.response
            if response.content_type == response.default_content_type:
                response.content_type = ct
            return body
        return _render
