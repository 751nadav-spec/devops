from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "hello word"


@app.get("/page/")
def fgff():
    return "this is good"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5500)
    # nadav
