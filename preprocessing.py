import regex as re
import emoji

def clean_tweet(text):
    if not isinstance(text, str):  # Check if it's not a string
        return ""  # Replace with an empty string
    text = emoji.demojize(text)  # Convert emojis to text
    text = re.sub(r'\brt\b', '', text, flags=re.IGNORECASE)  # Remove 'rt' or 'RT'
    text = text.replace('\n', ' ')  # Replace newlines with space
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"@\w+", "", text)  # Remove mentions
    text = re.sub(r'[^\p{L}\s:_\-]', "", text)  # Keep all letters (from any language) and common symbols
    return text.lower().strip()

def add_cleaned_prefix(col_name):
    if not col_name.startswith('cleaned_'):
        return f'cleaned_{col_name}'
    return col_name