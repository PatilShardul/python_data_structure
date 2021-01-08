''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 16:13:40
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 16:13:40  
  @Description : python program to create a tuple 
'''
class CreateTuple:
    def get_tuple_elements(self):
        """This Method Takes comma seperated input elements from user andf store in tuple
        """
        self.tuple_element=[eval(element) for element in input("Enter the Tuples Elements : ").split(",")]
        self.original_tuple=tuple(self.tuple_element)
        self.print_tuple_elements()


    def print_tuple_elements(self):
        """This menthod prints a tuple elements
        """
        print(self.original_tuple)

if __name__ == "__main__":
    create_tuple=CreateTuple()
    create_tuple.get_tuple_elements()