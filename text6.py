from flask import Flask, request, jsonify
from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip
import os

app = Flask(__name__)

@app.route("/generate_video", methods=["POST"])
def generate_video():
    try:
        data = request.json
        print("Received JSON:", data)  # Debugging purpose

        # Validate input data
        if not data or "text" not in data:
            return jsonify({"error": "Text is required"}), 400

        text = data.get("text", "")
        voice = data.get("voice", "en")  # Default English voice
        image_path = data.get("image", "black.jpg")  # Default black image

        # Check if image file exists
        if not os.path.exists(image_path):
            return jsonify({"error": "Image file not found"}), 400

        # Generate audio from text
        audio_path = "output.mp3"
        tts = gTTS(text=text, lang=voice)
        tts.save(audio_path)

        # Load audio and image
        audio = AudioFileClip(audio_path)
        image = ImageClip(image_path, duration=audio.duration)

        # Set audio to video
        video = image.set_audio(audio)
        video_path = "output_video.mp4"
        video.write_videofile(video_path, fps=24)

        return jsonify({"message": "Video generated successfully!", "video_path": video_path})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)