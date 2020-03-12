import sys, os, socket, time
import urllib.request

print(urllib.request.urlopen('http://ip.42.pl/raw').read())

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ("", 5000)


sock.bind(server_address)
sock.listen(1)

print("waiting...")

connection, client_address = sock.accept()
print("Connected to :", client_address)


while True:
    data = connection.recv(1024)
    if data:
        msg = data.decode()
        print(msg)
