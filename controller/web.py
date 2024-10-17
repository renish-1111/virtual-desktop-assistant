import webbrowser

def handle_web_commands(command):
    command = command.lower()

    if "search" in command:
        search_query = command.split("search")[-1].strip()
        webbrowser.open(f"http://www.google.com/search?q={search_query}")
        return f"Searching Google for {search_query}."

    websites = {
        "google": "http://www.google.com",
        "youtube": "http://www.youtube.com",
        "leetcode": "http://www.leetcode.com",
        "github": "http://www.github.com",
        "facebook": "http://www.facebook.com",
        "instagram": "http://www.instagram.com",
        "twitter": "http://www.twitter.com",
        "linkedin": "http://www.linkedin.com",
        "whatsapp": "http://www.whatsapp.com",
        "gmail": "http://www.gmail.com",
        "amazon": "http://www.amazon.com",
        "flipkart": "http://www.flipkart.com",
        "netflix": "http://www.netflix.com",
        "spotify": "http://www.spotify.com",
        "chrome": "http://www.chrome.com",
        "setting": "ms-settings:"
        
    }

    for site in websites:
        if site in command:
            webbrowser.open(websites[site])
            return f"Opening {site.capitalize()}."
    
    return "Website not recognized."
