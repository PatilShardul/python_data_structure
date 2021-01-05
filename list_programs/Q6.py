''' 
  @Author: Shardul Patil
  @Date: 2021-01-05 08:49:47
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-05 08:49:47  
'''
class Q6:
    def __init__(self):
        self.general_list = ["abc","abc","def","a","b","5","1991","test","pop","a"]
        self.unique_list = list()
    def remove_duplicates_from_string(self):
        for value in self.general_list:
            if(value not in self.unique_list ):
                self.unique_list.append(value)
            else:
                continue     
        print(self.unique_list)
if __name__ == "__main__":
    q6 = Q6()
    q6.remove_duplicates_from_string()