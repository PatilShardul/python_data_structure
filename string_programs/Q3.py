''' 
  @Author: Shardul Patil
  @Date: 2021-01-06 22:53:54
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-06 22:53:54  
  @Description : Module to Replace occurance first character value in a string from leaving the first occurance as it is  
'''
class ReplaceCharacter:
    
    def __init__(self):
        """
        Initialize original _string,char_list,modified_string
        """
        self.original_string="restart"
        self.char_list=list()
        self.modified_string=str()
    
    def get_first_character(self):
        """
        Getting the first character in a String and storing it in first_char var
        """
        
        first_char=self.original_string[0]
        self.update_occurance_of_first_char(first_char)
    
    def convert_string_to_list(self):
        """
        converting string to list so that it can be modified/updated in the list 
        """
    
        self.char_list=list(self.original_string)


    def convert_list_to_string(self):
        """
        Reconverting list to modified string after updating the list char 
        """
        self.modified_string=''.join(self.char_list)

    def update_occurance_of_first_char(self,first_char):
        """
        First Calling the convert_string_to_list method, then replacing occurance of first character values with $
        ,lastly calling the convert_list_to_string method to convert modfied char_list to modified_string   
        """
        self.convert_string_to_list()
        for index in range(1,len(self.char_list)):
            if(self.char_list[index] == first_char):
                self.char_list[index]="$"
        self.convert_list_to_string()
        self.print_updated_string()
    
    def print_updated_string(self):
        """
        Printing the Updated String with char replacement
        """
        print(f"Update String : {self.modified_string}")


if __name__ == "__main__":
   replace_char = ReplaceCharacter()
   replace_char.get_first_character()