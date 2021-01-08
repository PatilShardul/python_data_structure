''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 23:51:58
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 23:51:58
  @Description:Python program to add leading zeroes to a string
'''
class LeadingZero:
    def get_user_string(self):
        self.value=input("Enter The String")
        self.add_zero_to_start()
    def add_zero_to_start(self):
        zero_filled_number = self.value.zfill(10)
        print(zero_filled_number)
if __name__ == "__main__":
    leading_zero=LeadingZero()            
    leading_zero.get_user_string()