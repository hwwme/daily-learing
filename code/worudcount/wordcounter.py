import sys
import string
from collections import Counter
import re

class wordcounter:
    """
    词频统计类
    """
    def __init__(self,filename):
        self.filename = filename
        self.text = self.read_file(filename)
        
    def read_file(self,filename):
        try:
            with open(filename,'r',encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")
            sys.exit(1)

    def show_top_words(self,n=10):
        # 去除所有标点符号（包括中文标点符号）
        # 使用正则表达式匹配所有Unicode标点符号类别
        text_no_punct = re.sub(r'[^\w\s]', '', self.text)
        
        # 转换为小写并分割单词
        words = text_no_punct.lower().split()
        word_count = Counter(words)
        print(f"\n=== Top {n} words ===")
        for word, count in word_count.most_common(n):
            print(f"{word}: {count}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python wordcounter.py <filename>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    wc = wordcounter(file_path)
    wc.show_top_words(1)


if __name__ == "__main__":
    main()