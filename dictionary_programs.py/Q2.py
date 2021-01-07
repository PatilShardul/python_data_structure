''' 
  @Author: Shardul Patil
  @Date: 2021-01-07 20:50:12
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-07 20:50:12  
  #description: module to create a new dictionary and add user element to the dictionary
'''
class CreateDictionary:
    def __init__(self):
        """
        Intialize an Empty Dictionary
        """
        self.original_dictionary=dict()
    def get_key_value_from_user(self):
        """
        Get key and values from user unit user set add value flag to n
        """
        try:
            add_value_flag=input("Do you wish to add Value to the dictionary : (y/n) ")
            if(add_value_flag=="y"):
                key=input("Enter Key : ")
                value=input("Enter Value : ")
                self.set_key_value(key,value)
            else:
                self.print_dictionary() 
                print("End Program")
                   
        except Exception as e:
            print("Enter Valid Input ",e)
            self.get_key_value_from_user()

    def set_key_value(self,key,value):
        """
        Store Key value in the dictionary
        Args : Key > Key for the user element
               value > Value for the user Element   
        """
        self.original_dictionary[key]=value
        self.get_key_value_from_user()

    def print_dictionary(self):
        """
        print the final values in the dictionary
        """
        print(f"final dictionary : {self.original_dictionary}")


if __name__ == "__main__":
    create_dictionary=CreateDictionary()
    create_dictionary.get_key_value_from_user()