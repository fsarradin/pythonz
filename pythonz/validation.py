class Validation(object):
    """Validation e a"""

    def is_success(self):
        pass

    def is_failure(self):
        return not self.is_success()

    def swap(self):
        """append :: Validation e a -> Validation a e"""
        pass

    def map(self, f):
        """map :: (a -> b) -> Validation b"""
        pass

    def flatmap(self, f):
        """flatmap :: (a -> Validation b) -> Validation b"""
        pass

    def foreach(self, f):
        """foreach :: (a -> ()) -> ()"""
        pass

    def fold(self, z, f):
        """append :: b -> (b -> a -> b) -> b"""
        pass

    def ap(self, f):
        """ap :: Validation e (a -> b) -> Validation e b"""
        pass

    def append(self, other):
        """append :: Validation e a -> Validation e a"""
        pass


class Success(Validation):
    def __init__(self, value):
        self.__value = value

    def is_success(self):
        return True

    def swap(self):
        return Failure(self.__value)

    def map(self, f):
        return Success(f(self.__value))

    def flatmap(self, f):
        return f(self.__value)

    def foreach(self, f):
        f(self.__value)

    def fold(self, z, f):
        return f(z, self.__value)

    def ap(self, f):
        if f.is_success():
            return f.__value(self.__value)
        else:
            return f

    def append(self, other):
        if other.is_success():
            return Success(self.__value + other.__value)
        else:
            return other

    def __add__(self, other):
        return self.append(other)

    def __repr__(self):
        return "Success(%s)" % repr(self.__value)

    def __hash__(self):
        return hash(self.__class__) ^ hash(self.__value)

    def __eq__(self, other):
        return other.__class__ == self.__class__ and other.__value == self.__value

    def __iter__(self):
        yield self.__value


class Failure(Validation):
    def __init__(self, value):
        self.__value = value

    def is_success(self):
        return False

    def swap(self):
        return Success(self.__value)

    def map(self, f):
        return self

    def flatmap(self, f):
        return self

    def fold(self, z, f):
        return z

    def ap(self, f):
        if f.is_success():
            return self
        else:
            return Failure(self.__value + f.__value)

    def append(self, other):
        if other.is_success():
            return self
        else:
            return Failure(self.__value + other.__value)

    def __add__(self, other):
        return self.append(other)

    def __repr__(self):
        return "Success(%s)" % repr(self.__value)

    def __hash__(self):
        return hash(self.__class__) ^ hash(self.__value)

    def __eq__(self, other):
        return other.__class__ == self.__class__ and other.__value == self.__value

    def __iter__(self):
        yield from ()
