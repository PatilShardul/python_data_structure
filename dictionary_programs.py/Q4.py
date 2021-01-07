''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 00:50:01
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 00:50:01  
  @Description :Python program to iterate over dictionaries using for loops
'''
class IterateDictionary:
    def __init__(self):
        """
        Inintialize Original Dictionary
        """
        self.original_dict={"worldCup":2011,"Champion Trophy":2015 , "World T20":2007}
    
    def iterate_over_dictionary(self):
        """
        Iterate Over Dictionary and print Key Value Pair
        """
        for key,value in self.original_dict.items():
            print(f"({key},{value})") 

if __name__ == "__main__":
    iterate_dict=IterateDictionary()
    iterate_dict.iterate_over_dictionary()    