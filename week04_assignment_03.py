import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#you can ignor it
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.varify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Axel.html'

def crawling(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    tree = BeautifulSoup(html,'html.parser')

    tags = tree('a')
    count = 0
    for tag in tags:
        if count == 17:
            name = tag.contents[0]
            new_url = tag.get('href',None)
            return name, new_url
            quit()
        else:
            count += 1


for i in range(7):
    new_name, url = crawling(url)
print(new_name)
