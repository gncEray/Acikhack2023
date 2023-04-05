# ERAI


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(694, 828)
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(18)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_email = QtWidgets.QLabel(self.centralwidget)
        self.btn_email.setGeometry(QtCore.QRect(0, 240, 691, 100))
        self.btn_email.setText("")
        self.btn_email.setPixmap(QtGui.QPixmap("photos/e_mail.png"))
        self.btn_email.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_email.setObjectName("btn_email")
        self.btn_musteri = QtWidgets.QLabel(self.centralwidget)
        self.btn_musteri.setGeometry(QtCore.QRect(0, 550, 691, 100))
        self.btn_musteri.setText("")
        self.btn_musteri.setPixmap(QtGui.QPixmap("photos/musteri.png"))
        self.btn_musteri.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_musteri.setObjectName("btn_musteri")
        self.btn_sosyal = QtWidgets.QLabel(self.centralwidget)
        self.btn_sosyal.setGeometry(QtCore.QRect(0, 400, 691, 100))
        self.btn_sosyal.setText("")
        self.btn_sosyal.setPixmap(QtGui.QPixmap("photos/sosyal_medya.png"))
        self.btn_sosyal.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_sosyal.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 730, 691, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_4.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("High Tower Text")
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(-60, -30, 821, 881))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("photos/intronlp.jpg"))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 60, 691, 91))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("photos/sim.png"))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_5.raise_()
        self.btn_email.raise_()
        self.btn_musteri.raise_()
        self.btn_sosyal.raise_()
        self.label_4.raise_()
        self.label_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "ERAI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
