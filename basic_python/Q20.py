''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 09:55:10
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 09:55:10  
  @Description:  Python program to sort three integers without using conditional statements and loops. 

'''
class SortNumber:
    def __init__(self):
        pass
    def get_user_input(self):
        try :     
            self.num1 = int(input("Input first number: "))
            self.num2 = int(input("Input second number: "))
            self.num3 = int(input("Input third number: "))
            self.sort_num()
        except:
            self.get_user_input()    
    def sort_num(self):    
            min_num = min(self.num1, self.num2, self.num3)
            max_num = max(self.num2, self.num2, self.num3)
            centre_num = (self.num1 + self.num2 + self.num3) - max_num - min_num
            print(max_num,centre_num,min_num)
if __name__ == "__main__":
    sort_number=SortNumber()
    sort_number.get_user_input()