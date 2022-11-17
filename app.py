from PyQt6.QtWidgets import QApplication,QDialog,QStackedWidget
from PyQt6.uic import load_ui
import sys




class Wellcome(QDialog):
    def __init__(self) -> None:
        super(Wellcome,self).__init__()
        load_ui.loadUi('wellcome.ui',self)
        widget.setFixedWidth(400)
        widget.setFixedHeight(250)
        self.btn_login.clicked.connect(self.login_p)
        self.btn_create.clicked.connect(self.create_p)


    def login_p(self):
        login=Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def create_p(self):
        create=Create()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex()+1)


class Login(QDialog):
    def __init__(self) -> None:
        super(Login,self).__init__()
        load_ui.loadUi('login.ui',self)

        widget.setFixedWidth(400)
        widget.setFixedHeight(300)



class Create(QDialog):
    def __init__(self) -> None:
        super(Create,self).__init__()
        load_ui.loadUi('create.ui',self)
        widget.setFixedWidth(400)
        widget.setFixedHeight(300)

        






app=QApplication(sys.argv)
widget=QStackedWidget()
window=Wellcome()
widget.addWidget(window)


widget.show()
app.exec()