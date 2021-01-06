''' 
  @Author: Shardul Patil
  @Date: 2021-01-06 21:25:50
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-06 21:25:50  
  @discription : program to count character frequency in a string
'''
class CountCharFrequencyString:
    def __init__(self):
        """
        Initialize a string set to get unique element in the string and count dictionary to 
        store the char count
        """
        self.string_set=set()
        self.count_dict=dict()

    def get_string_from_user(self):
        """
        Get input String from the user And call convert_string_to_set_function 
        """

        self.user_string=input("Enter the String : ")
        self.convert_string_to_set()

    def convert_string_to_set(self):
        """
        Convert Input String to a Set of unique values in the String
        And call count frequncy method 
        """
        self.string_set.update(self.user_string)
        self.count_frequency_of_char_in_string()

    def count_frequency_of_char_in_string(self):
        """
            store each element in the string Set as Key in the Dictionary and there 
            count from input string as values
        """
        for element in self.string_set:
            self.count_dict[element]=self.user_string.count(element)
        print(self.count_dict)

if __name__ == "__main__":
    count_freq = CountCharFrequencyString()
    count_freq.get_string_from_user()