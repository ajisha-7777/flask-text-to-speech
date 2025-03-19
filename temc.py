from flask import Flask, render_template, request, send_file, jsonify
from gtts import gTTS
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download_audio", methods=["POST"])
def download_audio():
    data = request.json
    text = data.get("text", "")
    voice = data.get("voice", "male")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Fix voice selection for gTTS
    lang = "en"
    
    if voice == "female":
        tld = "co.in"  # Indian accent (Female)
        gender = "female"
    else:
        tld = "us"  # US accent (Male)
        gender = "male"

    # Set filename based on voice selection
    audio_path = f"static/speech_{gender}.mp3"
    
    # Generate speech
    tts = gTTS(text, lang=lang, tld=tld, slow=False)
    tts.save(audio_path)

    return send_file(audio_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)