''' 
  @Author: Shardul Patil
  @Date: 2021-01-09 09:44:43
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-09 09:44:43
  @Description: Count unique word in string and store them in dictionary
'''
class StrToDict:

    def get_string_from_user(self):
        """Get String from user 
        """
        try:
            self.origianl_string=input("Enter your string")
            self.get_dict()
        except Exception as e:
            print("Enter Valid String",e)
            self.get_string_from_user()
            
    def get_dict(self):
        """compute character count to dictionary from string 
        """
        
        key_count_dictionary=dict()

        for char in self.origianl_string:
            if char not in key_count_dictionary.keys():
                key_count_dictionary[char]=self.origianl_string.count(char)

        print(key_count_dictionary)

if __name__ == "__main__":
    str_to_dict=StrToDict()
    str_to_dict.get_string_from_user()

