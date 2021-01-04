''' 
  @Author: Shardul Patil
  @Date: 2021-01-04 23:04:51
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-04 23:04:51  
'''
class Q3:
    
    def __init__(self):
     
        self.colors_list=["Red","Green","White","Black"]
        self.get_first_and_last_color()
    
    def get_first_and_last_color(self):

        color_list_length=len(self.colors_list)
        
        print(self.colors_list[0])
        print(self.colors_list[color_list_length-1])

if __name__ == "__main__":
    q3 = Q3()