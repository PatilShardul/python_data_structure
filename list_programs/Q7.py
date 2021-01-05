''' 
  @Author: Shardul Patil
  @Date: 2021-01-05 08:55:51
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-05 08:55:51  
'''
class Q7:
    def __init__(self):
        self.general_list = ["abc","abc","def","a","b","5","1991","test","pop","a"]
        self.copied_list = list()
        self.cloned_list = list()
    def copy_list(self):

        self.copied_list=self.general_list.copy()
        print(f"copied list :  {self.copied_list}")
    def clone_list(self):

        self.cloned_list=self.general_list[0:]
        print(f"cloned list :  {self.cloned_list}")
    
if __name__ == "__main__":
    q7 = Q7()
    q7.copy_list()
    q7.clone_list()