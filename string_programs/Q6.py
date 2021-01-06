''' 
  @Author: Shardul Patil
  @Date: 2021-01-06 23:47:24
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-06 23:47:24  
  @Description : Module to Convert String to lower and upper case  
'''
class ToLowerToUpper:
    def __init__(self):
        pass
    def get_string_from_user(self):
        """
        Get String from user and apps it to convert to upper and convert to lower function
        """
        user_string=input("Enter The String : ")
        print(f"User String is {user_string}")
        print(f"String in Upper Case : {self.convert_string_to_upper_case(user_string)}")
        print(f"STring in Lower Case : {self.convert_string_to_lower_case(user_string)}")
    
    def convert_string_to_upper_case(self,user_string):
        """
        Convert User_string to Upper Case and Return
        Args: user_string > Value inserted by user
        return: String with all Upper Cases Character
        """
        return user_string.upper()
        
    def convert_string_to_lower_case(self,user_string):
        """
        Convert User_string to Lower Case and Return
        Args: user_string > Value inserted by user
        return: String with all Lower Cases Character
        """
        return user_string.lower()

if __name__ == "__main__":
    to_lower_to_upper=ToLowerToUpper()
    to_lower_to_upper.get_string_from_user()    