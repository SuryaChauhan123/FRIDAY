import webbrowser
from urllib.parse import quote

def searchweb(query):
    webbrowser.open(
        f"https://www.google.com/search?q={quote(query)}"
    )

    return f"searching {query}, sir"
