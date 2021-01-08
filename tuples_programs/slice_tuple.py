''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 18:36:29
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 18:36:29  
  @Description : program to to slice a tuple
'''
class SliceTuple:
    
    def get_tuple_elements(self):
        """This Method Takes comma seperated input elements from user andf store in tuple
            Also Take starting and ending index location
        """
        try:
            self.list_element=[eval(element) for element in input("Enter the Tuples Elements : ").split(",")]
            self.original_tuple=tuple(self.list_element)
            self.start_index=int(input("Enter The Start index : "))
            self.end_index=int(input("Enter The End index : "))
            self.slice_tuple_elements(self.start_index,self.end_index)
        except Exception as e : 
            print(e)
            self.get_tuple_elements()    

    def slice_tuple_elements(self,start_index,end_index):
        """This method Slices the Tuple

        Args:
            first_index (int): startind index for slicing
            last_index (int): ending index for slicing
        """
        new_tuple=tuple(self.original_tuple[start_index:end_index+1])
        print(new_tuple)    

if __name__ == "__main__":
    slice_tuple=SliceTuple()
    slice_tuple.get_tuple_elements()