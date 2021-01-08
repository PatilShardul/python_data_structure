''' 
  @Author: Shardul Patil
  @Date: 2021-01-09 00:41:37
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-09 00:41:37
  @Description: program to get execution time for a Python method
'''
import time
class ExecutionTime:
    def execution_time(self):
        start = time.time()
        for i in range(10):
            print("",end="")
            time.sleep(1)
        end = time.time()
        print(f"Runtime of the program is {end - start}")

if __name__ == "__main__":
        et=ExecutionTime()
        et.execution_time()