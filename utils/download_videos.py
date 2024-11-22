from pytubefix import YouTube

# Video URL
url = "https://www.youtube.com/watch?v=a5B8Xx1RPSc"

# Initialize YouTube object
yt = YouTube(url)

# List all available streams for debugging (optional)
# print(yt.streams.filter(progressive=False))  

# Get the video stream with the highest bitrate
best_video = yt.streams.filter(only_video=True).order_by('bitrate').desc().first()

# Get the audio stream separately (if needed)
best_audio = yt.streams.filter(only_audio=True).order_by('abr').desc().first()

# Paths for downloads
video_path = "resources/videos"
audio_path = "resources/audios"

# Download the best video and audio streams
best_video.download(output_path=video_path)
best_audio.download(output_path=audio_path)

print(f"Downloaded video to {video_path}")
print(f"Downloaded audio to {audio_path}")
