import pyttsx3
import time
import os
from moviepy.editor import *
from flask import Flask, request, render_template
from elevenlabs import generate, play

app = Flask(__name__)

# Step 1: Convert Hindi Text to Speech
def text_to_speech(text, output_file="static/output.mp3"):
    audio = generate(text=text, voice="hindi")  # Use ElevenLabs AI for realistic Hindi voice
    with open(output_file, "wb") as f:
        f.write(audio)
    return output_file

# Step 2: Generate Simple Animation (Placeholder for 3D Animation Integration)
def create_animation(audio_file, output_video="static/animation.mp4"):
    # Placeholder: Use a static image as background
    img = ImageClip("static/cartoon_bg.jpg").set_duration(5)
    
    # Add AI-generated voice-over
    audio = AudioFileClip(audio_file)
    video = img.set_audio(audio)
    video.write_videofile(output_video, codec="libx264", fps=24)
    return output_video

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        hindi_text = request.form['text']
        audio_path = text_to_speech(hindi_text)
        video_path = create_animation(audio_path)
        return render_template('index.html', video=video_path)
    return render_template('index.html', video=None)

if __name__ == "__main__":
    app.run(debug=True)
