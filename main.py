import os
from fastapi import FastAPI
from moviepy.editor import TextClip, CompositeVideoClip, ColorClip

# ImageMagick path set pannanum
os.environ["IMAGEMAGICK_BINARY"] = r"C:\Program Files\ImageMagick-7.1.1-Q16\magick.exe"

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Video Generator API Running!"}

@app.get("/generate_video")
def generate_video(text: str):
    try:
        # Background color clip
        bg_clip = ColorClip(size=(1280, 720), color=(0, 0, 0), duration=5)

        # Text clip
        txt_clip = TextClip(text, fontsize=70, color='white', font="Arial-Bold")
        txt_clip = txt_clip.set_position("center").set_duration(5)

        # Merge text & background
        final_video = CompositeVideoClip([bg_clip, txt_clip])
        
        # Save video
        output_path = "output.mp4"
        final_video.write_videofile(output_path, fps=24)

        return {"message": "Video Generated!", "file": output_path}
    
    except Exception as e:
        return {"error": str(e)}
