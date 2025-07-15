from stats import word_counter ,character_count , sorting
import sys 

if len(sys.argv) != 2:
   
   print("Usage: python3 main.py <path_to_book>")
   sys.exit(1)
else:
   
   book_path = sys.argv[1] 

def get_book_text(filepath):

    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
 
 print( "============ BOOKBOT ============")
 print(f"Analyzing book found at {book_path}...")
 print("----------- Word Count ----------")
 content= get_book_text(book_path)
 num_words = word_counter(content)
 dictionary = character_count(content)
 sorted_list = sorting(dictionary)
 print("--------- Character Count -------")
 print(f"Found {num_words} total words")
 for item in sorted_list:
    if item["char"].isalpha():
       print(f"{item['char']}: {item['num']}")
       
 print("============= END ===============")       
 
 
    
main()
