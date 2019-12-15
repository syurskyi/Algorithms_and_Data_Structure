import pytest

from account import Account

checking = Account('Checking')
saving = Account('Saving', 10)


def test_account_balance():
    assert checking.start_balance == 0
    checking + 10
    assert checking.balance == 10

    assert saving.start_balance == 10
    with pytest.raises(ValueError):
        saving - 'a'
    saving - 5
    assert saving.balance == 5


def test_account_comparison():
    assert checking > saving
    assert checking >= saving
    assert saving < checking
    assert saving <= checking
    saving + 5
    assert checking == saving


def test_account_len():
    checking + 10
    checking + 3
    checking - 8
    assert len(checking) == 4


def test_account_indexing_iter():
    assert checking[0] == 10
    assert checking[-1] == -8
    assert list(checking) == [10, 10, 3, -8]


def test_account_str():
    assert str(checking) == 'Checking account - balance: 15'
    assert str(saving) == 'Saving account - balance: 10'
    saving + 5
    assert str(saving) == 'Saving account - balance: 15'