import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMainWindow, QHeaderView, QApplication, QTableWidget, QTableWidgetItem
from PyQt6.uic import loadUi
import mysql.connector as mc

class ManagerRiwayatPembayaran:
    def __init__(self):
        self.mydb = None

    def connect_DB(self):
        try:
            self.mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="db_kos"
            )
            return True
        except mc.Error as e:
            return False

    def execute_query(self, query, values=None):
        try:
            if not self.mydb:
                self.connect_DB()

            mycursor = self.mydb.cursor()

            if values:
                mycursor.execute(query, values)
            else:
                mycursor.execute(query)

            self.mydb.commit()
            mycursor.close()
        except mc.Error as e:
            print("Error executing query:", e)

    def show_tagihan(self, table_widget):
        try:
            if not self.mydb:
                self.connect_DB()

            mycursor = self.mydb.cursor()

            # Query untuk menampilkan data tagihan
            query = """
            SELECT 
                tbl_penghuni.nama_penghuni, 
                tbl_penghuni.no_kamar, 
                MONTHNAME(tbl_tagihan_kos.tanggal) AS bulan_pembayaran,
                tbl_tagihan_kos.jml_pembayaran,
                tbl_tagihan_kos.denda,
                tbl_tagihan_kos.kekurangan
            FROM 
                tbl_penghuni
            JOIN
                tbl_tagihan_kos ON tbl_penghuni.id_penghuni = tbl_tagihan_kos.id_penghuni
            """

            mycursor.execute(query)
            data = mycursor.fetchall()

            # Menambahkan data ke dalam tabel
            table_widget.setRowCount(len(data))
            for row, values in enumerate(data):
                for col, value in enumerate(values):
                    item = QTableWidgetItem(str(value))
                    table_widget.setItem(row, col, item)

            # Menutup kursor
            mycursor.close()
        except mc.Error as e:
            print("Error showing tagihan data:", e)