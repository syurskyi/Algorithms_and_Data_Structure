import os

ONE_KB = 1024


def get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""
    return [file for file in os.listdir(dirname)
            if os.stat(f'{dirname}{os.sep}{file}').st_size / ONE_KB >= size_in_kb]
