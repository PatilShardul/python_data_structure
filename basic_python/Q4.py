''' 
  @Author: Shardul Patil
  @Date: 2021-01-04 23:23:40
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-04 23:23:40  
'''
class Q4:
    
    def __init__(self):
        pass

    def get_user_method(self):
        
        method = input("Enter Method name")
        self.check_mehtod_validity(method) 

    def check_mehtod_validity(self,method):
        try:
                print(help(method))    
        except Exception as e:
            print(f"{method} is not a built in function ",e)    


if __name__ == "__main__":
    q4 = Q4()
    q4.get_user_method()

