''' 
  @Author: Shardul Patil
  @Date: 2021-01-05 22:46:27
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-05 22:46:27  
  @Description : module to remove user given element from the set
'''
class RemoveItem:
    def __init__(self):
    """
    initialize original_set set 
    ARGS: None
    """    
        self.original_set={5,6,9,65,100}
    
    def remove_element_in_the_list(self):
    """
    get Value from user and remove element from the original set  
    ARGS: None
    """    
        print(self.original_set)
        try:
            value=int(input("Enter the value to be removed"))
            self.original_set.discard(value)
            print(f"After Removing element {value} : {self.original_set}")
        except Exception as e :
            print(e)
                
if __name__ == "__main__":
    remove_item=RemoveItem()
    remove_item.remove_element_in_the_list()

