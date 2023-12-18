import MyTCPServer as ms

server = ms.TCPServer(2500)
print("Waitiong for connection")

while True:
    if not server.connected:
        server.accept()
    else:
        msg = server.receive()
        if msg:
            print('수신메세지 : ', msg)
            server.send(msg)
        else:
            print("Disconnected")
            break

server.disconnect()