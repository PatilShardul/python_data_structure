''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 00:48:14
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 00:48:14  
  @Description :  Python script to concatenate following dictionaries to create a new 
'''
class ConcatDictionary:
    """
    Initializing 3 dictionary and a final dictionary that will have all values from 3 dictionary
    """
    def __init__(self):
        self.first_dictionary={"a":1,"b":2,"c":3,"d":4}
        self.second_dictionary={"f":5,"g":6,"h":7,"i":8}
        self.third_dictionary={"j":9,"k":10,"l":11,"m":12}
        self.final_dictionary=dict()
    
    def concat_dictionary(self):
        """
        Concatinate all dictioanry to final dictioanry 
        """

        self.final_dictionary.update(self.first_dictionary)
        self.final_dictionary.update(self.second_dictionary)
        self.final_dictionary.update(self.third_dictionary)
        print(self.final_dictionary)

if __name__ == "__main__":
    concat_dict=ConcatDictionary()
    concat_dict.concat_dictionary()    