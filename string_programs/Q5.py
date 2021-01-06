''' 
  @Author: Shardul Patil
  @Date: 2021-01-06 23:32:14
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-06 23:32:14  
  @Discriptinon : module to get max length word from a list of words
'''
class LengthOfWords:
    def __init__(self):
        """
        Initialize the word List
        """
        self.word_list=["Hello","World","this","shardul","is"]
    def get_max_length_word(self):
        """
        counting the word length , if word length is greater than max length the assig word as max_length_word
        and max_length to that word length
        """
        max_length=0
        for element in self.word_list:
            if(len(element)>=max_length):
                max_length_word=element
                max_length=len(element)
        print(max_length_word,max_length)

if __name__ == "__main__":
        length_of_word=LengthOfWords()
        length_of_word.get_max_length_word()        