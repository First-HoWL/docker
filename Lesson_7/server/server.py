import json
from flask import Flask, jsonify
from flask_cors import CORS


motd = "Hello world!"

with open('motd/response.txt', 'r') as f:
    motd = f.read()


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    with open('motd/response.txt', 'r') as f:
        motd = f.read()
    return json.dumps(motd)

@app.route("/edit/<newText>")
def edit(newText):
    with open('motd/response.txt', 'w', encoding="utf-8") as f:
        f.write(newText)
    return json.dumps(newText)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)


# pip freeze > requirements.txt