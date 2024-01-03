import mysql.connector as mc
from PyQt6.QtWidgets import QTableWidgetItem, QHeaderView, QMainWindow, QApplication, QLineEdit, QDialog, QLabel
from PyQt6.uic import loadUi
from managerPenghuni import Manager_penghuni
from addpenghuini import AddPenghuni
from edit_penghuni import EditPenghuni
import sys

class Main_Penghuni(QMainWindow, Manager_penghuni):
    def __init__(self):
        super().__init__()
        loadUi('widget_resident.ui', self)

        # Menampilkan data penghuni saat aplikasi pertama kali dijalankan
        self.show_penghuni(self.tbl_penghuni)

        # Menghubungkan tombol hapus dengan fungsi delete
        self.pb_del.clicked.connect(self.delete_penghuni)

        # Menampilkan dialog Update
        self.pb_edit.clicked.connect(self.show_dialog_update)

        
        # Menampilkan dialog Update
        self.pb_add.clicked.connect(self.show_dialog_add)

        # Menghubungkan tombol cari dengan fungsi search
        self.pb_serch.clicked.connect(self.search_penghuni)

        # Merapikan Tabel
        self.tbl_penghuni.resizeColumnsToContents()
        self.tbl_penghuni.resizeRowsToContents()

         # Mengatur ukuran kolom sesuai dengan ukuran tabel
        header = self.tbl_penghuni.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)


    def delete_penghuni(self):
        # Mendapatkan baris yang dipilih
        selected_row = self.tbl_penghuni.currentRow()

        if selected_row != -1:
            # Mendapatkan ID Penghuni dari baris yang dipilih
            id_penghuni = self.tbl_penghuni.item(selected_row, 0).text()

            # Menghapus penghuni dari database
            self.del_penghuni(id_penghuni)

            # Memperbarui tampilan tabel setelah penghapusan
            self.show_penghuni(self.tbl_penghuni)

    def search_penghuni(self):
        # Mendapatkan nama penghuni dari input
        nama_penghuni = self.input_nama.text()

        # Mengecek apakah input pencarian tidak kosong
        if nama_penghuni:
            # Mencari penghuni berdasarkan nama
            result = self.search_penghuni_by_name(nama_penghuni)

            # Menampilkan hasil pencarian di tabel
            self.show_search_result(result)
        else:
            # Jika input pencarian kosong, tampilkan semua penghuni
            self.show_penghuni(self.tbl_penghuni)

    def show_search_result(self, data):
        # Menampilkan hasil pencarian di tabel
        self.tbl_penghuni.setRowCount(len(data))
        for row, values in enumerate(data):
            for col, value in enumerate(values):
                item = QTableWidgetItem(str(value))
                self.tbl_penghuni.setItem(row, col, item)
    
    def show_dialog_update(self):
        edit = EditPenghuni()
        edit.exec()
    
    def show_dialog_add(self):
        add = AddPenghuni()
        add.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    penghuni_app = Main_Penghuni()
    penghuni_app.show()
    sys.exit(app.exec())