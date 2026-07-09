"""
KOKI Tool Registry
Week 4

Maps tool names to their handler functions.
"""

from brain.music import play_on_youtube_music
from brain.search_tool import web_search
from brain.git_tool import git_commit
from brain.browser import open_website

TOOLS = {
    "music": play_on_youtube_music,
    "search": web_search,
    "git": git_commit,
    "browser": open_website,
}