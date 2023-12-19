from PyQt5.QtWidgets import *
from PyQt5 import uic
from socket import *
from threading import *
import matplotlib.pyplot as plt
import numpy as np
import sys

from PyQt5.QtWidgets import QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

form_class = uic.loadUiType("untitled.ui")[0]

class WindowClass(QMainWindow, form_class) :
    msg = "경기"
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.clnt_sock = socket(AF_INET, SOCK_STREAM)
        remote_ip = ''
        remote_port = 2500
        self.clnt_sock.connect((remote_ip, remote_port))


        self.stackedWidget.setCurrentIndex(0)
        self.btn_home.clicked.connect(self.go_home)
        self.p1btn.clicked.connect(self.go_to_page1) #지역선택창
        self.p2btn.clicked.connect(self.go_to_page2)

        self.q1b.clicked.connect(self.go_to_page3)

        self.q2b.clicked.connect(self.go_to_page4)
        self.q3b.clicked.connect(self.go_to_page5)
        self.q4b.clicked.connect(self.go_to_page6)
        self.q5b.clicked.connect(self.go_to_page7)
        self.q6b.clicked.connect(self.go_to_page8)
        self.q7b.clicked.connect(self.go_to_page9)
        self.q8b.clicked.connect(self.go_to_page10)
        self.q9b.clicked.connect(self.go_to_page11)
        self.q10b.clicked.connect(self.go_to_page12)
        self.q11b.clicked.connect(self.go_to_page13)
        self.q12b.clicked.connect(self.go_to_page14)
        self.q13b.clicked.connect(self.go_to_page15)
        self.q14b.clicked.connect(self.go_to_page16)
        self.q15b.clicked.connect(self.go_to_page17)
        self.q16b.clicked.connect(self.go_to_page18)
        self.q17b.clicked.connect(self.go_to_page19)
        # 1경기 2서울 3부산 4경남 5인천 6경북 7충남 8전북 9충북 10강원 11대전 12광주 13울산 14제주 15세종 16대구 17전남

        self.g1b.clicked.connect(self.go_to_page1)
        self.g2b.clicked.connect(self.go_to_page1)
        self.g3b.clicked.connect(self.go_to_page1)
        self.g4b.clicked.connect(self.go_to_page1)
        self.g5b.clicked.connect(self.go_to_page1)
        self.g6b.clicked.connect(self.go_to_page1)
        self.g7b.clicked.connect(self.go_to_page1)
        self.g8b.clicked.connect(self.go_to_page1)
        self.g9b.clicked.connect(self.go_to_page1)
        self.g10b.clicked.connect(self.go_to_page1)
        self.g11b.clicked.connect(self.go_to_page1)
        self.g12b.clicked.connect(self.go_to_page1)
        self.g13b.clicked.connect(self.go_to_page1)
        self.g14b.clicked.connect(self.go_to_page1)
        self.g15b.clicked.connect(self.go_to_page1)
        self.g16b.clicked.connect(self.go_to_page1)
        self.g17b.clicked.connect(self.go_to_page1)

    def go_home(self):
        self.stackedWidget.setCurrentIndex(0)
    def go_to_page1(self):
        self.stackedWidget.setCurrentIndex(1)
    def go_to_page2(self):
        self.stackedWidget.setCurrentIndex(2)

    def go_to_page3(self):
        self.stackedWidget.setCurrentIndex(3)

    def go_to_page4(self):
        self.stackedWidget.setCurrentIndex(4)

        # for draw graph
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)

        self.graph_verticalLayout.addWidget(self.canvas)

        x = np.arange(0, 100, 1)
        y = np.sin(x)

        ax = self.fig.add_subplot(111)
        ax.plot(x, y, label="sin")
        ax.set_xlabel("x")
        ax.set_xlabel("y")

        ax.set_title("my sin graph")
        ax.legend()
        self.canvas.draw()

    def go_to_page5(self):
        self.stackedWidget.setCurrentIndex(5)
    def go_to_page6(self):
        self.stackedWidget.setCurrentIndex(6)
    def go_to_page7(self):
        self.stackedWidget.setCurrentIndex(7)
    def go_to_page8(self):
        self.stackedWidget.setCurrentIndex(8)
    def go_to_page9(self):
        self.stackedWidget.setCurrentIndex(9)
    def go_to_page10(self):
        self.stackedWidget.setCurrentIndex(10)
    def go_to_page11(self):
        self.stackedWidget.setCurrentIndex(11)
    def go_to_page12(self):
        self.stackedWidget.setCurrentIndex(12)
    def go_to_page13(self):
        self.stackedWidget.setCurrentIndex(13)
    def go_to_page14(self):
        self.stackedWidget.setCurrentIndex(14)
    def go_to_page15(self):
        self.stackedWidget.setCurrentIndex(15)
    def go_to_page16(self):
        self.stackedWidget.setCurrentIndex(16)
    def go_to_page17(self):
        self.stackedWidget.setCurrentIndex(17)
    def go_to_page18(self):
        self.stackedWidget.setCurrentIndex(18)
    def go_to_page19(self):
        self.stackedWidget.setCurrentIndex(19)






if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec()