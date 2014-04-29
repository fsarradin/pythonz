class Maybe(object):
    def is_defined(self):
        pass

    def get(self):
        pass

    def map(self, f):
        pass

    def flatmap(self, f):
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

    def get(self):
        return self.__value

    def map(self, f):
        return Maybe.pure(f(self.__value))

    def flatmap(self, f):
        return f(self.__value)

    def __repr__(self):
        return "Just(%s)" % self.__value

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.__value == other.__value


class _Nothing(Maybe):
    def is_defined(self):
        pass

    def get(self):
        raise ValueError

    def map(self, f):
        return self

    def flatmap(self, f):
        return self

    def __repr__(self):
        return "Nothing"

    def __eq__(self, other):
        return self.__class__ == other.__class__


Nothing = _Nothing()

