import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#you can ignor it
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.varify_mode = ssl.CERT_NONE

url = input('Enter address- ')
page = urllib.request.urlopen(url,context=ctx).read()
tag_tree = BeautifulSoup(page, 'html.parser')


sites = list()

##Retrieve all of the anchor tags
tags = tag_tree('a')
for tag in tags:
    n = tag.get('href', None)
    sites.append(n)
    #print(tag.get('href', None))
print(sites)
