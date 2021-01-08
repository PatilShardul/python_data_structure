''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 19:31:31
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 19:31:31
  @Description: Program to get Host Name of the server
'''
import socket
class HostName:
    def get_host_name(self):
        """Method to print Host name of the Local Server
        """
        print("Host name:", socket.gethostname())
if __name__ == "__main__":
    host_name=HostName()
    host_name.get_host_name()