from curses.panel import new_panel
from inspect import getsource
from pathlib import Path
import glob
import vlc

CACHE_DIR = './cache'


def get_sound_files(cache_dir, ext='mp3'):
    return glob.glob(f'{cache_dir}/*.{ext}')


mp3_files = get_sound_files(CACHE_DIR, ext='mp3')
print(mp3_files)

player = vlc.MediaListPlayer()
mediaList = vlc.MediaList(mp3_files)
player.set_media_list(mediaList)
player.set_playback_mode(vlc.PlaybackMode.loop)
player.play()

while True:
    data = input()

    #POSITION
    if data == 'a':
        p = player.get_media_player()
        pos = p.get_position()
        print(pos, '|'*int(pos*10))

    #INDEX
    elif data == 'b':
        p = player.get_media_player()
        media_instance = p.get_media()
        index = mediaList.index_of_item(media_instance)
        print(index)

    #NEXT
    elif data == 'c':
        player.next()

    #STOP
    elif data == 'd':
        player.stop()
        break

