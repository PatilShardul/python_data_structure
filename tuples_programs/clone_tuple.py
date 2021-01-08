''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 17:50:55
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 17:50:55  
  @Description : a create the clone of tuple
'''
from copy import deepcopy 
class CloneTuple:
    
    def get_tuple_elements(self):
        """This Method Takes comma seperated input elements from user andf store in tuple
        """
        self.list_element=[eval(element) for element in input("Enter the Tuples Elements : ").split(",")]
        self.original_tuple=tuple(self.list_element)
        self.clone_tuple_elements()


    def clone_tuple_elements(self):
        """This menthod creates the clone of tuple
        """
        self.tuple_clone= deepcopy(self.original_tuple)
        print(f"Cloned Tuple : {self.tuple_clone}")

if __name__ == "__main__":
    clone_tuple=CloneTuple()
    clone_tuple.get_tuple_elements()