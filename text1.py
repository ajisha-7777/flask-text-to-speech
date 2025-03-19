from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello, Flask!"

@app.route("/text")  # 🔥 text.py ku route create
def text():
    return "This is text API!"

if __name__ == "__main__":
    app.run(debug=True)