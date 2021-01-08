''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 16:13:40
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 16:13:40  
  @Description :  Python program to remove the first occurrence of a specified element from an array.
'''
class RemoveElement:
    def get_array_elements(self):
        """This Method Takes comma seperated input elements from user andf store in array list
           and also take input element from user 
        """

        try:
            self.array_list=[eval(element) for element in input("Enter the Array Numerical Elements : ").split(",")]
            print(self.array_list)
            element=eval(input('enter the element to be removed'))
            self.remove_element(element)
        except Exception as e:
            print("please Enter a Valid Array : ",e)
            self.get_array_elements()


    def remove_element(self,element):
        """This Method delete element in the array
        Args:
            element (Any): user defined element value that need to be deleted
        """
        try:
            self.array_list.remove(element)
            print(self.array_list)
        except ValueError as e:
            print("Value doesnt exist in the list",e)
        except Exception as e:
            print("Error ",e)    
            
if __name__ == "__main__":
    remove_element=RemoveElement()
    remove_element.get_array_elements()