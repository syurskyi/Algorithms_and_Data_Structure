from decimal import Decimal


def check_split(item_total, tax_rate, tip, people):
    total = Decimal(item_total[1:])
    tax = Decimal(tax_rate[:-1]) / 100 + 1
    tip_p = Decimal(tip[:-1]) / 100 + 1
    grand_total = round(round(total * tax, 2) * tip_p, 2)
    split = round(grand_total / people, 2)
    split_arr = [split for _ in range(people - 1)]
    split_arr.append(grand_total - sum(split_arr))
    return f'{item_total[0]}{grand_total:.2f}', split_arr
