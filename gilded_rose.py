import dataclasses
import operator
import typing
from abc import ABC, abstractmethod

Transformer = typing.Callable[[int], int]


class Pipe:
    def __init__(self, *funcs):
        self.head, *self.tail = funcs

    def __call__(self, *args, **kwargs):
        ret = self.head(*args, **kwargs)
        for f in self.tail:
            ret = f(ret)
        return ret

    def __iter__(self):
        yield self.head
        yield from self.tail

    def __repr__(self):
        return '[' + '; '.join(str(f) for f in self) + ']'


class BindRight:
    def __init__(self, op, *bound_args):
        self.op = op
        self.bound_args = bound_args

    def __call__(self, *args):
        return self.op(*args, *self.bound_args)

    def __repr__(self):
        return f'{self.op.__name__}(' + ', '.join(str(a) for a in self.bound_args) + ')'


class Clamp:
    def __init__(self, minimum, maximum):
        self.minimum, self.maximum = minimum, maximum

    def __call__(self, arg):
        return max(min(arg, self.maximum), self.minimum)

    def __repr__(self):
        return f'clamp({self.minimum}, {self.maximum})'


class Identity:
    def __call__(self, arg):
        return arg

    def __repr__(self):
        return 'identity'


identity = Identity()


class Constant:
    def __init__(self, v):
        self.v = v

    def __call__(self, *args, **kwargs):
        return self.v

    def __repr__(self):
        return f'constant({self.v})'


clamp_quality = Clamp(0, 50)


def clamped(transformer: Transformer) -> Transformer:
    return Pipe(transformer, clamp_quality)


def add(n):
    return BindRight(operator.add, n)


@dataclasses.dataclass
class Item:
    name: str
    sell_in: int
    quality: int


class Factory(ABC):
    @abstractmethod
    def sell_in_transformer(self, item: Item) -> Transformer:
        ...

    @abstractmethod
    def quality_transformer(self, item: Item) -> Transformer:
        ...

    def transformers(self, item: Item) -> tuple[Transformer, Transformer]:
        return self.sell_in_transformer(item), self.quality_transformer(item)

    def __repr__(self):
        return str(type(self))


class SulfurasFactory(Factory):
    def sell_in_transformer(self, item: Item) -> Transformer:
        return identity

    def quality_transformer(self, item: Item) -> Transformer:
        return identity


class DefaultSellInFactory(Factory, ABC):
    def sell_in_transformer(self, item: Item) -> Transformer:
        return add(-1)


class DefaultFactory(DefaultSellInFactory):
    def __init__(self, on_positive_sell_in: Transformer, on_non_positive_sell_in: Transformer):
        self.on_positive_sell_in = on_positive_sell_in
        self.on_non_positive_sell_in = on_non_positive_sell_in

    def quality_transformer(self, item: Item) -> Transformer:
        return clamped(self.on_positive_sell_in if item.sell_in > 0 else self.on_non_positive_sell_in)


class BackstagePassFactory(DefaultSellInFactory):
    def quality_transformer(self, item: Item) -> Transformer:
        if item.sell_in <= 0:
            return Constant(0)

        amount = (3 if 1 <= item.sell_in <= 5 else
                  2 if 6 <= item.sell_in <= 10 else
                  1)
        return clamped(add(amount))


AGED_BRIE = "Aged Brie"
BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"
CONJURED = "Conjured Mana Cake"

TRANSFORMER_FACTORIES = {
    SULFURAS: SulfurasFactory(),
    AGED_BRIE: DefaultFactory(on_positive_sell_in=add(+1), on_non_positive_sell_in=add(+2)),
    BACKSTAGE_PASS: BackstagePassFactory(),
    CONJURED: DefaultFactory(on_positive_sell_in=add(-2), on_non_positive_sell_in=add(-4)),
}

DEFAULT_FACTORY = DefaultFactory(on_positive_sell_in=add(-1), on_non_positive_sell_in=add(-2))


def printing_transformer(transformer: Transformer) -> Transformer:
    def result(value: int) -> int:
        new_value = transformer(value)
        print(f'({value}) -[ {transformer} ]-> ({new_value})')
        return new_value

    return result


def update_item(item: Item) -> None:
    factory = TRANSFORMER_FACTORIES.get(item.name, DEFAULT_FACTORY)
    transform_sell_in, transform_quality = factory.transformers(item)

    if False:
        transform_sell_in, transform_quality = tuple(
            printing_transformer(t) for t in (transform_sell_in, transform_quality))

    item.sell_in = transform_sell_in(item.sell_in)
    item.quality = transform_quality(item.quality)


def update_quality(items: typing.Iterable[Item]) -> None:
    for item in items:
        update_item(item)
