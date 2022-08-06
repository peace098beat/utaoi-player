import youtube_dl

class MyLogger(object):
    def debug(self, msg):
        print(msg)
        pass

    def warning(self, msg):
        pass
        print(msg)

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'outtmpl': './cache/%(id)s.%(ext)s',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

urls = [
    'https://www.youtube.com/watch?v=RDD9bJUamYs',
]

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(urls)

