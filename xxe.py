import requests
import urllib.parse
import base64

with open('xxe-utf-16.xml', 'rb') as reader:
    data = reader.read()

data = base64.b64encode(data)

data = urllib.parse.quote(data, safe='')

print(data)