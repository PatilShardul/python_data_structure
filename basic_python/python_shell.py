''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 23:25:05
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 23:25:05
  @Description: Python program to determine if the python shell is executing in 32bit or 64bit mode on operating system
'''
import platform

class PythonShellArchSize:
    def get_arch_size(self):
        print(platform.architecture()[0])

if __name__ == "__main__":
    arch=PythonShellArchSize()
    arch.get_arch_size()       