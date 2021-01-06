''' 
  @Author: Shardul Patil
  @Date: 2021-01-07 00:49:28
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-07 00:49:28  
  @Discription : Module to reverse the String 
'''
class ReverseString:
    def __init__(self):
        pass
    
    def get_string_from_user(self):
        """
        Get input String From user 
        """
        try:
            self.user_string=input("Enter String")
            self.reverse_string()
        except Exception as e :
            print("Enter Valid String : ",e)
            self.get_string_from_user()    
    def reverse_string(self):
        """
        reverse string usinf reversed function and join is to ''
        """
        reversed_string=''.join(reversed(self.user_string))
        print(reversed_string)    

if __name__ == "__main__":
    reverse_string=ReverseString()
    reverse_string.get_string_from_user()    