# 2.4 Снятие задач и задание тайм-аутов

import asyncio
from util import delay


async def main_cancel() -> None:
    long_task = asyncio.create_task(delay(10))
    seconds_elapsed: int = 0

    while not long_task.done():
        print("Задача не закончилась, следующая проверка через секунду")
        await asyncio.sleep(1)
        seconds_elapsed += 1
        if seconds_elapsed == 5:
            long_task.cancel()
    try:
        await long_task
        print("Задача отработала полностью")
    except asyncio.CancelledError:
        print("Задача снята")


async def main_timeout() -> None:
    delay_task = asyncio.create_task(delay(5))
    try:
        await asyncio.wait_for(delay_task, timeout=2)
        print("Задача отработала полностью")
    except asyncio.TimeoutError:
        print("Timeout. Задача снята", delay_task.cancelled())
        print("Выполнена ли задача:", delay_task.done())


async def main_timeout_shield() -> None:
    delay_task = asyncio.create_task(delay(7))
    try:
        await asyncio.wait_for(asyncio.shield(delay_task), timeout=2)
        print("Задача отработала полностью")
    except asyncio.TimeoutError:
        print("Задача отработала 2 с, осталось 5 с")
        print("Статус снятия задачи:", delay_task.cancelled())
        print("Выполнена ли задача:", delay_task.done())
        print(await delay_task)
        print("Выполнена ли задача:", delay_task.done())


asyncio.run(main_cancel())
asyncio.run(main_timeout())
asyncio.run(main_timeout_shield())
