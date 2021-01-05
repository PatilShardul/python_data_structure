''' 
  @Author: Shardul Patil
  @Date: 2021-01-05 08:41:16
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-05 08:41:16  
'''
class Q4:
    def __init__(self):
        self.string_list = ["abc","def","a","b","5","1991","test","pop"]
        self.computed_string_list = list()
    def get_valid_length_strings(self):
        for string in self.string_list:
            if(len(string) >= 2 and string.endswith(string[0])):
                self.computed_string_list.append(string) 
        print(self.computed_string_list)
if __name__ == "__main__":
    q4 = Q4()
    q4.get_valid_length_strings()