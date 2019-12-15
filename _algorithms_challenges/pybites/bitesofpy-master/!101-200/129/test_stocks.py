from Previous.stocks import (_cap_str_to_mln_float,
                             get_stock_symbol_with_highest_cap,
                             get_industry_cap,
                             get_sectors_with_max_and_min_stocks)


def test_cap_str_to_mln_float():
    assert _cap_str_to_mln_float('n/a') == 0
    assert _cap_str_to_mln_float('$100.45M') == 100.45
    assert _cap_str_to_mln_float('$20.9B') == 20900


def test_get_stock_symbol_with_highest_cap():
    assert get_stock_symbol_with_highest_cap() == 'JNJ'


def test_get_industry_cap():
    assert get_industry_cap("Business Services") == 368853.27
    assert get_industry_cap("Real Estate Investment Trusts") == 243295.36


def test_get_sectors_with_max_and_min_stocks():
    assert get_sectors_with_max_and_min_stocks() == ('Finance',
                                                     'Transportation')