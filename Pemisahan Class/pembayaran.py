import mysql.connector as mc
from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi
from managerRiwayatPembayaran import ManagerRiwayatPembayaran

class Pembayaran(QDialog, ManagerRiwayatPembayaran):
    def __init__(self):
        super().__init__()
        loadUi('pembayaran.ui', self)

        # menampilkan total biaya
        self.refresh_total_biaya()
    
    def refresh_total_biaya(self):
        total_biaya = self.total_biaya_penghuni()  
        self.lbl_totalbiaya.setText(f"Rp. {total_biaya}")