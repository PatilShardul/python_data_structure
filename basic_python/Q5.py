''' 
  @Author: Shardul Patil
  @Date: 2021-01-04 23:35:36
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-04 23:35:36  
'''
import calendar
class Q5:
    
    def __init__(self):
        pass
    
    def get_month_and_year(self):
        month = int(input("Enter month in MM : "))
        year = int(input("Enter Year in YYYY Format : "))
        self.get_calender(month,year)
        
    def get_calender(self,month,year):
        print(calendar.month(year, month))


if __name__ == "__main__":
    q5 = Q5()
    q5.get_month_and_year()

