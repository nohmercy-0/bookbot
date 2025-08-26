import sys
from stats import (
    count_words,
    count_char, 
    sort
)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars = count_char(text)
    sorted_chars = sort(chars)
    report(book_path, num_words, sorted_chars)
    
 
def get_book_text(pathfile):
    with open(pathfile) as f:
        return f.read()

def report(book_path, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if not item["char"].isalpha():
            continue
        print(f"{item["char"]}: {item["num"]}")
        
    print("============= END ===============")

if __name__ == "__main__":
    main()