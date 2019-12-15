    sum = 0
    index = 0
    while index < len(change):
        if index == 0:
            sum += change[index] * 0.25
        elif index == 1:
            sum += change[index] * 0.10
        elif index == 2:
            sum += change[index] * 0.05
        else:
            sum += change[index] * 0.01
        index += 1
    if sum >= amount_due:
        return True
    else:
        return False
