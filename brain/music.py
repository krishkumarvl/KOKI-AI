# brain/music.py — Project KOKI
# "play X" sunke YouTube pe direct video kholta hai

import webbrowser
import yt_dlp

def play_on_youtube_music(query: str) -> str:
    """
    yt-dlp se YouTube pe search karta hai,
    pehle result ka direct URL browser mein kholta hai.
    """
    try:
        ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "noplaylist": True,
            "extract_flat": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch1:{query}", download=False)
            video = info["entries"][0]
            video_id = video["id"]
            title = video["title"]
            url = f"https://www.youtube.com/watch?v={video_id}"

        webbrowser.open(url)
        return f"Playing: {title} 🎵"

    except Exception as e:
        return f"Music play nahi ho payi — {e}"