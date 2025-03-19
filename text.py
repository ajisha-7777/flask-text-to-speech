from flask import Flask, request, jsonify
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/speak', methods=['POST'])
def speak():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({"error": "Text not provided"}), 400
    
    text = data['text']
    tts = gTTS(text=text, lang='en')
    audio_file = "output.mp3"
    tts.save(audio_file)

    return jsonify({"message": "Audio created successfully!", "file": audio_file})

if __name__ == '__main__':
    app.run(debug=True)