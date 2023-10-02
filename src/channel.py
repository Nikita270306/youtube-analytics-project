import json
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()
API_KEY = os.getenv("API_KEY")


class Channel:
    """Класс для ютуб-канала"""

    youtube = build('youtube', 'v3', developerKey=API_KEY)
    channel_id = 'UCwHL6WHUarjGfUM_586me8w'
    channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))
