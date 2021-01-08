''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 09:46:44
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 09:46:44  
  @Description : Python program to get file creation and modification date/times.
'''
import os.path, time
class LastModified:
    def __init__(self):
        print("Last modified: %s" % time.ctime(os.path.getmtime(r"C:\Users\Shardul-HP\fellowship\com\bridgelabz\data_structures\basic_python\Q7.py")))
        print("Created: %s" % time.ctime(os.path.getctime(r"C:\Users\Shardul-HP\fellowship\com\bridgelabz\data_structures\basic_python\Q7.py")))

if __name__ == "__main__":
    l_m=LastModified()        