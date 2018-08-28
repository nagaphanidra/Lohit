''' you can try connecting multiple clients to this server at the same time
by using 'telnet localhost 9000' from multiple terminals
'''
import socket
import time, threading

def handle_client(sock, a):
    print("Received connection from", a)
    time.sleep(7)
    sock.send(("Hello " + str(a[0]) + "\n").encode())
    sock.close()
                
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   
s.bind(("", 9000))
s.listen(5)
while True:
    c,a = s.accept()
    threading.Thread(target = handle_client, args = (c, a)).start()
    