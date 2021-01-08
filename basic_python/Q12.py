from subprocess import call

class ExtCommand:
    def __init__(self):
        pass

    def ext_command(self): 
        call('dir', shell=True)   
        call(['cmd','dir'])    

if __name__ == "__main__":
    ext_cmd=ExtCommand()
    ext_cmd.ext_command()       