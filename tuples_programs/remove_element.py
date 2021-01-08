''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 17:50:55
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 17:50:55  
  @Description : remove an element within a tuple
'''
class RemoveElement:
    
    def get_tuple_elements(self):
        """This Method Takes comma seperated input elements from user andf store in tuple
           and Take element that need to be removed from the tuple 
        """
        try:

            self.list_element=[eval(element) for element in input("Enter the Tuples Elements : ").split(",")]
            self.original_tuple=tuple(self.list_element)
            user_element=eval(input("Enter User Element"))
            
            if user_element in self.original_tuple:
                self.remove_element(user_element)
        
        except Exception as e:
            print(e)
            self.get_tuple_elements()

    def remove_element(self,user_element):
        """This method remove a element from the tuple
        Args:
            user_element ([Any]): element that need to be check if present in the tuple
        """
        element_index=self.original_tuple.index(user_element)
        self.new_tuple=self.original_tuple[:element_index]+self.original_tuple[element_index+1:]
        print(self.new_tuple)

        
if __name__ == "__main__":

    remove=RemoveElement()
    remove.get_tuple_elements()