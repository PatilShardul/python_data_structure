''' 
  @Author: Shardul Patil
  @Date: 2021-01-05 09:08:41
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-05 09:08:41  
'''
class Q9:
    def __init__(self):
        self.first_word_list = ["abc","def","a","b","5","1991","test","pop"]
        self.second_word_list = ["ab1c","def1","a1","b1","51","19911","test1","pop1"]
    def check_comman_words(self):
        have_command_element=False

        for word in self.first_word_list:
            if word in self.second_word_list:
                have_command_element=True
                break
        if(have_command_element):
            print("List Have Comman Elements")
        else:
            print("No comman element")

if __name__ == "__main__":
    q9 = Q9()
    q9.check_comman_words()