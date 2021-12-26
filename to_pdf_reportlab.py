# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import ttfonts
from reportlab.pdfbase import pdfmetrics
from PyPDF2 import PdfFileMerger
import os

def obedin(s, nZak):
    name = "Наклейки Заказ №" + nZak + ".pdf"
    # из списка создаем по одной наклейке и объединяем их в общий файл.
    spis = []
    # создаем наклейки, для каждой секции по наклейке
    for i in s:
        spis.append(simple_table(i))
    # объединяем все наклейки в одну
    merger = PdfFileMerger()

    for pdf in spis:
        merger.append(pdf)

    merger.write(name)
    merger.close()
    # удаляем исходные наклейки
    for i in spis:
        os.remove(i)

    return name

def simple_table(spis):
    # создаем однк наклейку
    def s_plus(s):
        s1 = []
        s2 = []
        while s:
            s1.append(s[0])
            s.pop(0)
            if len(s1) == 20:
                s2.append(''.join(s1))
                s1 = []
                if len(s) <= 20:
                    s2.append(''.join(s))
                else:
                    s1 = []
        return s2

    name = str(spis[1]) + '.pdf'
    MyFontObject = ttfonts.TTFont('GOTHIC', 'GOTHICB.TTF')
    pdfmetrics.registerFont(MyFontObject)
    c = canvas.Canvas(name, pagesize=(100, 50))
    c.setLineWidth(.3)
    c.setFont('GOTHIC', 3)

    c.drawString(8, 39, 'с/н: ' + spis[1])
    c.drawString(8, 29, 'art: ' + spis[0])
    c.drawString(10, 20, "Наименование")
    c.drawString(45, 20, 'Размер, мм.')
    c.drawString(75, 20, 'Масса, кг.')

    # Наименование
    c.setFont('GOTHIC', 2.8)
    s = list(spis[2])
    n = 12
    if len(s) > 20:
       ss = s_plus(s)
       for i in ss:
           c.drawString(7, n, i)
           n -= 2.5
    else:
        c.drawString(7, 12, spis[2])

    # Размер
    c.drawString(45, 12, spis[3])
    #Вес
    c.drawString(80, 12, str(spis[5]))
    # Обозначение по проекту
    c.setFont('GOTHIC', 18)
    c.drawString(50, 28, spis[4])

    c.line(5, 45, 5, 5)
    c.line(5, 45, 95, 45)
    c.line(5, 5, 95, 5)
    c.line(95, 45, 95, 5)

    c.line(45, 45, 45, 25)
    c.line(5, 35, 45, 35)
    c.line(5, 25, 95, 25)

    c.line(40, 25, 40, 5)
    c.line(70, 25, 70, 5)
    c.line(5, 18, 95, 18)

    c.save()
    return name
if __name__ == '__main__':
    obedin([['E3-55-Al-4000-4-uv', '1-1-0001', 'угловая вертикальная секция', '450*450', 'A1', 34.47],
            ['E3-55-Al-4000-4-uv', '1-1-0002', 'угловая вертикальная секция', '450*450', 'A2', 34.47]])
