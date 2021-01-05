''' 
  @Author: Shardul Patil
  @Date: 2021-01-05 09:43:19
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-05 09:43:19  
'''
class Q12:
    
    def __init__(self):

        self.first_word_list = ["abc","def","a","b","5","1991","test","pop"]
        self.second_word_list = ["abc","def","51","19911","test1","pop1"]
        self.difference_list=list()
    
    def check_comman_words(self):

        for word in self.first_word_list:
            if word not in self.second_word_list:
                self.difference_list.append(word)
        print(self.difference_list)

if __name__ == "__main__":
    q12 = Q12()
    q12.check_comman_words()       