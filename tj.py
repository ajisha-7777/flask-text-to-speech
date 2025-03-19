from flask import Flask, render_template, request, send_file, jsonify
from gtts import gTTS
import os
import pydub
import tempfile

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download_audio", methods=["POST"])
def download_audio():
    data = request.json
    text = data.get("text", "")
    voice = data.get("voice", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    audio_path = "static/speech.mp3"

    if voice == "female":
        tts = gTTS(text, lang="en")
        tts.save(audio_path)
    else:
        temp_path = tempfile.mktemp(suffix=".mp3")
        tts = gTTS(text, lang="en")
        tts.save(temp_path)

        sound = pydub.AudioSegment.from_file(temp_path, format="mp3")
        sound.export(audio_path, format="mp3")

    return send_file(audio_path, as_attachment=True, mimetype="audio/mp3")
if __name__ == "__main__":
    app.run(debug=True)