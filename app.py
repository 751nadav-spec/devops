from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello today, how can I help?"


@app.get("/page/")
def fgff():
    return "Hello dear customer, how are you today?"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
    # nadav
