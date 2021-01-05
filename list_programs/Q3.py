''' 
  @Author: Shardul Patil
  @Date: 2021-01-05 08:30:18
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-05 08:30:18  
'''

class Q3:
    def __init__(self):
        self.number_list = [5,10,4,20,50]
        self.minimum_number=self.number_list[0]
    def smallest_elements(self):
        for number in self.number_list:
            if(number<=self.minimum_number):
                self.minimum_number = number 
        print(self.minimum_number)

if __name__ == "__main__":
    q3 = Q3()
    q3.smallest_elements()