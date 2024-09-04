import yt_dlp
import sys

# Define default path
path = r"./downloads/"

# Define download rate limit in byte
ratelimit = 5000000

# Define download format
format = 'best[ext=mp4]'

# Get url as argument
try:
    url = sys.argv[1]
except Exception:
    sys.exit('Usage: python downloader.py "URL"')

# Download all videos of a channel
if url.startswith((
    'https://www.youtube.com/c/',
    'https://www.youtube.com/channel/',
    'https://www.youtube.com/user/')):
    ydl_opts = {
        'ignoreerrors': True,
        'abort_on_unavailable_fragments': True,
        'format': format,
        'outtmpl': path + '/channels/%(uploader)s/%(title)s_%(uploader)s_%(id)s.%(ext)s',
        'ratelimit': ratelimit,
    }

# Download all videos in a playlist
elif url.startswith('https://www.youtube.com/playlist'):
    ydl_opts = {
        'ignoreerrors': True,
        'abort_on_unavailable_fragments': True,
        'format': format,
        'outtmpl': path + '/playlists/%(playlist_uploader)s_%(playlist)s/%(playlist_index)s_%(title)s_%(uploader)s_%(id)s.%(ext)s',
        'ratelimit': ratelimit,
    }

# Download single video from url
elif url.startswith((
    'https://www.youtube.com/watch',
    'https://www.youtube.com/shorts/',
    'https://www.twitch.tv/',
    'https://clips.twitch.tv/')):
    ydl_opts = {
        'ignoreerrors': True,
        'abort_on_unavailable_fragments': True,
        'format': format,
        'outtmpl': path + '/videos/%(title)s_%(uploader)s_%(id)s.%(ext)s',
        'ratelimit': ratelimit,
    }

# Downloads depending on the options set above
if ydl_opts is not None:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)
