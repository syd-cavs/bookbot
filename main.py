import sys
from stats import word_counter, character_counter, sort_char

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = f"{sys.argv[1]}"
        result = get_book_text(filepath)
        num_words = word_counter(result)
        num_char = character_counter(result)
        sorted_char = sort_char(num_char)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for char in sorted_char:
            if char["char"].isalpha():
                print(f"{char['char']}: {char['num']}")

main()
