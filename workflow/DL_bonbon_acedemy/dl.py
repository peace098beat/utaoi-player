import sys
import os

from pathlib import Path

from loguru import logger
import youtube_dl

import json

import slack


logger.add(slack.send, level='INFO')
logger.add("./logs/dl.py.log", rotation="1 days", level='INFO')

cnt=0
def my_hook(d):
    global cnt
    if d['status'] == 'downloading':
        if (cnt%30 == 0) : 
            # logger.info(str(d))
            logger.info(d['filename'])
            db = d['downloaded_bytes']
            tb = d['total_bytes']
            r = db/tb
            s = f'{int(100*r)}%:' + '|'+ int(30*r)*'|' + int(30*(1-r))*'-' + '|'
            logger.info(s)
        cnt += 1
        

    if d['status'] == 'finished':
        logger.info('Done downloading, now converting ...')


if __name__ == '__main__':

    CACHE_DIR = './download'

    ydl_opts = {
        'outtmpl': f'{CACHE_DIR}/%(playlist)s/%(playlist_index)s - %(id)s - %(title)s.%(ext)s',
        'nooverwrites': True,
        'writeinfojson': True,
        'rejecttitle': '〈英語の歌〉',
        'ignoreerrors': True,
        # 'format': 'bestaudio/best',
        # 'postprocessors': [{
            # 'key': 'FFmpegExtractAudio',
            # 'preferredcodec': 'mp3',
            # 'preferredquality': '192',
        # }],
        'logger': logger,
        'progress_hooks': [my_hook],
    }


    urls =[
        'https://www.youtube.com/playlist?list=PL1DnK3_eexigLrF_Jc5wvkx6vjsw9ACSn',
        'https://www.youtube.com/playlist?list=PL1DnK3_eexigY79fq2fDGP6n9VWEArxMa',
        'https://www.youtube.com/playlist?list=PL1DnK3_eexijoHNVWAlC69PH6VWvrhnhr',
        'https://www.youtube.com/playlist?list=PL1DnK3_eexihX8VAgPvk44j_VE5K4zG4_',
        'https://www.youtube.com/playlist?list=PL1DnK3_eexihPqUVszOo-f6vH6n0SIxkE',
        'https://www.youtube.com/playlist?list=PL1DnK3_eexigK84NQ400lB4Jh81MQzzxM',
        'https://www.youtube.com/playlist?list=PL1DnK3_eexigyJHy58m93t3QTp733FYxP',

    ]


    logger.info('Process Start')

    logger.info(f'CACHE_DIR : {CACHE_DIR}')
    logger.info(f'download urls: {urls}')

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)

    logger.info('Process Done')