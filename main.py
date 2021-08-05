import PIL.Image
from PIL import Image
from PIL.ExifTags import TAGS
import filetype

import webbrowser
import threading
import warnings
from concurrent.futures import ThreadPoolExecutor

import os

from main_form import *
import show_pic
import qss
from PyQt5 import QtGui, QtWidgets

lock = threading.RLock()
url_list = []

ui = Ui_MainWindow()


def get_pic_gps_point(img_filename):
    try:
        exif_data = {}
        # print(img_filename)
        img_file = Image.open(img_filename)
        info = img_file._getexif()
        if info:
            for (tag, value) in info.items():
                decoded = TAGS.get(tag, tag)
                exif_data[decoded] = value

            exif_gps = exif_data['GPSInfo']
            if exif_gps:
                return {'lat': exif_gps[2], 'lon': exif_gps[4]}
                # lat：纬度；lon：经度
            else:
                return {}

    except KeyError:
        return {}

    except AttributeError:
        return {}

    except OSError:
        return {}

    except PIL.Image.DecompressionBombError:
        return {}


def get_file_list(dir, file_list):
    """只返回文件，不返回目录；返回全目录"""
    newDir = dir

    if os.path.isfile(dir) and filetype.is_image(dir):

        file_list.append(dir)
        # ui.statusBar.showMessage("搜索到图片“" + os.path.basename(dir) + "”")

        # 若只是要返回文件文，使用这个

        # file_list.append(os.path.basename(dir))

    elif os.path.isdir(dir):

        for s in os.listdir(dir):
            try:
                # 如果需要忽略某些文件夹，使用以下代码

                # if s == "xxx":

                # continue

                newDir = os.path.join(dir, s)

                get_file_list(newDir, file_list)
            except PermissionError:
                continue

    return file_list


def get_ok_point(point):
    ok_lat = int(point['lat'][0]) + int(point['lat'][1]) / 60 + int(point['lat'][2]) / 3600
    ok_lon = int(point['lon'][0]) + int(point['lon'][1]) / 60 + int(point['lon'][2]) / 3600

    return [ok_lat, ok_lon]


def get_map_url(file_name, file_path, ok_lat, ok_lon):
    url = 'https://apis.map.qq.com/uri/v1/marker?marker=coord:' + str(ok_lat) + ',' + str(ok_lon) + ';' \
        'title:照片“' + file_name + '”拍摄地点;addr:原文件路径：' + file_path.replace(
        '\\', '/') + '&coord_type=1&referer=demo'

    return url


def open_in_explorer():
    index = ui.lstPictures.selectedIndexes()
    for i in index:
        pic_path = mid(url_list[i.row()], "：", "&")
        if os.path.exists(pic_path):
            # print("explorer.exe " + pic_path.replace("/", "\\"))
            os.system("start /B explorer.exe /n,/select," + pic_path.replace("/", "\\"))
        else:
            QtWidgets.QMessageBox.warning(MainWindow, "警告", "您选择的图片中无GPS坐标，请自行查看！")


def open_url():
    index = ui.lstPictures.selectedIndexes()
    for i in index:
        if url_list[i.row()]:
            webbrowser.open(url_list[i.row()])
        else:
            QtWidgets.QMessageBox.warning(MainWindow, "警告", "您选择的图片中无GPS坐标，无法打开地图！")


def show_picture():
    windows = []
    index = ui.lstPictures.selectedIndexes()
    for i in index:
        pic_path = mid(url_list[i.row()], "：", "&")
        windows.append(show_pic.PicWindow(pic_path))

    for window in windows:
        window.start()


def calc_size(pic):
    height = pic.height()
    width = pic.width()

    n = 1
    while width / n > MainWindow.width() * 0.4:
        n += 1
    width /= n
    print(width)

    height = (width * height) / pic.width()

    return {'height': height, 'width': width}


def mid(var, start, stop):
    start_index = var.index(start)
    stop_index = var.index(stop)
    return var[start_index + 1:stop_index]


def set_enable(status):
    ui.txtPath.setEnabled(status)
    ui.lstPictures.setEnabled(status)
    ui.cmdGetFile.setEnabled(status)
    ui.cmdGetFolder.setEnabled(status)
    ui.cmdStart.setEnabled(status)
    ui.cmdOpenMap.setEnabled(status)
    ui.cmdOpenFile.setEnabled(status)
    ui.cmdViewPicture.setEnabled(status)


