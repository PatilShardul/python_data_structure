''' 
  @Author: Shardul Patil
  @Date: 2021-01-05 09:01:52
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-05 09:01:52  
'''
class Q8:
    def __init__(self):
        self.word_list = ["abc","def","a","b","5","1991","test","pop"]
        self.computed_word_list = list()
    def get_valid_length_words(self):
        minimum_length=int(input("Enter the minimum length of the word"))
        for word in self.word_list:
            if(len(word) >= minimum_length):
                self.computed_word_list.append(word) 
        print(self.computed_word_list)
if __name__ == "__main__":
    q8 = Q8()
    q8.get_valid_length_words()