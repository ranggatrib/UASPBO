import sys
import mysql.connector as mc
from PyQt6.QtWidgets import QMainWindow, QApplication
from pembayaran import Pembayaran
from PyQt6.uic import loadUi

class TagihanUsr(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('tagihan.ui', self)

        self.pb_bayar.clicked.connect(self.show_bayar)
    
    def show_bayar(self):
        pembayaran = Pembayaran()
        pembayaran.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pembayaran_app = TagihanUsr()
    pembayaran_app.show()
    sys.exit(app.exec())
