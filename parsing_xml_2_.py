import xml.etree.ElementTree as ET
data = '''
<person>
    <users>
        <user x="3">
            <name>imtiaz</name>
            <id>16101068</id>
        </user>
        <user x="5">
            <name>nanji</name>
            <id>16301153</id>
        </user>
    </users>
</person>'''

tree = ET.fromstring(data)
new_tree = tree.findall('users/user')
print('number of items', len(new_tree))
print()
for item in new_tree:
    print('name:', item.find('name').text)
    print('id:', item.find('id').text)
    print('User No.', item.get('x'))
    print()