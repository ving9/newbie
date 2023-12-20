from socket import *
from threading import *

class ThreadClnt:
    def __init__(self, ip, port):
        servaddr = (ip, port)
        self.clntsock = socket(AF_INET, SOCK_STREAM)
        abc = self.clntsock.connect(servaddr)
        print(abc)
        self.writeThread()
        self.readThread()

    def writeThread(self):
        w = Thread(target=self.writeMessage, args=(self.clntsock,))
        w.start()

    def readThread(self):
        w = Thread(target=self.readMessage, args=(self.clntsock,))
        w.start()

    def writeMessage(self, w):
        while True:
            msg = input("Message to send: ")
            if not msg:
                continue
            elif msg == 'q' or msg == 'Q':
                print("연결을 종료합니다")
                self.clntsock.close()
                break
            else:
                w.send(msg.encode())

    def readMessage(self, r):
        while True:
            msg = r.recv(1024)
            print("Message from server : %s" % msg.decode())
            if not msg:
                break

if __name__ == "__main__":
    ip = input("server IP addr : ")
    port = input("server PORT : ")
    ThreadClnt(ip, int(port))
