import threading
import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',55555))
nickname=input("Enter the Nickname ")


# ANSI escape code for green text
GREEN = "\033[32m"
RESET = "\033[0m"





def receive():
    while True:
        try:
            message=client.recv(1024).decode("ascii")

            if message.startswith(nickname):  # Check if message starts with the client's nickname
                continue
            if message=="NICK":
                client.send(nickname.encode("ascii"))
            else:
                print(message)
        except:
            print("{GREEN}Error Occurred !  {RESET}")
            client.close()
            break

def write():
    while True:
        message=f'{nickname}: {input("")}'
        client.send(message.encode("ascii"))


receive_thread=threading.Thread(target=receive)
receive_thread.start()

write_thread=threading.Thread(target=write)
write_thread.start()

