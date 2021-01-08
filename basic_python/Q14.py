import os
class GetAllFiles:
    def __init__(self):
        self.list_file = os.listdir('.')
        print(self.list_file)

if __name__ == "__main__":
    files=GetAllFiles()    