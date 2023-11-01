import json
from datetime import timedelta

import isodate

from src.implemented import youtube
from src.video import Video


class PlayList:
    youtube_api = youtube

    def __init__(self, _playlist_id):
        self._playlist_id = _playlist_id
        self._playlist = self.youtube_api.playlistItems().list(playlistId=_playlist_id,
                                                               part='snippet, status').execute()
        self._playlist_content = self.youtube_api.playlistItems().list(playlistId=self._playlist_id,
                                                                       part='contentDetails',
                                                                       maxResults=50).execute()

    @staticmethod
    def printj(dict_to_print: dict) -> None:
        """
        Выводит словарь в json-подобном удобном формате с отступами
        :return: словарь
        """
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    def print_info(self):
        """
        Метод возвращает информацию о канале
        :return: словарь с информацией
        """
        return self.printj(self._playlist_content)

    @property
    def title(self):
        t = self._playlist['items'][0]['snippet']['title']
        return t.split('.')[0]

    @property
    def url(self):
        return f"https://www.youtube.com/playlist?list={self._playlist_id}"

    @property
    def total_duration(self):
        content = self._playlist_content
        duration = timedelta(hours=0, minutes=0, seconds=0)

        for item in content['items']:
            video_id = item['contentDetails']['videoId']
            video_instance = Video(video_id)
            video_duration = isodate.parse_duration(video_instance.duration)

            hours = int(str(video_duration)[:1])
            minutes = int(str(video_duration)[2:4])
            seconds = int(str(video_duration)[5:])

            duration += timedelta(hours=hours, minutes=minutes, seconds=seconds)
        return duration

    def show_best_video(self):
        content = self._playlist_content
        max_likes = 0
        d = {}

        for item in content['items']:
            video_id = item['contentDetails']['videoId']
            video_instance = Video(video_id)
            video_info = video_instance._video['items']

            for j in video_info:
                likes = int(j['statistics']['likeCount'])
                if likes > max_likes:
                    max_likes = likes
                link = f"https://youtu.be/{video_id}"
                d[link] = likes

        for key, value in d.items():
            if value == max_likes:
                return key
