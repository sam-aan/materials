
import xlwt
from xlrd import open_workbook

def calculations(Inom):
    if Inon in range(1, 631):
        socket = [['Разъем на коробку', 1, 'шт.', 0, ''],
                  ['Герметичный ввод_10.02', 1, 'шт.', 0, ''],
                  ['Знак безопасности Заземление 30х30', 3, 'шт.', 0, ''],
                  ['Знак безопасности Молния 50х50х50 треугольник', 1, 'шт.', 0, ''],
                  ['Контакт до 200А', 1, 'шт.', 0.2, ''],
                  ['Болт М10х25 8.8 DIN 933', 10, 'шт.', 0.237, ''],
                  ['Гайка шестигранная с фланцем DIN 6923 М10', 10, 'шт.', 0.1108, ''],
                  ['Шайба простая М10', 10, 'шт.', 0.0408, ''],
                  ['Провод ПуГВ 1х6 Жёлто - зелёный', 1, 'шт.', 0, ''],
                  ['Наконечник кольцевой НКИ 6,0-10', 1, 'шт.', 0, ''],
                  ['Провод ПуГВ 1х6 Жёлто - зелёный', 1, 'шт.', 0, ''],
                  ['Провод ПуГВ 1х6 Жёлто - зелёный', 1, 'шт.', 0, '']]

        if Inom in range(1, 251):
            size = '450/250/250'
            nameBox = ['Бокс малогабаритный  ВТ-250 В2, 450/250/250 RAL7035', 1, 'шт.', 7.5, '']

if __name__ == '__main__':
    calculations(250, 1)