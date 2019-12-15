from pandas.core.frame import DataFrame
import pytest

from movies import group_by_genre


@pytest.fixture(scope="module")
def df():
    return group_by_genre()


def test_df_type(df):
    assert type(df) == DataFrame


def test_df_shape(df):
    assert df.shape == (19, 1)


def test_first_genre_and_count(df):
    assert df.index[0] == 'Drama'
    assert df.iloc[0].movie == 485


def test_last_genre_and_count(df):
    assert df.index[-1] == 'IMAX'
    assert df.iloc[-1].movie == 9