import pytest

from enchantable_items import (
    Enchantment,
    Item,
    generate_items,
    get_soup,
    generate_enchantments,
)

mock_html = """
<table id="minecraft_items" class="std_table">
<tr>
<th data-search="1" width="175">Enchantment<br>(<em>Minecraft ID Name</em>)</th>
<th data-search="1">Max Level</th>
<th class="hidden-xs">Description</th>
<th data-search="1"><span class="hidden-xs">Minecraft </span>ID</th>
<th class="hidden-xs">Items</th>
<th>Version</th>
</tr>
<tr>
<td><a href="/enchantments/aqua_affinity.php">Aqua Affinity</a><br>(<em>aqua_<wbr>affinity</em>)</td>
<td>I</td>
<td class="hidden-xs">Speeds up how fast you can mine blocks underwater</td>
<td>6</td>
<td class="hidden-xs"><img class="img-rounded b-lazy" src="/images/thumbnail_loading.gif" data-src="/armor_recipes/images/enchanted_iron_helmet.png" alt="aqua affinity" width="40" height="40"></td>
<td></td>
</tr>
<tr>
<td><a href="/enchantments/bane_of_arthropods.php">Bane of Arthropods</a><br>(<em>bane_<wbr>of_<wbr>arthropods</em>)</td>
<td>V</td>
<td class="hidden-xs">Increases attack damage against arthropods</td>
<td>18</td>
<td class="hidden-xs"><img class="img-rounded b-lazy" src="/images/thumbnail_loading.gif" data-src="/enchantments/images/sword_axe_sm.png" alt="bane of arthropods" width="40" height="40"></td>
<td></td>
</tr>
<tr>
<td><a href="/enchantments/blast_protection.php">Blast Protection</a><br>(<em>blast_<wbr>protection</em>)</td>
<td>IV</td>
<td class="hidden-xs">Reduces blast and explosion damage</td>
<td>3</td>
<td class="hidden-xs"><img class="img-rounded b-lazy" src="/images/thumbnail_loading.gif" data-src="/enchantments/images/armor_sm.png" alt="blast protection" width="40" height="40"></td>
<td></td>
</tr>
<tr>
<td><a href="/enchantments/channeling.php">Channeling</a><br>(<em>channeling</em>)</td>
<td>I</td>
<td class="hidden-xs">Summons a lightning bolt at a targeted mob when enchanted item is thrown (targeted mob must be standing in raining)</td>
<td>68</td>
<td class="hidden-xs"><img class="img-rounded b-lazy" src="/images/thumbnail_loading.gif" data-src="/weapon_recipes/images/enchanted_trident.png" alt="channeling" width="40" height="40"></td>
<td>1.13</td>
</tr>
</table>
"""


@pytest.fixture(scope="module")
def enchantment_mock():
    enchant = Enchantment(
        "python_developer",
        "Python Developer",
        10,
        "Ability automate really boring and repetitive tasks at work",
    )
    return enchant


@pytest.fixture(scope="module")
def item_mock(enchantment_mock):
    item = Item("clamytoe")
    return item


@pytest.fixture(scope="module")
def mock_soup():
    return get_soup(mock_html)


@pytest.fixture(scope="module")
def mock_data(mock_soup):
    return generate_enchantments(mock_soup)


@pytest.fixture(scope="module")
def mocked_generate_items(mock_data):
    return generate_items(mock_data)


@pytest.fixture(scope="module")
def coders_dataset():
    soup = get_soup()
    mc_data = generate_enchantments(soup)
    items = generate_items(mc_data)
    return items


def test_enchantment_class(enchantment_mock):
    assert enchantment_mock.name == "Python Developer"
    assert enchantment_mock.items == []


def test_enchantment_class_add_items(enchantment_mock, item_mock):
    enchantment_mock.items.append(item_mock.name)
    assert len(enchantment_mock.items) == 1
    bob = Item("bob")
    enchantment_mock.items.append(bob.name)
    assert len(enchantment_mock.items) == 2
    assert enchantment_mock.items == ["clamytoe", "bob"]
    assert enchantment_mock.max_level == 10


def test_enchantment_class_print(enchantment_mock, capfd):
    print(enchantment_mock)
    output = capfd.readouterr()[0].split("\n")[0]
    assert (
        output
        == "Python Developer (10): Ability automate really boring and repetitive tasks at work"
    )


def test_item_class(item_mock, enchantment_mock):
    item_mock.enchantments.append(enchantment_mock)
    assert item_mock.enchantments[0].name == "Python Developer"


def test_item_class_print(item_mock, capfd):
    print(item_mock)
    output = capfd.readouterr()[0].strip()
    assert output == "Clamytoe: \n  [10] python_developer"


def test_enchantment_print(mock_data, capfd):
    print(mock_data["channeling"])
    output = capfd.readouterr()[0].split("\n")[0]
    assert (
        output
        == "Channeling (1): Summons a lightning bolt at a targeted mob when enchanted item is thrown (targeted mob must be standing in raining)"
    )


