# brain/search_tool.py — Project KOKI
# "search X" sunke DuckDuckGo se result laata hai

from ddgs import DDGS

def web_search(query: str) -> str:
    """
    DuckDuckGo se top 3 results fetch karta hai.
    Free, no API key, privacy-first.
    """
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=3))

        if not results:
            return f"Koi result nahi mila '{query}' ke liye."

        reply = f"🔍 Search results for '{query}':\n\n"
        for i, r in enumerate(results, 1):
            reply += f"{i}. {r['title']}\n"
            reply += f"   {r['body'][:150]}...\n"
            reply += f"   {r['href']}\n\n"

        return reply.strip()

    except Exception as e:
        return f"Search nahi ho payi — {e}"