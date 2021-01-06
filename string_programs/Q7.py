''' 
  @Author: Shardul Patil
  @Date: 2021-01-07 00:10:14
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-07 00:10:14  
  @Description : sort comman seperated Word list aplhanumerically
'''
class SortWords:
    def __init__(self):
        """
        Initialize comma seperated value as string and comma seperated values set
        """
        self.comma_seperated_string=str()
        self.comma_seperated_set=set()
    
    def get_value_from_user(self):
        """
        Take Comma Seprated String from user
        then call convert_value_string_to_set(),convert_set_to_list(),sort_list() methods
        """

        self.comma_seperated_string=input("Enter Comma Seperated Values : ")
        self.convert_value_string_to_set()
        self.convert_set_to_list()
        self.sort_list()
    
    def convert_value_string_to_set(self):
        """
        Convert string to set after spiting string on the basis of comma
        """
        
        for value in self.comma_seperated_string.split(","):
            self.comma_seperated_set.add(value)
    
    def convert_set_to_list(self):
        """
        Convert Comma seperated set to list 
        """
        self.comma_seperated_list=list(self.comma_seperated_set)
    
    def sort_list(self):
        """
        Sort The List having values that were comma seperate earler in the program
        """
        print(sorted(self.comma_seperated_list))

if __name__ == "__main__":
    sort_word = SortWords()
    sort_word.get_value_from_user()        