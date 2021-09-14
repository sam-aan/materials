import re
import copy
import openpyxl

class sorting():
    def __init__(self, tip, IN_name_file, OUT_name_file, N_stolb, zagolvok, razdelitel):
        '''     если мы хотим на выходе получить список а не записывать все в файл, то вместо имени выходного файла в\
            значение "OUT_name_file" нужно поставть "False".
                если мы хотим на входе загрузить список, а не читать из файла, то вместо имени входного файла в
            значение "IN_name_file" нужно поставить "False", а значение "tip" ставим "0"    '''

        self.tip = tip      # xl или txt или False если это просто список
        self.IN_name_file = IN_name_file
        self.OUT_name_file = OUT_name_file
        self.N_stolb = N_stolb  # столбец по которому идет сравнение
        self.zagolvok = zagolvok
        self.razdelitel = razdelitel
        self.q = []
        self.w = []

    def addition(self):
        """модуль сложения всех повторяющихся строк"""
        print('СЛОЖЕНИЕ ПОВТОРОВ')

        arrayApp = []
        array2 = []

        if self.tip == 'xl':  # если мы читаем из экселя
            wb = openpyxl.load_workbook(self.IN_name_file, data_only=True)
            sheet = wb.get_sheet_by_name('Спецификация')

            for row in sheet.rows:
                sel = []

                for cell in row:
                    sel.append(str(cell.value))

                arrayApp.append(sel)

            #print(arrayApp)

            if self.zagolvok == True:   # спрашиваем про заголовок
                del arrayApp[0]    # удаляем первую строку
            else:
                print('без заголовка')

            # удаляем ненужные слобцы
            for i in arrayApp:
                i[13] = int(i[13])
                del i[12]
                del i[0]

        elif self.tip == 'txt':     # если мы хотим прочитать файл в список и отсортировать его

            with open(self.IN_name_file) as file:
                array = [row.strip() for row in file]   # переписываем все строки в список ['первая строка', 'вторая строка...

                if self.zagolvok == True:
                    del array[0]    # удаляем первую строку
                else:
                    print('без заголовка')

            for i in array:

                if self.razdelitel == ';':
                    j = re.findall(r'[^;]+', i)
                elif self.razdelitel == ' ':
                    j = re.findall(r'[^\s]+', i)
                else:
                    j = re.findall(r'[^;\s]+', i)
                arrayApp.append(j)

            #print('Начальный список', arrayApp)

        else:       # если мы сразу запустили список а не читаем из файла
            arrayApp = self.IN_name_file

            if self.zagolvok == True:   # спрашиваем про заголовок
                del arrayApp[0]    # удаляем первую строку
            else:
                print('без заголовка')

        kol_str = len(arrayApp)    # записываем клличесвто элементов в списке

        for j in arrayApp:
            self.q = copy.copy(j)
            #print('список который сравниваем', self.q)
            qN = self.q[int(self.N_stolb) - 1]  # присваиваем значение количества строки которую нужно сравнить
            del self.q[int(self.N_stolb) - 1]   # удаляем значение количества строки которую нужно сравнить
            #print('Теперь у нас есть список', self.q)
            y = arrayApp.index(j) + 1  # нам нужна следующая строка
            sov = False                 # это счетчик совпадений

            # начинаем проверять на совпадение
            while y <= kol_str-1:   # начинаем сравнивать со следующей строкой
                i = 0
                self.w = copy.copy(arrayApp[y])     # строка с которой сравниваем это следующая строка
                #print('список с которым сравниваем', self.w)
                wN = self.w[int(self.N_stolb) - 1]  # присваиваем значение количества строки с которой нужно сравнить
                del self.w[int(self.N_stolb) - 1]   # удаляем значение количества строки с которой нужно сравнить
                #print('Теперь у нас есть список', self.w)

                if self.q == self.w:
                    i += 1
                    #print(qN)
                    qN = str(int(wN) + int(qN))  # складываем количество
                    #print('Складываем количество +' + wN + ' Итог=' + qN)
                    sov = True  # сообщаем что были совпадения
                    del arrayApp[y]
                    kol_str = len(arrayApp)
                else:
                    #print('элемент не похож')
                    y = y + 1

            # проверяем есть ли совпадения
            if sov == False:
                array2.append(j)
            else:
                self.q.insert(int(self.N_stolb)-1, qN)
                array2.append(self.q)

        if self.OUT_name_file == False:
            #print('Отсортированный список:', array2)
            return array2
        else:   # записываем результат в файл
            f = open(self.OUT_name_file, 'w')

            for i in array2:
                in_dat2 = (';'.join(i))
                f.write(in_dat2 + '\n')

            f.close()

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    sorting('txt', 'комплектующие.txt', 'комплектующие ИТОГ.txt', 4, False).sort()