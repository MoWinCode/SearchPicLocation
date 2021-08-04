import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui
import pic_form


class PicWindow(QMainWindow):
    def __init__(self, pic_path, parent=None):
        super().__init__(parent)
        self.ui = pic_form.Ui_MainWindow()
        self.ui.setupUi(self)
        self.pic_path = pic_path

        pic = QtGui.QPixmap(self.pic_path)
        self.ui.lblPicture.setPixmap(pic)
        self.resize(pic.width(), pic.height())


if __name__ == '__main__':
    my_app = QApplication(sys.argv)
    my_dlg = PicWindow(r"C:\Users\Administrator.SC-202107041348\Desktop\r.jpg")
    my_dlg.show()
    sys.exit(my_app.exec_())
