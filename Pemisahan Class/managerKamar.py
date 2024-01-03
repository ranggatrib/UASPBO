import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog, QLineEdit, QTableWidgetItem, QHeaderView, QTableWidget
from PyQt6.uic import loadUi
import mysql.connector as mc   


class ManagerKamar:
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

    def add_kamar(self, id_kamar, no_kamar, biaya_kos):
        try:
            if not self.mydb:
                self.connect_DB()

            query = "INSERT INTO tbl_kamar (id_kamar, no_kamar, biaya_kos) VALUES (%s, %s, %s)"
            values = (id_kamar, no_kamar, biaya_kos)

            self.execute_query(query, values)
            return True

        except mc.Error as e:
            print("Error Inserting Kamar Data:", e)
            return False


    def show_kamar(self, table_widget):
        try:
            if not self.mydb:
                self.connect_DB()

            mycursor = self.mydb.cursor()

            # Mengambil data dari tabel tbl_kamar
            query = "SELECT * FROM tbl_kamar"
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
            print("Error showing kamar data:", e)

  
    def del_kamar(self, table_widget):
        try:
            # Pastikan bahwa objek adalah instans dari QTableWidget
            if not isinstance(table_widget, QTableWidget):
                raise ValueError("Error: Invalid table_widget object type. Expected QTableWidget or its subclass.")
            
            # Mendapatkan baris yang dipilih
            selected_row = table_widget.currentRow()

            if selected_row != -1:
                # Mendapatkan ID Kamar dari baris yang dipilih
                id_kamar = table_widget.item(selected_row, 0).text()

                # Membuat kursor untuk menjalankan query di database
                if not self.mydb:
                    self.connect_DB()

                query = "DELETE FROM tbl_kamar WHERE id_kamar = %s"
                values = (id_kamar,)
                self.execute_query(query, values)

                # Memperbarui tampilan tabel setelah penghapusan
                self.show_kamar(table_widget)

        except ValueError as ve:
            print(ve)

        except mc.Error as e:
            print("Error deleting kamar:", e)


    def edit_kamar(self, id_kamar, no_kamar, biaya_kos):
        try:
            if not self.mydb:
                self.connect_DB()

            query = """UPDATE tbl_kamar
                       SET no_kamar = %s,
                           biaya_kos = %s
                       WHERE id_kamar = %s
                    """
            values = (no_kamar, biaya_kos, id_kamar)

            self.execute_query(query, values)

            return True
        except mc.Error as e:
            print("Error Updating Kamar Data:", e)
            return False

    def search_kamar_by_no(self, no_kamar):
        try:
            if not self.mydb:
                self.connect_DB()

            mycursor = self.mydb.cursor()

            # Query untuk mencari data kamar berdasarkan nomor kamar
            query = "SELECT * FROM tbl_kamar WHERE no_kamar LIKE %s"
            values = ("%" + no_kamar + "%",)  # Gunakan tanda persen untuk pencarian substring

            mycursor.execute(query, values)
            data = mycursor.fetchall()

            # Menutup kursor
            mycursor.close()

            return data
        except mc.Error as e:
            print("Error Searching Kamar Data:", e)
            return None