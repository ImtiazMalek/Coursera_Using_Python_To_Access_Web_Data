import urllib.request, urllib.parse, urllib.error

fhead = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

count = dict()

for line in fhead:
    words = line.decode().split()
    for word in words:
        count[word] = count.get(word,0)+1
print(count)