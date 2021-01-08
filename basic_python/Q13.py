import multiprocessing
class GetSubProcess:
    def __init__(self):
        print(multiprocessing.cpu_count())
if __name__ == "__main__":
    sub_process=GetSubProcess()
    
