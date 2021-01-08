''' 
  @Author: Shardul Patil
  @Date: 2021-01-09 00:55:50
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-09 00:55:50
  @Description: Python program to create a histogram from a given list of integers. 
'''
class Histogram:
    def __init__(self):
        self.items=[11,5,15,13,7]
    def compute_histogram(self):
        for n in self.items:
            output = ''
            times = n
            count=0
            while( times > 0 ):
                output += '>'
                times = times - 1
                count+=1
            print(output,count)
if __name__ == "__main__":
    histogram=Histogram()
    histogram.compute_histogram()