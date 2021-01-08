''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 10:05:50
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 10:05:50  
  @Description : Python program to sort files by date 
'''
import os    

class SortFiles:
    def __init__(self):
        self.path = r'C:\Users\Shardul-HP\fellowship\com\bridgelabz\data_structures\basic_python'
        self.name_list = os.listdir(self.path)

    def sort_by_modified_date(self):    
        self.full_list = [os.path.join(self.path,i) for i in self.name_list]
        self.time_sorted_list = sorted(self.full_list, key=os.path.getmtime)
    def get_sorted_file_name(self):
        sorted_filename_list = [ os.path.basename(i) for i in self.time_sorted_list]
        print (sorted_filename_list)
if __name__ == "__main__":
    sort=SortFiles()
    sort.sort_by_modified_date()
    sort.get_sorted_file_name()