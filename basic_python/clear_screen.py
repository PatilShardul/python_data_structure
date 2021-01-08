''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 19:17:27
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 19:17:27
  @Description: python program to  clear console
'''
import os
import time

class ClearScreen:
    def clear_screen(self):
        os.system('cls')

if __name__ == "__main__":
    clear = ClearScreen()
    clear.clear_screen()