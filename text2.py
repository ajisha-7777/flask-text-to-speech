from flask import Flask, request
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/speak', methods=['GET'])
def speak():
    text = request.args.get('text', 'Hello! How are you?')
    tts = gTTS(text=text, lang='en')
    tts.save("speech.mp3")
    os.system("start speech.mp3")  # Windows ku
    return f"Speech generated for: {text}"

if __name__ == '__main__':
    app.run(debug=True)