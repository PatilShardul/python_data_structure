''' 
  @Author: Shardul Patil
  @Date: 2021-01-09 00:23:18
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-09 00:23:18
  @Description: Python program to get numbers divisible by fifteen from a list using an anonymous function.
'''
class DivideByFifteen:
    def __init__(self):
        self.my_list = [12, 60, 54, 39, 120, 150, 225,]

    def compute_values(self):
        result = list(filter(lambda x: (x % 15 == 0), self.my_list))
        print("Numbers divisible by 15 are",result)

if __name__ == "__main__":
    dbf=DivideByFifteen()
    dbf.compute_values()        