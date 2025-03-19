from flask import Flask, jsonify

app = Flask(__name__)  # File Name Automatic-ஆ Assign

@app.route('/')
def home():
    return jsonify({"message":"Hello, Flask is running!","status":"success"})

if __name__ == '__main__':
    app.run(debug=True)
    