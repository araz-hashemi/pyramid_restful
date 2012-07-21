

class Resource(object):
    __name__ = None
    __parent__ = None

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


class Element(Resource):
    """Represents an individual resource.

    If the Element has any children, they should be defined in the children
    dict, i.e.:
    __children__ = {'child1name': Child1Class,
                    'child2name': Child2Class}
    """
    __children__ = None

    def __getitem__(self, key):
        if isinstance(self.__children__, dict):
            return self.__children__[key](self, key)
        raise KeyError


class Collection(Resource):
    """Represents a collection of a single type of element.

    The child class of the collection is represented as the
    __child__ attribute.
    """
    __child__ = None

    def __getitem__(self, key):
        return self.__child__(self, key)
