def get_book_text(filepath):

    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def word_counter(file_contents):
   
   file_contents = file_contents.split()
   num_words = 0
   for content in file_contents:
      num_words +=1
   return num_words



def main():
 
 content= get_book_text("books/frankenstein.txt")
 num_words = word_counter(content)
 
 print(f"{num_words} words found in the document")

    
main()
