import sys
from collections import Counter

def read_file(filename):
    try:
        with open(filename,'r',encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        sys.exit(1)

def count_words(text):
    words = text.lower().split()
    return Counter(words)

def main():
    if len(sys.argv) < 2:
        print("Usage: python wordcounter.py <filename>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    text = read_file(file_path)
    word_count = count_words(text)

    print("\n=== Top 10 words ===")
    for word, count in word_count.most_common(10):
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()