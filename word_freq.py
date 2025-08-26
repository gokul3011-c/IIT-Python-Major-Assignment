import sys
import re
from collections import Counter

# A simple stop words list
STOP_WORDS = {
    "the", "is", "in", "and", "to", "of", "a", "an", "for", "on", "with",
    "as", "at", "this", "that", "by", "it", "from", "or", "be", "are",
    "was", "were", "but", "not", "can", "if", "then", "so", "out", "up",
    "about", "into", "over", "after", "more", "than", "also"
}

def get_top_words(file_path, top_n=20):
    try:
        # Read file
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read().lower()

        # Tokenize words (only alphabets)
        words = re.findall(r"\b[a-z]+\b", text)

        # Remove stop words
        filtered_words = [w for w in words if w not in STOP_WORDS]

        # Count frequencies
        counter = Counter(filtered_words)

        # Print top N
        for word, freq in counter.most_common(top_n):
            print(f"{word}: {freq}")

    except FileNotFoundError:
        print("❌ File not found. Please check the path.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python word_freq.py <input_file>")
    else:
        get_top_words(sys.argv[1])

