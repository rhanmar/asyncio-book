# 2.1 Знакомство с сопрограммами
# 2.2 Моделирование длительных операций с помощью sleep
# 2.3 Конкурентное выполнение с помощью задач


import asyncio
from utils import delay


async def say_hello() -> str:
    print("print Hello")
    await delay(3)
    return "return Hello"


async def add_one(number: int) -> int:
    print(f"Делаем {number} + 1")
    return number + 1


async def hello_every_second() -> None:
    for _ in range(2):
        await asyncio.sleep(1)
        print("пока я жду, исполняется другой код!")


async def main1() -> None:
    # Такой запуск не будет конкурентным
    first_hello = await say_hello()
    second_hello = await say_hello()
    o_plus_o = await add_one(1)
    print(first_hello)
    print(second_hello)
    print(o_plus_o)


async def main2() -> None:
    # Конкурентный апуск с помощью задач
    sleep_for_3: asyncio.Task = asyncio.create_task(delay(3))
    sleep_for_2: asyncio.Task = asyncio.create_task(delay(2))
    sleep_for_1: asyncio.Task = asyncio.create_task(delay(1))
    # sleep_for_3 = await delay(3)
    # print(type(sleep_for_3))
    # result = await sleep_for_3
    # result2 = await sleep_for_2
    # print(result)
    await sleep_for_3
    await sleep_for_2
    await sleep_for_1

    print("----")

    # Выполнение какого-то кода во время ожидания
    hello_1: asyncio.Task = asyncio.create_task(say_hello())
    hello_2: asyncio.Task = asyncio.create_task(say_hello())
    # o_plus_o: asyncio.Task = asyncio.create_task(add_one(1))
    # print(await o_plus_o)
    print(await add_one(2))
    await hello_every_second()
    print(await hello_1)
    print(await hello_2)

# print(say_hello())  # coroutine
# print(asyncio.run(say_hello()))
asyncio.run(main2())

