''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 19:23:27
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 19:23:27
  @Description:Python Program to get properties of a file 
'''
import os.path
import time
class FileProperties:
    
    def get_file_name(self):
        """Method to get file Name from the user
        """
        try:
            path='C:\\Users\\Shardul-HP\\fellowship\\com\\bridgelabz\\data_structures\\basic_python\\'
            file_name=input("Get File Name")
            self.get_properties(path+file_name)
        except Exception as e:
            print("Issue While Opening the File ",e)
            self.get_file_name()
    def get_properties(self,filepath):
        """method to print propeties of a file at given Location

        Args:
            filepath ([string]): file Path(location)
        """
        print('File         :', filepath)
        print('Last Access   :', time.ctime(os.path.getatime(filepath)))
        print('Last Modified :', time.ctime(os.path.getmtime(filepath)))
        print('Last Change  :', time.ctime(os.path.getctime(filepath)))
        print('Size Of the File  :', os.path.getsize(filepath))


if __name__ == "__main__":
    f_p=FileProperties()
    f_p.get_file_name()