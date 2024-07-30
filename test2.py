from collections.abc import Callable

class Foo:
    name = 'sssss'

    @staticmethod
    def dec(func: Callable):
        def wrapper(cls, *args, **kwargs)-> int:
            a = 12
            res = func(cls, a, *args, **kwargs)
            return res

        return wrapper


    @classmethod
    @dec
    def foo(cls, first, second)-> int:
        print(cls.name)
        return first * second

    @staticmethod
    @dec
    def bar(first, second)-> int:
        return first + second

print('hello, {}'.format('Vasya'))

print(Foo.foo(7))
print(Foo.bar(14))
