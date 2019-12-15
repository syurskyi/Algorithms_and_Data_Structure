def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    if not isinstance(value, (int, float)):
        raise TypeError()
    fn = {'in': lambda x: round(x / 2.54, 4),
          'cm': lambda x: round(x * 2.54, 4)}
    if fmt.lower() in fn:
        return fn[fmt.lower()](value)
    raise ValueError()
