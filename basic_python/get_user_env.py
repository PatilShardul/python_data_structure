''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 19:29:14
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 19:29:14
  @Description: Program to get user Env Variables
'''
import os
class UserEnv:
    def user_env_details(self):
        """method to print Enviornment Varaible details 
        """
        print(os.environ)

if __name__ == "__main__":
    user_env=UserEnv()
    user_env.user_env_details()