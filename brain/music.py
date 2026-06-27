# brain/music.py — Project KOKI
# "play X" sunke YouTube Music mein search karta hai

import webbrowser

def play_on_youtube_music(query):
    """
    query ko YouTube Music search URL mein convert karta hai
    aur browser mein kholta hai.
    """
    search_query = query.strip().replace(" ", "+")
    url = f"https://music.youtube.com/search?q={search_query}"
    webbrowser.open(url)
    return f"Playing '{query}' on YouTube Music 🎵"