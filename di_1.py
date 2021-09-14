# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'di.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import os
import sys
import shutil
import re
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QWidget, QMessageBox,
                             QAction, QFileDialog, QApplication, QCheckBox, QLineEdit)
from rashet_sekcii import rashet
from PyQt5 import QtCore, QtGui, QtWidgets
import logg_solaris
import logging

class Raschet_sekcii(object):
    def setupUi(self, MainWindow):
        logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                            level=logging.DEBUG, filename=u'mylog.log')
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(20, 280, 100, 20))
        self.pushButton2.setObjectName("pushButton2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 280, 75, 20))
        self.pushButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 420, 230))
        self.label.setObjectName("label")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 60, 500, 100))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_zakaz = QtWidgets.QLabel(self.centralwidget)
        self.label_zakaz.setGeometry(QtCore.QRect(20, 220, 100, 10))
        self.label_zakaz.setObjectName("label")
        self.label_zakaz.setText('№ заказ')
        self.line = QLineEdit(self)
        self.line.move(20, 230)
        self.line.resize(80, 20)
        self.label_etap = QtWidgets.QLabel(self.centralwidget)
        self.label_etap.setGeometry(QtCore.QRect(120, 220, 100, 10))
        self.label_etap.setObjectName("label")
        self.label_etap.setText('№ этапа')
        self.line2 = QLineEdit(self)
        self.line2.move(120, 230)
        self.line2.resize(80, 20)

        MainWindow.setCentralWidget(self.centralwidget)
        open('mylog.log', 'w').close()
        sys.stdout = logg_solaris.print_to_txt("logfilename.txt")

        self.material = 0
        self.fname = ''
        self.srav = 0
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        '''openFile = QAction(QIcon('open.png'), 'Открыть', self)  # создаем меню открыть файл
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Открыть файл')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Файл')
        fileMenu.addAction(openFile)'''

        btn = self.pushButton  # если кнопка нажата
        logging.debug(u'НАЧАЛО ПРОГРАМЫ')
        btn.clicked.connect(self.nachalo)

        btn2 = self.pushButton2  # если кнопка нажата
        logging.debug(u'ОТКРЫВАЕМ ФАЙЛ')
        btn2.clicked.connect(self.showDialog)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Solaris specification"))
        self.pushButton.setText(_translate("MainWindow", "Пуск"))
        self.pushButton2.setText(_translate("MainWindow", "Открыть файл"))
        self.label.setText(_translate("MainWindow", "1. Откройте исходный файл *.txt\n2. Запустите расчет\n"
                                                    "3. Все строки в исходном фале должны быть следующего формата:"
                                                    "\n\nМАТЕРИАЛ ПРОВОДНИКА\nНОМИНАЛЬНЫЙ ТОК\nКОЛИЧЕСТВО ПРОВОДНИКОВ\nОБОЗНАЧЕНИЕ\n"
                                                    "РАЗМЕР\nКОЛ-ВО\n\n"
                                                    "Пример: а 4 630 П 3000 2"))

    def showDialog(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Открыть файл', '', "Text Files (*.txt)", )[0]
        print('Открыть файл: ', self.fname)

    def nachalo(self):
        N_zakaza = self.line.text()
        N_etap = self.line2.text()
        if self.fname == '':    # ничего не выбрано показывает предупреждение
            print('файл не выбран')
            logging.warning(u'Файл не выбран')
            self.predupregdenie()
        elif N_zakaza == '' or N_etap == '':
            reply = QtWidgets.QMessageBox.question(self, 'Уведомление', 'Введите номер заказа и этапаэ',
                                                   QtWidgets.QMessageBox.Ok)
        else:
            print('№ заказа', N_zakaza, '№ этапа', N_etap)
            ras = rashet(self.fname, N_zakaza, N_etap)
            print('zapusk')
            logging.debug(u'Запуск модуля расчета')
            ras.zapusk()
            self.saveFileDialog("Exel (*.xlsx);;pdf (*.pdf)")
            print('e')

    def saveFileDialog(self, rashirenie):
        savefname = re.findall(r'[^/.]+', self.fname)
        name = savefname[-1]
        del savefname[-1]
        savefname = '/'.join(savefname)
        print('Путь для сохранения: ', savefname)
        options = QFileDialog.Options()
        options = QFileDialog.DontUseNativeDialog
        fileName = QFileDialog.getSaveFileName(self, "Сохранить как", savefname, rashirenie)[0]
        filter = re.findall(r'[^/.]+', fileName)[-1]
        if fileName:
            print('Сохранить файл: ', fileName)
            thisFile = ["example.xlsx"]
            print('filter=', filter)
            if filter == 'xlsx':
                put = os.path.abspath(thisFile[0])
                print(put)
                shutil.copyfile(put, fileName)
                self.konec_rashetov()
                '''reply = QtWidgets.QMessageBox.question(self, 'Уведомление',
                                                       'Расчет окончен! \n Хотите сохранить файл в формате PDF?',
                                                       QtWidgets.QMessageBox.Ok, QMessageBox.No)
                if reply == QtWidgets.QMessageBox.Ok:
                    self.saveFileDialog("pdf (*.pdf)")

                else:
                    self.konec_rashetov()'''
            elif filter == 'pdf':
                put = os.path.abspath(thisFile[1])
                print(put)
                shutil.copyfile(put, fileName)

                #  записываем путь к файлу и удаляем его
                path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'example.xlsx')
                os.remove(path)
                self.konec_rashetov()

    def predupregdenie(self):
        message = 'Вы не выбрали файл. Хотите выбрать? \n Или хотите закончить расчет? \n'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message, QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Close)
        if reply == QtWidgets.QMessageBox.Ok:
            print('продолжить')
            self.showDialog()
        else:
            print('отмена')
            exit()

    def konec_rashetov(self):
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление',
                                               'Хотите повторить расчет? (Ok) \n Или закрыть программу? (Cancel)',
                                               QtWidgets.QMessageBox.Ok, QMessageBox.Cancel)
        if reply == QtWidgets.QMessageBox.Ok:
            self.material = 0
            self.fname = ''
            self.srav = 0
            self.showDialog()
        else:
            print('Закрытие программы')
            exit()