''' 
  @Author: Shardul Patil
  @Date: 2021-01-05 22:55:35
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-05 22:55:35
  @description : module to remove element from set if the value is present in the set  
'''
class RemoveItem:
    def __init__(self):
        """
        initialize original_set set 
        ARGS: None
        """    
        self.original_set={5,6,9,65,100}
    
    def remove_element_in_the_set(self):
        """
        get Value from user and remove element from the original set if the element is present else throe error  
        ARGS: None
        """    
        print(self.original_set)
        try:
            value=int(input("Enter the value to be removed"))
            self.original_set.remove(value)
            print(f"After Removing element {value} : {self.original_set}")
        except Exception as e :
            print("Value not Presetnt in the set : ",e)
            self.remove_element_in_the_set()

if __name__ == "__main__":
    remove_item=RemoveItem()
    remove_item.remove_element_in_the_set()