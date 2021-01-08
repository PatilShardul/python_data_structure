''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 12:08:35
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 12:08:35  
  @Description : Python program to count the number occurrence of a specific character in a string
'''
class NumberOfOccurance:
    def get_input_from_user(self):
        """
        Get String From the user 
        """
        user_string=input("Enter String")
        user_value=input("Enter The Value to count Occurance : ")
        self.count_number_of_occurances(user_string,user_value)

    def count_number_of_occurances(self,user_string,user_value):
        """Count number of occurance of a character in string

        Args:
            user_string ([string]): String given by the user
            user_value ([string]): charater given by the user
        """
        print(user_string.count(user_value))

if __name__ == "__main__":
    
    number_of_occurance=NumberOfOccurance()
    number_of_occurance.get_input_from_user()

        