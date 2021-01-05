''' 
  @Author: Shardul Patil
  @Date: 2021-01-05 08:25:53
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-05 08:25:53  
'''
class Q2:
    def __init__(self):
        self.number_list = [1,5,6,10,20,50]
        self.temp_product=1
    def multiply_all_elements(self):
        for number in self.number_list:
            self.temp_product=number*self.temp_product
        print(self.temp_product)

if __name__ == "__main__":
    q2 = Q2()
    q2.multiply_all_elements()