# -*- coding: utf-8 -*- 

import sys
import os
import math

from draw_target import *
from make_solution import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QPushButton
from PIL.ImageQt import ImageQt

try:
    from scipy.spatial import cKDTree as KDTree
    import numpy as np
    IMPORTED_SCIPY = True
except ImportError:
    IMPORTED_SCIPY = False

TOTAL_CIRCLES = 500
image2 = None

first_flag = True
overlap_image = Image
second_image = Image
second_overlap_image = Image

firstFileName = None
firstOverFileName = None
secondFileName = None
secondOverFileName = None
target_num = 1

def generate_circle(image_width, image_height, min_diameter, max_diameter):
    # define the location of circle, return : circle(x-coordinate, y-coordinate, radius)
    radius = random.triangular(min_diameter, max_diameter,
                               max_diameter * 0.2 + min_diameter * 0.8) / 2
    # the diameter of circle achieve triangular distribution and it is inclined to minimum

    angle = random.uniform(0, math.pi * 2)
    # random angle
    distance_from_center = random.uniform(0, image_width * 0.48 - radius)
    # random distance
    x = image_width  * 0.5 + math.cos(angle) * distance_from_center
    y = image_height * 0.5 + math.sin(angle) * distance_from_center
    # assign a random diameter circle to the random location from center

    return x, y, radius


def circle_intersection(x1_y1_r1, x2_y2_r2):
    # check whether or not two circles are intersection, if not, return true, return : boolean
    x1, y1, r1 = x1_y1_r1
    x2, y2, r2 = x2_y2_r2
    return (x2 - x1)**2 + (y2 - y1)**2 < 1.13*(r2 + r1)**2


def circle_draw(draw_image, image, x_y_r, target_num):
    global overlap_image
    global second_image
    global second_overlap_image
    if target_num in [1, 7]:
        circle_draw_type_1st(draw_image, image, second_image, x_y_r, target_num)
    elif target_num in [2, 4, 11]:
        circle_draw_type_2nd(draw_image, image, overlap_image, x_y_r, target_num)
    elif target_num in [3, 5]:
        circle_draw_type_3rd(draw_image, image, second_image, overlap_image, second_overlap_image, x_y_r, target_num)
    elif target_num in [6, 8, 12]:
        circle_draw_type_4th(draw_image, image, x_y_r, target_num)
    elif target_num in [9]:
        circle_draw_type_5th(draw_image, image, overlap_image, x_y_r)
    elif target_num in [10, 13, 14, 15, 16, 17, 18]:
        circle_draw_type_6th(draw_image, image, second_image, x_y_r, target_num)
    elif target_num in [19, 20, 21]:
        circle_draw_type_7th(draw_image, image, second_image, x_y_r, target_num)
    else:
        print('1~21 사이의 숫자를 입력해주세요')
        sys.exit()


def bounded_check(image, x_y_r):
    # check circle cross boundary, if not, return true, return : boolean
    x, y, r = x_y_r
    cnt = 0
    points_x = [x, x, x, x-r, x+r]
    points_y = [y, y-r, y+r, y, y]

    for k in image:
        for xy in zip(points_x, points_y):
            if k.getpixel(xy)[:3] != BACKGROUND:
                cnt += 1
        if 0 < cnt < 5:
            return False
    return True


dic = {'first': 1, 'second': 2, 'overlap': 3, 'second overlap': 4, 'filter': 3}


def shortcut(keyword, tmp):

    name = tmp
    if 'up' in tmp.lower():
        tmp = '상'
    elif 'down' in tmp.lower():
        tmp = '하'
    sol_table[dic[keyword]] = tmp
    return Image.open('./sample_input/' + name + '.png')


