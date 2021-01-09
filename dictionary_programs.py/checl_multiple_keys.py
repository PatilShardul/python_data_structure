''' 
  @Author: Shardul Patil
  @Date: 2021-01-09 09:35:49
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-09 09:35:49
  @Description: Python program to check multiple keys exists in a dictionary
'''
class CheckKey:
    def __init__(self):
        """Initialize original dictionary and check key set
        """
        self.original_dict = {"Mon":3, "Tue":11,"Wed":6,"Thu":9}
        self.check_keys={"Tue","fri"}
    def check_if_multiple_key_persent(self):
        """Check if the given keys are present in the set
        """
        if(self.original_dict.keys()) >= self.check_keys:
            print("All keys are present")
        else:
            print("All keys are not present")
if __name__ == "__main__":
    check_key=CheckKey()
    check_key.check_if_multiple_key_persent()