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
        self.ip = '127.0.0.1'     # 고정적으로 접속할 IP와 PORT
        self.port = 8889

        self.totalArray = []       # 받은 데이터 전체 저장
        self.productArray = []     # 받은 데이터 분리해서 상품명만 저장
        self.priceArray = []       # 받은 데이터 분리해서 가격만 저장
        self.dateArray = []        # 받은 데이터 분리해서 날짜만 저장
        self.grape_date_arr = []   # 사용자가 선택하고 난 후의 그래프를 그리기 위한 날짜 리스트
        self.grape_price_arr = []  # 그래프 그리기 위한 가격 리스트

        self.btn_graph.setDisabled(True)
        # 상품을 조회하기 전까지 그래프 화면으로 넘어가는 것을 막기 위함

        self.table_product_price.horizontalHeader().setVisible(True)
        self.table_product_price.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table_product_price.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        # 헤더 사이즈 조절

        self.btn_graph.clicked.connect(self.draw_grape) # 그래프로 넘어가는 버튼
        self.btn_exit.clicked.connect(self.go_home)  # 메인 화면으로 돌아가는 버튼
        self.btn_connect.clicked.connect(self.connect_serv) # 메인화면에서 서버와 접속 시도하는 버튼
        self.btn_inquiry.clicked.connect(self.inquiry_price) # 상품 목록에서 상품을 골라 가격을 조회하는 버튼

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




    def connect_serv(self): # 서버와 접속하는 함수
        self.clnt_sock = socket(AF_INET, SOCK_STREAM)
        self.clnt_sock.connect((self.ip, self.port))
        self.stackedWidget.setCurrentIndex(1)

    def send_year_region(self, year, regi, idx):  # 서버에 어떤 년도, 어떤 지역인지 보내는 함수
        self.label_year.setText(year)
        self.label_year_2.setText(year)
        self.label_region.setText(regi)
        self.label_region_2.setText(regi)
        self.clnt_sock.send(bytes(idx.encode()))
        self.stackedWidget.setCurrentIndex(2)
        self.recv_data()

    def recv_data(self):  # 서버에서 데이터를 받아오고 상품명 목록에 출력하기 위한 함수
        self.listen_thread()  # 데이터를 받을때 작동시킬 쓰레드
        time.sleep(1.5)
        self.totalArray.pop()
        self.totalArray.pop()
        print(self.totalArray)
        for i in range(0, int((len(self.totalArray) / 3))):
            self.dateArray.append(self.totalArray[i*3])
            self.productArray.append(self.totalArray[i*3+1])
            self.priceArray.append(self.totalArray[i*3+2])
        product = []
        for i in range(0, len(self.productArray)):
            if self.productArray[i] not in product:
                product.append(self.productArray[i])
        for i in range(0, len(product)):
            self.combo_product.addItem(product[i])



    def inquiry_price(self):  # 상품명 목록에서 상품을 골라 조회하는 버튼
        curPro = self.combo_product.currentText()
        self.label_product_2.setText(curPro)
        datearr = []
        pricearr = []
        for i in range(0, len(self.productArray)):
            if self.productArray[i] == curPro:
                datearr.append(self.dateArray[i])
                pricearr.append(self.priceArray[i])
        self.grape_date_arr = datearr
        self.grape_price_arr = pricearr
        intprice = list(map(int, pricearr))
        self.line_min.setText(str(min(intprice)) + "원")
        self.line_max.setText(str(max(intprice)) + "원")
        self.line_aver.setText(str(int((sum(intprice)/len(pricearr)))) + "원")
        self.table_product_price.setRowCount(len(datearr))
        for i in range(0, len(datearr)):
            self.table_product_price.setItem(i, 0, QTableWidgetItem(datearr[i]))
            self.table_product_price.setItem(i, 1, QTableWidgetItem(pricearr[i]+"원"))
        self.btn_graph.setEnabled(True)

    def listen_thread(self): # 데이터 수신 쓰레드 생성 시작
        t = Thread(target=self.receive_message, args=(self.clnt_sock,))
        t.start()

    def receive_message(self, cs):  # 서버로부터 데이터를 수신하고 메인 리스트에 저장
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

    def draw_grape(self):  # 그래프를 그리기 위한 함수
        temp = [[],[],[],[],[],[],[],[],[],[],[],[]]
        result = []
        month_list = []

        if self.label_year_2.text() == "2013":
            for i in range(0, len(self.grape_date_arr)):
                if "201301" in self.grape_date_arr[i]:
                    temp[0].append(self.grape_price_arr[i])
                elif "201302" in self.grape_date_arr[i]:
                    temp[1].append(self.grape_price_arr[i])
                elif "201303" in self.grape_date_arr[i]:
                    temp[2].append(self.grape_price_arr[i])
                elif "201304" in self.grape_date_arr[i]:
                    temp[3].append(self.grape_price_arr[i])
                elif "201305" in self.grape_date_arr[i]:
                    temp[4].append(self.grape_price_arr[i])
                elif "201306" in self.grape_date_arr[i]:
                    temp[5].append(self.grape_price_arr[i])
                elif "201307" in self.grape_date_arr[i]:
                    temp[6].append(self.grape_price_arr[i])
                elif "201308" in self.grape_date_arr[i]:
                    temp[7].append(self.grape_price_arr[i])
                elif "201309" in self.grape_date_arr[i]:
                    temp[8].append(self.grape_price_arr[i])
                elif "201310" in self.grape_date_arr[i]:
                    temp[9].append(self.grape_price_arr[i])
                elif "201311" in self.grape_date_arr[i]:
                    temp[10].append(self.grape_price_arr[i])
                elif "201312" in self.grape_date_arr[i]:
                    temp[11].append(self.grape_price_arr[i])
            for i in range(0, 12):
                if temp[i]:
                    sumprice = list(map(int, temp[i]))
                    result.append(int((sum(sumprice)/len(sumprice))))
                    month_list.append(i+1)
        elif self.label_year_2.text() == "2014":
            for i in range(0, len(self.grape_date_arr)):
                if "201401" in self.grape_date_arr[i]:
                    temp[0].append(self.grape_price_arr[i])
                elif "201402" in self.grape_date_arr[i]:
                    temp[1].append(self.grape_price_arr[i])
                elif "201403" in self.grape_date_arr[i]:
                    temp[2].append(self.grape_price_arr[i])
                elif "201404" in self.grape_date_arr[i]:
                    temp[3].append(self.grape_price_arr[i])
                elif "201405" in self.grape_date_arr[i]:
                    temp[4].append(self.grape_price_arr[i])
                elif "201406" in self.grape_date_arr[i]:
                    temp[5].append(self.grape_price_arr[i])
                elif "201407" in self.grape_date_arr[i]:
                    temp[6].append(self.grape_price_arr[i])
                elif "201408" in self.grape_date_arr[i]:
                    temp[7].append(self.grape_price_arr[i])
                elif "201409" in self.grape_date_arr[i]:
                    temp[8].append(self.grape_price_arr[i])
                elif "201410" in self.grape_date_arr[i]:
                    temp[9].append(self.grape_price_arr[i])
                elif "201411" in self.grape_date_arr[i]:
                    temp[10].append(self.grape_price_arr[i])
                elif "201412" in self.grape_date_arr[i]:
                    temp[11].append(self.grape_price_arr[i])
            for i in range(0, 12):
                if temp[i]:
                    sumprice = list(map(int, temp[i]))
                    result.append(int((sum(sumprice)/len(sumprice))))
                    month_list.append(i+1)
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        self.verticalLayout.addWidget(self.canvas)

        x = month_list
        y = result

        ax = self.fig.add_subplot(111)
        ax.plot(x, y)
        ax.set_xlabel("month")
        ax.set_ylabel("price")
        self.canvas.draw()
        self.stackedWidget.setCurrentIndex(3)

    def go_home(self): # 리스트를 초기화 시키면서 메인화면으로 돌아가기위한 함수
        self.canvas.close()
        self.totalArray = []
        self.productArray = []
        self.priceArray = []
        self.dateArray = []
        self.table_product_price.setRowCount(0)
        self.stackedWidget.setCurrentIndex(0)


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()