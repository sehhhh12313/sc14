import socket
import threading

# Функція для обробки повідомлень від клієнта
def handle_client(client_socket, client_address):
    # Отримати нікнейм від клієнта
    nickname = client_socket.recv(1024).decode()
    print(f"[{nickname}] приєднався {client_address}")
    broadcast(f"[{nickname}] приєднався до чату!")

    while True:
        try:
            # Отримати повідомлення від клієнта
            message = client_socket.recv(1024).decode()
            if message == "exit":
                break
            # Розсилка повідомлення всім клієнтам
            broadcast(f"[{nickname}] {message}")
        except:
            break

    print(f"[{nickname}] вийшов")
    broadcast(f"[{nickname}] покинув чат.")
    # Закрити з'єднання з клієнтом
    client_socket.close()

# Функція для розсилки повідомлення всім клієнтам
def broadcast(message):
    for client in clients:
        client.send(message.encode())

# Адреса та порт сервера
SERVER_HOST = '192.168.0.203'
SERVER_PORT = 5555

# Створення серверного сокету
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Прив'язка серверного сокету до адреси та порту
server_socket.bind((SERVER_HOST, SERVER_PORT))

# Прослуховування з'єднань
server_socket.listen(4)
print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

# Список клієнтів
clients = []

while True:
    # Прийняття нового з'єднання
    client_socket, client_address = server_socket.accept()
    print(f"[*] Accepted connection from {client_address}")
    clients.append(client_socket)
    # Створення окремого потоку для обробки клієнта
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
