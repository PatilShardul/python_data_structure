''' 
  @Author: Shardul Patil
  @Date: 2021-01-04 22:59:05
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-04 22:59:05  
'''
class Q2:

    def __init__(self):
        pass
    
    
    def get_user_values(self):
        
        letter_list = input("Enter Comma Seperated Values : ")

        self.put_values_in_list(letter_list)
        self.put_values_in_tuples(letter_list)
    
    def put_values_in_list(self,letter_list):
       
       char_list = list(letter_list.split(","))
       print(char_list) 
        
    
    
    def put_values_in_tuples(self,letter_list):
        char_tuple = tuple(letter_list.split(","))
        print(char_tuple) 
    
if __name__ == "__main__":
    q2 = Q2()
    q2.get_user_values()
