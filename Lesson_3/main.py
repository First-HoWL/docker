import requests
from colorama import Fore, Back, Style, init
import time
import json
import threading
from flask import Flask, jsonify
from flask_cors import CORS

init(autoreset=True)



config = {}
with open("data/config.json", "r", encoding="utf-8") as file:
    config = json.load(file)
delay = config.get("delay")
url = config.get("endpoint")

def task(resp):
    while (True):
        r = requests.get(url,{
            "ids": ",".join(config.get("coins")),
            "vs_currencies": ",".join(config.get("vs_currencies"))
        })
        if r.ok:
            resp.clear()
            resp.update(r.json())
        time.sleep(delay)

resp = {}
thread1 = threading.Thread(target=task, args=(resp,))
thread1.start() 

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return resp

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)


# docker build . -t my-hello-world:0.0.1
# docker run -it my-hello-world
# pip freeze > requirements.txt