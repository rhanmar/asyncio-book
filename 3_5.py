# 3.5 Эхо-сервер с asyncio


import asyncio
import logging
import socket


async def echo(
        connection: socket.socket,
        loop: asyncio.AbstractEventLoop
) -> None:
    # ожидание данных от клиента в бесконечном цикле
    try:
        while data := await loop.sock_recv(connection, 1024):
            if data == b"boom\r\n":
                raise Exception("boom")
            #  отправка данных обратно клиенту
            await loop.sock_sendall(connection, data)
    except Exception as e:
        logging.exception(e)
    finally:
        connection.close()


async def listen_for_connection(
        server_socket: socket.socket,
        loop: asyncio.AbstractEventLoop
) -> None:
    while True:
        print("Ожидание подключений...")
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f"Получен запрос на подключение от {address}")
        # После получения запроса на подключение создаем
        # задачу echo, ожидающую данные от клиента
        asyncio.create_task(echo(connection, loop))


async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = ('127.0.0.1', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    # Запускаем сопрограмму прослушивания порта на предмет подключений
    await listen_for_connection(server_socket, asyncio.get_event_loop())

asyncio.run(main())
