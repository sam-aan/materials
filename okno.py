# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'okno.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(357, 275)
        self.pushButton = QtWidgets.QPushButton(widget)
        self.pushButton.setGeometry(QtCore.QRect(120, 230, 99, 27))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(widget)
        self.widget.resize(291, 201)
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_2.setObjectName("textEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit_2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.textEdit_3 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_3.setObjectName("textEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textEdit_3)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.textEdit_4 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_4.setObjectName("textEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.textEdit_4)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.textEdit_5 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_5.setObjectName("textEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.textEdit_5)
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.textEdit_6 = QtWidgets.QTextEdit(self.widget)
        self.textEdit_6.setObjectName("textEdit_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.textEdit_6)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Form"))
        self.pushButton.setText(_translate("widget", "Пуск"))
        self.label_5.setText(_translate("widget", "Номинал"))
        self.label.setText(_translate("widget", "Длина трассы"))
        self.label_2.setText(_translate("widget", "Длина сварных секций"))
        self.label_3.setText(_translate("widget", "Количество стыков"))
        self.label_4.setText(_translate("widget", "Количество фланцев"))
        self.label_8.setText(_translate("widget", "Количество заглушек"))

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
ui = Ui_myForm()
ui.setupUi(window)
QtCore.QObject.connect(ui.butQuit, QtCore.SIGNAL("clicked()"), QtGui.qApp.quit)
window.show()
sys.exit(app.exec_())