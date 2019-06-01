# -*- coding: utf-8 -*- 

import sys
import os
import math
from view import *
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

class Ui_MainWindow(Ui_SubWindow):

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

    def btnClickEventOpenFileDialog1(self):
        global firstFileName
        fileName, _ = QFileDialog.getOpenFileName(self)
        print(fileName)
        if fileName:
            firstFileName = fileName.split('/')[-1].split('.')[0]
            self.txtfirst.setText(fileName)


    def btnClickEventOpenFileDialog2(self):
        global firstOverFileName
        fileName, _ = QFileDialog.getOpenFileName(self)
        print(fileName)
        if fileName:
            firstOverFileName = fileName.split('/')[-1].split('.')[0]
            self.txtFirstOver.setText(fileName)


    def btnClickEventOpenFileDialog3(self):
        global secondFileName
        fileName, _ = QFileDialog.getOpenFileName(self)
        print(fileName)
        if fileName:
            secondFileName = fileName.split('/')[-1].split('.')[0]
            self.txtSnd.setText(fileName)

    def btnClickEventOpenFileDialog4(self):
        global secondOverFileName
        fileName, _ = QFileDialog.getOpenFileName(self)

        if fileName:
            secondOverFileName = fileName.split('/')[-1].split('.')[0]
            self.txtSndOver.setText(fileName)

    def btnClickEventTranspose(self):
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

    def btnClickEventSaveImage(self):
        global image2

        output_dir = "./sample_output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        image2.save(os.path.join(output_dir, 'new_colorblindness_sample.png'))
        print("저장되었습니다")


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
