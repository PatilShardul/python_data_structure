''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 16:13:40
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 16:13:40  
  @Description : Python program to get the number of occurrences of a specified element in an array.  
'''
class CountElement:
    def get_array_elements(self):
        """This Method Takes comma seperated input elements from user andf store in array list
           and also take input element from user 
        """

        try:
            self.array_list=[eval(element) for element in input("Enter the Array Numerical Elements : ").split(",")]
            print(self.array_list)
            element=eval(input('enter the element'))
            self.count_element_occurance(element)
        except Exception as e:
            print("please Enter a Valid Array : ",e)
            self.get_array_elements()


    def count_element_occurance(self,element):
        """This count the number of time a specific element is present in the array
        Args:
            element (Any): user defined element value that need to be counted
        """

        if element in self.array_list  :
            print(element," has occured ",self.array_list.count(element)," times") 
        else: 
            print('element does not exist')


if __name__ == "__main__":
    element_count=CountElement()
    element_count.get_array_elements()