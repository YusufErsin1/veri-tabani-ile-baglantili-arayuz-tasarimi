import sqlite3
import sys
from PyQt5 import QtWidgets

class window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.connect_db()
        self.init_ui()
    
    def connect_db(self):
        connect1=sqlite3.connect("database1.db")
        self.cursor=connect1.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS üyeler(Kullanici_adi TEXT, Sifre TEXT)")
        connect1.commit()
        
        
        
    def init_ui(self):
        self.name=QtWidgets.QLabel("KULLANICI ADI")
        self.sifre=QtWidgets.QLabel("ŞİFRE")
        self.user=QtWidgets.QLineEdit()
        self.password=QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login=QtWidgets.QPushButton("Login")
        self.yazi_alani=QtWidgets.QLabel("")
        
        v_box=QtWidgets.QVBoxLayout()
        
        v_box.addWidget(self.name)
        v_box.addWidget(self.user)
        v_box.addWidget(self.sifre)
        v_box.addWidget(self.password)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.login)
        
        h_box=QtWidgets.QHBoxLayout()
         
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
       
        self.setLayout(h_box)
        self.setWindowTitle("Kullanıcı Girişi")
        
        self.login.clicked.connect(self.log1)
        
        self.show()
    def log1(self):
        ad=self.user.text()
        passwd=self.password.text()
        
        self.cursor.execute("Select * From üyeler where Kullanici_adi=? and Sifre=?",(ad,passwd))
        data=self.cursor.fetchall()
        
        if len(data)==0:
            self.yazi_alani.setText("Yanlış kullanıcı adı veya şifre")
        else:
            self.yazi_alani.setText("Giriş yapılıyor. Hoş geldiniz...")
        
        
app=QtWidgets.QApplication(sys.argv)
window=window()
sys.exit(app.exec_())
