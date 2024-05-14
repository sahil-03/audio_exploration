from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv() 
client = OpenAI()

def extract_transcript() -> json: 
    audio_file = open("audio.mp3", "rb")
    transcript = client.audio.transcriptions.create(
        model='whisper-1',
        file=audio_file,
    )

    return transcript


if __name__ ==  '__main__':
    transcript = extract_transcript()
    print(transcript.text)