import random

def tell_joke():
    jokes = [
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I told my computer I needed a break, and now it won’t stop sending me to the beach!",
        "Why don’t scientists trust atoms? Because they make up everything!",
        "What do you call a fish wearing a crown? A kingfish!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "What do you call a pile of cats? A meowtain!",
    ]
    return random.choice(jokes)
