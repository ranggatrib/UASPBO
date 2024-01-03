import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog, QLineEdit
from PyQt6.uic import loadUi
import mysql.connector as mc
from Manager_akun_admin import Akun_admin
from menuAdmin import MenuAdmin

class VerifyAdmin(QDialog, Akun_admin):
    def __init__(self):
        super().__init__()
        loadUi('widgetVerifyAdmin.ui', self)

        self.input_passAdmin_2.setEchoMode(QLineEdit.EchoMode.Password)

        self.pb_login_2.clicked.connect(self.verify_login)
        
    def verify_login(self):
        username = self.input_admin_2.text()
        password = self.input_passAdmin_2.text()

        if self.check_credentials_admin(username, password):
            self.lbl_tes_2.setText("Login Success")
            self.accept()  # Tutup dialog login
            self.show_admin()
        else:
            self.lbl_tes_2.setText("Login Failed")
    
    def show_admin(self):
        self.menuAdmin = MenuAdmin()
        self.menuAdmin.show()