# 2.5 Задачи, сопрограммы, будущие объекты и объекты, допускающие ожидание

import asyncio
from util import delay


# 2.14

async def test_future() -> None:
    future_obj: asyncio.Future = asyncio.Future()
    print("is done?", future_obj.done())  # False
    # print("result: ", future_obj.result()) asyncio.exceptions.InvalidStateError
    print("set result...")
    future_obj.set_result(101)
    print("is done?", future_obj.done())  # True
    print("result: ", future_obj.result())  # 101


####

# 2.15

async def set_future_value(future: asyncio.Future) -> None:
    # Ждать 1 с, прежде чем установить значение
    await asyncio.create_task(delay(2))
    future.set_result(101)


def make_request() -> asyncio.Future:
    future_obj = asyncio.Future()
    # Создать задачу, которая асинхронно установит значение future
    asyncio.create_task(set_future_value(future_obj))
    return future_obj


async def main() -> None:
    future: asyncio.Future = make_request()
    print("Объект Future готов?", future.done())
    # Приостановить main, пока значение future не установлено
    value = await future
    print("Объект Future готов?", future.done())
    print(value)

# asyncio.run(test_future())
asyncio.run(main())
