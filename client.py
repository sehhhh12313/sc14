import socket
import threading


# Функція для обробки введення повідомлень користувачем та надсилання на сервер
def send_message():
    while True:
        message = input(': ')
        if message.lower() == "exit":
            client_socket.send(message.encode())
            break
        else:
            client_socket.send(message.encode())

# Адреса та порт сервера
SERVER_HOST = '192.168.0.203'
SERVER_PORT = 5555

# Створення клієнтського сокету
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Підключення до сервера
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Введення нікнейму
nickname = input("Введіть ваш нікнейм: ")

# Надсилання нікнейму на сервер
client_socket.send(nickname.encode())

# Створення потоку для введення та надсилання повідомлень на сервер
message_thread = threading.Thread(target=send_message)
message_thread.start()

# Отримання повідомлень від сервера та їх виведення
while True:
    message = client_socket.recv(1024).decode()
    print(message)

# Закриття з'єднання з сервером
client_socket.close()
