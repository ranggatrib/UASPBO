import mysql.connector as mc
from PyQt6.QtWidgets import QTableWidgetItem, QHeaderView, QMainWindow, QApplication, QLineEdit, QDialog, QLabel
from PyQt6.uic import loadUi
from managerPenghuni import Manager_penghuni
import sys

class EditPenghuni(QDialog, Manager_penghuni):
    def __init__(self):
        super().__init__()
        loadUi('dialogEdit.ui', self)

        self.pb_update.clicked.connect(self.updatePenghuni)
        
    def updatePenghuni(self):
        id = self.input_id.text()
        nama = self.input_nama.text()
        alamat = self.input_alamat.text()
        noHp = self.input_noHp.text()
        idkmr = self.input_idkmr.text()
        nokmr = self.input_kmr.text()
        biaya_tambahan = self.input_biayaTambahan.text()
        tot_biaya = self.input_totBiaya.text()

        add_success = self.edit_penghuni(id, nama, alamat, noHp, idkmr, nokmr, biaya_tambahan, tot_biaya)

        # Set teks status_label berdasarkan keberhasilan operasi
        if add_success:
            self.lbl_status.setText("Insert Success")
        else:
            self.lbl_status.setText("Inser Failed")