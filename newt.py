from flask import Flask, render_template, request, send_file
import os
from gtts import gTTS

app = Flask(__name__)

# Folder to store audio files
AUDIO_FOLDER = "static/audio"
os.makedirs(AUDIO_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert_text_to_speech():
    text = request.form["text"]
    if not text.strip():
        return "Error: No text provided", 400

    # Convert text to speech
    tts = gTTS(text=text, lang="en")
    audio_path = os.path.join(AUDIO_FOLDER, "output.mp3")
    tts.save(audio_path)

    return "success"

@app.route("/download")
def download_audio():
    return send_file("static/audio/output.mp3", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)