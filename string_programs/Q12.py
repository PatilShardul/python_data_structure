''' 
  @Author: Shardul Patil
  @Date: 2021-01-07 00:49:28
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-07 00:49:28  
  @Discription : Module to make first n char lowercase 
'''
class ReverseString:
    def __init__(self):
        pass
    
    def get_string_from_user(self):
        """
        Get input String and number of characters From user 
        """
        try:
            self.user_string=input("Enter String")
            number_of_character=int(input("Enter the no. character : "))
            self.convert_to_lowercase(number_of_character)
        except Exception as e :
            print("Enter Valid String : ",e)
            self.get_string_from_user()    
    
    def convert_to_lowercase(self,number_of_character):
        """
        get firstSubstring and covert it to lower case and get second part from the original string and concatinate 
        both the firstsubstring and second sub string
        """
        first_sub_string=self.user_string[0:number_of_character].lower()
        second_sub_string=self.user_string[number_of_character:]
        final_string=first_sub_string+second_sub_string
        print(final_string)
        
if __name__ == "__main__":
    reverse_string=ReverseString()
    reverse_string.get_string_from_user()