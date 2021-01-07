''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 01:08:20
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 01:08:20  
  @Description : Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 
'''
class SquareValues:
    def __init__(self):
        """
        Initialize Final dictionary
        """
        self.final_dict=dict()
    
    def get_input_from_user(self):
        """
        get number of iteration value from user
        """
        number_of_iteration=int(input("Enter the number of iteration : "))
        self.compute_dictionary(number_of_iteration)
    
    def compute_dictionary(self,number_of_iteration):
        """
        set dictionary Values
        """
        for index in range(1,number_of_iteration+1):
            self.final_dict[index]=index*index
        print(self.final_dict)

if __name__ == "__main__":
    square_val=SquareValues()
    square_val.get_input_from_user()
        