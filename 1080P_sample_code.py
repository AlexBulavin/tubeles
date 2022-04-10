__author__ = 'Alex Bulavin'

# Этот пример взят из видео: https://www.youtube.com/watch?v=3FIS2MiAXW8
import os.path

from pytube import YouTube
import ffmpeg

yt = YouTube("https://www.youtube.com/watch?v=3FIS2MiAXW8")
path = '/Users/alex/Downloads/YouTube'

# Download video stream for 1080p resolution
v_path = yt.streams.filter(resolution="1080p").first().download(path, "video.mp4")

# Download audio stream
a_path = yt.streams.filter(only_audio=True).first().download(path, "audio.mp4")

v = ffmpeg.input(v_path)
a = ffmpeg.input(a_path)
r = ffmpeg.concat(v, a, v=1, a=1).output(os.path.join(path, "result.mp4")).run()

print(r)
