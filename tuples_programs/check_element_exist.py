''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 17:50:55
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 17:50:55  
  @Description : check whether an element exist within a tuple
'''
class CheckElement:
    
    def get_tuple_elements(self):
        """This Method Takes comma seperated input elements from user andf store in tuple
           and Take element that need to be checked in the tuple 
        """
        try:

            self.list_element=[eval(element) for element in input("Enter the Tuples Elements : ").split(",")]
            self.original_tuple=tuple(self.list_element)
            user_element=eval(input("Enter User Element"))
            self.check_element_in_tuple(user_element)
        except Exception as e:
            print(e)
            self.get_tuple_elements()

    def check_element_in_tuple(self,user_element):
        """This menthod check if the element is present in the tuple
        Args:
            user_element ([Any]): element that need to be check if present in the tuple
        """

        if user_element in self.original_tuple: 
            print (f'{user_element} exist in tuple')
        else:
             print('does not exist')

        
if __name__ == "__main__":

    check=CheckElement()
    check.get_tuple_elements()