import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog, QLineEdit
from Manager_akun_admin import Akun_admin
from PyQt6.uic import loadUi
from menuPenghuni import MenuPenghuni

class VerifyPenghuni(QDialog, Akun_admin):
    def __init__(self):
        super().__init__()
        loadUi('widgetVerifyPenghuni.ui', self)
        
        self.input_pass.setEchoMode(QLineEdit.EchoMode.Password)

        self.pb_login.clicked.connect(self.verify_login)
        
    def verify_login(self):
        username = self.input_users.text()
        password = self.input_pass.text()

        if self.check_credentials_penghuni(username, password):
            self.lbl_tes.setText("Login Success")
            self.show_penghuni()

        else:
            self.lbl_tes.setText("Login Failed")

    def show_penghuni(self):
        app = QApplication(sys.argv)
        menuPenghuni = MenuPenghuni()
        menuPenghuni.show()
        sys.exit(app.exec())