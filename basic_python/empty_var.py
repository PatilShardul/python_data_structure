''' 
  @Author: Shardul Patil
  @Date: 2021-01-09 00:01:27
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-09 00:01:27
  @Description: Python program to empty a variable without destroying it
'''
class EmptyVar:
    def __init__(self):
        self.dumy_list = ["aa",1,{"b":2 }, [3,"c"],(4,5)]
    
    def EmptyVarItems(self):
        for i in self.dumy_list:
            print(type(i)())

if __name__ == "__main__":
    emt_var=EmptyVar()
    emt_var.EmptyVarItems()        