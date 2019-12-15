import pytest
from pandas.core.frame import DataFrame

from Previous.orders import (load_excel_into_dataframe,
                             get_year_region_breakdown,
                             get_best_sales_rep,
                             get_most_sold_item)


@pytest.fixture(scope="module")
def df():
    return load_excel_into_dataframe()


def test_load_excel_into_dataframe(df):
    assert type(df) == DataFrame
    assert df.shape == (43, 7)


def test_get_year_region_breakdown(df):
    ret = get_year_region_breakdown(df)

    assert ret.index.levels[0][0] == 2018
    assert ret.index.levels[0][1] == 2019

    assert ret.index.names[0] == 'Year'
    assert ret.index.names[1] == 'Region'

    actual = [round(val, 2) for val in ret.values]
    expected = [3833.51, 5193.71, 231.12, 7305.56,
                808.38, 2255.6]
    assert actual == expected


def test_get_best_sales_rep(df):
    best_rep = get_best_sales_rep(df)
    assert best_rep[0] == 'Kivell'
    assert best_rep[1] == 3109.44


def test_get_most_sold_item(df):
    most_sold = get_most_sold_item(df)
    assert most_sold[0] == 'Binder'
    assert int(most_sold[1]) == 722