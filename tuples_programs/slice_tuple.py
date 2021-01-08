''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 18:49:02
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 18:49:02  
  @Description :  Python program to reverse a tuple.
'''
class ReverseTuple:
    
    def get_tuple_elements(self):
        """This Method Takes comma seperated input elements from user andf store in tuple
        """
        try:
            self.list_element=[eval(element) for element in input("Enter the Tuples Elements : ").split(",")]
            self.original_tuple=tuple(self.list_element)
            
            print(f"original tuple : {self.original_tuple}")
            
            self.reverse_tuple_elements()
        except Exception as e : 
            
            print(e)
            self.get_tuple_elements()    

    def reverse_tuple_elements(self):
        """This method reverse the Tuple
        """
        reverse_tuple=reversed(self.original_tuple)
        print(f"reversed tuple : {tuple(reverse_tuple)}")    

if __name__ == "__main__":
    reverse_tuple=ReverseTuple()
    reverse_tuple.get_tuple_elements()