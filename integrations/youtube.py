from typing import List
import youtube_dl
from youtube_transcript_api import YouTubeTranscriptApi
from playsound import playsound


def download_audio_video(url: str):
    audio_path = download_wav_from_video(url=url)
    video_path = download_video(url=url)

    return audio_path, video_path

def download_transcript(url: str):
    video_id = url.split("=")[1]
    video_id = video_id.split("&")[0]
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    FinalTranscript = ' '.join([i['text'] for i in transcript])
    return FinalTranscript,transcript

def download_video(url: str, progress_hooks: List=[]):
    video_info = youtube_dl.YoutubeDL().extract_info(url=url, download=False)

    video_path = f"{video_info['title']}.mp4"

    options = {
        'noplaylist' : True, 
        'outtmpl': video_path,
        'progress_hooks': progress_hooks,
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    return video_path

def download_wav_from_video(url: str):
    video_info = youtube_dl.YoutubeDL().extract_info(url=url, download=False)

    options = {
        'audio-format': 'wav',
        'keepvideo': False,
        'outtmpl': f"{video_info['title']}.wav",
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    return f"{video_info['title']}" + "-" + f"{video_info['webpage_url']}".split("=")[-1] + ".wav"

def main():
    url = "https://www.youtube.com/watch?v=LA8L3IvFBvQ" #Explaining the confusion matrix
    file_name = download_video(url)
    print(file_name)

if __name__ == "__main__":
    main()
