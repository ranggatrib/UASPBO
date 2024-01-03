import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog, QLineEdit, QTableWidgetItem, QHeaderView, QTableWidget
from PyQt6.uic import loadUi
import mysql.connector as mc
from add_kamar import AddKamar
from managerKamar import ManagerKamar
from updatekamar import UpdateKamar 

class EditKamar(QDialog, ManagerKamar):
    def __init__(self):
        super().__init__()  # Memanggil konstruktor QDialog
        ManagerKamar.__init__(self)  # Memanggil konstruktor ManagerKamar
        loadUi('widget_kamar.ui', self)

        # Menampilkan data Kamar saat aplikasi pertama kali dijalankan
        self.show_kamar(self.tbl_kamar)

        # Menghubungkan tombol hapus dengan fungsi delete
        self.pb_del.clicked.connect(lambda: self.del_kamar(self.tbl_kamar))

        # Menghubungkan tombol search dengan fungsi cari
        self.pb_search.clicked.connect(self.search_kamar)

        # Menampilkan dialog Update
        self.pb_update.clicked.connect(self.show_dialog_update)

        # Menampilkan dialog Add
        self.pb_add.clicked.connect(self.show_dialog_add)

        # Merapikan Tabel
        self.tbl_kamar.resizeColumnsToContents()
        self.tbl_kamar.resizeRowsToContents()

        # Mengatur ukuran kolom sesuai dengan ukuran tabel
        header = self.tbl_kamar.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

    def search_kamar(self):
        # Mendapatkan nomor kamar dari input
        no_kamar = self.input_nomor.text()

        # Mengecek apakah input pencarian tidak kosong
        if no_kamar:
            # Mencari kamar berdasarkan nomor kamar
            result = self.search_kamar_by_no(no_kamar)

            # Menampilkan hasil pencarian di tabel
            self.show_search_result(result)
        else:
            # Jika input pencarian kosong, tampilkan semua kamar
            self.show_kamar(self.tbl_kamar)

    def show_search_result(self, data):
        # Menampilkan hasil pencarian di tabel
        self.tbl_kamar.setRowCount(len(data))
        for row, values in enumerate(data):
            for col, value in enumerate(values):
                item = QTableWidgetItem(str(value))
                self.tbl_kamar.setItem(row, col, item)

    def show_dialog_update(self):
        update_dialog = UpdateKamar()
        update_dialog.exec()
        # Setelah dialog ditutup, refresh data di tabel
        self.show_kamar(self.tbl_kamar)

    def show_dialog_add(self):
        add_dialog = AddKamar()
        add_dialog.exec()
        # Setelah dialog ditutup, refresh data di tabel
        self.show_kamar(self.tbl_kamar)