import socket
import requests

r = requests.get('http://localhost:9090', auth=('admin', 'admin'))

# получение статуса
print(r.status_code)

# получение заголовков
print(r.headers['content-type'])

# получение кодировки
print(r.encoding)

# получение тела запроса в формате json
print(r.json())