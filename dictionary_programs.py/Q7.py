''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 00:16:46
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 00:16:46  
  @Description: Write a Python program to print all unique values in a dictionary
'''
class UniqueValue:
    def __init__(self):
    """
    Initailize a Original Dictionary and unique values set
    """    
            self.original_dictionary= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
            self.unique_set=set()
    def store_dictionary_val_in_set(self):
        """
        Get element from list of dictionary and get val from element is dictinary and store it in the set
        """
        for element in self.original_dictionary:
            for val in element.values():
                self.unique_set.add(val)
        
        self.print_set()
    
    def print_set(self):
        """
        Print Unique Value set
        """
        print(self.unique_set)

if __name__ == "__main__":
    
    unique_values=UniqueValue()
    unique_values.store_dictionary_val_in_set()