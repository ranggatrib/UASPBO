import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QStackedWidget
from PyQt6.uic import loadUi
from main_tagihan import TagihanUsr
from riwayatpembayaranusers import RiwayatPemabayaranUsr
# from DB_manage.DB_admin import ManagerAdmin

class MenuPenghuni(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('menuPenghuni.ui', self)

        self.pb_tagihan.clicked.connect(self.show_pembayaran)
        self.pb_riwayat.clicked.connect(self.show_riwayat)
    
    def show_pembayaran(self):
        self.tagihan = TagihanUsr()
        self.tagihan.show()
    
    def show_riwayat(self):
        self.riwayat = RiwayatPemabayaranUsr()
        self.riwayat.show()

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    verify = MenuPenghuni()
    verify.show()
    sys.exit(app.exec())