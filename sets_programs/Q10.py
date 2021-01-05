''' 
  @Author: Shardul Patil
  @Date: 2021-01-05 23:18:54
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-05 23:18:54  
  @Description : module to delete all set Values 
'''
class ClearSet:

    def __init__(self):
        """
        Initialize original set 
        """
        self.original_set={1,2,3,5,6,"Shardul"}
    
    def clear_set_values(self):
        """
        
        clearing all values in the set and printing it again

        """
        print (f"before Clearing : {self.original_set}")
        
        self.original_set.clear()

        print (f"After Clearing : {self.original_set}")

if __name__ == "__main__":
    clear_set=ClearSet()
    clear_set.clear_set_values()