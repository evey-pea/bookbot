from stats import get_num_words
from stats import get_num_characters
from stats import get_num_characters_sorted

def get_book_txt(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_path = 'books/frankenstein.txt'
    text = (get_book_txt(file_path))
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print(f"--------- Character Count -------")
    
    for each in get_num_characters_sorted(get_num_characters(text)):
        print(f"{each['char']}: {each['num']}")
    
main()