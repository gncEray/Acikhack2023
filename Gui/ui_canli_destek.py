# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'canli_destek.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(478, 599)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 481, 601))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("photos/canli_des.jpg"))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 516, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.btn_send = QtWidgets.QLabel(Form)
        self.btn_send.setGeometry(QtCore.QRect(390, 520, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_send.setFont(font)
        self.btn_send.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_send.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_send.setObjectName("btn_send")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btn_send.setText(_translate("Form", "Gönder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
