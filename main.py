from stats import get_num_words
from stats import get_num_characters
from stats import get_num_characters_sorted
import sys

def get_book_txt(file_path):
    try:
        with open(file_path, "r") as f:
            file_contents = f.read()
        return file_contents
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
        sys.exit(1)
    except IOError:
        print(f"An error occurred opening {file_path}")
        sys.exit(1)

def main():
 
    if len(sys.argv) == 2:
        file_path = ""

        file_path = sys.argv[1]
        text = (get_book_txt(file_path))
        print(f"============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        
        print(f"----------- Word Count ----------")
        print(f"Found {get_num_words(text)} total words")
        
        print(f"--------- Character Count -------")
        for each in get_num_characters_sorted(get_num_characters(text)):
            print(f"{each['char']}: {each['num']}")
        
        sys.exit(0)

    else:
        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)
        

main()