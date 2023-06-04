import asyncio
from typing import Callable, Any
import time
import functools


async def delay(delay_seconds: int) -> int:
    print(f'@ Засыпаю на {delay_seconds} с')
    await asyncio.sleep(delay_seconds)
    print(f'@ Сон в течение {delay_seconds} с закончился')
    return delay_seconds


def async_timed() -> Any:
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapped(*args, **kwargs) -> Any:
            print(f"выполняется {func} с аргументами {args} {kwargs}")
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f"{func} завершилась за {total:.4f} с")
        return wrapped
    return wrapper
