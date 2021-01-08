''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 23:39:51
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 23:39:51
  @Description:Python program to find files and skip directories of a given directory.
'''
import os
class SkipDir:
    def __init__(self):
        self.basepath = r'C:\Users\Shardul-HP\fellowship\com\bridgelabz'
    def get_file(self):
        for fname in os.listdir(self.basepath):
            path = os.path.join(self.basepath, fname)
            if os.path.isdir(path):
                continue
            else: 
                print(fname)
if __name__ == "__main__":
    skip_dir=SkipDir()
    skip_dir.get_file()                