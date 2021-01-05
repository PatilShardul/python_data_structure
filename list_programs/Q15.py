''' 
  @Author: Shardul Patil
  @Date: 2021-01-05 10:05:55
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-05 10:05:55  
'''
class Q15:
    def __init__(self):
        self.first_word_list = ["abc","def","a","b","5","1991","test","pop"]
        self.second_word_list = ["ab1c","def","a","b","5","19911","test","pop1"]
        self.command_word_list = list()
    def get_comman_words(self):

        for word in self.first_word_list:
            if word in self.second_word_list:
                self.command_word_list.append(word)
        print(self.command_word_list)        

if __name__ == "__main__":
    q15 = Q15()
    q15.get_comman_words()