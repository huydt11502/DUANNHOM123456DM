# Form implementation generated from reading ui file 'D:\DUANNHOM123456DM\MainWindowPTB2\UI\giaodienptb2_nhom.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 40, 481, 81))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 111, 61))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 160, 111, 61))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 210, 111, 61))
        self.label_4.setObjectName("label_4")
        self.lineEditA = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditA.setGeometry(QtCore.QRect(160, 130, 441, 31))
        self.lineEditA.setObjectName("lineEditA")
        self.lineEditB = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditB.setGeometry(QtCore.QRect(160, 180, 441, 31))
        self.lineEditB.setObjectName("lineEditB")
        self.lineEditC = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditC.setGeometry(QtCore.QRect(160, 230, 441, 31))
        self.lineEditC.setObjectName("lineEditC")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 300, 71, 31))
        self.label_5.setObjectName("label_5")
        self.lineEditKetQua = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditKetQua.setGeometry(QtCore.QRect(170, 290, 241, 61))
        self.lineEditKetQua.setObjectName("lineEditKetQua")
        self.pushButtonCalc = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonCalc.setGeometry(QtCore.QRect(110, 390, 131, 71))
        self.pushButtonCalc.setObjectName("pushButtonCalc")
        self.pushButtonContinue = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonContinue.setGeometry(QtCore.QRect(320, 390, 141, 71))
        self.pushButtonContinue.setObjectName("pushButtonContinue")
        self.pushButtonClose = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonClose.setGeometry(QtCore.QRect(540, 390, 141, 71))
        self.pushButtonClose.setObjectName("pushButtonClose")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffaa00;\">PHẦN MỀM TÍNH PHƯƠNG TRÌNH BẬC 2 </span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Hệ số a: </span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Hệ số b: </span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Hệ số c: </span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Kết quả: </span></p></body></html>"))
        self.pushButtonCalc.setText(_translate("MainWindow", "Calc"))
        self.pushButtonContinue.setText(_translate("MainWindow", "Continue"))
        self.pushButtonClose.setText(_translate("MainWindow", "Close"))