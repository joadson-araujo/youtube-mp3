from pytube import YouTube
import os

yt = YouTube('https://www.youtube.com/watch?v=Sv8XHiTkDYg')

video = yt.streams.filter(only_audio=True).first()

exit_file = video.download(output_path="C:/Users/Example-PC/Desktop")

base, ext = os.path.splitext(exit_file)
new_file = base + '.mp3'
os.rename(exit_file, new_file)
