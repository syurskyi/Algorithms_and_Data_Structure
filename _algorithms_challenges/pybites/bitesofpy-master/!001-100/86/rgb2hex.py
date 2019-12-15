def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    if any(0 > x or 255 < x for x in rgb):
        raise ValueError('Value for element is 0…255')
    return f'#{bytes(rgb).hex().upper()}'
