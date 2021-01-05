''' 
  @Author: Shardul Patil
  @Date: 2021-01-05 21:30:25
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-05 21:30:25
  @Description: program to create A set by taking value from user  
'''
class CreateSet:
    def __init__(self):
        """
        initializing original set
        Args:None
        Return:None 
        """
        
        self.original_set=set()

    def get_values(self):
        """
        Getting values from user and storing that in set 
        Args:None
        Return:None
        """    
        no_of_values=int(input("Enter number of values in the set"))

        for i in range(no_of_values):
            element_value=input("Enter The Element")
            self.original_set.add(element_value)
        self.get_set_values()
    
    def get_set_values(self):
        """
        Printing Value persent in the original_set
        Args:None
        Return:None
        """

        print(self.original_set)

if __name__ == "__main__":
    
    create_set = CreateSet()
    create_set.get_values()

