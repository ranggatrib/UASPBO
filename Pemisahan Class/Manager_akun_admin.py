
import mysql.connector as mc

class Akun_admin:
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

    def check_credentials_admin(self, username, password):
        try:
            if not self.mydb:
                if not self.connect_DB():
                    print("Gagal terhubung ke basis data.")
                    return False

            mycursor = self.mydb.cursor()

            sql = """SELECT * 
                      FROM tbl_akun_amin 
                      WHERE username_admin = %s AND paswordHash = %s
                    """
            
            val = (username, password)

            mycursor.execute(sql, val)

            result = mycursor.fetchone()

            mycursor.close()

            if result:
                return True
            else:
                return False
        except mc.Error as e:
            print("Error saat memeriksa kredensial:", e)
            return False

    def check_credentials_penghuni(self, username, password):
        try:
            if not self.mydb:
                if not self.connect_DB():
                    print("Gagal terhubung ke basis data.")
                    return False

            mycursor = self.mydb.cursor()

            sql = """SELECT * 
                      FROM tbl_akun_penghuni
                      WHERE username_penghuni = %s AND paswordHash = %s
                    """
            
            val = (username, password)

            mycursor.execute(sql, val)

            result = mycursor.fetchone()

            mycursor.close()

            if result:
                return True
            else:
                return False
        except mc.Error as e:
            print("Error saat memeriksa kredensial:", e)
            return False
