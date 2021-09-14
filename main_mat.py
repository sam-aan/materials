import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import materials_simple
import os
import shutil
import to_exl_main_mat
import re
import xlrd
import xlwt

class ExampleApp(QtWidgets.QMainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(340, 600)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 20, 249, 520))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_1 = QtWidgets.QLabel(self.layoutWidget)
        self.label_1.setObjectName("label")
        self.verticalLayout.addWidget(self.label_1)
        self.seria = QtWidgets.QComboBox(self.layoutWidget)
        self.seria.setObjectName("seria")
        self.seria.addItem("")
        self.seria.addItem("")
        self.verticalLayout.addWidget(self.seria)

        self.label_0 = QtWidgets.QLabel(self.layoutWidget)
        self.label_0.setObjectName("label")
        self.verticalLayout.addWidget(self.label_0)

        self.material = QtWidgets.QComboBox(self.layoutWidget)
        self.material.setObjectName("material")
        self.material.addItem("")
        self.material.addItem("")
        self.verticalLayout.addWidget(self.material)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.nominal = QtWidgets.QComboBox(self.layoutWidget)
        self.nominal.setObjectName("nominal")
        self.nominal.addItem("")
        self.nominal.addItem("")
        self.nominal.addItem("")
        self.nominal.addItem("")
        self.nominal.addItem("")
        self.nominal.addItem("")
        self.nominal.addItem("")
        self.nominal.addItem("")
        self.nominal.addItem("")
        self.nominal.addItem("")
        self.nominal.addItem("")
        self.verticalLayout.addWidget(self.nominal)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.dlina_trassi = QtWidgets.QLineEdit(self.layoutWidget)
        self.dlina_trassi.setObjectName("dlina_trassi")
        self.verticalLayout.addWidget(self.dlina_trassi)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.kol_stik = QtWidgets.QLineEdit(self.layoutWidget)
        self.kol_stik.setObjectName("kol_stik")
        self.verticalLayout.addWidget(self.kol_stik)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.kol_seks = QtWidgets.QLineEdit(self.layoutWidget)
        self.kol_seks.setObjectName("kol_seks")
        self.verticalLayout.addWidget(self.kol_seks)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.kol_zag = QtWidgets.QLineEdit(self.layoutWidget)
        self.kol_zag.setObjectName("kol_zag")
        self.verticalLayout.addWidget(self.kol_zag)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.kol_flanc = QtWidgets.QLineEdit(self.layoutWidget)
        self.kol_flanc.setObjectName("kol_flanc")
        self.verticalLayout.addWidget(self.kol_flanc)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.dlina_svarka = QtWidgets.QLineEdit(self.layoutWidget)
        self.dlina_svarka.setObjectName("dlina_svarka")
        self.verticalLayout.addWidget(self.dlina_svarka)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton2.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        btn = self.pushButton  # если кнопка нажата запускаем расчет материадлов
        btn.clicked.connect(self.zapusk)

        btn2 = self.pushButton2  # если кнопка нажата запускаем объединение файлов
        btn2.clicked.connect(self.slogenie)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Расчет материалов"))
        self.label_1.setText(_translate("Dialog", "Серия шинопровода"))
        self.seria.setItemText(0, _translate("Dialog", "E3"))
        self.seria.setItemText(1, _translate("Dialog", "CR1"))

        self.label_0.setText(_translate("Dialog", "Материал проводника"))
        self.material.setItemText(0, _translate("Dialog", "Алюминий"))
        self.material.setItemText(1, _translate("Dialog", "Медь"))
        self.label.setText(_translate("Dialog", "Номинал тока А."))
        self.nominal.setItemText(0, _translate("Dialog", "630"))
        self.nominal.setItemText(1, _translate("Dialog", "800"))
        self.nominal.setItemText(2, _translate("Dialog", "1000"))
        self.nominal.setItemText(3, _translate("Dialog", "1250"))
        self.nominal.setItemText(4, _translate("Dialog", "1600"))
        self.nominal.setItemText(5, _translate("Dialog", "2000"))
        self.nominal.setItemText(6, _translate("Dialog", "2500"))
        self.nominal.setItemText(7, _translate("Dialog", "3200"))
        self.nominal.setItemText(8, _translate("Dialog", "4000"))
        self.nominal.setItemText(9, _translate("Dialog", "5000"))
        self.nominal.setItemText(10, _translate("Dialog", "6300"))
        self.label_2.setText(_translate("Dialog", "Длина трассы м.п."))
        self.label_3.setText(_translate("Dialog", "Количество стыков шт."))
        self.label_4.setText(_translate("Dialog", "Количество секций шт."))
        self.label_5.setText(_translate("Dialog", "Количество концевых заглушек шт."))
        self.label_6.setText(_translate("Dialog", "Количество фланцевых блоков шт."))
        self.label_7.setText(_translate("Dialog", "Длина сварных изделий м.п."))
        self.pushButton.setText(_translate("Dialog", "Запустить"))
        self.pushButton2.setText(_translate("Dialog", "Объеденить файлы"))

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options = QFileDialog.DontUseNativeDialog
        fileName = QFileDialog.getSaveFileName(self, "Сохранить как", "Материалы для заказа ", "Exel (*.xls)", )[0]
        print(fileName)
        thisFile = "example2.xls"
        put = os.path.abspath(thisFile)
        print(put)
        shutil.copyfile(put, fileName)
        os.remove('example2.xls')

    def zapusk(self):
        print('запускаем расчет материалов')
        rezult = materials_simple.vvod(self.seria.currentText(), self.material.currentText(),
                                       self.nominal.currentText(), self.dlina_trassi.text(),
                                       self.kol_stik.text(), self.kol_seks.text(), self.kol_zag.text(),
                                       self.kol_flanc.text(), self.dlina_svarka.text()).fg()
        print('преобразование')
        to_exl_main_mat.preobrazovanie(rezult, [self.seria.currentText(), self.material.currentText(),
                                       self.nominal.currentText(), self.dlina_trassi.text(),
                                       self.kol_stik.text(), self.kol_seks.text(), self.kol_zag.text(),
                                       self.kol_flanc.text(), self.dlina_svarka.text()])

        self.saveFileDialog()

    def slogenie(self):
        '''модуль сложения нескольких файлов в один'''
        zse = 0
        vals = []

        while zse != 1:
            fname = QFileDialog.getOpenFileName(self, 'Открыть файл', '', "Exel (*.xls)", )[0]
            print('Открыть файл: ', fname)
            rb = xlrd.open_workbook(fname, on_demand=True, formatting_info=True)
            nameSheet = rb.sheet_names()  # считываем имена листов в файле эксель
            nomSheet = nameSheet.index('Артикулы')  # ищем номер нужного листа и записываем его
            sheet = rb.sheet_by_index(nomSheet)  # открываем нужный нам лист
            vals_one = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]  # делаем список из всех строк
            rb.release_resources()
            del rb
            del vals_one[0]
            vals = vals + vals_one
            zse = self.vopros(vals)

    def vopros(self, vals):
        message = 'Открыть другой файл?'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message, QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.Yes)
        if reply == QtWidgets.QMessageBox.No:
            print('Ответ НЕТ')
            itog = sorting_det(vals)
            for i in vals:
                print(i)
            print('Список отсортирован')
            to_exl_main_mat.preobrazovanie(itog, ['Суммирование'])
            print('сохранение файла')
            self.saveFileDialog()
            zse = 1
            return zse
        else:
            print('Продолжить расчеты')
            zse = 0
            return zse

