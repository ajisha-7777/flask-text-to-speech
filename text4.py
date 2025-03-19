from flask import Flask, request, jsonify
from gtts import gTTS
import os
from moviepy.editor import ImageSequenceClip, AudioFileClip

app = Flask(__name__)

@app.route("/generate_video", methods=["POST"])
def generate_video():
    data = request.json
    text = data.get("text")
    voice = data.get("voice", "en")  # Default English voice
    
    if not text:
        return jsonify({"error": "Text is required"}), 400

    # Generate AI Voice
    tts = gTTS(text=text, lang=voice)
    audio_path = "output.mp3"
    tts.save(audio_path)

    # Create Simple Video (Black screen + Audio)
    duration = AudioFileClip(audio_path).duration
    video_path = "output.mp4"
    
    clip = ImageSequenceClip(["black.jpg"], durations=[duration])  # Dummy Image
    clip = clip.set_audio(AudioFileClip(audio_path))
    clip.write_videofile(video_path, codec="libx264", fps=1)

    return jsonify({"message": "Video generated successfully!", "video_path": video_path})

if _name_ == "__main__":
    app.run(debug=True)