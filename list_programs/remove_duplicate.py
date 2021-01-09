''' 
  @Author: Shardul Patil
  @Date: 2021-01-09 09:05:13
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-09 09:05:13
  @Description:Python program to remove duplicates from a list of lists. 
'''
class RemoveDuplicate:
    
    def __init__(self):
        """Intialize a origianl list and final list
        """
        self.original_list=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
        self.final_list=list()
    
    def get_unique_list(self):
        """Get unique elements from the original list and store them in final list
        """
        for value in self.original_list:
            if value not in self.final_list:
                self.final_list.append(value)
                    
        print(self.final_list)

if __name__ == "__main__":
    rd=RemoveDuplicate()
    rd.get_unique_list()