class Maybe(object):
    """Maybe a"""

    def is_defined(self):
        pass

    def get_or_else(self, default):
        """get_or_else :: a -> a"""
        pass

    def or_else(self, default):
        """or_else :: Maybe a -> Maybe a"""
        pass

    def map(self, f):
        """map :: (a -> b) -> Maybe b"""
        pass

    def flatmap(self, f):
        """flatmap :: (a -> Maybe b) -> Maybe b"""
        pass

    def foreach(self, f):
        pass

    def fold(self, z, f):
        """fold :: b -> (b -> a -> b) -> b"""
        pass

    @staticmethod
    def pure(value):
        if value is None:
            return Nothing
        else:
            return Just(value)


class Just(Maybe):
    def __init__(self, value):
        self.__value = value

    def is_defined(self):
        return True

    def get_or_else(self, default):
        return self.__value

    def or_else(self, default):
        return self

    def map(self, f):
        return Maybe.pure(f(self.__value))

    def flatmap(self, f):
        return f(self.__value)

    def foreach(self, f):
        f(self.__value)

    def fold(self, z, f):
        return f(z, self.__value)

    def __hash__(self):
        return hash(self.__class__) ^ hash(self.__value)

    def __repr__(self):
        return "Just(%s)" % self.__value

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.__value == other.__value

    def __iter__(self):
        yield self.__value


class _Nothing(Maybe):
    def is_defined(self):
        pass

    def get_or_else(self, default):
        return default

    def or_else(self, default):
        return default

    def map(self, f):
        return self

    def flatmap(self, f):
        return self

    def fold(self, z, f):
        return z

    def __hash__(self):
        return hash(self.__class__)

    def __repr__(self):
        return "Nothing"

    def __eq__(self, other):
        return self.__class__ == other.__class__

    def __iter__(self):
        yield from ()


Nothing = _Nothing()

