''' 
  @Author: Shardul Patil
  @Date: 2021-01-07 00:34:33
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-07 00:34:33  
  @Description : Module to count substring in original string
'''
class CountOccurances:
    def __init__(self):
        pass
    def get_user_string_input(self):
        """
        Get original String From the User  
        """
        try:
            self.original_string=input("Enter String : ")
            self.get_sub_string_from_user()
        except:
            print("Enter Valid String")
            self.get_user_string_input()
    def get_sub_string_from_user(self):
        """
        Get Sub String from the User
        """
        try:
            self.sub_string=input("Enter String : ")
            self.count_occurance_of_sub_string()
        except:
            print("Enter Valid Sub String")
            self.get_sub_string_from_user()
    def count_occurance_of_sub_string(self):
        """
        Count the Number of occurance of Sub-String in the original String 
        """
        
        print(self.original_string.count(self.sub_string))
        

if __name__ == "__main__":
    count_occurance=CountOccurances()
    count_occurance.get_user_string_input()