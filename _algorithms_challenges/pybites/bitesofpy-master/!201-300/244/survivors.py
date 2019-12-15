import os
from pathlib import Path
from urllib.request import urlretrieve

S3 = "https://bites-data.s3.us-east-2.amazonaws.com/{}"
FILE_NAME = "mutpy.out"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, FILE_NAME)

if not PATH.exists():
    urlretrieve(S3.format(FILE_NAME), PATH)


def _get_data(path=PATH):
    with open(path) as f:
        return [line.rstrip() for line in f.readlines()]


def filter_killed_mutants(mutpy_output: list = None) -> list:
    """Read in the passed in mutpy output and filter out the code snippets of
       mutation tests that were killed. Surviving mutants should be shown in
       full, as well the surrounding output.

       For example, this is a killed mutant:

         - [#  15] DDL account:
      --------------------------------------------------------------------------------
        23:         if not (isinstance(amount, int)):
        24:             raise ValueError('please use int for amount')
        25:         self._transactions.append(amount)
        26:
      - 27:     @property
      - 28:     def balance(self):
      + 27:     def balance(\
      + 28:         self):
        29:         return self.amount + sum(self._transactions)
        30:
        31:     def __len__(self):
        32:         return len(self._transactions)
      --------------------------------------------------------------------------------
      [0.10240 s] killed by test_account.py::test_balance

      You should reduce this to:

         - [#  15] DDL account:
      [0.10240 s] killed by test_account.py::test_balance

      So you mute all that is in between the two dashed lines.

      You do the same for incompetent mutants, for example:
         - [#   3] AOR account:
      --------------------------------------------------------------------------------
        43:     def __add__(self, other):
        44:         owner = '{}&{}'.format(self.owner, other.owner)
        45:         start_amount = self.amount + other.amount
        46:         acc = Account(owner, start_amount)
      - 47:         for t in list(self) + list(other):
      + 47:         for t in list(self) - list(other):
        48:             acc.add_transaction(t)
        49:         return acc
      --------------------------------------------------------------------------------
      [0.10011 s] incompetent

      ... becomes:
         - [#   3] AOR account:
      [0.10011 s] incompetent
      
      Return the filtered output as a list of lines.
    """
    if mutpy_output is None:
        mutpy_output = _get_data()

    output = []
    test_result = []
    in_test = False
    for line in mutpy_output:
        if in_test:
            if line.startswith('['):
                if 'survived' in line:
                    output.extend(test_result)
                test_result.clear()
                output.append(line)
                in_test = False
            else:
                test_result.append(line)
        else:
            if line.startswith('   - [#'):
                in_test = True
            output.append(line)
    return output
