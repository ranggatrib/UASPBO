import sys
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6.uic import loadUi
from edit_kamar import EditKamar
import mysql.connector as mc 
from managerKamar import ManagerKamar

class UpdateKamar(QDialog, ManagerKamar):
    def __init__(self):
        super().__init__()
        loadUi('dialogUpdateKamar.ui', self)

        self.pb_update.clicked.connect(self.update)
        self.status_label = self.lbl_status  # Tentukan atribut status_label untuk QLabel

    def update(self):
        id_kamar = self.input_id.text()
        no_kmr = self.input_nokmr.text()
        biaya_kamar = self.input_biaya.text()

        update_success = self.edit_kamar(id_kamar, no_kmr, biaya_kamar)

        # Set teks status_label berdasarkan keberhasilan operasi
        if update_success:
            self.status_label.setText("Update Success")
        else:
            self.status_label.setText("Update Failed")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    edit = EditKamar()
    edit.show()
    sys.exit(app.exec())