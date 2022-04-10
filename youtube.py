__author__ = 'Alex Bulavin'
from pytube import YouTube

DOWNLOAD_FOLDER = '/Users/alex/Downloads/YouTube'
video_url = 'https://www.youtube.com/watch?v=ROoo1eoOOvg'
video_obj = YouTube(video_url)

stream = video_obj.streams.get_highest_resolution()
stream.download(DOWNLOAD_FOLDER)