from typing import Union

import pytest

from pomodoro import break_time, lunch_time, main, session, work_time


@pytest.mark.asyncio
async def test_break_time(capfd):
    anno = break_time.__annotations__
    assert anno["delay"] == Union[int, float]
    assert anno["loop"] == int
    assert anno["return"] is None
    delay = 0.0001
    await break_time(delay, 1)
    output = capfd.readouterr()[0].strip()
    assert "[1]" in output
    assert f"Time for a {int(delay/60)} min break!" in output


@pytest.mark.asyncio
async def test_lunch_time(capfd):
    anno = lunch_time.__annotations__
    assert anno["delay"] == Union[int, float]
    assert anno["return"] is None
    delay = 0.06
    await lunch_time(delay)
    output = capfd.readouterr()[0].strip()
    assert "Time for lunch!" in output


@pytest.mark.asyncio
async def test_work_time(capfd):
    anno = work_time.__annotations__
    assert anno["delay"] == Union[int, float]
    assert anno["return"] is None
    delay = 0.0025
    await work_time(delay, 3)
    output = capfd.readouterr()[0].strip()
    assert "[3]" in output
    assert "Time to work!" in output


@pytest.mark.asyncio
async def test_session(capfd):
    anno = session.__annotations__
    assert anno["work_length"] == Union[int, float]
    assert anno["short_break_length"] == Union[int, float]
    assert anno["long_break_length"] == Union[int, float]
    assert anno["return"] is None
    await session(0.0025, 0.0005, 0.003)
    output = capfd.readouterr()[0].strip()
    assert "Time to work!" in output
    assert "min break!" in output
    assert "Time for lunch!" not in output
    assert len(output.splitlines()) == 8


@pytest.mark.asyncio
async def test_main(capfd):
    anno = main.__annotations__
    assert anno["work_length"] == Union[int, float]
    assert anno["short_break_length"] == Union[int, float]
    assert anno["long_break_length"] == Union[int, float]
    assert anno["lunch_length"] == Union[int, float]
    assert anno["return"] is None
    await main(0.0025, 0.0005, 0.003, 0.01)
    output = capfd.readouterr()[0].strip()
    assert "Pomodor timer started at" in output
    assert "Time to work!" in output
    assert "min break!" in output
    assert "Time for lunch!" in output
    assert "Work day completed at" in output
    assert len(output.splitlines()) == 45