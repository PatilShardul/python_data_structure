''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 01:21:37
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 01:21:37  
  @Description: Write a Python program to convert a list into a nested dictionary of keys.
'''
class NestedDict:
    def __init__(self):
        self.original_list=[1,2,3,4]
        self.nested_dictionary=dict()
    def create_nested_dictionary(self):
        self.nested_dictionary = current = {}
        for val in self.original_list:
            current[val] = {}
            current = current[val]
        print(self.nested_dictionary)
if __name__ == "__main__":
    nested_dict=NestedDict()
    nested_dict.create_nested_dictionary()    
