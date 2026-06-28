# brain/music.py — Project KOKI
# Week 3: Basic YouTube Music search (browser)
# Week 4+: Direct play with yt-dlp

import webbrowser
import urllib.parse

def play_on_youtube_music(query):
    try:
        encoded = urllib.parse.quote(query)
        url = f"https://music.youtube.com/search?q={encoded}"
        webbrowser.open(url)
        return f"Searching '{query}' on YouTube Music 🎵"
    except Exception as e:
        return f"Music play nahi ho payi — {e}"