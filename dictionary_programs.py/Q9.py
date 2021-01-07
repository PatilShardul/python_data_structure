''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 00:36:25
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 00:36:25  
  @Description : Python program to print a dictionary in table format
'''
class DictionaryToTable:
    
    def __init__(self):
        """
        Initialize original dictionary
        """
        self.original_dictionary={"a":"1","b":"2","c":"3","d":"4"}
    
    def print_dict_in_table_format(self):
        """
        Print Dictionary in table format
        """
        for element in self.original_dictionary:
            print(f" key > {element}, value > {self.original_dictionary[element]}")    

if __name__ == "__main__":
    dict_to_table=DictionaryToTable()
    dict_to_table.print_dict_in_table_format()    