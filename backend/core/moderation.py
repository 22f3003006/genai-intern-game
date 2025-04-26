profanity = {
    "ass", "bastard", "bitch", "crap", "damn", "dick", "fuck",
    "motherfucker", "nigga", "nigger", "piss", "shit", "slut", "whore",
    "cock", "cunt", "faggot", "douche", "bollocks", "bugger"
}

def is_clean(text: str) -> bool:
    words = text.lower().split()
    return not any(word in profanity for word in words)
