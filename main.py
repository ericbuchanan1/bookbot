from stats import get_num_words,get_num_letter,sort
from sys import argv,exit

def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents

def main():
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    for arg in argv:
        file_path = arg
    book_text = get_book_text(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("--------- Character Count -------")
    num_letter = get_num_letter(book_text)
    sort(num_letter)


main()