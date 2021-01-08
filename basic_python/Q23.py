''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 10:37:28
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 10:37:28  
  @Description :  Python program to get the size of an object in bytes.
'''
import sys

class ObjectSize:
    
    def __init__(self):
        self.name_list = ["shardul","patil"]
    
    def get_oject_size(self):
        print(sys.getsizeof(self.name_list))

if __name__ == "__main__":
    obj_size=ObjectSize()
    obj_size.get_oject_size()        

