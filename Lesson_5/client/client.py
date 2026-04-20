import socket
import json
import time

time.sleep(1)

config = {}
with open("data/config.json", "r", encoding="utf-8") as file:
    config = json.load(file)
host = config.get("host")
port = config.get("port")

address = (host, port)
server = socket.socket()
print(f"Connecting to server: \"{address}\"...")
server.connect(address)

#response = input("Enter responce: ")
resp = server.recv(2048).decode('utf-8') #.send(response.encode('utf-8'))

print(resp)


# docker build . -t my-hello-world:0.0.1
# docker run -it my-hello-world
# pip freeze > requirements.txt