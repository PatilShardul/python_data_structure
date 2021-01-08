import getpass
class UserDetails:
    def __init__(self):
        print(getpass.getuser())
if __name__ == "__main__":
    user_details = UserDetails()        