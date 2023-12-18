import socket
s_sock = socket.socket()
host = "localhost"
port = 2500

s_sock.connect((host, port))
s_sock.send("I am ready".encode())
fn = s_sock.recv(1024).decode()

with open('e:/'+fn, 'wb') as f:
    print('file opened')
    print('receiving file...')
    while True:
        data = s_sock.recv(8192)
        if not data:
            break
        f.write(data)

print('Download complete')
s_sock.close()
print('Connection closed')