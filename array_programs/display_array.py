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
        self.array_list=[eval(element) for element in input("Enter the Array Elements : ").split(",")]
        print(self.array_list)

    def print_array_elements(self):
        """This menthod prints a array elements
        """
        for index in range(0,len(self.array_list)):
            print(self.array_list[index])

if __name__ == "__main__":
    display=DisplayArray()
    display.get_array_elements()