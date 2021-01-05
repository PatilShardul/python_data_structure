''' 
  @Author: Shardul Patil
  @Date: 2021-01-05 09:43:19
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-05 09:43:19  
'''
class Q13:
    
    def __init__(self):

        self.first_word_list = ["abc","def","a","b","5","1991","test","pop"]
        self.second_word_list = ["abc","def","51","19911","test1","pop1"]
        self.difference_list=list()
    
    def append_list(self):
        print(f"List 1 :  {self.first_word_list}")
        print(f"List 2 :  {self.second_word_list}")

        self.second_word_list.extend(self.first_word_list)
        print(f"Appended list :  {self.second_word_list}")

if __name__ == "__main__":
    q13 = Q13()
    q13.append_list() 