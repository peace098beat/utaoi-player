# home
# youtube-dl --output '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' \
# 	--no-overwrites\
# 	--write-info-json\
# 	https://www.youtube.com/c/bom2ac
# --simulate \
# --no-cache-dir\
# --rm-cache-dir\
# --skip-download\

# eigo no uta medore
youtube-dl --output '%(playlist)s/%(playlist_index)s - %(id)s - %(title)s.%(ext)s' \
	--no-overwrites\
	--write-info-json\
	--reject-title '〈英語の歌〉'\
	https://www.youtube.com/playlist?list=PL1DnK3_eexigLrF_Jc5wvkx6vjsw9ACSn


# short movie
youtube-dl --output '%(playlist)s/%(playlist_index)s - %(id)s - %(title)s.%(ext)s' \
	--no-overwrites\
	--write-info-json\
	--reject-title '〈英語の歌〉'\
	https://www.youtube.com/playlist?list=PL1DnK3_eexigY79fq2fDGP6n9VWEArxMa


# [en] jp story
youtube-dl --output '%(playlist)s/%(playlist_index)s - %(id)s - %(title)s.%(ext)s' \
	--no-overwrites\
	--write-info-json\
	https://www.youtube.com/playlist?list=PL1DnK3_eexijoHNVWAlC69PH6VWvrhnhr

# [ja] jp story
youtube-dl --output '%(playlist)s/%(playlist_index)s - %(id)s - %(title)s.%(ext)s' \
	--no-overwrites\
	--write-info-json\
	https://www.youtube.com/playlist?list=PL1DnK3_eexihX8VAgPvk44j_VE5K4zG4_

# ehon
youtube-dl --output '%(playlist)s/%(playlist_index)s - %(id)s - %(title)s.%(ext)s' \
	--no-overwrites\
	--write-info-json\
	https://www.youtube.com/playlist?list=PL1DnK3_eexihPqUVszOo-f6vH6n0SIxkE



# uta te a so be
youtube-dl --output '%(playlist)s/%(playlist_index)s - %(id)s - %(title)s.%(ext)s' \
	--no-overwrites\
	--write-info-json\
	https://www.youtube.com/playlist?list=PL1DnK3_eexigK84NQ400lB4Jh81MQzzxM



 # nihon no uta medle
youtube-dl --output '%(playlist)s/%(playlist_index)s - %(id)s - %(title)s.%(ext)s' \
	--no-overwrites\
	--write-info-json\
	https://www.youtube.com/playlist?list=PL1DnK3_eexigyJHy58m93t3QTp733FYxP