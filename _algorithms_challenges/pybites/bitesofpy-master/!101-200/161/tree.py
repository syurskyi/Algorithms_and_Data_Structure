import os


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    count_dir = count_files = 0
    for _, dir, files in os.walk(directory):
        count_dir += len(dir)
        count_files += len(files)
    return count_dir, count_files
