#!/usr/bin/env python

"""Verify and benchmark solutions"""

import sys
from concurrent.futures import ProcessPoolExecutor
from heapq import nlargest
from importlib import import_module
from time import process_time

from utils import get_path


def read_answers():
    """Read the answers file"""

    with get_path("answers").open() as f:
        return [line.rstrip() for line in f]


def run(num):
    """Run the solution and measure the execution time"""
    mod_name = f"p{num:03d}"
    mod = import_module(mod_name)

    begin = process_time()
    answer = mod.main()
    time = process_time() - begin

    return answer, time


def main():
    answers = read_answers()

    if len(sys.argv) == 1:
        problems = range(1, len(answers)+1)
    else:
        # a parameter can be an actual number or a filename
        problems = [int(arg) if arg.isdigit() else int(''.join(filter(str.isdigit, arg)))
                    for arg in sys.argv[1:]]

    total_time = 0
    times = {}

    with ProcessPoolExecutor() as executor:
        for num, (answer, time) in zip(problems, executor.map(run, problems,
                                                              chunksize=2)):
            print(f"{num:03d} ", end="")

            if str(answer) != answers[num-1]:
                print(f"FAIL ({answer} != {answers[num-1]})")
                return 1

            print(f"OK ({time:.6f}s)")
            total_time += time
            times[num] = time

    if len(sys.argv) == 1:
        print(f"\nTotal {len(problems)} problems solved.\n")
        print("Slowest solutions:")

        for problem in nlargest(5, times, times.get):
            print(f"{problem:03d}  {times[problem]:.2f}s {times[problem]/total_time:6.2%}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
