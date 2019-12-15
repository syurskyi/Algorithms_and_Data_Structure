from inventory import items, duplicate_items


def test_change_copy_only():
    items_copy = duplicate_items(items)
    assert items == items_copy

    # modify the copy
    items_copy[0]['name'] = 'macbook'
    items_copy[1]['id'] = 4
    items_copy[2]['value'] = 30

    # only copy should have been updated, check original items values
    assert items[0]['name'] == 'laptop'
    assert items[1]['id'] == 2
    assert items[2]['value'] == 20