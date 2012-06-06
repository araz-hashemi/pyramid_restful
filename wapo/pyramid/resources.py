

class Resource(object):
    __name__ = None
    __parent__ = None
    __children__ = None

    def __init__(self, parent=None, name=None):
        self.__name__ = name
        self.__parent__ = parent

    def __getitem__(self, key):
        if isinstance(self.__children__, dict):
            return self.__children__[key](self, key)
        elif self.__children__ is None:
            raise KeyError
        elif isinstance(self.__children__, object):
            return self.__children__(self, key)
        raise KeyError
