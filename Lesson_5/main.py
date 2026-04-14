import socket
import json


config = {}
with open("data/config.json", "r", encoding="utf-8") as file:
    config = json.load(file)
host = config.get("host")
port = config.get("port")

address = (host, port)
server = socket.socket()
print(f"Connecting to server: \"{address}\"...")
server.connect(address)

response = input("Enter responce: ")
server.send(response.encode('utf-8'))



# docker build . -t my-hello-world:0.0.1
# docker run -it my-hello-world
# pip freeze > requirements.txt