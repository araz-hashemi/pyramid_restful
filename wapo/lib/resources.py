
class Resource(object):
    __name__ = None
    __parent__ = None
    __children__ = None

    def __init__(self, parent = None, name = None):
        self.__name__ = name
        self.__parent__ = parent

    def __getitem__(self, key):
        if not self.__children__:
            raise KeyError
        return self.__children__(self, key)

