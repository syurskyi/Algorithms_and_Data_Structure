import pytest

from color import Color


@pytest.mark.parametrize("color, expected", [
    ("white", (255, 255, 255)),
    ("black", (0, 0, 0)),
    ("blue", (0, 0, 255)),
    ("red", (255, 0, 0)),
    ("green", (0, 128, 0)),
    ("orange", (255, 128, 0)),
    ("puke", None),
])
def test_color_class(color, expected):
    c = Color(color)
    assert c.rgb == expected


@pytest.mark.parametrize("rgb, expected", [
    ((255, 255, 255), "#ffffff"),
    ((0, 0, 0), "#000000"),
    ((0, 0, 255), "#0000ff"),
    ((255, 0, 0), "#ff0000"),
    ((0, 128, 0), "#008000"),
    ((255, 128, 0), "#ff8000"),
])
def test_color_classmethod_rgb2hex(rgb, expected):
    assert Color.rgb2hex(rgb) == expected


@pytest.mark.parametrize("rgb", [
    ("puke"),
    ("0, 0, 0"),
    ((0, -5, 255)),
    ((256, 0, 0)),
])

def test_color_rgb2hex_bad_value(rgb):
    with pytest.raises(ValueError):
        Color.rgb2hex(rgb)


@pytest.mark.parametrize("hex, expected", [
    ("#ffffff", (255, 255, 255)),
    ("#000000", (0, 0, 0)),
    ("#0000ff", (0, 0, 255)),
    ("#ff0000", (255, 0, 0)),
    ("#008000", (0, 128, 0)),
    ("#ff8000", (255, 128, 0)),
])
def test_color_classmethod_hex2rgb(hex, expected):
    assert Color.hex2rgb(hex) == expected


@pytest.mark.parametrize("value", [
    ("puke"),
    ("#ccc"),
    ("#stopit"),
    ("pink"),
])
def test_color_hex2rgb_bad_value(value):
    with pytest.raises(ValueError):
        Color.hex2rgb(value)


def test_color_string_output():
    color = Color("brown")
    assert str(color) == "(165, 42, 42)"


def test_color_repr_output():
    color = Color("brown")
    assert repr(color) == "Color('brown')"


def test_unknown_color():
    color = Color("puke green")
    assert str(color) == "Unknown"