from stats import get_num_words


def get_book_text(filepath):
    with open(filepath) as f:
        return (f.read())


def main():
    count = get_num_words(get_book_text("books/frankenstein.txt"))
    print(f"{count} words found in the document")


main()
