import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('localhost', 5000))
print("현재 시각 : ", sock.recv(1024).decode())
print(sock.recv(1024).decode())

sock.close()

