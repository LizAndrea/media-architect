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
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            # Extracción de datos básicos
            title = info.get('title', 'Unknown Title')
            description = info.get('description', '')
            duration = info.get('duration', 0)
            view_count = info.get('view_count', 0)
            
            # Revisar si hay subtitulos
            subs = info.get('subtitles', {})
            auto_subs = info.get('automatic_captions', {})
            
            print(f"--- VIDEO: {title} ---")
            print(f"URL: {url}")
            print(f"Duration: {duration}s")
            print(f"Views: {view_count}")
            print(f"Description snippet: {description[:200]}...\n")
            print("Subtitles available:", list(subs.keys()) + list(auto_subs.keys()))
            print("\n")
            
        except Exception as e:
            print(f"Error fetching info for {url}: {e}")

urls = [
    "https://www.youtube.com/watch?v=uXlWYZ022zU",
    "https://www.youtube.com/watch?v=IXWEQHCKR20",
    "https://www.youtube.com/watch?v=u3ybWiEUaUU",
    "https://www.youtube.com/watch?v=an7krXQW4aU",
    "https://www.youtube.com/watch?v=rYITKyEGLSM"
]

for u in urls:
    get_video_info(u)
