''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 23:31:32
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 23:31:32
  @Description: Python program to extract single key-value pair of a dictionary in variables
'''
class KeyValuePair:
    def __init__(self):
        self.country_dict = {'country': "India",
             'States':28 }
    def get_key_val_pairs(self):         
        for k,v in self.country_dict.items():
            (var1, var2) = (k,v)
            print(f"{var1} = {var2}")
if __name__ == "__main__":
    key_value_pair=KeyValuePair()
    key_value_pair.get_key_val_pairs()            