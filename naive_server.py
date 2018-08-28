import socket

s = socket.socket()
# The SO_REUSEADDR flag tells the kernel to reuse a local socket in
# TIME_WAIT state, without waiting for its natural timeout to expire.
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
s.bind(("", 9000))
s.listen(5)
while True:
    c,a = s.accept()
    print("Received connection from", a)
    c.send(("Hello " + str(a[0]) + "\n").encode())
    c.close()
