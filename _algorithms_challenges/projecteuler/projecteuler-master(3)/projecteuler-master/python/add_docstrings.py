#!/usr/bin/env python

"""Add docstrings to solutions."""

import argparse
import asyncio
import sys

import aiohttp
import async_timeout
from bs4 import BeautifulSoup

from utils import get_path


def parse_args(args=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Add docstrings to solutions")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("path", nargs="*", default=[],
                       help="A path (or paths) to the module file")
    group.add_argument("-a", "--all", action="store_true",
                       help="Process all files")

    return parser.parse_args(args)


def get_docstring(html) -> str:
    soup = BeautifulSoup(html, "html.parser")
    problem_number = soup.body.find("h3").contents[0].strip()
    problem_title = soup.body.find("h2").text
    return f'"""{problem_number}: {problem_title}"""\n'


def update_file(path, docstring):
    with path.open("r+") as f:
        lines = f.readlines()

        if lines[2] != docstring:
            print(docstring[3:-4])
            lines[2:2] = [docstring, "\n"]
            f.seek(0)
            f.writelines(lines)


async def fetch_url(session, url):
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            return url, await response.text()


async def add_docstrings(paths):
    async with aiohttp.ClientSession() as session:
        coros = []
        url2path = {}
        for path in paths:
            num = path.stem[-3:]  # extract the problem number
            url = f"https://projecteuler.net/problem={num}"
            url2path[url] = path
            coros.append(fetch_url(session, url))

        for future in asyncio.as_completed(coros):
            url, html = await future
            path = url2path[url]
            docstring = get_docstring(html)
            update_file(path, docstring)


def main():
    args = parse_args()

    if args.path:
        paths = []
        for path in args.path:
            path_obj = get_path("python", path)
            if not path_obj.exists():
                print(f"File not found: {path}")
                return 1
            paths.append(path_obj)
    else:
        paths = sorted(get_path("python").glob("p???.py"))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(add_docstrings(paths))
    return 0


if __name__ == "__main__":
    sys.exit(main())
