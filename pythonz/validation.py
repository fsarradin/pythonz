class Validation(object):
    """Validation e a"""

    def isSuccess(self):
        pass

    def isFailure(self):
        return not self.isSuccess()

    def get(self):
        pass

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

    def isSuccess(self):
        return True

    def get(self):
        return self.__value

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
        if f.isSuccess():
            return f.get()(self.__value)
        else:
            return f

    def append(self, other):
        if other.isSuccess():
            return Success(self.__value + other.__value)
        else:
            return other

    def __add__(self, other):
        return self.append(other)

    def __eq__(self, other):
        return other.__class__ == self.__class__ and other.__value == self.__value


class Failure(Validation):
    def __init__(self, value):
        self.__value = value

    def isSuccess(self):
        return False

    def get(self):
        raise ValueError

    def swap(self):
        return Success(self.__value)

    def map(self, f):
        return self

    def flatmap(self, f):
        return self

    def fold(self, z, f):
        return z

    def ap(self, f):
        if f.isSuccess():
            return self
        else:
            return Failure(self.__value + f.__value)

    def append(self, other):
        if other.isSuccess():
            return self
        else:
            return Failure(self.__value + other.__value)

    def __add__(self, other):
        return self.append(other)

    def __eq__(self, other):
        return other.__class__ == self.__class__ and other.__value == self.__value
