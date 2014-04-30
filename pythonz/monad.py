from maybe import Maybe
from typeclass import Typeclass
from validation import Validation


class Monad(Typeclass()):
    def bind(self, callable, monad):
        pass

@Monad.instance_for(Maybe)
class MaybeMonad(Monad):
    def bind(self, callable, monad):
        return monad.bind(callable)

@Monad.instance_for(Validation)
class ValidationMonad(Monad):
    def bind(self, callable, monad):
        return monad.bind(callable)

def bind(callable, monad):
    return Monad.get_instance_for(monad).bind(callable, monad)
