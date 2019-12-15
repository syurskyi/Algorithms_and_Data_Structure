#!/usr/bin/env python

import asyncio

import aiohttp
import async_timeout

from utils import get_path


async def fetch_one(session, num):
    """Fetch a pdf file for a problem, if there's one."""

    url = f'https://projecteuler.net/overview={num:03}'

    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            if response.status == 200:
                if response.headers['Content-Type'] == 'application/pdf':
                    data = await response.read()
                    filename = f'{num:03}_overview.pdf'

                    with get_path('doc', filename).open('wb') as pdf_file:
                        pdf_file.write(data)
                    return num
            else:
                print(f"Got {response.status} while fetching {url}")


async def fetch_all():
    """Fetch pdf files."""

    with get_path("answers").open() as answers_file:
        nsolved = sum(1 for line in answers_file)

    cookies = {
        'DYNSRV': 'lin-10-170-0-31',
        'PHPSESSID': 'a4fb01c0de27e200683b4d556461b5aa',
        'keep_alive': '1119831347%23333574%233PpV0T6RtnqnCB6GNF4PvEH1TiEX1nlc'
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0',
    }

    async with aiohttp.ClientSession(cookies=cookies, headers=headers) as session:
        coros = [fetch_one(session, num) for num in range(1, nsolved + 1)]

        results = await asyncio.gather(*coros)
        files = 0
        for num in results:
            if num is not None:
                print(f'Saved a file for problem {num}')
                files += 1

        return files


def main():
    """The script's entry point."""

    loop = asyncio.get_event_loop()
    nfiles = loop.run_until_complete(fetch_all())
    print(f"{nfiles} file(s) saved")


if __name__ == '__main__':
    main()
