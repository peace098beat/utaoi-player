# home(
# 	--no-overwrites\
# 	--write-info-json\
# 	--simulate \
# 	--no-cache-dir\
# 	--rm-cace-dir\
# h	--skip-download\

# bom bom academy
# yt-dlp --output './download/%(playlist)s/%(playlist_index)s - %(id)s - %(title)s.%(ext)s' \
	# --no-overwrites\
	# --reject-title '〈英語の歌〉'\
	# https://www.youtube.com/c/bom2ac


# Utasata
yt-dlp --output './download/%(channel)s/%(playlist)s/%(playlist_index)s - %(id)s - %(title)s.%(ext)s' \
	--no-overwrites\
	https://www.youtube.com/channel/UCuICbqzz8-SvKK8kAe_IwdQ

