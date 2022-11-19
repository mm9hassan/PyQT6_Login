from PyQt6.QtWidgets import QApplication,QDialog,QStackedWidget,QMessageBox
from PyQt6.uic import load_ui
import sys
import sqlite3
db=sqlite3.connect('system.db')
command=db.cursor()




class Wellcome(QDialog):
    def __init__(self) -> None:
        super(Wellcome,self).__init__()
        load_ui.loadUi('login.ui',self)
        widget.setFixedWidth(400)
        widget.setFixedHeight(300)
        self.btn_enter.clicked.connect(self.login)
        
    # login option
    
    def login(self):
        user=self.id.text()
        password=self.password.text()
        command.execute('SELECT * FROM login')
        back=command.fetchall()
        if len(user)==0 or len(password)==0:
            print('fill value')

        elif user== back[0][1] and  password==back[0][2]:
            print('working')
  
            menu= Menu()
            widget.addWidget(menu)
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            print ('error')
        
        
        
        
        

        # -----Class Menu-------

        # _____END_____


class Menu(QDialog):
    def __init__(self) -> None:
        super(Menu,self).__init__()
        load_ui.loadUi('menu.ui',self)
        
        widget.setMinimumWidth(700)
        widget.setMinimumHeight(500)


        self.save.clicked.connect(self.option)
    

    def option(self):
        name=self.name.text()
        father=self.father.text()
        cnic=self.cnic.text()
        cell=self.cell.text()
        if len(name)==0 or len(father)==0 or len(cnic)==0 or len(cell)==0:
            print('fill all value')
        else:
            command.execute('INSERT INTO profile (name,f_name,cnic,cell) VALUES ("{}","{}","{}","{}")'.format(name,father,cnic,cell))
            db.commit()
            db.close()

            print('working')

    

    

        






app=QApplication(sys.argv)
widget=QStackedWidget()
window=Wellcome()
widget.addWidget(window)


widget.show()
app.exec()