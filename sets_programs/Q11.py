''' 
  @Author: Shardul Patil
  @Date: 2021-01-05 23:09:47
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-05 23:09:47  
  @Description : module to create a frozen set that is immutable 
'''
class FrozenSet:

    def __init__(self):
        """
        Initialize Two set frozen and original
        """
        self.original_set={1,2,3,5,6,"Shardul"}
        self.frozen_set={}
    
    def freeze_set_value(self):
        """
        Getting frozen set using frozenset method
        """
        self.frozen_set=frozenset(self.original_set)
        print(f"Froze Set {self.frozen_set}")

if __name__ == "__main__":
    frozen_set=FrozenSet()
    frozen_set.freeze_set_value() 