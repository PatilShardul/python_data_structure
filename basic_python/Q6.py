''' 
  @Author: Shardul Patil
  @Date: 2021-01-04 23:51:21
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-04 23:51:21  
'''
from datetime import date
class Q6:
    
    def __init__(self):
        pass
    def get_dates_from_user(self):

        get_initial_date=int(input("Enter Initial Date in DD"))
        get_initial_month=int(input("Enter Initial Month in MM"))
        get_initial_year=int(input("Enter Initial Year in YYYY"))
        
        get_final_date=int(input("Enter Final Date in DD"))
        get_final_month=int(input("Enter Final Month in MM"))
        get_final_year=int(input("Enter Final Year in YYYY"))

        difference=(date(get_final_year,get_final_month,get_final_date) - date(get_initial_year,get_initial_month,get_initial_date) ) 
        print(f" the difference between {get_final_year}/{get_final_month}/{get_final_date} and {get_initial_year}/{get_initial_month}/{get_initial_date} : {difference} ")

if __name__ == "__main__":
    q6 = Q6()

    q6.get_dates_from_user()