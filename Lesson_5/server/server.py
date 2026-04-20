import socket
import datetime
import random

host = "0.0.0.0"
port = 7000
address = (host, port)

print("Running server...")
server = socket.socket()
server.bind(address)
server.listen()
print(f"Listerning to port {port}...")

while True:
    client, client_address = server.accept()
    print(f"connected with {client_address}")
    response = ""
    with open('motd/response.txt', 'r') as f:
        response = f.read()

    # response = str(random.randint(1000, 9999)) #client.recv(2048).decode('utf-8')
    # print(f"{datetime.datetime.now()}Responce from \"{client_address}\": {response}")
    # with open('logs/log.log', 'a', encoding='utf-8') as f:
    #     f.write(f'\n{datetime.datetime.now()}Responce from \"{client_address}\": {response}')
    client.send(response.encode('utf-8'))

    client.close()