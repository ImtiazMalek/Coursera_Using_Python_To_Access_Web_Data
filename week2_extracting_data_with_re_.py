import re
f = open('actual_data.txt')
file = f.read()
l = re.findall('[0-9]+', file)
total = list()
for index in range(len(l)):
    n = l[index]
    num = int(n)
    total.append(num)
print(sum(total))
