from typing import Any


class BaseSingletonMixin:
    __instances: dict[Any, "BaseSingletonMixin"] = {}
    _initialized = False

    @classmethod
    def __new__(cls, *args: Any, **kwargs: Any) -> "BaseSingletonMixin":
        def _recursive_hashable(val: Any) -> Any | tuple[Any]:
            if isinstance(val, dict):
                return tuple((k, _recursive_hashable(v)) for k, v in sorted(val.items()))
            elif isinstance(val, list):
                return tuple(_recursive_hashable(item) for item in val)
            return val

        key = tuple(tuple(map(_recursive_hashable, item)) for item in (args, kwargs))
        if key not in cls.__instances:
            cls.__instances[key] = super().__new__(cls)
        return cls.__instances[key]

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        if not self._initialized:
            super().__init__(*args, **kwargs)
            self._initialized = True


# Test BaseSingletonMixin:


# class A(BaseSingletonMixin):
#     def __init__(self, dict_arg: Any, *args: Any, **kwargs: Any) -> None:
#         super().__init__(*args, **kwargs)
#         self.dict_arg = dict_arg


# some_dict = {"some_key": "some_value", "some_dict_value": {"some_key_1": "some_value_1", "some_key_2": "some_value_2"}}
# a = A(some_dict)

# some_dict["some_key"] = "not_a_some_value"
# some_dict["new_key"] = "new_value"
# b = A(some_dict)

# some_dict2 = {"some_dict_value": {"some_key_1": "some_value_1", "some_key_2": "some_value_2"}, "some_key": "some_value"}
# c = A(some_dict2)

# print(a is b)  # False
# print(a is c)  # True
