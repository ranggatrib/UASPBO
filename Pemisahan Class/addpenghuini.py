import mysql.connector as mc
from PyQt6.QtWidgets import  QDialog
from PyQt6.uic import loadUi
from managerPenghuni import Manager_penghuni
import sys

class AddPenghuni(QDialog, Manager_penghuni):
    def __init__ (self):
        super().__init__()
        loadUi('dialogAdd.ui', self)

        self.pb_add.clicked.connect(self.add)
        self.status_label = self.lbl_status  # Tentukan atribut status_label untuk QLabel

    def add(self):
        id = self.input_id.text()
        nama = self.input_nama.text()
        alamat = self.input_alamat.text()
        noHp = self.input_noHp.text()
        idkmr = self.input_idkmr.text()
        nokmr = self.input_kmr.text()
        biaya_tambahan = self.input_biayaTambahan.text()
        tot_biaya = self.input_totBiaya.text()

        add_success = self.add_penghuni(id, nama, alamat, noHp, idkmr, nokmr, biaya_tambahan, tot_biaya)

        # Set teks status_label berdasarkan keberhasilan operasi
        if add_success:
            self.status_label.setText("Insert Success")
        else:
            self.status_label.setText("Inser Failed")
 