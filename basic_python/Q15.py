import os 
class EnvVariable:
    def __init__(self):
        print(os.environ)

if __name__ == "__main__":
    env_var=EnvVariable()