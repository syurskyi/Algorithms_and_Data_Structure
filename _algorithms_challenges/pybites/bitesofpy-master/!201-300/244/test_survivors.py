import pytest

from survivors import filter_killed_mutants, _get_data

EXPECTED_OUTPUT = """
[*] Start mutation process:
   - targets: account
   - tests: /tmp/test_account.py
[*] 9 tests passed:
   - test_account [0.12459 s]
[*] Start mutants generation and execution:
   - [#   1] AOR account:
[0.12042 s] killed by test_account.py::test_balance
   - [#   2] AOR account:
[0.10003 s] killed by test_account.py::test_merge_account
   - [#   3] AOR account:
[0.10011 s] incompetent
   - [#   4] COD account:
[0.11709 s] killed by test_account.py::test_balance
   - [#   5] COI account:
[0.11089 s] killed by test_account.py::test_balance
   - [#   6] CRP account:
[0.09470 s] killed by test_account.py::test_balance
   - [#   7] CRP account:
[0.09643 s] killed by test_account.py::test_repr
   - [#   8] CRP account:
[0.09736 s] killed by test_account.py::test_repr
   - [#   9] CRP account:
[0.09909 s] killed by test_account.py::test_str
   - [#  10] CRP account:
[0.09923 s] killed by test_account.py::test_str
   - [#  11] CRP account:
--------------------------------------------------------------------------------
  20:             self.amount)
  21:
  22:     def add_transaction(self, amount):
  23:         if not (isinstance(amount, int)):
- 24:             raise ValueError('please use int for amount')
+ 24:             raise ValueError('mutpy')
  25:         self._transactions.append(amount)
  26:
  27:     @property
  28:     def balance(self):
--------------------------------------------------------------------------------
[0.09799 s] survived
   - [#  12] CRP account:
--------------------------------------------------------------------------------
  20:             self.amount)
  21:
  22:     def add_transaction(self, amount):
  23:         if not (isinstance(amount, int)):
- 24:             raise ValueError('please use int for amount')
+ 24:             raise ValueError('')
  25:         self._transactions.append(amount)
  26:
  27:     @property
  28:     def balance(self):
--------------------------------------------------------------------------------
[0.09931 s] survived
   - [#  13] CRP account:
[0.10067 s] killed by test_account.py::test_merge_account
   - [#  14] CRP account:
[0.10083 s] killed by test_account.py::test_merge_account
   - [#  15] DDL account:
[0.10240 s] killed by test_account.py::test_balance
   - [#  16] ROR account:
[0.09937 s] killed by test_account.py::test_comparison
   - [#  17] ROR account:
[0.09987 s] killed by test_account.py::test_comparison
   - [#  18] ROR account:
--------------------------------------------------------------------------------
  37:     def __eq__(self, other):
  38:         return self.balance == other.balance
  39:
  40:     def __lt__(self, other):
- 41:         return self.balance < other.balance
+ 41:         return self.balance <= other.balance
  42:
  43:     def __add__(self, other):
  44:         owner = '{}&{}'.format(self.owner, other.owner)
  45:         start_amount = self.amount + other.amount
--------------------------------------------------------------------------------
[0.10084 s] survived
[*] Mutation score [7.08526 s]: 82.4%
   - all: 18
   - killed: 14 (77.8%)
   - survived: 3 (16.7%)
   - incompetent: 1 (5.6%)
   - timeout: 0 (0.0%)
[*] Coverage: 240 of 240 AST nodes (100.0%)
"""
EXPECTED_OUTPUT_WITH_GAP = """
[*] Start mutation process:
   - targets: account
   - tests: /tmp/test_account.py
[*] 9 tests passed:
   - test_account [0.12459 s]
[*] Start mutants generation and execution:
   - [#   1] AOR account:
[0.12042 s] killed by test_account.py::test_balance
   - [#   2] AOR account:
[0.10003 s] killed by test_account.py::test_merge_account
   - [#   3] AOR account:
[0.10011 s] incompetent
   - [#   4] COD account:
[0.11709 s] killed by test_account.py::test_balance
   - [#   5] COI account:
[0.11089 s] killed by test_account.py::test_balance
   - [#   6] CRP account:
[0.09470 s] killed by test_account.py::test_balance
   - [#   7] CRP account:
[0.09643 s] killed by test_account.py::test_repr
   - [#   8] CRP account:
[0.09736 s] killed by test_account.py::test_repr
   - [#   9] CRP account:
[0.09909 s] killed by test_account.py::test_str
   - [#  12] CRP account:
--------------------------------------------------------------------------------
  20:             self.amount)
  21:
  22:     def add_transaction(self, amount):
  23:         if not (isinstance(amount, int)):
- 24:             raise ValueError('please use int for amount')
+ 24:             raise ValueError('')
  25:         self._transactions.append(amount)
  26:
  27:     @property
  28:     def balance(self):
--------------------------------------------------------------------------------
[0.09931 s] survived
   - [#  13] CRP account:
[0.10067 s] killed by test_account.py::test_merge_account
   - [#  14] CRP account:
[0.10083 s] killed by test_account.py::test_merge_account
   - [#  15] DDL account:
[0.10240 s] killed by test_account.py::test_balance
   - [#  16] ROR account:
[0.09937 s] killed by test_account.py::test_comparison
   - [#  17] ROR account:
[0.09987 s] killed by test_account.py::test_comparison
   - [#  18] ROR account:
--------------------------------------------------------------------------------
  37:     def __eq__(self, other):
  38:         return self.balance == other.balance
  39:
  40:     def __lt__(self, other):
- 41:         return self.balance < other.balance
+ 41:         return self.balance <= other.balance
  42:
  43:     def __add__(self, other):
  44:         owner = '{}&{}'.format(self.owner, other.owner)
  45:         start_amount = self.amount + other.amount
--------------------------------------------------------------------------------
[0.10084 s] survived
[*] Mutation score [7.08526 s]: 82.4%
   - all: 18
   - killed: 14 (77.8%)
   - survived: 3 (16.7%)
   - incompetent: 1 (5.6%)
   - timeout: 0 (0.0%)
[*] Coverage: 240 of 240 AST nodes (100.0%)
"""


@pytest.fixture(scope='module')
def actual():
    return [line.rstrip() for line in filter_killed_mutants()]


@pytest.fixture(scope='module')
def actual2():
    """Same output but filter out test 10 (killed) and 11 (survived),
       to avoid the hardcoded output gets returned from function
    """
    mutpy_output = _get_data()
    test10 = mutpy_output.index('   - [#  10] CRP account:')
    test12 = mutpy_output.index('   - [#  12] CRP account:')
    output = mutpy_output[:test10] + mutpy_output[test12:]
    return [line.rstrip() for line in filter_killed_mutants(output)]


def test_output_matches(actual):
    expected = [line.rstrip() for line in
                EXPECTED_OUTPUT.strip().splitlines()]
    assert actual == expected


def test_different_output(actual2):
    expected = [line.rstrip() for line in
                EXPECTED_OUTPUT_WITH_GAP.strip().splitlines()]
    assert actual2 == expected