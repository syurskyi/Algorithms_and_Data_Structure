import os
from tempfile import TemporaryDirectory

from tree import count_dirs_and_files

TMP = '/tmp'


def test_only_files():
    with TemporaryDirectory(dir=TMP) as dirname:
        for i in range(5):
            filename = f'{i}.txt'
            path = os.path.join(dirname, filename)
            with open(path, 'w') as f:
                f.write('hello')

        assert count_dirs_and_files(dirname) == (0, 5)


def test_only_dirs():
    with TemporaryDirectory(dir=TMP) as dirname:
        for i in range(5):
            os.makedirs(os.path.join(dirname, str(i)))

        assert count_dirs_and_files(dirname) == (5, 0)


def test_files_and_dirs():
    with TemporaryDirectory(dir=TMP) as dirname:
        for i in range(10):
            if i % 2 == 0:
                target_dir = os.path.join(dirname, str(i))
                os.makedirs(target_dir)
                for j in range(5):
                    filename = f'{j}.txt'
                    path = os.path.join(target_dir, filename)
                    with open(path, 'w') as f:
                        f.write('hello')

        assert count_dirs_and_files(dirname) == (5, 25)