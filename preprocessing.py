import re
import emoji

def clean_tweet(text):
    if not isinstance(text, str):  # Check if it's not a string
        return ""  # Replace with an empty string
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"@\w+", "", text)  # Remove mentions
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Remove special characters
    text = emoji.demojize(text)  # Convert emojis to text
    return text.lower()

