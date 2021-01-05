''' 
  @Author: Shardul Patil
  @Date: 2021-01-05 23:04:38
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-05 23:04:38  
  @Description : module to get intersection of two sets
'''
class IntersectionOfSet:

    def __init__(self):
        """
        Initialize Two set 
        """
        self.first_set={1,2,3,5,6,"Shardul"}
        self.second_set={"Shardul","Patil",1,2,3}
    
    def get_intersection(self):
        """
        Getting intersection of two sets and print the intersection
        """
        
        intersection_set=self.first_set.intersection(self.second_set)

        print(f"InterSection of  \n{self.first_set} \nand \n{self.second_set} \nis\n{intersection_set}")

if __name__ == "__main__":
    intersction_of_set=IntersectionOfSet()
    intersction_of_set.get_intersection()        
