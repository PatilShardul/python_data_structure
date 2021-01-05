''' 
  @Author: Shardul Patil
  @Date: 2021-01-05 22:33:41
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-05 22:33:41  
  @Description : module to calculate Sum of all the element in set  
'''
class AddMembersInSet:
    
    def __init__(self):
        """
        Initialize a original set
        Args:None
        Return:None
        """
        self.original_set={1,2,5,4,7,0}
    def add_members(self):
        """
        Adding members in the list
        Args:None
        Return:None
        """
        Total=0
        try:
            for element in self.original_set:
                Total=Total+element
            print(f"Total : {Total}")    
        except Exception as e :
            print(e)

if __name__ == "__main__":
   add_member_in_set=AddMembersInSet()
   add_member_in_set.add_members()