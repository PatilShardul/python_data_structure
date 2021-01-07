''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 00:26:32
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 00:26:32  
  @Description : Python program to remove a key from a dictionary.
'''
class RemoveKey:
    def __init__(self):
        """
        Initialize Original Dictionary
        """
        self.original_dictionary={"a":5,"b":6,"c":{"d":"7"}}
    def get_key_from_user(self):
        """
        Get Key from user and delete the key value pair the key is present in the dictionary
        """
        print(f"original Dictionary : {self.original_dictionary}")

        input_key=input("Enter the User key that you want to remove")
        
        if(input_key not in self.original_dictionary.keys()):
            print("Enter Valid Key : ")
            self.get_key_from_user()
        else:
            self.remove_key(input_key)    
    
    def remove_key(self,input_key):
        """
        Use Inbuilt del funtion to delete key value apit from the dictionary
        """
        del self.original_dictionary[input_key]
        print(self.original_dictionary)

if __name__ == "__main__":
    remove_key=RemoveKey()
    remove_key.get_key_from_user()  
      