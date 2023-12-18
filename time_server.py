import socket
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('', 5000)
sock.bind(address)
sock.listen(5)

idx = 1
while True:
    client, addr = sock.accept() # 연결 허용. 클라이언트 소켓과 주소 변환
    print("Connection requested from", addr)
    client.send(time.ctime(time.time()).encode()) # 바이트형 메세지 전송
    client.send(("당신은 %d번째 접속자입니다." % idx).encode())
    idx += 1
    client.close()
