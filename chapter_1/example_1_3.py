import threading
import os

print(f'Исполняется Python-процесс с идентификатором: {os.getpid()}')


def hello_from_thread():
    print(f'Привет от потока {threading.current_thread()}!')


hello_thread = threading.Thread(target=hello_from_thread)
hello_thread.start()

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f'В данный момент Python выполняет {total_threads} поток(ов)')
print(f'Имя текущего потока {thread_name}')

hello_thread.join()

# OUTPUT:
# Исполняется Python-процесс с идентификатором: 67659
# Привет от потока <Thread(Thread-1 (hello_from_thread), started 140444879025920)>!
# В данный момент Python выполняет 2 поток(ов)
# Имя текущего потока MainThread
