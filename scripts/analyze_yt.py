import yt_dlp
import sys
import json

def get_video_info(url):
    ydl_opts = {
        'skip_download': True,
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitleslangs': ['es', 'en'],
        'quiet': True,
        'no_warnings': True,
        'dump_single_json': True,
        'cookiefile': '/home/henrytaby/cookies/cookies.txt',
        'extractor_args': {'youtube': {'player_client': ['android']}},
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            title = info.get('title', 'Unknown Title')
            description = info.get('description', '')
            duration = info.get('duration', 0)
            
            print(f"--- VIDEO: {title} ---")
            print(f"URL: {url}")
            print(f"Duration: {duration}s")
            print(f"Description snippet: {description[:200]}...\n")
            
        except Exception as e:
            print(f"Error fetching info for {url}: {e}")

urls = [
    "https://www.youtube.com/watch?v=To6pOimJxlM"
]

for u in urls:
    get_video_info(u)
