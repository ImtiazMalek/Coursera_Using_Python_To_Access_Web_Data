import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

#you can ignor it
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.varify_mode = ssl.CERT_NONE



url = 'http://py4e-data.dr-chuck.net/comments_466020.xml'
html = urllib.request.urlopen(url, context=ctx).read()

tree = ET.fromstring(html)
new_tree = tree.findall('.//comment')

total = 0
for item in new_tree:
    number = int(item.find('count').text)
    total = total+number
print(total)