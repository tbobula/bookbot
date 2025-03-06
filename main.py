import sys

from stats import get_num_words, get_characters, sort_dictionary
from raport import raport

def get_book_text(book):
    with open(book) as f:
        content = f.read()
        return content

def main():
    args = sys.argv
    if len(args) == 2:
        book_name = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    content = get_book_text(book_name)

    num_words = get_num_words(content)
    # print(f"{num_words} words found in the document")

    characters = get_characters(content)
    sorted_characters = sort_dictionary(characters)
    raport(book_name, num_words, sorted_characters)



if __name__ == "__main__":
    main()



