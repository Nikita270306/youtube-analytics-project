import json

from src.implemented import youtube

class Video:
    youtube_api = youtube

    def __init__(self, video_id):
        self.video_id = video_id
        self.title = ''
        self.url = ''
        self.views = 0
        self.likes = 0

        self.video_info()
    def video_info(self) -> None:
        try:
            video_info = youtube.videos().list(part='snippet,statistics', id=self.video_id).execute()

            if 'items' in video_info:
                video_info = video_info['items'][0]
                self.title = video_info['snippet']['title']
                self.url = f'https://www.youtube.com/watch?v={self.video_id}'
                self.views = int(video_info['statistics']['viewCount'])
                self.likes = int(video_info['statistics']['likeCount'])
        except IndexError:
            self.title = None
            self.url = None
            self.views = None
            self.likes = None
            print('Передан несуществующий id видео')
    def __str__(self):
        return str(self.title)


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str__(self):
        return self.title
