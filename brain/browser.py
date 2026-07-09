import webbrowser

WEBSITES = {
    "youtube": "https://youtube.com",
    "github": "https://github.com",
    "linkedin": "https://linkedin.com",
    "spotify": "https://spotify.com",
    "gmail": "https://mail.google.com",
    "chatgpt": "https://chat.openai.com",
    "claude": "https://claude.ai",
    "gemini": "https://gemini.google.com",
    "instagram": "https://instagram.com",
    "x": "https://x.com",
    "twitter": "https://x.com",
}


def open_website(site):

    site = site.lower().strip()

    if site in WEBSITES:
        webbrowser.open(WEBSITES[site])
        return f"Opening {site}..."

    return f"Sorry, I don't know the website '{site}'."