''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 17:50:55
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 17:50:55  
  @Description : convert list to tuple
'''
class ListToTuples:
    
    def get_tuple_elements(self):
        """This Method Takes comma seperated input elements from user as List and  store in tuple 
        """
        try:
            self.list_element=[eval(element) for element in input("Enter the Tuples Elements : ").split(",")]
            print(f"list : {self.list_element}")
            self.original_tuple=tuple(self.list_element)
            print(f"tuple {self.original_tuple}")
        except Exception as e:
            print(e)
            self.get_tuple_elements()
        
if __name__ == "__main__":

    list_to_tuples=ListToTuples()
    list_to_tuples.get_tuple_elements()