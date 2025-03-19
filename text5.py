from flask import Flask, request, jsonify
from gtts import gTTS
import os
from moviepy.editor import ImageClip, AudioFileClip

app = Flask(__name__)

@app.route("/generate_video", methods=["POST"])
def generate_video():
    data = request.get_json()
    print("Received JSON:", data)  # Debugging print

    text = data.get("text")
    voice = data.get("voice", "en")  # Default English voice
    image_path = data.get("image", "black.jpg")  # Default black image

    if not text:
        return jsonify({"error": "Text is required"}), 400

    # Generate AI Voice
    tts = gTTS(text=text, lang=voice)
    audio_path = "output.mp3"
    tts.save(audio_path)

    return jsonify({"message": "Video generation started!"})

if __name__ == "__main__":
    app.run(debug=True)