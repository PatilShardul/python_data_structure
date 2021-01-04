''' 
  @Author: Shardul Patil
  @Date: 2021-01-05 00:14:22
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-05 00:14:22  
'''
class Q9:
    def __init__(self):
        
        self.name_list=['s','h','a','r','d','u','l']
        self.namestr=""
    def convert_list_to_string(self):
        
        for characters in self.name_list:
            self.namestr+=characters
        print(self.namestr)


if __name__ == "__main__":
    q9 = Q9()
    q9.convert_list_to_string()            