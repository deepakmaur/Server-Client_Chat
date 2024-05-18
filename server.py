import threading
import socket

host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# ANSI escape code for green text
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"


clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{YELLOW}{nickname} left the chat{RESET}'.encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f'{YELLOW}Connected with {str(address)}{RESET}')

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f'{GREEN}Nickname of the client is {nickname}{RESET}')
        broadcast(f'{GREEN}{nickname} has joined the chat!{RESET}'.encode('ascii'))
        client.send(f'{GREEN}Connected to the server!{RESET}'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening...")
receive()
