''' 
  @Author: Shardul Patil
  @Date: 2021-01-09 00:06:01
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-09 00:06:01
  @Description:Python program to convert an integer to binary keep leading zeros
'''
class ZeroLeadBinary:
    
    def get_number_from_user(self):
        self.num = int(input("Enter an positive integer"))
        self.get_format()
    
    def get_format(self):
        binary = format(self.num, "08b")
        print(binary)

if __name__ == "__main__":
    zlb=ZeroLeadBinary()
    zlb.get_number_from_user()