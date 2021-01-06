''' 
  @Author: Shardul Patil
  @Date: 2021-01-06 21:07:37
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-06 21:07:37
  @Description : Count The Length Of a String  
'''
class StringLength:
    def __init__(self):
        """
        Initialize the String
        """
        self.original_string="Hello World..!"

    def get_string_length(self):
        """
        Get The length of the original String
        """
        self.print_length(len(self.original_string))

    def print_length(self,length):
        """
        print the Length of the String on the screen
        Args: Length > Length of the  original_string 
        """    
        print(f"Length of the String is : {length}" )


if __name__ == "__main__":
    string_length=StringLength()
    string_length.get_string_length()
