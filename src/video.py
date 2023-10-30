import json

from src.implemented import youtube

class Video:
    youtube_api = youtube

    def __init__(self, video_id):
        self.video_id = video_id
        self._video = self.youtube_api.videos().list(id=video_id, part='snippet,contentDetails,'
                                                                       'statistics,status').execute()

    def __str__(self):
        return str(self.title)

    def item(self):
        return self._video.get("items")[0]

    def snippet(self) -> dict | None:
        return self.item().get('snippet')

    def statistics(self) -> dict | None:
        return self.item().get('statistics')

    def content_details(self) -> dict | None:
        return self.item().get('contentDetails')

    @property
    def id(self):
        value = self.video_id
        return value

    @property
    def title(self):
        try:
            value = self.snippet().get('title')
        except:
            return None
        else:
            return value

    @property
    def link(self):
        try:
            value = f"https://www.youtube.com/watch?v={self.id}"
        except:
            return None
        else:
            return value

    @property
    def view_count(self):
        try:
            value = self.statistics().get('viewCount')
        except:
            return None
        else:
            return value

    @property
    def like_count(self):
        try:
            value = self.statistics().get('likeCount')
        except:
            return None
        else:
            return value

    @property
    def duration(self):
        try:
            value = self.content_details().get('duration')
        except:
            return None
        else:
            return value

    @staticmethod
    def printj(dict_to_print: dict) -> None:
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    def print_info(self):
        return self.printj(self._video)


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id


    def __str__(self):
        return self.title

