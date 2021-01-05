''' 
  @Author: Shardul Patil
  @Date: 2021-01-05 09:59:49
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-05 09:59:49  
'''
class Q14:
    def __init__(self):
        self.first_string_list = ["abc","def","a","b","5","1991","test","pop"]
        self.second_string_list = ["p","def","a","b","5","1991","test","abc"]
        self.is_circular=False
    
    def check_list_is_circular(self):
       if ((self.first_string_list[0] == self.second_string_list[-1]) and (self.first_string_list[-1] == self.second_string_list[0] )):
            print("List are circular")
       else :
            print("List are not circular")     
if __name__ == "__main__":
    q14 = Q14()
    q14.check_list_is_circular()