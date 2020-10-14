import urllib.request, urllib.parse, urllib.error
import ssl
import json
#you can ignor it
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.varify_mode = ssl.CERT_NONE
url = 'http://py4e-data.dr-chuck.net/comments_466021.json'
data = urllib.request.urlopen(url, context=ctx).read()
tree = json.loads(data)
n_tree = tree['comments']
total = 0
for item in n_tree:
    num = int(item["count"])
    total = total + num
print(total)