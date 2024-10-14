import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
msg = b'hello, server'
sock.send(msg)

data = sock.recv(1024)
sock.close()


print("sended: ", msg)
print("recived: ", data)