def find_file():
    # return QtWidgets.QFileDialog.getOpenFileName(None, "请选择图片文件", "./", "图片文件(*.jpg);;图片文件(*.png);;"
    #                                                                     "图片文件(*.jpeg);;图片文件(*.bmp);;图片文件(*.gif)")
    file_path = QtWidgets.QFileDialog.getOpenFileName(None, "选择图片文件", ui.txtPath.text(), "图片文件(*.jpg *.jpeg *.png *.bmp *.gif)")
    ui.txtPath.setText(file_path[0].replace("/", "\\"))


def find_folder():
    folder_path = QtWidgets.QFileDialog.getExistingDirectory(None, "选择待搜索的文件夹", ui.txtPath.text())
    # print(folder_path)
    ui.txtPath.setText(folder_path.replace("/", "\\"))


def change_txt():
    if ui.txtPath.text() == '' or not os.path.exists(ui.txtPath.text()):
        set_enable(False)
    else:
        pass


def start_check():
    if ui.txtPath.text():
        for n in ui.txtPath.text().split("|"):
            if not os.path.exists(n):
                QtWidgets.QMessageBox.warning(MainWindow, "警告", "文件/文件夹路径无效，请重新填写！")
                return 0

        thread1 = threading.Thread(target=check_pic)
        thread1.start()
    else:
        QtWidgets.QMessageBox.warning(MainWindow, "警告", "请填写文件/文件夹路径！")


def check_pic():
    urls = []
    set_enable(False)

    for n in ui.txtPath.text().split("|"):
        if not os.path.isdir(n) and filetype.is_image(n):
            ui.cmdStart.setText("检测GPS信息...")

            point = get_pic_gps_point(n)
            if point:
                ok_point = get_ok_point(point)
                ui.lstPictures.addItem("图片“" + os.path.basename(n) + "”检测出GPS坐标：纬度" + str(ok_point[0]) + "，经度：" + str(ok_point[1]))
                urls.append(get_map_url(os.path.basename(n), n, ok_point[0], ok_point[1]))
            else:
                ui.lstPictures.addItem("图片“" + os.path.basename(n) + "”未检测出GPS坐标。\n")
        else:
            ui.cmdStart.setText("扫描图片文件中...")
            ui.statusBar.showMessage("扫描图片文件中...")

            lock.acquire()
            pool = ThreadPoolExecutor(max_workers=1)
            thread = pool.submit(get_file_list, n, [])
            # while not thread.done():
            #     pass
            file_list = thread.result()
            pool.shutdown()
            # print(file_list)
            lock.release()

            ui.lstPictures.clear()
            ui.cmdStart.setText("检测GPS信息中...")

            lock.acquire()
            for c in file_list:
                ui.statusBar.showMessage("正在检测：" + c)
                point = get_pic_gps_point(c)
                if point:
                    ok_point = get_ok_point(point)
                    ui.lstPictures.addItem("图片“" + os.path.basename(c) + "”检测出GPS坐标：纬度" + str(ok_point[0]) +
                                           "，经度：" + str(ok_point[1]) + "\n")
                    urls.append(get_map_url(os.path.basename(c), c, ok_point[0], ok_point[1]))
                else:
                    # print("图片“" + os.path.basename(c) + "”未检测出GPS坐标。\n")
                    pass
            lock.release()

    lock.acquire()

    url_list.clear()
    for a in urls:
        if isinstance(a, list):
            for b in a:
                url_list.append(b)
        else:
            url_list.append(a)

    ui.cmdStart.setText("开始检测")
    ui.statusBar.showMessage("检测结束")
    set_enable(True)

    lock.release()


if __name__ == '__main__':
    import sys

    warnings.filterwarnings('ignore')

    app = QtWidgets.QApplication(sys.argv)
    # apply_stylesheet(app, theme='light_blue.xml')

    global MainWindow
    MainWindow = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setStyleSheet(qss.qss_light_blue)

    # MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
    ui.cmdGetFile.clicked.connect(find_file)
    ui.cmdGetFolder.clicked.connect(find_folder)
    ui.cmdStart.clicked.connect(start_check)
    ui.cmdOpenMap.clicked.connect(open_url)
    ui.cmdOpenFile.clicked.connect(open_in_explorer)
    ui.cmdViewPicture.clicked.connect(show_picture)
    ui.txtPath.textChanged.connect(change_txt)
    # ui.lstPictures.itemClicked.connect(show_picture)
    ui.lstPictures.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

    ret = ''
    path = sys.argv[1:]
    if path:
        for a in path:
            ret += a + "|"
        ui.txtPath.setText(ret)

    MainWindow.show()
    sys.exit(app.exec_())
