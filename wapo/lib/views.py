from pyramid.httpexceptions import HTTPNotImplemented

# View
def items(request):
    try:
        op = getattr(request.context,request.method)
    except AttributeError:
        raise HTTPNotImplemented
    return op()


