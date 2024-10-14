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
