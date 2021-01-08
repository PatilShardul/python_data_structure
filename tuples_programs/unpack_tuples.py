''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 17:50:55
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 17:50:55  
  @Description : a Python program to unpack a tuple in several variables
'''
class UnpackTuple:
    
    def get_tuple_elements(self):
        """This Method Takes comma seperated input elements from user andf store in tuple
           Initialize a variable list
        """
        self.list_element=[eval(element) for element in input("Enter the Tuples Elements : ").split(",")]
        self.original_tuple=tuple(self.list_element)
        self.var_list=list()
        self.print_tuple_elements()


    def print_tuple_elements(self):
        """This menthod Upacks the a tuple elements to varaible and print output
        """
        for index in range(1,len(self.original_tuple)+1):
            self.var_list.append('var'+str(index))
        unpacked_tuple={var:value for var,value in zip(self.var_list,self.original_tuple)} 
        print(unpacked_tuple)

if __name__ == "__main__":
    unpack_tuple=UnpackTuple()
    unpack_tuple.get_tuple_elements()