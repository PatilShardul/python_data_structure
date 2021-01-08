''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 23:19:07
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 23:19:07
  @Description: get min max value in list with out using inbuilt function
'''

class MinMax:

    def __init__(self):
        self.value_list=[0, 10, 15, 40, -5, 42, 17, 28, 75]

    def get_min_max_values(self):
        """Get min and Max Value
        """
        max = self.value_list[0]
        min = self.value_list[0]
        for value in self.value_list:
            if (value >= max):
                max = value
            elif (value <= min):
                min = value
        print(f"minimum value = {min} , maximum_value={max}")

if __name__ == "__main__":
    min_max=MinMax()
    min_max.get_min_max_values()