''' 
  @Author: Shardul Patil
  @Date: 2021-01-05 22:22:08
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-05 22:22:08
  @Description: program to iterate over set and print set values in new line     
'''
class IterateOverSet:
    def __init__(self):
        """
        Initialize a original_set set 
        Args: None
        Return: None
        """
        self.original_set={14,15,16,"Shardul"}

    def iterate(self):
        """
        Iterating over the original_set to print values 
        Args: None
        Return: None
        """

        for element in self.original_set:
            print(element)     


if __name__ == "__main__":
    iterate_over_set = IterateOverSet()
    iterate_over_set.iterate()            