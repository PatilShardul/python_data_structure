''' 
  @Author: Shardul Patil
  @Date: 2021-01-09 08:39:21
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-09 08:39:21
  @Description:Python program to sum all the items in a list.
'''
class SumOfList:

    def get_list_from_user(self):
        """Get List of number from the user
        """
        try: 
            self.number_list=[eval(element) for element in input("Enter the Tuples Elements : ").split(",")]
            self.get_sum()
        except Exception as e:
            print("list must contain numbers only")
    
    def get_sum(self):
        """Use Sum function to get the summation of the list elements
        """
        print(f"Sum Total of List Element is : {sum(self.number_list,0)}")    

if __name__ == "__main__":
    sum_of_list=SumOfList()
    sum_of_list.get_list_from_user()    