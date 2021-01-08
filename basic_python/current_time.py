''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 19:21:13
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 19:21:13
  @Description: Python Program to get current time on the system
'''
import time 

class CurrentTime:
    def get_current_time(self):
        """method to print Current Time in the System
        """
        print(time.ctime())

if __name__ == "__main__":
    current_time=CurrentTime()
    current_time.get_current_time()