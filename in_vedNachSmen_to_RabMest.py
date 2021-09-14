import re
import copy
import openpyxl

class obrabotka():
    def __init__(self, IN_name_file):
        self.IN_name_file = IN_name_file
        self.spisok()

    def spisok(self):
        '''создаем словарь из нужной странциы в файле эксель'''
        wb = openpyxl.load_workbook(self.IN_name_file, data_only=True)
        sheet = wb.get_sheet_by_name('Ведомость Нач.смен')
        # создаем словарь из файла
        cybc = {col[0]: col[1:] for col in zip(*sheet.values)}
        print(cybc)
        return cybc

    def RabMest(self, slovar):

        print()

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    obrabotka('Заказ №180 Опалубка стыка.xlsx')