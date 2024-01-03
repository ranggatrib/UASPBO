import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QStackedWidget
from PyQt6.uic import loadUi
from main_penghuni import Main_Penghuni
from edit_kamar import EditKamar
from riwayatpembayaranusers import RiwayatPemabayaranUsr

# from DB_manage.DB_admin import ManagerAdmin

class MenuAdmin(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('menuAdmin.ui', self)
        
        self.pb_penghuni.clicked.connect(self.show_penghuni)
        self.pb_kamar.clicked.connect(self.show_kamar)
        self.pb_riwayat.clicked.connect(self.show_riwayat_pembayaran)
    
    def show_penghuni(self):
        self.penghuni = Main_Penghuni()
        self.penghuni.show()
    
    def show_kamar(self):
        edit = EditKamar()
        edit.show()
    
    def show_riwayat_pembayaran(self):
        self.riwayat = RiwayatPemabayaranUsr()
        self.riwayat.show()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    verify = MenuAdmin()
    verify.show()
    sys.exit(app.exec())