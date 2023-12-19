from socket import *
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from threading import *

class ChatClient:
    client_socket = None

    def __init__(self, ip, port):
        self.initialize_socket(ip, port)
        self.initialize_gui()
        self.listen_thread()

    def initialize_socket(self, ip, port):
        #  소켓 생성하고 서버와 연결하는 함수
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        remote_ip = ip
        remote_port = port
        self.client_socket.connect((remote_ip, remote_port))

    def send_chat(self):
        #  메세지를 전송하는 버튼 콜백 함수
        senders_name = self.name_widget.get().strip() + ":"
        data = self.enter_text_widget.get(1.0, 'end').strip()
        message = (senders_name + data).encode('utf-8')
        self.chat_transcript_area.insert("end", message.decode('utf-8') + '\n')
        self.chat_transcript_area.yview(END)
        self.enter_text_widget.delete(1.0, 'end')
        return 'break'

    def listen_thread(self):
        # 데이터 수신 쓰레드 생성 시작
        t = Thread(target=self.receive_message, args=(self.client_socket,))
        t.start()

    def receive_message(self, so):
        while True:
            buf = so.recv(256)
            if not buf:  # 연결이 종료됨
                break
            self.chat_transcript_area.insert('end', buf.decode('utf-8') + '\n')
            self.chat_transcript_area.yview(END)
        so.close()

if __name__ == "__main__":
    ip = input("server IP addr: ")
    if ip == '':
        ip = '127.0.0.1'
    port = 2500
    ChatClient(ip, port)
    mainloop()