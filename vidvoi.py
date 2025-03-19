from flask import Flask, request, jsonify
from gtts import gTTS
import os
from moviepy.editor import ImageClip, AudioFileClip, CompositeVideoClip

app = Flask(__name__)

@app.route("/generate_video", methods=["POST"])
def generate_video():
    data = request.json
    text = data.get("text")
    voice = data.get("voice", "en")  # Default English voice
    image_path = data.get("image", "black.jpg")  # Default background image

    if not text:
        return jsonify({"error": "Text is required"}), 400

    # Generate speech from text
    tts = gTTS(text=text, lang=voice)
    audio_path = "output.mp3"
    tts.save(audio_path)

    # Load audio and image
    audio = AudioFileClip(audio_path)
    image = ImageClip(image_path).set_duration(audio.duration)

    # Combine image and audio
    video = CompositeVideoClip([image.set_audio(audio)])

    # Save final video
    video_path = "final_video.mp4"
    video.write_videofile(video_path, fps=24, codec="libx264")

    return jsonify({"message": "Video created successfully!", "video_path": video_path})

if __name__ == "__main__":
    app.run(debug=True)