## Работа с TCP-сервером и клиентом

### Сервер
```Python
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Устанавливаем код ответа
        self.send_response(200)
        
        # Добавляем заголовки (например, тип контента)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Отправляем тело ответа
        response_content = '{"message": "Hello from server!"}'
        self.wfile.write(response_content.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 9090)  # IP и порт для сервера
    httpd = server_class(server_address, handler_class)
    print("Starting server on port 9090...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()

```

### Клиент с GET-запросом
```Python
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
```

### Запуск
```
docker-compose up -d
```

```
python tcp_client/client.py
```