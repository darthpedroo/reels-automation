from moviepy import *

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920

video = VideoFileClip("resources/videos/cuphead1.mp4").resized(width=VIDEO_WIDTH,height=VIDEO_HEIGHT)

video.write_videofile("movie_resized.mp4")