def sorting_det(array):
    array2 = []
    kol_str = len(array)  # записываем клличесвто элементов в списке, оно же
    print('всего строк ', kol_str)

    for x in array:  # пока Х в списке
        kol = float(x[3])  # количество деталей из строки
        print('Строка которую сравниваем: ', x)
        y = array.index(x) + 1  # нам нужна следующая строка
        print(y, 'YYYYYYYYY')
        sov = 0  # это счетчик совпадений
        while y <= kol_str - 1:  # начинаем сравнивать со следующей строкой
            w = array[y]  # строка с которой сравниваем это следующая строка
            print('Строка c которой сравниваем: ', w)
            if x[0] == w[0]:  # если значения строк совпадают, то
                kol = kol + float(w[3])  # складываем количество
                sov = sov + 1  # сообщаем что были совпадения
                print('*' * 25 + 'СОВПАДЕНИЕ!!!' + '*' * 25)
                print('Совпадение в ' + str(y) + ' строке  +' + str(w[3]) + 'шт.')
                print('Строка которую удаляем: ', array[y])
                del array[y]
                kol_str = len(array)
                print('Итого строк осталось: ', kol_str)
            else:
                print('нет совпадений в ', y, ' строке')
                y = y + 1

        # проверяем есть ли совпадения

        if sov == 0:
            array2.append(x)
            print('***Совпадений нет!***\n')
        else:
            spis = [x[0], x[1], x[2], str(kol), x[4], x[5]]
            print('Записываем в список ', spis)
            array2.append(spis)
        print('КОЛИЧЕСТВО СОВПАДЕНИЙ: ' + str(sov) + '\n')

    # записываем результат в файл
    #array2.sort(key=lambda i: (i[3]))
    return array2
