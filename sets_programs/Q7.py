''' 
  @Author: Shardul Patil
  @Date: 2021-01-05 23:07:18
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-05 23:07:18  
  @Description : module to get Union of two sets
'''
class UnionOfSet:

    def __init__(self):
        """
        Initialize Two set 
        """
        self.first_set={1,2,3,5,6,"Shardul"}
        self.second_set={"Shardul","Patil",1,2,3}
    
    def get_union(self):
        """
        Getting union of two sets and print the union
        """
        
        intersection_set=self.first_set.union(self.second_set)

        print(f"Union of  \n{self.first_set} \nand \n{self.second_set} \nis\n{intersection_set}")

if __name__ == "__main__":
    union_of_set=UnionOfSet()
    union_of_set.get_union()        
