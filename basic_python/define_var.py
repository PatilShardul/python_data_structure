''' 
  @Author: Shardul Patil
  @Date: 2021-01-09 00:14:05
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-09 00:14:05
  @Description:Python program to determine if variable is defined or not
'''
class CheckVar:
    def undefined_var(self):
        try:
            thevariable
        except NameError:
            print("variable wasn't defined")
        else:
            print("variable was defined.")

    def defined_var(self):
        try:
            thevariable=1
        except NameError:
            print(" variable wasn't defined")
        else:
            print("variable was defined.")


if __name__ == "__main__":
    check_var=CheckVar()
    check_var.undefined_var()
    check_var.defined_var()