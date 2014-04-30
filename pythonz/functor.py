from maybe import Maybe
from typeclass import Typeclass
from validation import Validation


class Functor(Typeclass()):
    def fmap(self, callable, functor):
        pass


@Functor.instance_for(Maybe)
class MaybeFunctor(Functor):
    def fmap(self, callable, functor):
        return functor.fmap(callable)


@Functor.instance_for(Validation)
class ValidationFunctor(Functor):
    def fmap(self, callable, functor):
        return functor.fmap(callable)


def fmap(callable, functor):
    return Functor.get_instance_for(functor).fmap(callable, functor)
