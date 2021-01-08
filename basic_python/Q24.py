''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 10:37:28
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 10:37:28  
  @Description :  Python program to get recurssion limit.
'''
import sys

class RecurssionLimit:
    
    def __init__(self):
        pass
    
    def get_recussion_limit(self):
        print(sys.getrecursionlimit())

if __name__ == "__main__":
    recussion_limit=RecurssionLimit()
    recussion_limit.get_recussion_limit()  