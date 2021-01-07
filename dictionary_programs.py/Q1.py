''' 
  @Author: Shardul Patil
  @Date: 2021-01-07 20:37:05
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-07 20:37:05  
  @Description : Module to sort Dictionary in ascending and descending order
'''

class SortDictionary:
    def __init__(self):
        """
        Initialize Original Dictionary
        """
        self.original_dict={"worldCup":2011,"Champion Trophy":2015 , "World T20":2007}
    def sort_ascending(self):
        """
        Sort Origianl Dictionary Ascending Using Sorted Method and useing Lambda function set value 
        """
        print(f"Ascending Order : {dict(sorted(self.original_dict.items(),key=lambda kv: kv[1]))}")
    def sort_descending(self):
        """
        Sort Original Dictionary In descending Order   Using Sorted Method and useing Lambda function set value 
        """
        print(f"Descending Order : {dict(sorted(self.original_dict.items(),key=lambda kv: kv[1],reverse=True))}")

if __name__ == "__main__":
    sort_dictionary=SortDictionary()
    sort_dictionary.sort_ascending()
    sort_dictionary.sort_descending()    