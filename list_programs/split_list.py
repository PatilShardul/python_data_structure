''' 
  @Author: Shardul Patil
  @Date: 2021-01-09 08:54:18
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-09 08:54:18
  @Description: Python program to split a list based on first character of word.  
'''
from itertools import groupby
from operator import itemgetter 
class SortList:
    def __init__(self):
        """Initiazlze the word list
        """
        self.word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

    def sort_items(self):
        """Sort items using itemgetter callable
        and groupby
        """
        for letter, words in groupby(sorted(self.word_list), key=itemgetter(0)):
            print(letter)
            for word in words:
                print(word)

if __name__ == "__main__":
    sort=SortList()      
    sort.sort_items()          