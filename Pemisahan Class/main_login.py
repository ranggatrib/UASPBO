import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog, QLineEdit
from PyQt6.uic import loadUi
from verifyAdmin import VerifyAdmin
from verifyPenghuni import VerifyPenghuni

class Main_Login(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('Login.ui', self)

        # menampilkan show verify admin
        self.bt_admin.clicked.connect(self.show_verify_admin)

        # menampilkan show verify penghuni
        self.bt_users.clicked.connect(self.show_verify_penghuni)

    def show_verify_admin(self):
        verify = VerifyAdmin()
        verify.exec()

    def show_verify_penghuni(self):
        verify = VerifyPenghuni()
        verify.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Main_Login()
    login.show()
    sys.exit(app.exec())