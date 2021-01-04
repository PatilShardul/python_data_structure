''' 
  @Author: Shardul Patil
  @Date: 2021-01-04 22:59:18
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-04 22:59:18  
'''
class Q1:
    def __init__(self):
        pass
    def get_user_name(self):
        
        first_name=input("Enter User Name")
        last_name=input("Enter User Name")
        self.reverse_user_name(first_name,last_name)

    def reverse_user_name(self,first_name,last_name):    
        
        user_name = list()

        first_part=list(first_name)
        first_part.reverse()
        last_part=list(last_name)
        last_part.reverse()
        
        user_name.append(last_part)
        user_name.append(first_part)
        
        print(user_name)
        
if __name__ == "__main__":
    q1 = Q1()
    q1.get_user_name()
