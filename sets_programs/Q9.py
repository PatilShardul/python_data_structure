''' 
  @Author: Shardul Patil
  @Date: 2021-01-05 23:09:47
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-05 23:09:47  
  @Description : module to get Set Symmetric diffrence of two sets
'''
class SymmetricDifferenceOfSet:

    def __init__(self):
        """
        Initialize Two set 
        """
        self.first_set={1,2,3,5,6,"Shardul"}
        self.second_set={"Shardul","Patil",1,2,3}
    
    def get_difference(self):
        """
        Getting  symmetric diffrence of two sets and print the symmetric difference
        """
        
        difference_set=self.first_set.symmetric_difference(self.second_set)

        print(f"Symmetric Difference of  \n{self.first_set} \nand \n{self.second_set} \nis\n{difference_set}")

if __name__ == "__main__":
    symmetric_difference_of_set=SymmetricDifferenceOfSet()
    symmetric_difference_of_set.get_difference()