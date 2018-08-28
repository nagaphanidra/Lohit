import socket
import time

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   
s.bind(("", 9000))
s.listen(5)
while True:
    c,a = s.accept()
    print("Received connection from", a)
    time.sleep(7)
    c.send(("Hello " + str(a[0]) + "\n").encode())
    c.close()
