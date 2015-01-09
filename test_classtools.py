import gc

from classtools import classproperty
from classtools import frozenproperty
from classtools import keyed_ordering
from classtools import reify
from classtools import weakattr


def test_classproperty():
    class Square(object):
        @classproperty
        def num_sides(cls):
            return 4

    assert Square.num_sides == 4
    assert Square().num_sides == 4

    # Should always get the class as an argument
    class Reflector(object):
        @classproperty
        def me(cls):
            return cls

    assert Reflector.me is Reflector
    assert Reflector().me is Reflector


def test_reify():
    class Lazy(object):
        @reify
        def attr(self):
            return []

    assert isinstance(Lazy.attr, reify)

    lazy = Lazy()
    value = lazy.attr
    assert value == []
    assert lazy.attr is value
    lazy.attr.append(3)
    assert lazy.attr == [3]
    del lazy.attr
    assert lazy.attr == []
    assert value == [3]
    assert lazy.attr is not value


def test_weakattr():
    class Foo(object):
        bar = weakattr('bar')

        def __init__(self, bar):
            self.bar = bar

    class Dummy(object):
        pass

    obj = Dummy()
    foo = Foo(obj)
    assert foo.bar is obj
    del foo.bar
    assert foo.bar is None

    foo = Foo(obj)
    assert foo.bar is obj
    del obj
    # PyPy reserves the right to delete objects whenever; encourage it
    gc.collect()
    assert foo.bar is None


def test_frozenproperty():
    class Cat(object):
        @frozenproperty
        def num_legs(self):
            return 2 + 2

    assert isinstance(Cat.num_legs, frozenproperty)

    cat = Cat()
    assert cat.num_legs == 4
    cat.num_legs = 5
    assert cat.num_legs == 5


def test_keyed_ordering():
    @keyed_ordering
    class NeedlesslyComplicatedPoint(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __key__(self):
            return (self.x, self.y)

    p = NeedlesslyComplicatedPoint(1, 3)
    q = NeedlesslyComplicatedPoint(2, 0)

    assert p == p
    assert q == q
    assert p != q
    assert q != p

    assert p < q
    assert p <= q
    assert p <= p

    assert q > p
    assert q >= p
    assert q >= q

    assert p != (p.x, p.y)
