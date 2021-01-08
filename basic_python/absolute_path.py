''' 
  @Author: Shardul Patil
  @Date: 2021-01-09 00:47:43
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-09 00:47:43
  @Description: Python program to get an absolute file path
'''
import os
class AbsPath:
    def get_absolute_path(self):
        try:
            file_name=input("Enter File Name with EXtension")
            print(os.path.abspath(file_name))
        except Exception as e:
            print(e)
            self.get_absolute_path() 
if __name__ == "__main__":
    abs_path=AbsPath()
    abs_path.get_absolute_path()        