from stats import get_num_words, get_letter_count


def get_book_text(filepath):
    with open(filepath) as f:
        return (f.read())


def main():
    text = "books/frankenstein.txt"
    word_count = get_num_words(get_book_text(text))
    char_count = get_letter_count(get_book_text(text))
    print(f"{word_count} words found in the document")
    print(char_count)


main()
