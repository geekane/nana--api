import requests
import json
from typing import Optional
from config import Config

class TTSService:
    def __init__(self, api_key: str, api_url:str, voice:str):
        self.api_key = api_key
        self.api_url = api_url
        self.voice = voice

    def generate_audio(self, text: str) -> bytes:
        """使用 edge_tts 生成音频"""
        if not self.api_key:
            print("TTS API KEY 未配置，无法使用TTS功能喵")
            return b""

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        data = {
            "model": "tts-1",
            "input": text,
            "voice": self.voice,
            "response_format": "mp3",
            "speed": 1,
        }

        try:
            response = requests.post(self.api_url, headers=headers, data=json.dumps(data))
            response.raise_for_status()  # 检查请求是否成功
            return response.content
        except requests.exceptions.RequestException as e:
            print(f"TTS Error: {e}")
            if response:
                print(f"Response status code: {response.status_code}")
                print(f"Response content: {response.text}")
            return b""
