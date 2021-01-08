''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 19:37:24
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 19:37:24
  @Description: python program to execute external command given by the user 
'''
import os

class CommandOutput:

    def get_command_from_user(self):
        """Method to Get commad from the user 
        """
        cmd=input("Enter Command to execute : ")
        self.run_command(cmd)

    def run_command(self,cmd):
        """Method to run the command 
        Args:
            cmd (string): command to run
        """            
        os.system(cmd)

if __name__ == "__main__":
    c_o=CommandOutput()
    c_o.get_command_from_user()     