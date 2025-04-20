from stats import get_num_words, get_letter_count, get_sorted_dict
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        return (f.read())


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = sys.argv[1]
    word_count = get_num_words(get_book_text(text))
    char_count = get_letter_count(get_book_text(text))
    sorted_counts = get_sorted_dict(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {text}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted_counts:
        if char["value"].isalpha():
            print(f"{char['value']}: {char['count']}")
    print("============= END ===============")


main()
