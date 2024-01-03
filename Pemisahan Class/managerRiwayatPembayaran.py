import mysql.connector as mc
from PyQt6.QtWidgets import QMainWindow, QHeaderView, QApplication, QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout, QPushButton, QLabel
import sys
from PyQt6.uic import loadUi

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
            print("Error connecting to the database:", e)
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

    def total_biaya_penghuni(self):
        try:
            if not self.mydb:
                self.connect_DB()

            mycursor = self.mydb.cursor()

            # Query untuk menghitung total biaya dari tabel penghuni
            query = """
            SELECT 
                total_biaya
            FROM 
                tbl_penghuni
            """

            mycursor.execute(query)
            total_biaya_penghuni = mycursor.fetchone()[0]

            # Menutup kursor
            mycursor.close()

            return total_biaya_penghuni
        except mc.Error as e:
            print("Error calculating total biaya penghuni:", e)
            return 0