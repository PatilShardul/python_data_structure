''' 
  @Author: Shardul Patil
  @Date: 2021-01-05 23:54:44
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-05 23:54:44  
  @Description : module to get min and max value from the set
'''
class MinMaxValue:

    def __init__(self):
        """
        Initialize set original_set and orginal_list list
        """
        self.original_set={7,55,52,88,1}
        self.original_list=list()
    
    def convert_set_to_list(self):
        """
        Storing set Elements to list
        """
        for element in self.original_set:
            self.original_list.append(element)
        
        self.sort_list()    
    
    def sort_list(self):
        """
        Sorting the list to get first and last value in the list as minimum and maximum
        """
        try:
            self.original_list.sort()
        except Exception as e :
            print(e)

        print(f" minimum number is : {self.original_list[0]}" )
        print(f" maximum number is : {self.original_list[-1]}" )

if __name__ == "__main__":
    min_max=MinMaxValue()
    min_max.convert_set_to_list() 