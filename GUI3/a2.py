# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'a2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 584)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 611, 551))
        self.textEdit.setStyleSheet("background-color: rgb(96, 65, 65);")
        self.textEdit.setObjectName("textEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(240, 0, 131, 25))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 248, 73);\n"
"font: 13pt \"Ubuntu\";\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 90, 113, 25))
        self.lineEdit_2.setStyleSheet("background-color: rgb(252, 175, 62);\n"
"font: 12pt \"Ubuntu\";\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 310, 113, 25))
        self.lineEdit_3.setStyleSheet("background-color: rgb(252, 175, 62);\n"
"font: 12pt \"Ubuntu\";\n"
"")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 30, 591, 51))
        self.textEdit_2.setStyleSheet("\n"
"background-color: rgb(200, 255, 252);\n"
"font: 12pt \"Ubuntu\";")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 120, 591, 181))
        self.textEdit_3.setStyleSheet("\n"
"background-color: rgb(200, 255, 252);\n"
"font: 12pt \"Ubuntu\";")
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(10, 340, 591, 191))
        self.textEdit_4.setStyleSheet("\n"
"background-color: rgb(200, 255, 252);\n"
"font: 12pt \"Ubuntu\";")
        self.textEdit_4.setObjectName("textEdit_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 22))
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
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.lineEdit.setText(_translate("MainWindow", "       Welcome"))
        self.lineEdit_2.setText(_translate("MainWindow", "        Gazebo"))
        self.lineEdit_3.setText(_translate("MainWindow", "        Mapviz"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%;\"><span style=\" font-family:\'Calibri, sans-serif\'; font-size:11pt; color:#000000; background-color:transparent;\">This design covered autonomous task. With use of ros control move the rover model in gazebo. </span></p></body></html>"))
        self.textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%;\"><span style=\" font-family:\'Calibri, sans-serif\'; font-size:11pt; color:#000000; background-color:transparent;\">Gazebo is an open-source 3D robotics simulator, while ROS serves as the interface for the robot. Combining both results in a powerful robot simulator. Gazebo can use multiple high-performance physics engines, such as ODE, Bullet, etc. It provides realistic rendering of environments including high-quality lighting, shadows, and textures. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%; font-family:\'Calibri, sans-serif\'; font-size:11pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%;\"><a name=\"docs-internal-guid-37ec4800-7fff-62c4-1a1a-e40d305b8fdd11\"></a><span style=\" font-family:\'Calibri, sans-serif\'; font-size:11pt; color:#000000; background-color:transparent;\">I</span><span style=\" font-family:\'Calibri, sans-serif\'; font-size:11pt; color:#000000; background-color:transparent;\">n camera feed, we can see camera screen as well as gazebo screen. Move the Rover model by adding a differential drive plugin. Control a rover model with help of a python script such that if there is an obstacle in front of the rover it takes a right or left turn without colliding with an obstacle.</span></p></body></html>"))
        self.textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%;\"><span style=\" font-family:\'Calibri, sans-serif\'; font-size:11pt; color:#000000; background-color:transparent;\">We use mapviz for rover to reach at their goal point. Mapviz is a highly customizable ROS-based visualization tool focused on large-scale 2D data, with a plugin system for extreme extensibility. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%; font-family:\'Calibri, sans-serif\'; font-size:11pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%;\"><span style=\" font-family:\'Calibri, sans-serif\'; font-size:11pt; color:#000000; background-color:transparent;\">For moving a rover to a particular location (at given latitude and longitude) in gazebo, we can calculate x and y of GPS and angle from GPS. Then calculate distance between Goal and current position. We need to calculate angle from IMU data. We can lauch mapviz using command </span><span style=\" font-family:\'Calibri, sans-serif, sans-serif\'; font-size:11pt; color:#000000; background-color:transparent;\">roslaunch mapviz mapviz.launch. </span><span style=\" font-family:\'Calibri, sans-serif\'; font-size:11pt; color:#000000; background-color:transparent;\">Using this all data rover is moving in mapviz and reach at goal point. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%; font-family:\'Calibri, sans-serif\'; font-size:11pt; color:#000000;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:115%;\"><span style=\" font-family:\'Calibri, sans-serif, sans-serif\'; font-size:11pt; color:#000000; background-color:transparent;\">We can load map using google map. We can see position and movement of rover in map.</span><span style=\" font-size:11pt; color:#000000; background-color:transparent;\"> </span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

