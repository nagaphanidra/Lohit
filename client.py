import socket

s = socket.socket()
s.connect(("www.fsu.edu", 80))
s.send(b"GET /index.html HTTP/1.0\n\n")
data = s.recv(2048)

print(data)
