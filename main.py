from PyQt6.uic import load_ui
from PyQt6.QtWidgets import QApplication,QDialog,QWidget,QStackedWidget
import sys
import sqlite3
from dabase import DataBase

db=DataBase()





class Login(QDialog):
    def __init__(self) -> None:
        super(Login,self).__init__()
        load_ui.loadUi('login.ui',self)
        self.btn_enter.clicked.connect(self.login)

    def login(self):
        id=self.id.text()
        password=self.password.text()
        
        if len(id)==0 or len(password)==0:
            print('fill information')
        else: 
            if id== 'admin' and password =='1234':
                menu=Menu()
                widget.addWidget(menu)
                widget.setCurrentIndex(widget.currentIndex()+1)                

            else:
                print('wrong information')
        
    # ------END----------







class Menu(QDialog):
    def __init__(self) -> None:
        super(Menu,self).__init__()
        load_ui.loadUi('addmenu.ui',self)
        self.btn_save.clicked.connect(self.add_product)

    def add_product(self):

        name=self.name.text()
        code=self.name_code.text()
        qty=self.qty.text()
        price=self.price.text()

        if len(name)==0 or len(code)==0 or len(qty)==0 or len(price)==0:
            self.warning.setText("Fill all Value's")
        else:
            db.add_Inventy(name,code,qty,price)
            self.warning.setText("Saved")

            
            





        









app=QApplication(sys.argv)
widget=QStackedWidget()
window=Login()
widget.addWidget(window)
widget.show()
sys.exit(app.exec())

