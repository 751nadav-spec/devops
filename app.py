from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "מה הולךךךךךךךךך"


@app.get("/kmujk/")
def fgff():
    return "מה ,mi9o9oijh"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5500)