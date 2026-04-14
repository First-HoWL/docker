import socket
import datetime

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
    
    response = client.recv(2048).decode('utf-8')
    print(f"{datetime.datetime.now()}Responce from \"{client_address}\": {response}")
    with open('logs/log.log', 'a', encoding='utf-8') as f:
        f.write(f'\n{datetime.datetime.now()}Responce from \"{client_address}\": {response}')

    client.close()