import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


#you can ignor it
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.varify_mode = ssl.CERT_NONE

#url = 'http://py4e-data.dr-chuck.net/comments_42.html'
url = 'http://py4e-data.dr-chuck.net/comments_466018.html'
html = urllib.request.urlopen(url, context=ctx).read()
tree = BeautifulSoup(html, 'html.parser')

tags = tree('span')
total = 0
for tag in tags:
    num = int(tag.contents[0])
    total = total + num
print(total)