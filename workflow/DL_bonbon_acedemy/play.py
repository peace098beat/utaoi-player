from curses.panel import new_panel
from inspect import getsource
from pathlib import Path
import glob
import vlc

CACHE_DIR = './download'


def get_sound_files(cache_dir, ext='mkv'):
    return glob.glob(f'{cache_dir}/**/*.{ext}')

v1 = get_sound_files(CACHE_DIR, ext='json')
print(len(v1))

v1 = get_sound_files(CACHE_DIR, ext='mkv')
v2 = get_sound_files(CACHE_DIR, ext='mp4')
v3 = get_sound_files(CACHE_DIR, ext='webm')
v4 = get_sound_files(CACHE_DIR, ext='m4a')

videos = v1 + v2 + v3 + v4

for i, f in enumerate(videos):
	print(i, len(videos), f)

player = vlc.MediaListPlayer()
mediaList = vlc.MediaList(videos)
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

