# 3.4 Использование selectors

import selectors
import socket
from typing import List, Tuple

selector = selectors.DefaultSelector()

server_socket = socket.socket()
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ("127.0.0.1", 8000)
server_socket.setblocking(False)
server_socket.bind(server_address)
server_socket.listen()

# регистрация сокета для получения уведомлений
selector.register(server_socket, selectors.EVENT_READ)

while True:
    # select блокирует выполнение, пока не произойдет какое-то событие,
    # после чего возвращает список сокетов, готовых для обработки, а также событие,
    # которое произошло с каждым сокетом.
    # Поддерживается также тайм-аут – если в течение указанного времени
    # ничего не произошло, то возвращается пустой список сокетов.
    events: List[Tuple[selectors.SelectorKey, int]] = selector.select(timeout=1)  # ждёт 1 секунду
    # events: List[Tuple[selectors.SelectorKey, int]] = selector.select()  - будет ждать подключений

    if len(events) == 0:  # ничего не произошло или таймаут
        print("Нет событий")

    for event, _ in events:
        # получить сокет, для которого произошло событие
        event_socket = event.fileobj

        # если событие произошло с серверным сокетом,
        # то значит была попытка подключения
        if event_socket == server_socket:
            connection, address = server_socket.accept()
            connection.setblocking(False)
            print(f"Получен запрос на подключение от {address}")
            # зарегистрировать клиент, подключившийся к сокету
            selector.register(connection, selectors.EVENT_READ)
        else:
            # если событие произошло не с серверным сокетом -
            # получить данные от клиента и отправить их обратно
            data = event_socket.recv(1024)
            print(f"Получены данные: {data}")
            event_socket.send(data)
