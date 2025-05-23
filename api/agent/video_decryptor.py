import os.path
from http.client import responses

import moviepy as mp
import speech_recognition as sr
from api.agent.emotion_detector import EmotionDetector


class VideoDecryptor:
    def __init__(self):
        self.emotion_agent = EmotionDetector()
        self.r = sr.Recognizer()

    def detect_from_urls(self, urls):
        responses = []
        for url in urls:
            _emotion = self.detect(url)
            responses.append({
                'url': url,
                'emotions': _emotion
            })
        return responses

    def detect(self, url):
        _text = self.extract_text(url)
        emotion = self.emotion_agent.answer(_text)
        return emotion

    def to_wav(self, url):
        path = f".{url}"
        video = mp.VideoFileClip(path)
        audio_file = video.audio
        audio_path = f"{path}.wav"
        if not os.path.exists(audio_path):
            audio_file.write_audiofile(audio_path)

    def extract_text(self, url):
        path = f".{url}"
        video = mp.VideoFileClip(path)
        audio_file = video.audio
        audio_path = f"{path}.wav"
        if not os.path.exists(audio_path):
            audio_file.write_audiofile(audio_path)
        with sr.AudioFile(audio_path) as source:
            data = self.r.record(source)
        text = self.r.recognize_google(data, language="fr-FR")
        return text