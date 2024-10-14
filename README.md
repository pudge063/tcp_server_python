## Работа с TCP-сервером и клиентом

### Сервер
```Python
import socket

sock = socket.socket()

sock.bind(('', 9090))

sock.listen(3)

while True:
    conn, addr = sock.accept()
    print("connected ", addr)
    data = conn.recv(1024)
    conn.send(b'hello, client!')
    conn.close()
```

### Клиент
```Python
import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
msg = b'hello, server'
sock.send(msg)

data = sock.recv(1024)
sock.close()


print("sended: ", msg)
print("recived: ", data)
```

### Запуск
```
docker-compose up -d
```

```
python tcp_client/client.py
```