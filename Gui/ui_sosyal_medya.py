# ERAI


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sosyal_medya(object):
    def setupUi(self, sosyal_medya):
        sosyal_medya.setObjectName("sosyal_medya")
        sosyal_medya.resize(374, 790)
        self.label = QtWidgets.QLabel(sosyal_medya)
        self.label.setGeometry(QtCore.QRect(0, 0, 371, 791))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("photos/insta.jpg"))
        self.label.setObjectName("label")
        self.text_yorum = QtWidgets.QTextEdit(sosyal_medya)
        self.text_yorum.setGeometry(QtCore.QRect(10, 720, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.text_yorum.setFont(font)
        self.text_yorum.setObjectName("text_yorum")
        self.btn_send = QtWidgets.QLabel(sosyal_medya)
        self.btn_send.setGeometry(QtCore.QRect(310, 740, 55, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.btn_send.setFont(font)
        self.btn_send.setObjectName("btn_send")

        self.retranslateUi(sosyal_medya)
        QtCore.QMetaObject.connectSlotsByName(sosyal_medya)

    def retranslateUi(self, sosyal_medya):
        _translate = QtCore.QCoreApplication.translate
        sosyal_medya.setWindowTitle(_translate("sosyal_medya", "Sosyal Medya"))
        self.btn_send.setText(_translate("sosyal_medya", "Gönder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sosyal_medya = QtWidgets.QWidget()
    ui = Ui_sosyal_medya()
    ui.setupUi(sosyal_medya)
    sosyal_medya.show()
    sys.exit(app.exec_())
