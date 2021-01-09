''' 
  @Author: Shardul Patil
  @Date: 2021-01-09 09:18:03
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-09 09:18:03
  @Description:Python program to convert a list into a nested dictionary of keys.
'''
class ListToDict:
    def __init__(self):
        """Intialize List and A dictionary
        """
        self.number_list = [12,8,1,9,9,4]
        self.new_dictionary = self.current = dict()
    
    def create_number_dictionary(self):
        """Get Nested Dictionary from list  
        """
        for number in self.number_list:
            self.current[number] = {}
            self.current = self.current[number]
        print(self.new_dictionary)

if __name__ == "__main__":
    list_to_dict=ListToDict()
    list_to_dict.create_number_dictionary()        