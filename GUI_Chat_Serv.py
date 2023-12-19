from socket import *
from threading import *

class MultiChatServer:
    def __init__(self):  # 소켓 생성하고 연결되면 accept_client() 호출
        self.clients = []  # 접속된 클라이언트 소켓 목록
        self.final_received_message = "" # 최종 수신 메세지
        self.s_sock = socket(AF_INET, SOCK_STREAM)
        self.ip = ''
        self.port = 2500
        self.s_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.s_sock.bind((self.ip, self.port))
        print("클라이언트 대기중....")
        self.s_sock.listen(100)
        self.accept_client()

    # 연결 클라이언트 소켓을 목록에 추가하고 스레드 생성하여 데이터 수신
    def accept_client(self):
        while True:
            client = c_socket, (ip, port) = self.s_sock.accept()
            if client not in self.clients:
                self.clients.append(client) # 접속된 소켓 목록에 추가
            print(ip, ':', str(port), "가 연결되었습니다")
            cth = Thread(target=self.receive_messages, args=(c_socket,))
            cth.start()

    # 데이터를 수신하여 모든 클라이언트에게 전송
    def receive_messages(self, c_socket):
        while True:
            try:
                incoming_message = c_socket.recv(256)
                if not incoming_message:  #연결 종료된 상황
                    break
            except:
                continue
            else:
                self.final_received_message = incoming_message.decode('utf-8')
                print(self.final_received_message)
                self.send_all_clients(c_socket)
        c_socket.close()

    #송신한 클라이언트를 제외한 모든 클라이언트에게 메세지 전송
    def send_all_clients(self, senders_socket):
        for client in self.clients: #목록에 있는 소켓에 대해서 하겠다
            socket, (ip, port) = client
            if socket is not senders_socket:  # 송신 클라이언트는 제외
                try:
                    socket.sendall(self.final_received_message.encode())
                except:
                    self.clients.remove(client)
                    print("{}, {} 연결이 종료되었습니다" .format(ip, port))

if __name__ == "__main__":
    MultiChatServer()