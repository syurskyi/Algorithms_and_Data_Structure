from collections import Counter

import requests

STOCK_DATA = 'https://bit.ly/2MzKAQg'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    if cap == 'n/a':
        return 0.0
    else:
        cap = cap.strip().lstrip('$')
        if cap[-1] == 'M':
            return float(cap[:-1])
        if cap[-1] == 'B':
            return float(cap[:-1]) * 1000.0
        raise BaseException('Oh no! error in cap value.')


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    return round(sum([_cap_str_to_mln_float(co['cap']) for co in data if co['industry'] == industry]), 3)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    return sorted([(co['symbol'], _cap_str_to_mln_float(co['cap'])) for co in data], key=lambda x: x[1])[-1][0]


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    sector_list = Counter()
    for co in data:
        sector_list += Counter({co['sector']: _cap_str_to_mln_float(co['cap'])})
    sectors = sorted([(k, v) for k, v in sector_list.items()], key=lambda x: x[1])
    return sectors[-1][0], sectors[0][0]
