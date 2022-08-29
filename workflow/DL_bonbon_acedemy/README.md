
# download - bon bon acedemy


https://www.youtube.com/c/bom2ac



## yt_dlp

Recomend

'''
sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp
'''



## (not recommend) youtube-dl

'''

youtube-dl --output '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' \
	--no-overwrites\
	--write-info-json\
	https://www.youtube.com/playlist?list=PL1DnK3_eexigK84NQ400lB4Jh81MQzzxM
	# --no-cache-dir\
	# --rm-cache-dir\

'''