def setting():
    global overlap_image
    global second_image
    global second_overlap_image
    global firstFileName
    global firstOverFileName
    global secondFileName
    global secondOverFileName
    global target_num

    sol_table[0] = target_num
    first_image = shortcut('first',firstFileName)
    images.append(first_image)
    if target_num in [2, 4, 11]:
        overlap_image = shortcut('overlap',firstOverFileName)
        images.append(overlap_image)
    elif target_num in [3, 5]:
        second_image = shortcut('second',secondFileName)
        overlap_image = shortcut('overlap',firstOverFileName)
        second_overlap_image = shortcut('second overlap',secondOverFileName)
        del images[0]
    elif target_num in [6, 8, 12]:
        pass
    elif target_num in [1, 7, 10, 13, 14, 15, 16, 17, 18]:
        second_image = shortcut('second',secondFileName)
        del images[0]
    elif target_num in [9]:
        overlap_image = shortcut('filter',firstOverFileName)
    elif target_num in [19, 20, 21]:
        second_image = shortcut('second',secondFileName)
        images.append(second_image)
    else:
        print('1~21 사이의 숫자를 입력해주세요')
        sys.exit()
    return target_num, first_image

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(693, 490)
        MainWindow.setStyleSheet("QGroupBox {\n"
                                    "    border: 1px solid gray;\n"
                                    "    border-radius: 9px;\n"
                                    "    margin-top: 0.5em;\n"
                                    "}\n"
                                    "\n"
                                    "QGroupBox::title {\n"
                                    "    subcontrol-origin: margin;\n"
                                    "    left: 10px;\n"
                                    "    padding: 0 3px 0 3px;\n"
                                    "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 331, 421))
        self.groupBox.setStyleSheet("QGroupBox {\n"
                                    "    border: 1px solid gray;\n"
                                    "    border-radius: 9px;\n"
                                    "    margin-top: 0.5em;\n"
                                    "}\n"
                                    "\n"
                                    "QGroupBox::title {\n"
                                    "    subcontrol-origin: margin;\n"
                                    "    left: 10px;\n"
                                    "    padding: 0 3px 0 3px;\n"
                                    "}")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.lblTargetNum = QtWidgets.QLabel(self.groupBox)
        self.lblTargetNum.setGeometry(QtCore.QRect(10, 30, 64, 15))
        self.lblTargetNum.setObjectName("lblTargetNum")
        self.comboTarget = QtWidgets.QComboBox(self.groupBox)
        self.comboTarget.setGeometry(QtCore.QRect(230, 30, 94, 22))
        self.comboTarget.setObjectName("comboTarget")
        for i in range(1,22):
            self.comboTarget.addItem("")
        self.lblFirstChar = QtWidgets.QLabel(self.groupBox)
        self.lblFirstChar.setGeometry(QtCore.QRect(10, 80, 81, 16))
        self.lblFirstChar.setObjectName("lblFirstChar")
        self.txtfirst = QtWidgets.QTextBrowser(self.groupBox)
        self.txtfirst.setGeometry(QtCore.QRect(10, 110, 311, 31))
        self.txtfirst.setOpenExternalLinks(False)
        self.txtfirst.setObjectName("txtfirst")
        self.btnFirst = QtWidgets.QPushButton(self.groupBox)
        self.btnFirst.setGeometry(QtCore.QRect(230, 80, 93, 28))
        self.btnFirst.setObjectName("btnFirst")
        self.btnFirstOver = QtWidgets.QPushButton(self.groupBox)
        self.btnFirstOver.setGeometry(QtCore.QRect(230, 150, 93, 28))
        self.btnFirstOver.setObjectName("btnFirstOver")
        self.txtFirstOver = QtWidgets.QTextBrowser(self.groupBox)
        self.txtFirstOver.setGeometry(QtCore.QRect(10, 180, 311, 31))
        self.txtFirstOver.setOpenExternalLinks(False)
        self.txtFirstOver.setObjectName("txtFirstOver")
        self.lblFirstOver = QtWidgets.QLabel(self.groupBox)
        self.lblFirstOver.setGeometry(QtCore.QRect(10, 150, 81, 16))
        self.lblFirstOver.setObjectName("lblFirstOver")
        self.lblSndOver = QtWidgets.QLabel(self.groupBox)
        self.lblSndOver.setGeometry(QtCore.QRect(10, 300, 81, 16))
        self.lblSndOver.setObjectName("lblSndOver")
        self.txtSndOver = QtWidgets.QTextBrowser(self.groupBox)
        self.txtSndOver.setGeometry(QtCore.QRect(10, 330, 311, 31))
        self.txtSndOver.setOpenExternalLinks(False)
        self.txtSndOver.setObjectName("txtSndOver")
        self.btnSndOver = QtWidgets.QPushButton(self.groupBox)
        self.btnSndOver.setGeometry(QtCore.QRect(230, 300, 93, 28))
        self.btnSndOver.setObjectName("btnSndOver")
        self.btnSnd = QtWidgets.QPushButton(self.groupBox)
        self.btnSnd.setGeometry(QtCore.QRect(230, 230, 93, 28))
        self.btnSnd.setObjectName("btnSnd")
        self.txtSnd = QtWidgets.QTextBrowser(self.groupBox)
        self.txtSnd.setGeometry(QtCore.QRect(10, 260, 311, 31))
        self.txtSnd.setOpenExternalLinks(False)
        self.txtSnd.setObjectName("txtSnd")
        self.lblSndChar = QtWidgets.QLabel(self.groupBox)
        self.lblSndChar.setGeometry(QtCore.QRect(10, 230, 81, 16))
        self.lblSndChar.setObjectName("lblSndChar")
        self.btnTrans = QtWidgets.QPushButton(self.groupBox)
        self.btnTrans.setGeometry(QtCore.QRect(230, 380, 93, 28))
        self.btnTrans.setObjectName("btnTrans")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(370, 10, 301, 421))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btnSave = QtWidgets.QPushButton(self.groupBox_2)
        self.btnSave.setGeometry(QtCore.QRect(200, 380, 93, 28))
        self.btnSave.setObjectName("btnSave")
        self.resultImage = QtWidgets.QLabel(self.groupBox_2)
        self.resultImage.setGeometry(QtCore.QRect(10, 30, 280, 330))
        self.resultImage.setObjectName("resultImage")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 693, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def selectionChanged(self):
        global target_num
        self.btnFirst.setEnabled(True)
        self.btnFirstOver.setEnabled(True)
        self.btnSnd.setEnabled(True)
        self.btnSndOver.setEnabled(True)

        target_num = int(self.comboTarget.currentText())
        print(target_num)
        if target_num in [2, 4, 11]:
            self.btnSnd.setEnabled(False)
            self.btnSndOver.setEnabled(False)
        elif target_num in [3, 5]:
            pass

        elif target_num in [6, 8, 12]:
            self.btnFirstOver.setEnabled(False)
            self.btnSnd.setEnabled(False)
            self.btnSndOver.setEnabled(False)

        elif target_num in [1, 7, 10, 13, 14, 15, 16, 17, 18]:
            self.btnFirstOver.setEnabled(False)
            self.btnSndOver.setEnabled(False)

        elif target_num in [9]:
            self.btnSnd.setEnabled(False)
            self.btnSndOver.setEnabled(False)
        elif target_num in [19, 20, 21]:
            self.btnFirstOver.setEnabled(False)
            self.btnSndOver.setEnabled(False)

    def openFileDialog1(self):
        global firstFileName
        fileName, _ = QFileDialog.getOpenFileName(self)
        print(fileName)
        if fileName:
            firstFileName = fileName.split('/')[-1].split('.')[0]
            self.txtfirst.setText(fileName)


    def openFileDialog2(self):
        global firstOverFileName
        fileName, _ = QFileDialog.getOpenFileName(self)
        print(fileName)
        if fileName:
            firstOverFileName = fileName.split('/')[-1].split('.')[0]
            self.txtFirstOver.setText(fileName)


    def openFileDialog3(self):
        global secondFileName
        fileName, _ = QFileDialog.getOpenFileName(self)
        print(fileName)
        if fileName:
            secondFileName = fileName.split('/')[-1].split('.')[0]
            self.txtSnd.setText(fileName)

    def openFileDialog4(self):
        global secondOverFileName
        fileName, _ = QFileDialog.getOpenFileName(self)

        if fileName:
            secondOverFileName = fileName.split('/')[-1].split('.')[0]
            self.txtSndOver.setText(fileName)

    def transpose(self):
        global image2
        global target_num
        target_num, image = setting()
        image2 = Image.new('RGB', image.size, BACKGROUND)
        draw_image = ImageDraw.Draw(image2)
        global images
        width, height = image.size

        min_diameter = height / 64
        max_diameter = height / 16
        ignore = False

        circle = generate_circle(width, height, min_diameter, max_diameter)
        circles = [circle]
        circle_draw(draw_image, image, circle, target_num)
        try:
            for i in range(TOTAL_CIRCLES):
                tries = 0
                if IMPORTED_SCIPY:
                    kdtree = KDTree([(x, y) for (x, y, _) in circles])
                    while True:
                        if i < TOTAL_CIRCLES / 10:
                            circle = generate_circle(width, height, max_diameter * 0.8, max_diameter)
                        elif i < TOTAL_CIRCLES / 2:
                            circle = generate_circle(width, height, min_diameter * 2, max_diameter * 0.8)
                        else:
                            ignore = True
                            circle = generate_circle(width, height, min_diameter, min_diameter * 2)

                        elements, indexes = kdtree.query([(circle[0], circle[1])], k=12)
                        # compare adjacent circles which upper limits are 12
                        for element, index in zip(elements[0], indexes[0]):
                            # escape loop when there is no infinite value and no overlapping
                            if not np.isinf(element) and circle_intersection(circle, circles[index]):
                                break
                        else:
                            if bounded_check(images, circle) or ignore:
                                break
                        tries += 1
                else:
                    while any(circle_intersection(circle, circle2) for circle2 in circles):
                        tries += 1
                        circle = generate_circle(width, height, min_diameter, max_diameter)

                print('{}/{} {}'.format(i, TOTAL_CIRCLES, tries))

                circles.append(circle)
                circle_draw(draw_image, image, circle, target_num)
        except (KeyboardInterrupt, SystemExit):
            pass

        # image2.show()
        print(type(image2))
        qim = ImageQt(image2)
        pix = QtGui.QPixmap.fromImage(qim)
        smaller_pixmap = pix.scaled(280, 280)
        print(type(smaller_pixmap))
        self.resultImage.setPixmap(smaller_pixmap)
        solution()

    def saveImage(self):
        global image2

        output_dir = "./sample_output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        image2.save(os.path.join(output_dir, 'new_colorblindness_sample.png'))
        print("저장되었습니다")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "setting"))
        self.lblTargetNum.setText(_translate("MainWindow", "지표설정"))
        for i in range(1,22):
            self.comboTarget.setItemText(i - 1, _translate("MainWindow", str(i) ))
        self.comboTarget.currentIndexChanged.connect(self.selectionChanged)
        self.lblFirstChar.setText(_translate("MainWindow", "첫번째 문자"))
        self.btnFirst.setText(_translate("MainWindow", "찾아보기"))
        self.btnFirstOver.setText(_translate("MainWindow", "찾아보기"))
        self.lblFirstOver.setText(_translate("MainWindow", "겹침 문자"))
        self.lblSndOver.setText(_translate("MainWindow", "겹침 문자"))
        self.btnSndOver.setText(_translate("MainWindow", "찾아보기"))
        self.btnSnd.setText(_translate("MainWindow", "찾아보기"))
        self.lblSndChar.setText(_translate("MainWindow", "두번째 문자"))
        self.btnTrans.setText(_translate("MainWindow", "변환"))
        self.groupBox_2.setTitle(_translate("MainWindow", "result"))
        self.btnSave.setText(_translate("MainWindow", "저장"))
        self.btnFirstOver.setEnabled(False)
        self.btnSndOver.setEnabled(False)
        self.btnFirst.clicked.connect(self.openFileDialog1)
        self.btnFirstOver.clicked.connect(self.openFileDialog2)
        self.btnSnd.clicked.connect(self.openFileDialog3)
        self.btnSndOver.clicked.connect(self.openFileDialog4)
        self.btnTrans.clicked.connect(self.transpose)
        self.btnSave.clicked.connect(self.saveImage)


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
