import asyncio
from util import delay

# 2.21 Ручное создание цикла


async def main():
    await delay(1)

loop = asyncio.new_event_loop()  # создать новый цикл событий

try:
    loop.run_until_complete(main())  # исполнение корутины
finally:
    loop.close()  # закрытие цикла событий


# --------------

# 2.22 Получение доступа к циклу событий


def call_later():
    print("Меня вызовут в ближайшем будущем!")


async def main():
    loop = asyncio.get_running_loop()  # получить ЦС
    # loop = asyncio.get_event_loop - получить или создать ЦС
    loop.call_soon(call_later)  # функция будет выполнена на следующей итерации цикла
    await delay(1)

asyncio.run(main())
