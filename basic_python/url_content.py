''' 
  @Author: Shardul Patil
  @Date: 2021-01-08 19:33:05
  @Last Modified by:   Shardul Patil
  @Last Modified time: 2021-01-08 19:33:05
  @Description: Program to print content from the url in console 
'''
from http.client import HTTPConnection
class UrlContent:

    def get_url_from_user(self):
        """Method to Get the Name of the url from user
        """
        url=input("Enter the name of the Website")
        self.get_url_content(url)
    
    def get_url_content(self,url):
        """Method to fetch data from url and print it on console

        Args:
            url (string): Url of the location 
        """
    
        try:
            conn = HTTPConnection("example.com")
            conn.request("GET", "/")  
            result = conn.getresponse()
        except Exception as e:      
            print("Error", e)    
        contents = result.read() 
        print(contents)

if __name__ == "__main__":
    url_content=UrlContent()
    url_content.get_url_from_user()
            