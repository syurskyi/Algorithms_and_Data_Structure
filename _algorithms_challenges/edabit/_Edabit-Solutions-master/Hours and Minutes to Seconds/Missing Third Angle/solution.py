def missing_angle(angle1, angle2):
    if angle1 + angle2 > 90:
        return "acute"
    elif angle1 + angle2 == 90:
        return "right"
    else:
        return "obtuse"
