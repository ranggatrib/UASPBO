import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog, QLineEdit, QTableWidgetItem, QHeaderView, QTableWidget
from PyQt6.uic import loadUi
import mysql.connector as mc 
from managerKamar import ManagerKamar

class AddKamar(QDialog, ManagerKamar):
    def __init__(self):
        super().__init__()
        loadUi('dialogAddKamar.ui', self)

        self.pb_add.clicked.connect(self.add)
        self.status_label = self.lbl_status  # Tentukan atribut status_label untuk QLabel

    def add(self):
        id_kamar = self.input_id.text()
        no_kmr = self.input_nokmr.text()
        biaya_kamar = self.input_biaya.text()

        add_success = self.add_kamar(id_kamar, no_kmr, biaya_kamar)

        # Set teks status_label berdasarkan keberhasilan operasi
        if add_success:
            self.status_label.setText("Insert Success")
        else:
            self.status_label.setText("Insert Failed")
