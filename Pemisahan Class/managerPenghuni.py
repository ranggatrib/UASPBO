import mysql.connector as mc
from PyQt6.QtWidgets import QTableWidgetItem


class Manager_penghuni:
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
    

    def add_penghuni(self, id, nama, alamat, no_hp, id_kmr, no_kmr, biaya_tam, tot_biaya):
        try:
            if not self.mydb:
                self.connect_DB()

            mycursor = self.mydb.cursor()

            sql = """INSERT INTO tbl_penghuni (
                    id_penghuni, 
                    nama_penghuni,
                    alamt_penghuni,
                    no_hp_penghuni,
                    id_kamar,
                    no_kamar,
                    biaya_tambahan,
                    total_biaya
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            
            val = (id, nama, alamat, no_hp, id_kmr, no_kmr, biaya_tam, tot_biaya)

            mycursor.execute(sql, val)

            # Committing the changes and closing the cursor
            self.mydb.commit()
            mycursor.close()
            return True
        except mc.Error as e:
            print("Error Inserting Data:", e)
            return False

    def show_penghuni(self, table_widget):
        try:
            if not self.mydb:
                self.connect_DB()

            mycursor = self.mydb.cursor()

            # Mengambil data dari tabel tbl_penghuni
            query = "SELECT * FROM tbl_penghuni"
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
            print("database not exist:", e)
    
    def del_penghuni(self, table_widget):
        try:
            # Mendapatkan baris yang dipilih
            selected_row = table_widget.currentRow()

            if selected_row != -1:
                # Mendapatkan ID Penghuni dari baris yang dipilih
                id_penghuni = table_widget.item(selected_row, 0).text()

                # Membuat kursor untuk menjalankan query di database
                if not self.mydb:
                    self.connect_DB()

                mycursor = self.mydb.cursor()

                # Menghapus penghuni dari database
                query = f"DELETE FROM tbl_penghuni WHERE id_penghuni = {id_penghuni}"
                mycursor.execute(query)
                self.mydb.commit()

                # Menutup kursor
                mycursor.close()

                # Memperbarui tampilan tabel setelah penghapusan
                self.show_penghuni(table_widget)

        except mc.Error as e:
            print("Error deleting penghuni:", e)

    def edit_penghuni(self, id_penghuni, nama, alamat, no_hp, id_kmr, no_kmr, biaya_tam, tot_biaya):
        try:
            if not self.mydb:
                self.connect_DB()

            mycursor = self.mydb.cursor()

            # Query untuk mengupdate data penghuni berdasarkan id_penghuni
            sql = """UPDATE tbl_penghuni
                    SET nama_penghuni = %s,
                        alamt_penghuni = %s,
                        no_hp_penghuni = %s,
                        id_kamar = %s,
                        no_kamar = %s,
                        biaya_tambahan = %s,
                        total_biaya = %s
                    WHERE id_penghuni = %s"""

            val = (nama, alamat, no_hp, id_kmr, no_kmr, biaya_tam, tot_biaya, id_penghuni)

            mycursor.execute(sql, val)

            # Committing the changes and closing the cursor
            self.mydb.commit()
            mycursor.close()

            return True
        except mc.Error as e:
            print("Error Updating Data:", e)
            return False

    def search_penghuni_by_name(self, nama):
        try:
            if not self.mydb:
                self.connect_DB()

            mycursor = self.mydb.cursor()

            # Query untuk mencari data penghuni berdasarkan nama
            sql = "SELECT * FROM tbl_penghuni WHERE nama_penghuni LIKE %s"
            val = ("%" + nama + "%",)  

            mycursor.execute(sql, val)
            data = mycursor.fetchall()

            # Menutup kursor
            mycursor.close()

            return data
        except mc.Error as e:
            print("Error Searching Data:", e)
            return None
        
    def search_penghuni_by_kamar(self, no_kamar):
        try:
            if not self.mydb:
                self.connect_DB()

            mycursor = self.mydb.cursor()

            # Query untuk mencari data penghuni berdasarkan nama
            sql = "SELECT * FROM tbl_penghuni WHERE no_kamar LIKE %s"
            val = ("%" + no_kamar + "%",)  

            mycursor.execute(sql, val)
            data = mycursor.fetchall()

            # Menutup kursor
            mycursor.close()

            return data
        except mc.Error as e:
            print("Error Searching Data:", e)
            return None
    
    def verify_akun_by_id_penghuni(self, id_penghuni, password_hash):
        try:
            if not self.mydb:
                self.connect_DB()

            mycursor = self.mydb.cursor()

            # Query untuk memverifikasi akun penghuni berdasarkan ID penghuni dan password hash
            sql = "SELECT * FROM tbl_akun_penghuni WHERE id_penghuni = %s AND paswordHash = %s"
            val = (id_penghuni, password_hash)

            mycursor.execute(sql, val)
            result = mycursor.fetchone()

            # Menutup kursor
            mycursor.close()

            return result is not None
        except mc.Error as e:
            print("ID not Exist:", e)
            return False