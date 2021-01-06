''' 
  @Author: Shardul Patil
  @Date: 2021-01-06 23:09:04
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-06 23:09:04  
  @Description : check String length is greater than 3 char join "ing" if the string doesn't end in "ing" else join "ly"  
'''
class ReplaceStringEnding:
    def __init__(self):
        pass
    
    def get_string_from_user(self):
        """
        Get input String From the user and call check_string_length method
        """
        try:
            self.original_string= input("Enter The String")
            self.check_string_length()
        except Exception as e:
            print("Enter Valid Values",e)
            self.get_string_from_user()
    def check_string_length(self):
        """
        check The length of string is greater than equal to 3 ,if true then call check_string_ending() 
        """
        
        if(len(self.original_string) >= 3):
            self.check_string_ending()  
        else:
            print("String Length is Less Than 3")
            self.get_string_from_user()

    def check_string_ending(self):
        """
        Check String Ending if it is ending with ing the pass "ly" to replace string method
        else pass ing to replace String method
        """
        if(self.original_string[-3:]=="ing"):
            self.replace_string_ending("ly")
        else:
            self.replace_string_ending("ing")    

    def replace_string_ending(self,replacement_val):
        """
        Concat replacement value to original string and store it  in the updated string
        Args: replacement_val > string that is to be concatinated at the end of the original string 
        """
        updated_string=self.original_string+replacement_val
        print(updated_string)
if __name__ == "__main__":
      replace_string_ending=ReplaceStringEnding()
      replace_string_ending.get_string_from_user()      