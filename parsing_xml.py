import xml.etree.ElementTree as ET
data = '''
<people>
    <name>imtiaz</name>
    <phone type="intl">+8801988148871</phone>
    <email hide="yes"/>
</people>'''

tree = ET.fromstring(data)
print(tree.find('name').text)
print(tree.find('email').get('hide'))