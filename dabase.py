import sqlite3

class DataBase:
    def __init__(self) -> None:
        try:
            self.db=sqlite3.connect('system.db')
            self.command=self.db.cursor()
            print('connected')
        except:
                print('Dabase Issue')


        

    def add_Inventy(self,name,code,qty,price):

        try:

            self.command.execute(f"""
            INSERT INTO inventry (p_name,p_code,p_qt,p_price) VALUES ('{name}','{code}','{qty}','{price}')
            """)
            self.db.commit()
        except :
            print('Entry issue')
        


