import socket
import requests

r = requests.get('http://localhost:9090', auth=('admin', 'admin'))
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())