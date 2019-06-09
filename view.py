# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *

class solutionDialog(QDialog):
    def __init__(self):
        super().__init__()


    def setupUI(self, sol):
        self.setGeometry(800, 400, 300, 300)
        self.setWindowTitle("결과")
        self.b = QPlainTextEdit(self)
        self.b.insertPlainText(sol)
        self.b.setGeometry(10, 10, 280, 240)
        self.b.setReadOnly(True)
        self.closeBtn = QtWidgets.QPushButton(self)
        self.closeBtn.setGeometry(QtCore.QRect(200, 260, 90, 28))
        self.closeBtn.setText("닫기")
        self.closeBtn.clicked.connect(self.closeButtonClicked)


    def closeButtonClicked(self):
        self.close()


class Ui_SubWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(693, 460)
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
        # self.btnTrans.setGeometry(QtCore.QRect(10, 380, 93, 28))
        self.btnTrans.setGeometry(QtCore.QRect(230, 380, 93, 28))

        self.btnTrans.setObjectName("btnTrans")
        self.progressBar = QProgressBar(self.groupBox)
        # self.progressBar.setGeometry(QtCore.QRect(110, 380, 220, 30))
        self.progressBar.setGeometry(QtCore.QRect(10, 380, 220, 30))

        self.progressBar.setMaximum(500)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(370, 10, 301, 421))
        self.groupBox_2.setObjectName("groupBox_2")
        self.btnSol = QtWidgets.QPushButton(self.groupBox_2)
        self.btnSol.setGeometry(QtCore.QRect(10, 380, 93, 28))
        self.btnSol.setObjectName("btnSol")
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
        self.btnSol.setText(_translate("MainWindow", "결과"))
        self.btnFirstOver.setEnabled(False)
        self.btnSndOver.setEnabled(False)
        self.btnFirst.clicked.connect(self.btnClickEventOpenFileDialog1)
        self.btnFirstOver.clicked.connect(self.btnClickEventOpenFileDialog2)
        self.btnSnd.clicked.connect(self.btnClickEventOpenFileDialog3)
        self.btnSndOver.clicked.connect(self.btnClickEventOpenFileDialog4)
        self.btnTrans.clicked.connect(self.btnClickEventTranspose)
        self.btnSave.clicked.connect(self.btnClickEventSaveImage)
        self.btnSol.clicked.connect(self.btnClickEventSolDialog)