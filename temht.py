from flask import Flask, render_template, request, send_from_directory
import pyttsx3
import os

app = Flask(__name__)

# Ensure 'static' folder exists
if not os.path.exists("static"):
    os.makedirs("static")

@app.route("/", methods=["GET", "POST"])
def index():
    audio_file = None
    if request.method == "POST":
        text = request.form["text"]
        if text.strip():  # Check if text is not empty
            engine = pyttsx3.init()
            filename = "speech.mp3"  # Fixed filename (overwrites each time)
            filepath = os.path.join("static", filename)
            engine.save_to_file(text, filepath)
            engine.runAndWait()
            audio_file = filename  # Send to template
    
    return render_template("index.html", audio_file=audio_file)

@app.route("/static/<path:filename>")
def serve_audio(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    app.run(debug=True)
    