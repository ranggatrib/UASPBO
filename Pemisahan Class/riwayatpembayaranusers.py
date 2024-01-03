import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMainWindow, QHeaderView, QApplication, QTableWidget, QTableWidgetItem
from PyQt6.uic import loadUi
import mysql.connector as mc
from managerRiwayatPembayaran import ManagerRiwayatPembayaran

class RiwayatPemabayaranUsr(QMainWindow, ManagerRiwayatPembayaran):
    def __init__(self):
        super().__init__()
        loadUi('R_tagihan.ui', self)

        # Menampilkan Riwayat pembayaran dalam tabel
        self.show_tagihan(self.tbl_riwayat)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    penghuni_app = RiwayatPemabayaranUsr()
    penghuni_app.show()
    sys.exit(app.exec())