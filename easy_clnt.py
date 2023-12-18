import socket

port = input("port : ")
sock = socket.create_connection(('localhost', port))

message = "클라이언트 메세지"
print('sending {}' .format(message))
sock.sendall(message.encode())

data = sock.recv(1024)

print('received {}' .format(data.decode()))
print('closing socket')
sock.close()