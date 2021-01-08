''' 
  @Author: Shardul Patil
  @Date: 2021-01-09 00:34:12
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-09 00:34:12
  @Description: Python program to get the current value of the recursion limi
'''
import sys
class RecursionLimit:
    def get_recursion_limit(self):
        print(sys.getrecursionlimit())

if __name__ == "__main__":
    recursion_limit=RecursionLimit()
    recursion_limit.get_recursion_limit()