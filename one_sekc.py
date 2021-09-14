# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_one_sekc(object):
    def setupUi_one(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(375, 141)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(20, 60, 101, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(160, 60, 101, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 30, 328, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nominal = QtWidgets.QComboBox(self.widget)
        self.nominal.setObjectName("nominal")
        self.horizontalLayout.addWidget(self.nominal)
        self.oboznach = QtWidgets.QComboBox(self.widget)
        self.oboznach.setObjectName("oboznach")
        self.horizontalLayout.addWidget(self.oboznach)
        self.razmer = QtWidgets.QLineEdit(self.widget)
        self.razmer.setObjectName("razmer")
        self.horizontalLayout.addWidget(self.razmer)
        self.kol = QtWidgets.QSpinBox(self.widget)
        self.kol.setObjectName("kol")
        self.horizontalLayout.addWidget(self.kol)
        self.nominal.raise_()
        self.oboznach.raise_()
        self.razmer.raise_()
        self.kol.raise_()
        self.pushButton.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        self.razmer.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Пуск"))
        self.radioButton.setText(_translate("Dialog", "новая крышка"))
        self.radioButton_2.setText(_translate("Dialog", "старая крышка"))

