def Typeclass():
    class _Typeclass(object):
        registered_class = {}

        @classmethod
        def instance_for(cls, object_type):
            def wrapper(instance_cls):
                cls.registered_class[object_type] = instance_cls()
                return instance_cls

            return wrapper

        @classmethod
        def get_instance_for(cls, obj):
            def findFor(object_type):
                for instance_cls in cls.registered_class.keys():
                    if issubclass(object_type, instance_cls):
                        return instance_cls
                return None

            return cls.registered_class[findFor(obj.__class__)]

    return _Typeclass
