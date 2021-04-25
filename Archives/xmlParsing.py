import xml.etree.ElementTree as Et
data = ''' 
        <person>
            <name>jay</name>
            <phone type="intl">123567898</phone>
            <email hide="yes"/>
        </person>
'''
tree = Et.fromstring(data)
print("name : ",tree.find('name').text)
print("attr : ",tree.find('email').get('hide'))