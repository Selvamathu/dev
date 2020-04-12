import requests
import wget
# 
# # Get file from website
# url = "https://www.python.org/static/img/python-logo@2x.png"
# myfile = requests.get(url)
# 
# # write file to desktop
# open(r"C:\Users\sepanneerselvam\Desktop\PythonImage.png", "wb"
#      ).write(myfile.content)


# url = "https://www.python.org/static/img/python-logo@2x.png"
# wget.download(url, r"C:\Users\sepanneerselvam\Desktop\PythonImage1.png" )

# Download file that redirects
url = "https://readthedocs.org/projects/python-guide/downloads/pdf/latest/"
myFile = requests.get(url, allow_redirects = True )
open(r"C:\Users\sepanneerselvam\Desktop\hello.pdf", "wb"
     ).write(myFile.content)
