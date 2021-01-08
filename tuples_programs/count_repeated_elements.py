''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 17:50:55
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 17:50:55  
  @Description : a find repeated items of tuple
'''
class RepeatCount:
    
    def get_tuple_elements(self):
        """This Method Takes comma seperated input elements from user andf store in tuple
        """
        self.list_element=[eval(element) for element in input("Enter the Tuples Elements : ").split(",")]
        self.original_tuple=tuple(self.list_element)
        self.count_repeat_elements()


    def count_repeat_elements(self):
        """This menthod counts the number of times a element is repeated 
        """
        unique_items=list()
        for element in self.original_tuple:
            if self.original_tuple.count(element)>1 and element not in unique_items:
                unique_items.append(element)
                print(f"{element} is repeated {self.original_tuple.count(element)} times",end="\n")

if __name__ == "__main__":
    repeat_count=RepeatCount()
    repeat_count.get_tuple_elements()