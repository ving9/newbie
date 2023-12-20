import sys
import matplotlib.pyplot as plt
import numpy as np
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
        # ip = '127.0.0.1'
        # port = 9500
        ip = '10.10.20.103'
        port = 8889
        self.clnt_sock.connect((ip, port))
        self.totalArray = []
        self.productArray = []
        self.priceArray = []
        self.dateArray = []




        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        self.verticalLayout.addWidget(self.canvas)

        x = np.arange(1, 12, 1)
        y = np.sin(x)

        ax = self.fig.add_subplot(111)
        ax.plot(x, y)
        ax.set_xlabel("month")
        ax.set_ylabel("price")

        ax.set_title("my sin graph")
        ax.legend()
        self.canvas.draw()




        # self.combo_product.activated.connect(self.send_product)
        self.btn_inquiry.clicked.connect(self.inquiry_price)
        self.btn_seoul_2013.clicked.connect(lambda: self.send_year_region("2013", "서울"))


        self.table_product_price.horizontalHeader().setVisible(True)  # 버그로 인해 디자이너에서 만져도 안보여서 추가한 코드
        self.table_product_price.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table_product_price.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

        self.btn_1.clicked.connect(self.move2)
        self.btn_2.clicked.connect(self.move3)

    def move2(self):
        self.stackedWidget.setCurrentIndex(1)

    def move3(self):
        self.stackedWidget.setCurrentIndex(2)

    def send_year_region(self, year, regi):
        self.label_year.setText(year)
        self.label_region.setText(regi)
        a = bytes(year.encode('utf-8'))
        b = bytes(regi.encode('utf-8'))
        # self.clnt_sock.send(a+b)
        self.stackedWidget.setCurrentIndex(1)
        self.recv_data()

    def recv_data(self):
        # temp_ = ""
        # while True:
        #     temp = self.clnt_sock.recv(1024)
        #     if not temp:
        #         # temp.decode('utf-8')
        #         # temp_ += temp
        #         break
        #     else:
        #         temp = temp.decode('utf-8')
        #         temp_ += temp
        # try:
        #     temp = self.clnt_sock.recv(1000)
        #     while temp:
        #         temp_ = temp.decode()
        #         temp = self.clnt_sock.recv(1000)
        # except IOError as e:
        #     pass
        # _temp = ""
        # while True:
        #     self.clnt_sock.settimeout(2)
        #     try:
        #         temp = self.clnt_sock.recv(1024)
        #         if not temp:
        #             break
        #     except timeout:
        #         break
        #     else:
        #         temp = temp.decode('utf-8')
        #         _temp += temp
        _temp = ""
        temp = self.clnt_sock.recv(500000)
        temp = temp.decode('utf-8')
        _temp += temp
        self.totalArray = _temp.split(',')
        print(self.totalArray)
        self.totalArray.pop()
        for i in range(0, int((len(self.totalArray) / 3))):
            self.dateArray.append(self.totalArray[i*3])
            self.productArray.append(self.totalArray[i*3+1])
            self.priceArray.append(self.totalArray[i*3+2])
        for i in range(0, len(self.priceArray)):
            self.priceArray[i] = self.priceArray[i].strip("\n")
        product = []
        for i in range(0, len(self.productArray)):
            if self.productArray[i] not in product:
                product.append(self.productArray[i])
        for i in range(0, len(product)):
            self.combo_product.addItem(product[i])
        print(self.totalArray)

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
        self.table_product_price.setRowCount(len(datearr))
        print(datearr)
        print(pricearr)
        for i in range(0, len(datearr)):
            self.table_product_price.setItem(i, 0, QTableWidgetItem(datearr[i]))
            self.table_product_price.setItem(i, 1, QTableWidgetItem(pricearr[i]))



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