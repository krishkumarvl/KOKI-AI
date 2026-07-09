def detect_tool(message: str):

    message = message.lower().strip()

    # Music
    if (
        message.startswith("play ")
        or "play " in message
        or "song" in message
        or "music" in message
    ):
        return "music"

    # Search
    if (
        message.startswith("search ")
        or "search " in message
        or "look up" in message
        or "find" in message
    ):
        return "search"

    # Git
    if message.startswith("git commit "):
        return "git"

    # Browser
    if message.startswith("open "):
        return "browser"
    
    # Calculator
    if message.startswith("calculate "):
        return "calculator"

    return None