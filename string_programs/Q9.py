''' 
  @Author: Shardul Patil
  @Date: 2021-01-07 00:23:22
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-07 00:23:22  
  @Discription : Module To wrap text in with max line char 50
'''
import textwrap

class TextWrapper:
    def __init__(self):
        """
        Initializing text in unwrap format
        """
        self.text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    def wrap_text(self):
        """
        Wrap Text with line length 50
        """
        print(textwrap.fill(self.text, width=50))

if __name__ == "__main__":
    text_wrapper = TextWrapper()
    text_wrapper.wrap_text()