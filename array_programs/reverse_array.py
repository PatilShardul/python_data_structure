''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 16:13:40
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 16:13:40  
  @Description : Python program to create an array of 5 integers and display the array items. Access individual element through indexes
'''
class DisplayArray:
    def get_array_elements(self):
        """This Method Takes comma seperated input elements from user andf store in array list
        """

        try:
            self.array_list=[eval(element) for element in input("Enter the Array Numerical Elements : ").split(",")]
            print(self.array_list)
            self.reverse_array_elements()
        except Exception as e:
            print("please Enter a Valid Array : ",e)
            self.get_array_elements()


    def reverse_array_elements(self):
        """This menthod reverse and prints a array elements
        """
        reverse_array=self.array_list[len(self.array_list)::-1]
        print(reverse_array)


if __name__ == "__main__":
    display=DisplayArray()
    display.get_array_elements()