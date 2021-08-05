import sys
import os

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui
import pic_form


def get_screen_size():
    import ctypes
    win_api = ctypes.windll.user32
    width = win_api.GetSystemMetrics(0)
    height = win_api.GetSystemMetrics(1)
    return {'width': width, 'height': height}


class PicWindow(QMainWindow):
    window = []

    def __init__(self, pic_path, parent=None):
        super().__init__(parent)
        self.ui = pic_form.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lblPicture.setScaledContents(True)

        self.pic_path = pic_path
        pic = QtGui.QPixmap(self.pic_path)

        size = get_screen_size()
        if pic.height() >= size['height'] and pic.width() >= size['width']:
            self.ui.lblPicture.setMaximumSize(size['width'], size['height'])
            self.showMaximized()
            self.showNormal()
            self.showMaximized()
        else:
            self.resize(pic.width(), pic.height())

        self.ui.lblPicture.setPixmap(pic)
        self.setWindowTitle("定位图片坐标 - 图片预览 - " + os.path.basename(self.pic_path))

    def start(self):
        a = PicWindow(self.pic_path)
        self.window.append(a)
        a.show()


if __name__ == '__main__':
    my_app = QApplication(sys.argv)
    my_dlg = PicWindow(r"C:\Users\Administrator.SC-202107041348\Desktop\r.jpg")

    my_dlg.show()
    sys.exit(my_app.exec_())
