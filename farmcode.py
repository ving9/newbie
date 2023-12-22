import sys
import matplotlib.pyplot as plt
import numpy as np
import time
from socket import *
from threading import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class WindowClass(QWidget) :
    def __init__(self):  # 생성자 함수 (처음 생성될떄 실행되는 함수)
        super().__init__()   # 부모의 생성자를 실행하겠다
        uic.loadUi('farm.ui', self)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.clnt_sock = socket(AF_INET, SOCK_STREAM)
        ip = '127.0.0.1'
        port = 8998
        # ip = '10.10.20.103'
        # port = 8889
        self.clnt_sock.connect((ip, port))
        self.totalArray = []
        self.productArray = []
        self.priceArray = []
        self.dateArray = []


        self.btn_test.clicked.connect(self.move)


        # self.fig = plt.Figure()
        # self.canvas = FigureCanvas(self.fig)
        # self.verticalLayout.addWidget(self.canvas)
        #
        # x = np.arange(1, 12, 1)
        # y = np.sin(x)
        #
        # ax = self.fig.add_subplot(111)
        # ax.plot(x, y)
        # ax.set_xlabel("month")
        # ax.set_ylabel("price")
        #
        # ax.set_title("my sin graph")
        # ax.legend()
        # self.canvas.draw()




        # self.combo_product.activated.connect(self.send_product)
        self.btn_inquiry.clicked.connect(self.inquiry_price)
        self.btn_seoul_2013.clicked.connect(lambda: self.send_year_region("2013", "서울", 'a'))
        self.btn_gyungki_2013.clicked.connect(lambda: self.send_year_region("2013", "경기", 'b'))
        self.btn_daegu_2013.clicked.connect(lambda: self.send_year_region("2013", "대구(경북)", 'c'))
        self.btn_busan_2013.clicked.connect(lambda: self.send_year_region("2013", "부산(울산,경남)", 'd'))
        self.btn_gwang_2013.clicked.connect(lambda: self.send_year_region("2013", "광주(전남)", 'e'))
        self.btn_jeonju_2013.clicked.connect(lambda: self.send_year_region("2013", "전주(전북)", 'f'))
        self.btn_daejeon_2013.clicked.connect(lambda: self.send_year_region("2013", "대전(충남)", 'g'))
        self.btn_gangwon_2013.clicked.connect(lambda: self.send_year_region("2013", "강원", 'h'))
        self.btn_choogbuk_2013.clicked.connect(lambda: self.send_year_region("2013", "충북", 'i'))
        self.btn_jeju_2013.clicked.connect(lambda: self.send_year_region("2013", "제주", 'j'))

        self.btn_seoul_2014.clicked.connect(lambda: self.send_year_region("2014", "서울", 'k'))
        self.btn_gyungki_2014.clicked.connect(lambda: self.send_year_region("2014", "경기", 'l'))
        self.btn_daegu_2014.clicked.connect(lambda: self.send_year_region("2014", "대구(경북)", 'm'))
        self.btn_busan_2014.clicked.connect(lambda: self.send_year_region("2014", "부산(울산,경남)", 'n'))
        self.btn_gwang_2014.clicked.connect(lambda: self.send_year_region("2014", "광주(전남)", 'o'))
        self.btn_jeonju_2014.clicked.connect(lambda: self.send_year_region("2014", "전주(전북)", 'p'))
        self.btn_daejeon_2014.clicked.connect(lambda: self.send_year_region("2014", "대전(충남)", 'q'))
        self.btn_gangwon_2014.clicked.connect(lambda: self.send_year_region("2014", "강원", 'r'))
        self.btn_choogbuk_2014.clicked.connect(lambda: self.send_year_region("2014", "충북", 's'))
        self.btn_jeju_2014.clicked.connect(lambda: self.send_year_region("2014", "제주", 't'))

        self.btn_seoul_2022.clicked.connect(lambda: self.send_year_region("2022", "서울", 'A'))
        self.btn_gyungki_2022.clicked.connect(lambda: self.send_year_region("2022", "경기", 'B'))
        self.btn_daegu_2022.clicked.connect(lambda: self.send_year_region("2022", "대구(경북)", 'C'))
        self.btn_busan_2022.clicked.connect(lambda: self.send_year_region("2022", "부산(울산,경남)", 'D'))
        self.btn_gwang_2022.clicked.connect(lambda: self.send_year_region("2022", "광주(전남)", 'E'))
        self.btn_jeonju_2022.clicked.connect(lambda: self.send_year_region("2022", "전주(전북)", 'F'))
        self.btn_daejeon_2022.clicked.connect(lambda: self.send_year_region("2022", "대전(충남)", 'G'))
        self.btn_gangwon_2022.clicked.connect(lambda: self.send_year_region("2022", "강원", 'H'))
        self.btn_choogbuk_2022.clicked.connect(lambda: self.send_year_region("2022", "충북", 'I'))
        self.btn_jeju_2022.clicked.connect(lambda: self.send_year_region("2022", "제주", 'J'))
        self.btn_sejong_2022.clicked.connect(lambda: self.send_year_region("2022", "세종", 'K'))


        self.table_product_price.horizontalHeader().setVisible(True)  # 버그로 인해 디자이너에서 만져도 안보여서 추가한 코드
        self.table_product_price.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table_product_price.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

        self.btn_1.clicked.connect(self.move2)
        self.btn_2.clicked.connect(self.move3)


    def move(self):
        self.stackedWidget.setCurrentIndex(0)
    def move2(self):
        self.stackedWidget.setCurrentIndex(1)

    def move3(self):
        self.stackedWidget.setCurrentIndex(2)

    def send_year_region(self, year, regi, idx):
        self.label_year.setText(year)
        self.label_region.setText(regi)
        self.clnt_sock.send(bytes(idx.encode()))
        self.stackedWidget.setCurrentIndex(1)
        self.recv_data()

    def recv_data(self):
        # temp = self.clnt_sock.recv(4096)
        # temp = temp.decode('utf-8')
        # self.totalArray = temp.split(',')
        self.listen_thread()
        time.sleep(2)
        self.totalArray.pop()
        print(self.totalArray)
        for i in range(0, int((len(self.totalArray) / 3))):
            self.dateArray.append(self.totalArray[i*3])
            self.productArray.append(self.totalArray[i*3+1])
            self.priceArray.append(self.totalArray[i*3+2])
        for i in range(0, len(self.priceArray)):
            self.priceArray[i] = self.priceArray[i].strip("\n")
        for i in range(0, len(self.dateArray)):
            self.dateArray[i] = self.dateArray[i].strip("\n")
        product = []
        for i in range(0, len(self.productArray)):
            if self.productArray[i] not in product:
                product.append(self.productArray[i])
        for i in range(0, len(product)):
            self.combo_product.addItem(product[i])

    # def send_product(self):
    #     sig = '1'
    #     sig = bytes(sig.encode('utf-8'))
    #     self.clnt_sock.send(sig)
    #     self.recv_price()
    #
    # def recv_price(self):
    #     temp = self.clnt_sock.recv(1024)
    #     temp = temp.decode('utf-8')
    #     self.priceArray = temp.split(',')
        # producarr = []
        # pricearr = []
        # for i in range(0, len(self.productArray)):
        #     if self.productArray[i] == curPro:
        #         producarr.append(self.productArray[i])
        #         pricearr.append(self.priceArray[i])

    def inquiry_price(self):
        curPro = self.combo_product.currentText()
        datearr = []
        pricearr = []
        for i in range(0, len(self.productArray)):
            if self.productArray[i] == curPro:
                datearr.append(self.dateArray[i])
                pricearr.append(self.priceArray[i])
        intprice = list(map(int, pricearr))
        self.line_min.setText(str(min(intprice)) + "원")
        self.line_max.setText(str(max(intprice)) + "원")
        self.line_aver.setText(str(int((sum(intprice)/len(pricearr)))) + "원")
        self.table_product_price.setRowCount(len(datearr))
        for i in range(0, len(datearr)):
            self.table_product_price.setItem(i, 0, QTableWidgetItem(datearr[i]))
            self.table_product_price.setItem(i, 1, QTableWidgetItem(pricearr[i]+"원"))

    def listen_thread(self):
        # 데이터 수신 쓰레드 생성 시작
        t = Thread(target=self.receive_message, args=(self.clnt_sock,))
        t.start()

    def receive_message(self, cs):
        temp = bytes()
        while True:
            try:
                buf = cs.recv(4096)
                temp += buf
                if not buf:
                    break
            except:
                temp += buf
        temp = temp.decode()
        temp = temp.split(',')
        self.totalArray = temp




    # def recv_date(self):
    #     curPro = self.combo_product.currentText()
    #     temp = self.clnt_sock.recv(1024)
    #     temp = temp.decode('utf-8')
    #     self.dateArray = temp.split(',')
    #     datearr = []
    #     pricearr = []
    #     for i in range(0, len(self.productArray)):
    #         if self.productArray[i] == curPro:
    #             datearr.append(self.dateArray[i])
    #             pricearr.append(self.priceArray[i])
    #     self.table_product_price.setRowCount(len(datearr))
    #     print(datearr)
    #     print(pricearr)
    #     for i in range(0, len(datearr)):
    #         self.table_product_price.setItem(i, 0, QTableWidgetItem(datearr[i]))
    #         self.table_product_price.setItem(i, 1, QTableWidgetItem(pricearr[i]))














if __name__ == "__main__" :
    app = QApplication(sys.argv)
    #QApplication : 프로그램 실행 클래스

    myWindow = WindowClass()
    # WindowClass의 인스턴스 생성

    myWindow.show()
    # 프로그램 화면을 보여주는 코드

    app.exec_()
    # 프로그램을 이벤트루프로 진입시키는 코드 (프로그램 작동)