from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
	html = urlopen("http://pythonscraping.com/pages/page1.html")

except HTTPError as e:
	print(e)
except URLError as e:
	print("The server could not found")

else:
	print(html.read())
	bsobj = BeautifulSoup(html.read() , 'lxml')
	print(bsobj.h1) 