from asyncio.log import logger
import sys
from pathlib import Path


import youtube_dl

from loguru import logger
logger.add("file_X.log", rotation="1 days")


def read_playlist(path):

    with open(path, 'r') as fp:
        txts = fp.readlines()

    urls = []
    for line in txts:
        if line.startswith('http'):
            line = line.replace('\n', '')
            urls.append(line)
    
    return urls


def yt_url2id(url):
    return url.split('watch?v=')[-1]


def not_exists(url, cache_dir, ext='mp3'):
    vid = yt_url2id(url)
    cache_name = f'{vid}.{ext}'
    return not Path(cache_dir, cache_name).exists()


PLAYLIST_PATH = 'playlist.txt'
CACHE_DIR = './cache'


ydl_opts = {
    'outtmpl': f'{CACHE_DIR}/%(id)s.%(ext)s',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': logger,
    # 'progress_hooks': [my_hook],
}



logger.info(f'CACHE_DIR : {CACHE_DIR}')
logger.info(f'PLAYLIST_PATH : {PLAYLIST_PATH}')

urls = read_playlist(PLAYLIST_PATH)
urls = [u for u in urls if not_exists(u, CACHE_DIR)]

logger.info(f'down load urls')
logger.info(urls)

with youtube_dl.YoutubeDL(ydl_opts) as ydl:

    ydl.download(urls)

