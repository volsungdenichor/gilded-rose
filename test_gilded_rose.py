from gilded_rose import Item, update_quality


def test_update_item():
    item = Item("foo", sell_in=3, quality=50)
    assert (item.sell_in, item.quality) == (3, 50)

    update_quality([item])
    assert (item.sell_in, item.quality) == (2, 49)

    update_quality([item])
    assert (item.sell_in, item.quality) == (1, 48)

    update_quality([item])
    assert (item.sell_in, item.quality) == (0, 47)

    update_quality([item])
    assert (item.sell_in, item.quality) == (-1, 45)

    update_quality([item])
    assert (item.sell_in, item.quality) == (-2, 43)

    update_quality([item])
    assert (item.sell_in, item.quality) == (-3, 41)


def test_update_brie():
    item = Item("Aged Brie", sell_in=3, quality=45)
    assert (item.sell_in, item.quality) == (3, 45)

    update_quality([item])
    assert (item.sell_in, item.quality) == (2, 46)

    update_quality([item])
    assert (item.sell_in, item.quality) == (1, 47)

    update_quality([item])
    assert (item.sell_in, item.quality) == (0, 48)

    update_quality([item])
    assert (item.sell_in, item.quality) == (-1, 50)

    update_quality([item])
    assert (item.sell_in, item.quality) == (-2, 50)

    update_quality([item])
    assert (item.sell_in, item.quality) == (-3, 50)


def test_update_backstage_pass():
    item = Item("Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=10)
    assert (item.sell_in, item.quality) == (15, 10)

    update_quality([item])
    assert (item.sell_in, item.quality) == (14, 11)

    update_quality([item])
    assert (item.sell_in, item.quality) == (13, 12)

    update_quality([item])
    assert (item.sell_in, item.quality) == (12, 13)

    update_quality([item])
    assert (item.sell_in, item.quality) == (11, 14)

    update_quality([item])
    assert (item.sell_in, item.quality) == (10, 15)

    update_quality([item])
    assert (item.sell_in, item.quality) == (9, 17)

    update_quality([item])
    assert (item.sell_in, item.quality) == (8, 19)

    update_quality([item])
    assert (item.sell_in, item.quality) == (7, 21)

    update_quality([item])
    assert (item.sell_in, item.quality) == (6, 23)

    update_quality([item])
    assert (item.sell_in, item.quality) == (5, 25)

    update_quality([item])
    assert (item.sell_in, item.quality) == (4, 28)

    update_quality([item])
    assert (item.sell_in, item.quality) == (3, 31)

    update_quality([item])
    assert (item.sell_in, item.quality) == (2, 34)

    update_quality([item])
    assert (item.sell_in, item.quality) == (1, 37)

    update_quality([item])
    assert (item.sell_in, item.quality) == (0, 40)

    update_quality([item])
    assert (item.sell_in, item.quality) == (-1, 0)

    update_quality([item])
    assert (item.sell_in, item.quality) == (-2, 0)

    update_quality([item])
    assert (item.sell_in, item.quality) == (-3, 0)

    update_quality([item])
    assert (item.sell_in, item.quality) == (-4, 0)

    update_quality([item])
    assert (item.sell_in, item.quality) == (-5, 0)


def test_update_sulfuras():
    item = Item("Sulfuras, Hand of Ragnaros", sell_in=3, quality=80)
    assert (item.sell_in, item.quality) == (3, 80)

    update_quality([item])
    assert (item.sell_in, item.quality) == (3, 80)

    update_quality([item])
    assert (item.sell_in, item.quality) == (3, 80)

    update_quality([item])
    assert (item.sell_in, item.quality) == (3, 80)

    update_quality([item])
    assert (item.sell_in, item.quality) == (3, 80)

    update_quality([item])
    assert (item.sell_in, item.quality) == (3, 80)


def test_update_conjured():
    item = Item("Conjured Mana Cake", sell_in=6, quality=50)
    assert (item.sell_in, item.quality) == (6, 50)

    update_quality([item])
    assert (item.sell_in, item.quality) == (5, 48)

    update_quality([item])
    assert (item.sell_in, item.quality) == (4, 46)

    update_quality([item])
    assert (item.sell_in, item.quality) == (3, 44)

    update_quality([item])
    assert (item.sell_in, item.quality) == (2, 42)

    update_quality([item])
    assert (item.sell_in, item.quality) == (1, 40)

    update_quality([item])
    assert (item.sell_in, item.quality) == (0, 38)

    update_quality([item])
    assert (item.sell_in, item.quality) == (-1, 34)

    update_quality([item])
    assert (item.sell_in, item.quality) == (-2, 30)
