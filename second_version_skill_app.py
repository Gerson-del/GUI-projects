

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 650)
        MainWindow.setMouseTracking(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.task_list_label = QtWidgets.QLabel(self.centralwidget)
        self.task_list_label.setGeometry(QtCore.QRect(120, 0, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.task_list_label.setFont(font)
        self.task_list_label.setStyleSheet("color: #FFFFFF;\n"
"background-color: #000000;")
        self.task_list_label.setObjectName("task_list_label")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(330, 260, 51, 31))
        self.spinBox.setStyleSheet("border: 2px solid grey;\n"
"border-radius: 5px;\n"
"QComboBox::drop-down {\n"
"    background-color: #FFFFFF;\n"
"}")
        self.spinBox.setObjectName("spinBox")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(330, 130, 69, 22))
        self.comboBox.setStyleSheet("border: 2px solid grey;\n"
"border-radius: 5px;\n"
"QComboBox::drop-down {\n"
"    background-color: #FFFFFF;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(330, 70, 151, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    border: 2px solid grey; /* Sets border thickness and color */\n"
"    border-radius: 5px; /* Rounds the corners */\n"
"    background-color: #FFFFFF; /* Sets the background color */\n"
"    text-align: center; /* Centers the text inside the progress bar */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #FFC0CB; /* Sets the color of the progress indicator */\n"
"    width: 20px; /* Sets the width of each progress indicator */\n"
"}\n"
"\n"
"")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(330, 190, 118, 22))
        self.timeEdit.setStyleSheet("border: 2px solid grey;\n"
"border-radius: 5px;\n"
"QComboBox::drop-down {\n"
"    background-color: #FFFFFF;\n"
"}")
        self.timeEdit.setObjectName("timeEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(330, 225, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #FFFFFF;\n"
"background-color: #000000;")
        self.label_5.setObjectName("label_5")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(330, 40, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("color: #FFFFFF;\n"
"background-color: #000000;")
        self.label_1.setObjectName("label_1")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(330, 160, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #FFFFFF;\n"
"background-color: #000000;")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(330, 100, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #FFFFFF;\n"
"background-color: #000000;")
        self.label_3.setObjectName("label_3")
        self.notes = QtWidgets.QLabel(self.centralwidget)
        self.notes.setGeometry(QtCore.QRect(330, 370, 161, 211))
        self.notes.setStyleSheet("color: #FFFFFF;")
        self.notes.setObjectName("notes")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 501, 621))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(r"C:\Users\gerso\Desktop\Nueva carpeta\GUI\skillApp project\fondo4.jpg"))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 450, 141, 81))
        self.pushButton_2.setStyleSheet("* {\n"
"    border: 4px solid #BC006C;\n"
"    border-radius: 45px;\n"
"    font-size: 20px;\n"
"    color: white;\n"
"    padding: 20px 0;\n"
"    margin: 70px 120px;\n"
"}\n"
"\n"
"*:hover {\n"
"    background: #BC006C;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 450, 141, 81))
        self.pushButton_3.setStyleSheet("* {\n"
"    border: 4px solid #BC006C;\n"
"    border-radius: 45px;\n"
"    font-size: 20px;\n"
"    color: white;\n"
"    padding: 20px 0;\n"
"    margin: 70px 120px;\n"
"}\n"
"\n"
"*:hover {\n"
"    background: #BC006C;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label.raise_()
        self.task_list_label.raise_()
        self.spinBox.raise_()
        self.comboBox.raise_()
        self.progressBar.raise_()
        self.timeEdit.raise_()
        self.label_5.raise_()
        self.label_1.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.notes.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
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
        self.task_list_label.setText(_translate("MainWindow", "task list:"))
        self.label_5.setText(_translate("MainWindow", "set a goal"))
        self.label_1.setText(_translate("MainWindow", "visualize progress"))
        self.label_4.setText(_translate("MainWindow", "tracking time"))
        self.label_3.setText(_translate("MainWindow", "skill category"))
        self.notes.setText(_translate("MainWindow", "Notes"))
        self.pushButton_2.setText(_translate("MainWindow", "add skill"))
        self.pushButton_3.setText(_translate("MainWindow", "remove skill"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
