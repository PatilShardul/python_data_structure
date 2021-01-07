''' 
  @Author: Shardul Patil
  @Date: 2021-01-07 23:51:15
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-07 23:51:15  
  @Description:  Python program to count number of items in a dictionary value that is a list. 

'''
class CountListItems:
    def __init__(self):
        """
        Initialize the orignal dictionary and total_item_count
        """
        self.original_dictionary = {1 : [100, "Shardul"], 2 : "patil", 3 : [12, 8, 19, 94], 4 : ["hello world"] }
        self.total_item_count=0
    def count_total_num_of_list_items(self):
        """
        check the value type is list if True calcualte length of the value(List)  
        """
        for element in self.original_dictionary.values():
            if type(element)==list:
                self.total_item_count+=len(element)
        self.print_total_count()        
    def print_total_count(self):
        """
        Print The Total List Items
        """
        print(f"Total List items in dictionary is : {self.total_item_count}")
if __name__ == '__main__': 
    count_list_item=CountListItems()
    count_list_item.count_total_num_of_list_items()