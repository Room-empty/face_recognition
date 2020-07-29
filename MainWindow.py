#로그인과 얼굴등록을 고르는 윈도우
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Reg_Window import Reg_Window
from Login_Window import Login_Window

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('메인 화면 ')
        self.setGeometry(600, 400, 300, 200)

        login = QPushButton("로그인",self)
        login.move(110, 60)
        login.clicked.connect(self.login_button)

        reg = QPushButton("FACE_ID 등록",self)
        reg.move(110, 100)
        reg.clicked.connect(self.reg_button)

    def login_button(self):

        win = Login_Window()
        r = win.showModal()

    def reg_button(self):
        win = Reg_Window()
        r = win.showModal()

    def show(self):
        super().show()
