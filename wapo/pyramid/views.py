from pyramid.httpexceptions import HTTPNotImplemented


class RestfulView(object):

    def __init__(self, request):
        self.request = request
        self.op = None
        try:
            self.op = getattr(request.context, request.method)
        except AttributeError:
            self.op = None

    def __call__(self):
        if not self.op:
            raise HTTPNotImplemented
        return self.op(self.request)
