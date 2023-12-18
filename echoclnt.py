import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servIP = input(("Server IP(dafault: 127.0.0.1) : "))
if servIP == '':
    servIP = '127.0.0.1'

port = input('port(dafault : 2500): ')
if port == '':
    port = 2500
else:
    port = int(port)

sock.connect((servIP, port))
print("Connected to " + servIP)
sock.settimeout(1.0)

while True:
    # try:
    #     r_msg = sock.recv(2014)
    #     print(r_msg.decode())
    #     print('\n')
    # except socket.timeout:
    #     pass

    msg = input("Message to send: ")
    if not msg:
        continue

    try:
        sock.send(msg.encode())
    except:
        print("연결이 종료되었습니다.")
        break

    try:
        r_msg = sock.recv(1024)
        if not msg:
            print("연결이 종료되었습니다")
            break
        print(f'Received message: {r_msg.decode()}')

    except:
        print("연결이 종료되었습니다.")
        break

sock.close()

