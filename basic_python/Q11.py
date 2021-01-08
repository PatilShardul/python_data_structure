import os.path

class CheckFileExist:
    def __init__(self):
        pass
    def get_file_name(self):
        try:
            file_name=input("Enter File Name : ")
            self.check_file_exists(file_name)
        except Exception as e :
            self.get_file_name()    
    def check_file_exists(self,file_name):
        if(os.path.isfile(file_name)):
            print("file exists")
        else:
            print("File not Found")
if __name__ == "__main__":
    check_file=CheckFileExist()    
    check_file.get_file_name()