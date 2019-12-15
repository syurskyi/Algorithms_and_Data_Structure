import asyncio
import time

# ONE_MIN = 60
# FIVE_MIN = ONE_MIN * 5
# TWENTY_FIVE_MIN = ONE_MIN * 25
# THIRTY_MIN = ONE_MIN * 30
# HOUR = ONE_MIN * 60
# CURRENT_SESSION = 1
from asyncio import sleep
from typing import Union

ONE_MIN = .006
FIVE_MIN = ONE_MIN * .0005
TWENTY_FIVE_MIN = ONE_MIN * .0025
THIRTY_MIN = ONE_MIN * .003
HOUR = ONE_MIN * .06
CURRENT_SESSION = 1


async def break_time(delay: Union[int, float], loop: int) -> None:
    """Break time

    :param delay: float of delay in seconds
    :param loop: int of the current loop
    :return: None
    """
    _delay = int(delay / ONE_MIN)
    print(f"[{loop}] {time.strftime('%X')} Time for a {_delay} min break!")
    await sleep(delay)


async def lunch_time(delay: Union[int, float]) -> None:
    """Lunch time

    :param delay: float of delay in seconds
    :return: None
    """
    print(f"\n** {time.strftime('%X')} Time for lunch! **")
    await sleep(delay)


async def work_time(delay: Union[int, float], loop: int) -> None:
    """Work time

    :param delay: float of delay in seconds
    :param loop: int of the current loop
    :return: None
    """
    print(f"[{loop}] {time.strftime('%X')} Time to work!")
    await sleep(delay)


async def session(
    work_length: Union[int, float] = TWENTY_FIVE_MIN,
    short_break_length: Union[int, float] = FIVE_MIN,
    long_break_length: Union[int, float] = THIRTY_MIN,
) -> None:
    """Session

    :param work_length: float of work length in seconds
    :param short_break_length: float of short break length in seconds
    :param long_break_length: float of long break length in seconds
    :return: None
    """
    loop = 1

    while loop < 4:
        await work_time(work_length, loop)
        await break_time(short_break_length, loop)
        loop += 1

    await work_time(work_length, loop)

    if CURRENT_SESSION % 2 != 0:
        await break_time(long_break_length, loop)


async def main(
    work_length: Union[int, float] = TWENTY_FIVE_MIN,
    short_break_length: Union[int, float] = FIVE_MIN,
    long_break_length: Union[int, float] = THIRTY_MIN,
    lunch_length: Union[int, float] = HOUR,
) -> None:
    """Main entry point

    :param work_length: float of work length in seconds
    :param short_break_length: float of short break length in seconds
    :param long_break_length: float of long break length in seconds
    :param lunch_length: float of lunch length in seconds
    :return: None
    """
    global CURRENT_SESSION
    print(f"Pomodor timer started at: {time.strftime('%X')}")

    while CURRENT_SESSION <= 4:
        print(f"\nSession: {CURRENT_SESSION}")
        await session(work_length, short_break_length, long_break_length)
        if CURRENT_SESSION == 2:
            await lunch_time(lunch_length)
        CURRENT_SESSION += 1

    print(f"\n{time.strftime('%X')} Time to go home!")

    print(f"\nWork day completed at: {time.strftime('%X')}")


if __name__ == "__main__":
    asyncio.run(main())