# coding^utf8
import re
import os


class schetchik:

    def shet0(self): # обнуляет счетчки
        q = '0'
        f = open('shet.txt', 'w')
        f.write(q + '\n')
        f.close()
        return q

    def shet1(self):    # изменяем номер сборки
        f = open('shet.txt', 'r')  # открываем файл для чтения
        all_lines = f.readlines()  # читсаем все строки
        last_line = all_lines[-1]  # присваиваем значение последней строки
        q = int(last_line) + 1
        f = open('shet.txt', 'a')
        f.write(str(q) + '\n')
        f.close()
        return str(q)