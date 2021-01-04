''' 
  @Author: Shardul Patil
  @Date: 2021-01-05 00:00:03
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-05 00:00:03  
'''
class Q7:
    def __init__(self):
        self.user_list=[0,5,45,-5]

    def get_user_input(self):

        value = int(input("Enter Value : "))
        
        if value in self.user_list:
            print(True)
        else:
            print(False)    


if __name__ == "__main__":
    q7 = Q7()
    q7.get_user_input()