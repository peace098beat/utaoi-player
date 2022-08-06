
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

test_url = 'https://www.youtube.com/watch?v=dTG7R66Mrs4'
assert yt_url2id(test_url)== 'dTG7R66Mrs4'

from pathlib import Path

def not_exists(url, cache_dir):

    vid = yt_url2id(url)
    cache_name = f'{vid}.mp3'

    return not Path(cache_dir, cache_name).exists()


PLAYLIST_PATH = 'playlist.txt'
CACHE_DIR = './cache'

# list
urls = read_playlist(PLAYLIST_PATH)
assert len(urls) == 2, len(urls)

urls = [u for u in urls if not_exists(u, CACHE_DIR)]
assert len(urls) == 0

print(urls)