@pytest.mark.parametrize(
    "enchant, expected",
    [
        ("aqua_affinity", 1),
        ("bane_of_arthropods", 5),
        ("blast_protection", 4),
        ("channeling", 1),
    ],
)
def test_roman_numeral_conversion(mock_data, enchant, expected):
    assert mock_data[enchant].max_level == expected


def test_generate_enchantments_with_mock(mock_data):
    assert isinstance(mock_data, dict)
    assert len(mock_data.keys()) == 4
    assert (
        mock_data["channeling"].description
        == "Summons a lightning bolt at a targeted mob when enchanted item is thrown (targeted mob must be standing in raining)"
    )


def test_generate_enchantments_from_source():
    soup = get_soup()
    data = generate_enchantments(soup)
    assert len(data.keys()) == 37
    assert data["efficiency"].max_level == 5


@pytest.mark.parametrize(
    "item, expected",
    [
        ("armor", "Blast Protection"),
        ("axe", "Bane of Arthropods"),
        ("helmet", "Aqua Affinity"),
        ("sword", "Bane of Arthropods"),
        ("trident", "Channeling"),
    ],
)
def test_gen_items_mocked(mocked_generate_items, item, expected):
    assert mocked_generate_items[item].enchantments[0].name == expected


@pytest.mark.parametrize(
    "item, expected",
    [
        (
            "armor",
            [
                "blast_protection",
                "binding_curse",
                "fire_protection",
                "projectile_protection",
                "protection",
                "thorns",
            ],
        ),
        (
            "axe",
            [
                "bane_of_arthropods",
                "efficiency",
                "fortune",
                "sharpness",
                "silk_touch",
                "smite",
            ],
        ),
        ("boots", ["depth_strider", "feather_falling", "frost_walker"]),
        ("bow", ["flame", "infinity", "power", "punch"]),
        ("chestplate", ["vanishing_curse", "mending", "unbreaking"]),
        ("crossbow", ["multishot", "piercing", "quick_charge"]),
        (
            "fishing_rod",
            ["vanishing_curse", "luck_of_the_sea", "lure", "mending", "unbreaking"],
        ),
        ("helmet", ["aqua_affinity", "respiration"]),
        (
            "pickaxe",
            [
                "vanishing_curse",
                "efficiency",
                "fortune",
                "mending",
                "silk_touch",
                "unbreaking",
            ],
        ),
        ("shovel", ["efficiency", "fortune", "silk_touch"]),
        (
            "sword",
            [
                "bane_of_arthropods",
                "vanishing_curse",
                "fire_aspect",
                "knockback",
                "looting",
                "mending",
                "sharpness",
                "smite",
                "sweeping",
                "unbreaking",
            ],
        ),
        ("trident", ["channeling", "impaling", "loyalty", "riptide"]),
    ],
)
def test_gen_items(coders_dataset, item, expected):
    assert [enc.id_name for enc in coders_dataset[item].enchantments] == expected


@pytest.mark.parametrize(
    "item, expected",
    [
        (
            "armor",
            "Armor: \n  [1] binding_curse\n  [4] blast_protection\n  [4] fire_protection\n  [4] projectile_protection\n  [4] protection\n  [3] thorns",
        ),
        (
            "axe",
            "Axe: \n  [5] bane_of_arthropods\n  [5] efficiency\n  [3] fortune\n  [5] sharpness\n  [1] silk_touch\n  [5] smite",
        ),
        (
            "boots",
            "Boots: \n  [3] depth_strider\n  [4] feather_falling\n  [2] frost_walker",
        ),
        ("bow", "Bow: \n  [1] flame\n  [1] infinity\n  [5] power\n  [2] punch"),
        (
            "chestplate",
            "Chestplate: \n  [1] mending\n  [3] unbreaking\n  [1] vanishing_curse",
        ),
        ("crossbow", "Crossbow: \n  [1] multishot\n  [4] piercing\n  [3] quick_charge"),
        (
            "fishing_rod",
            "Fishing Rod: \n  [3] luck_of_the_sea\n  [3] lure\n  [1] mending\n  [3] unbreaking\n  [1] vanishing_curse",
        ),
        ("helmet", "Helmet: \n  [1] aqua_affinity\n  [3] respiration"),
        (
            "pickaxe",
            "Pickaxe: \n  [5] efficiency\n  [3] fortune\n  [1] mending\n  [1] silk_touch\n  [3] unbreaking\n  [1] vanishing_curse",
        ),
        ("shovel", "Shovel: \n  [5] efficiency\n  [3] fortune\n  [1] silk_touch"),
        (
            "sword",
            "Sword: \n  [5] bane_of_arthropods\n  [2] fire_aspect\n  [2] knockback\n  [3] looting\n  [1] mending\n  [5] sharpness\n  [5] smite\n  [3] sweeping\n  [3] unbreaking\n  [1] vanishing_curse",
        ),
        (
            "trident",
            "Trident: \n  [1] channeling\n  [5] impaling\n  [3] loyalty\n  [3] riptide",
        ),
    ],
)
def test_item_print(coders_dataset, item, expected, capfd):
    print(coders_dataset[item])
    output = capfd.readouterr()[0].strip()
    assert output == expected