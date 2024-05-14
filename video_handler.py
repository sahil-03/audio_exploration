from pytube import YouTube 
from moviepy.editor import *


def download_video(video_url: str) -> None: 
    yt = YouTube(video_url)
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    video.download(filename='video.mp4')

    print("Video downloaded successfully")


def extract_audio(video_url: str) -> None: 
    download_video(video_url)

    video_clip = VideoFileClip('video.mp4')
    audio_clip = video_clip.audio
    audio_clip.write_audiofile('audio.mp3')

    audio_clip.close()
    video_clip.close()

    print("Audio extracted successfully")


if __name__ == '__main__':
    video_url = "https://www.youtube.com/watch?v=Sby1uJ_NFIY"
    extract_audio(video_url)