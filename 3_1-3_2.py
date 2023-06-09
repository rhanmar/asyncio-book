import socket

# Блокирующие сокеты

# telnet 127.0.0.1 8000


# socket.AF_INET, – тип адреса, в данном случае адрес будет содержать имя хоста и номер порта.
# socket.SOCK_STREAM, означает, что для взаимодействия будет использоваться протокол TCP.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# позволит повторно использовать номер порта,
# после того как мы остановим и заново запустим приложение, избегнув тем самым ошибки «Адрес уже используется».
# Если этого не сделать, то операционной системе потребуется некоторое время, чтобы освободить порт,
# после чего приложение сможет запуститься без ошибок.
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ("127.0.0.1", 8000)
server_socket.bind(server_address)

# слушаем подключения
server_socket.listen()

try:
    # дождаться подключения
    connection, client_address = server_socket.accept()
    print(f'Получен запрос на подключение от {client_address}!')

    while True:
        data: bytes = connection.recv(1024)  # чтение из канала
        if not data:  # если ничего не прочтено - значит, клиент закрыл соединение
            break
        print("Принято:", data.decode('utf-8'))  # считывание данных
        connection.sendall(data)  # эхо
finally:
    server_socket.close()



# 3.3 подключение нескольких клиентов

# import socket
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server_address = ('127.0.0.1', 8000)
# server_socket.bind(server_address)
# server_socket.listen()
#
# connections = []
#
# try:
#     while True:
#         connection, client_address = server_socket.accept()
#         print(f'Получен запрос на подключение от {client_address}!')
#         connections.append(connection)
#         for connection in connections:
#             buffer = b''
#             while buffer[-2:] != b'\r\n':
#                 data = connection.recv(2)
#                 if not data:
#                     break
#                 else:
#                     print(f'Получены данные: {data}!')
#                     buffer = buffer + data
#             print(f"Все данные: {buffer}")
#             connection.send(buffer)
# finally:
#     server_socket.close()
