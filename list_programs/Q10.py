''' 
  @Author: Shardul Patil
  @Date: 2021-01-05 09:27:33
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-05 09:27:33  
'''
class Q10:
    def __init__(self):
        self.sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
        self.output_list = list()
    
    def truncate_list(self):

        self.sample_list.pop(5)
        self.sample_list.pop(4)
        self.sample_list.pop(0)
        print(self.sample_list)
        

if __name__ == "__main__":
    q10 = Q10()
    q10.truncate_list()