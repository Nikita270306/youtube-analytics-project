
import json
from googleapiclient.discovery import build
from src.implemented import youtube


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

        self.channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()

        self.title = self.channel["items"][0]["snippet"]["title"]
        self.description = self.channel["items"][0]["snippet"]["description"]
        self.url = "https://www.youtube.com/" + self.channel["items"][0]["snippet"]["customUrl"]
        self.subscribers = int(self.channel["items"][0]["statistics"]["subscriberCount"])
        self.video_count = int(self.channel["items"][0]["statistics"]["videoCount"])
        self.views = int(self.channel["items"][0]["statistics"]["viewCount"])

    def __str__(self):
        return f"'{self.title} ({self.url})'"

    def __add__(self, other):
        return self.subscribers + other.subscribers

    def __sub__(self, other):
        return self.subscribers - other.subscribers

    def __mul__(self, other):
        return self.subscribers * other.subscribers

    def __truediv__(self, other):
        return self.subscribers / other.subscribers

    def __lt__(self, other):
        return self.subscribers < other.subscribers

    def __le__(self, other):
        return self.subscribers <= other.subscribers

    def __gt__(self, other):
        return self.subscribers > other.subscribers

    def __ge__(self, other):
        return self.subscribers >= other.subscribers

    def __eq__(self, other):
        return self.subscribers == other.subscribers

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=API_KEY)

    def to_json(self, file):
        directory = "data"
        if not os.path.exists(directory):
            os.makedirs(directory)
        path = os.path.join(directory, file)

        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                youtube_data = json.load(f)
        else:
            youtube_data = []

        youtube_data.append({
            "channel_id": self.channel_id,
            "title": self.title,
            "description": self.description,
            "url": self.url,
            "subscribers": self.subscribers,
            "video_count": self.video_count,
            "views": self.views,
        })

        with open(path, "w", encoding="utf-8") as f:
            json.dump(youtube_data, f, ensure_ascii=False)


