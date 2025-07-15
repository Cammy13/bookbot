def word_counter(file_contents):
   
   file_contents = file_contents.split()
   num_words = 0
   for content in file_contents:
      num_words +=1
   return num_words

def character_count(file_contents):
   file_contents=file_contents.lower()

   
   
   dictionary = {}
   for character in file_contents:
      if character in dictionary:
         dictionary[character] +=1
      else:
         dictionary[character] =1
   return dictionary

def sort_on(item):
    return item["num"]
     
def sorting(dictionary):
    
   dictionary_list =[]
   for character, count in dictionary.items():
     
         new_dictionary={"char":character , "num":count}
         dictionary_list.append(new_dictionary)

   dictionary_list.sort(reverse=True, key =sort_on)
   return dictionary_list 
         
             