import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog, QLineEdit
from PyQt6.uic import loadUi
import mysql.connector as mc

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('Login.ui', self)

        # menampilkan show verify admin
        self.bt_admin.clicked.connect(self.show_verify_admin)

        # menampilkan show verify penghuni
        self.bt_users.clicked.connect(self.show_verify_penghuni)

    def show_verify_admin(self):
        verify = VerifyAdmin()
        verify.exec()

    def show_verify_penghuni(self):
        verify = VerifyPenghuni()
        verify.exec()

class ManagerAdmin:
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

class VerifyPenghuni(QDialog, ManagerAdmin):
    def __init__(self):
        super().__init__()
        loadUi('verifyAcount.ui', self)
        
        self.input_pass.setEchoMode(QLineEdit.EchoMode.Password)

        self.pb_login.clicked.connect(self.verify_login)
        
    def verify_login(self):
        username = self.input_users.text()
        password = self.input_pass.text()

        if self.check_credentials_penghuni(username, password):
            self.lbl_tes.setText("Login Success")

        else:
            self.lbl_tes.setText("Login Failed")

class VerifyAdmin(QDialog, ManagerAdmin):
    def __init__(self):
        super().__init__()
        loadUi('verifyAcount.ui', self)

        self.input_pass.setEchoMode(QLineEdit.EchoMode.Password)

        self.pb_login.clicked.connect(self.verify_login)
        
    def verify_login(self):
        username = self.input_users.text()
        password = self.input_pass.text()

        if self.check_credentials_admin(username, password):
            self.lbl_tes.setText("Login Success")
          
        else:
            self.lbl_tes.setText("Login Failed")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec())