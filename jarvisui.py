# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jarvisui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_jarvisui(object):
    def setupUi(self, jarvisui):
        jarvisui.setObjectName("jarvisui")
        jarvisui.resize(1095, 763)
        self.centralwidget = QtWidgets.QWidget(jarvisui)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 1101, 851))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:\Users\VISHNUVARDHAN\Desktop\jarvis"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(860, 690, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(970, 690, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 401, 141))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../Jarvis_Loading_Screen.gif"))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(530, 60, 281, 61))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(810, 60, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setObjectName("textBrowser_2")
        jarvisui.setCentralWidget(self.centralwidget)

        self.retranslateUi(jarvisui)
        QtCore.QMetaObject.connectSlotsByName(jarvisui)

    def retranslateUi(self, jarvisui):
        _translate = QtCore.QCoreApplication.translate
        jarvisui.setWindowTitle(_translate("jarvisui", "MainWindow"))
        self.pushButton.setText(_translate("jarvisui", "RUN"))
        self.pushButton_2.setText(_translate("jarvisui", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    jarvisui = QtWidgets.QMainWindow()
    ui = Ui_jarvisui()
    ui.setupUi(jarvisui)
    jarvisui.show()
    sys.exit(app.exec_())