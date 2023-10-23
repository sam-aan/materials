# coding^utf8
import copy
import re

from to_exel import writing_to_exl
from сравнение import sorting
from detali import Detali
import nominal
import line_raskroi
import socket
import exel_to_spisok   # для обработки входного файла эксель
import to_pdf_reportlab
import to_pdf
from datetime import datetime

class rashet:
    def __init__(self, atr, fname, PP):
        self.index = 0
        self.N_zak = atr[0]
        self.N_proj = atr[1]
        self.Name_proj = atr[2]
        self.fname = fname      #Имя файла для расчета
        self.spisok_filov = []
        self.spis_kompl = {'profil': [], 'st_izd': []}
        self.spisok_dla_mater = {}  # словарь для расчета материалов
        self.Proiz = PP     # Выбранное производство, 1-Кама, 0-Солярис

    def zapusk(self):
        print('Начало')
        #Создаем словарь для записи комплектующих
        nom_shet = int(re.findall(r'\w+', open('nom_rashet.txt', "r").readlines()[-1])[0]) + 1
        line = '№' + str(nom_shet) + '\n' + '' + str(socket.gethostname())    # строка с данными о компьютере и дате расчета

        # словарь для контрольной ведомости
        KtrSlvr = exel_to_spisok.InOut(self.fname, 'k').zapusk()

        # получаем список для запуска
        di = exel_to_spisok.InOut(self.fname, 'n').zapusk()
        print(di)
        sklad = {}  # словарь для создания контрольной ведомости
        self.index = 0

        for i in di:
            RabVed = {}      # Словарь для раб. ведомости
            SpisKomplekt = []  # список для направляющих, сухарей, фланцев.
            self.spisok_dla_mater[i] = {'seria': 'E3', 'material': 'Al', 'nominal': 630, 'dlina': 0,
                                        'Nstik': 0, 'Nsekc': 0, 'Nkon_zag': 0, 'Nflanc': 0, 'Lsvar_izd': 0}

            for input_data in di[i]:  # начинаем перебор построчно
                self.spisok_dla_mater[i]['material'] = input_data[2]
                self.spisok_dla_mater[i]['nominal'] = input_data[4]
                self.spisok_dla_mater[i]['seria'] = input_data[0]
                data = nominal.calc(input_data, self.Proiz).calc_nom()
                itog = calculation(data, input_data, self.index, RabVed, SpisKomplekt,
                                   self.spis_kompl, self.spisok_dla_mater[i]).choice()

                if itog[0] == False:
                    print('Ошибка: нестандартная секция')
                    itog[2]['категория'] = 'спецификация'
                    sklad[self.index] = itog[2]
                else:
                    self.index = itog[1]
                    RabVed = itog[2]
                    self.komplekt = itog[3]

                self.spisok_dla_mater[i] = copy.deepcopy(itog[4])
            RabVed = line_raskroi.techno(self.komplekts(SpisKomplekt, RabVed))
            self.spisok_filov.append(writing_to_exl([self.N_zak, self.N_proj, self.Name_proj, self.Proiz], i, RabVed, line, 'vedomost').setting_exl())

        sklad = exel_to_spisok.InOut([sklad, KtrSlvr], 'o').zapusk()
        '''делаем файл эксель с котр.вед. и получем имя файла и список'''
        ret = writing_to_exl([self.N_zak, self.N_proj, self.Name_proj, self.Proiz], False, sklad, line, 'upakovka').setting_exl()
        self.spisok_filov.append(ret[0])        # добавляем в список файлов для удаления имя контрольной ведомсти

        for sss in to_pdf_reportlab.obedin(ret[1], self.N_zak):     # запускаем создание наклеек в pdf
            self.spisok_filov.append(sss)

        return [self.spisok_filov, self.spisok_dla_mater]

    def komplekts(self, spisok, itog):
        '''модуль eto нужен исключительно для счета направляющих и сухарей.'''
        print('РАСЧЕТ НАПРАВЛЯЮЩИХ И СУХАРЕЙ')
        print(spisok)
        spisok_strok = sorting('0', spisok, False, 5, False, None).addition()
        print(spisok_strok)

        for i in spisok_strok:
            dat = nominal.calc(['E3', '55', i[1], i[0], i[2], '', i[3], '', '', i[4]], self.Proiz).calc_nom()
            self.index += 1
            kol = int(i[4])
            det = Detali(0, dat, '', kol, [0, 0], [0, 0, 0], self.spis_kompl)
            det = getattr(det, i[3])()  # создаем список
            det.insert(0, '-')          # добавляем в список
            det.insert(0, self.index)   # добавляем в список
            det.append(kol)             # добавляем в конец списка
            #print('det', det)
            itog[det[0]] = {'Серия': det[2], 'ip': det[3], 'Материал': det[4], 'In': det[5],
                                 'Кол. пров.': det[6], 'Наименование': det[7], 'Обозначение': det[8], 'Разм.L': det[9],
                                 'Разм.L1': det[10], 'Разм.A': det[11], 'Разм.B': det[12], 'Разм.C': det[13],
                                 'количество': det[14], 'тип': '', 'категория': 'ведомость'}
        return itog


class calculation:
    def __init__(self, data, input_data, index, itog, komplekt, spis_kompl, spisok_dla_mater):
        self.dat = data                                                     # обработанный словарь вводных данных
        self.input_data = input_data                                        # начальный список вводных данных
        self.index = index                                                  # номер счетчика
        self.itog = itog                                                    # итоговый список деталей и сборок
        self.tip = re.findall(r'\d', str(self.dat['тип']))                  # ТИП список [1, 1]
        self.os = re.findall(r'\d+', self.dat['размер'])                    # список размеров по осям
        self.length_OS = self.listsum(self.os)                              # длина секции по осям
        self.kol_os = len(self.os)                                          # вычисляем количество осей
        self.komplekt = komplekt                                            # счетчик комплектующих
        self.spis_kompl = spis_kompl                                        # словарь со списками комплектующих
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.X = '-'
        self.Y = '-'
        self.L = '-'
        self.L1 = '-'
        self.spisok_dla_mater = spisok_dla_mater                            # для расчета материалов

    def listsum(self, numList):
        '''модуль для разделения в размерах размеры секции от прочих параметров'''
        theSum = 0

        if self.dat['Обозначение'] in ['tsv', 'ом']:
            numList = re.findall(r'[^\s]+', re.sub(r'[()]', ' ', self.dat['размер']))[0]

        for i in numList:
            theSum = theSum + int(i)

        return theSum

    def choice(self):
        print('НАЧАЛО РАСЧЕТА СЕКЦИИ: ', self.dat['Материал'], self.dat['Кол. пров.'],
              self.dat['Обозначение'], self.dat['In'], self.dat['размер'])

        section = {'п': 'p', 'уг': 'ug', 'ув': 'uv', 'зг': 'z_g', 'зв': 'z_v', 'кп': 'k_p', 'кл': 'k_l',
                   'ом': 'om', 'омф': 'omf', 'пф': 'p', 'згф': 'z_g', 'звф': 'z_v', 'увф': 'uv', 'угф': 'ug',
                   'тв': 'tv', 'тс': 'ts', 'pt': 'p', 'pf': 'p', 'pfk': 'p', 'ug': 'ug', 'ugf': 'ug',
                   'uv': 'uv', 'uvf': 'uv', 'kp': 'k_p', 'kl': 'k_l', 'kpfuv': 'k_p', 'klfuv': 'k_l',
                   'kpfug': 'k_p', 'klfug': 'k_l',
                   'zv': 'z_v', 'zvf': 'z_v',
                   'zg': 'z_g', 'zgf': 'z_g', 'tv': 'tv', 'tg': 'tg', 'tsv': 'ts', 'sb': 'sb',
                   'сб': 'sb', 'pr': 'om', 'prf': 'omf', 'kz': 'kz', 'pn': 'pn', 'om': 'bom',
                   'omf': 'bom', 'ks': 'ks', 'ksb': 'ksb', 'pp': 'pp', 'sk': 'sk'}

        if str(self.dat['Обозначение']) not in section:
            znach = False
        else:
            znach = getattr(calculation, section[str(self.dat['Обозначение'])])(self)  # запускаем выбранную секцию

        if znach == True:
            print('ЗАВЕРШЕНИЕ РАСЧЕТА СЕКЦИИ')
            return [True, self.index, self.itog, self.komplekt, self.spisok_dla_mater]
        else:
            print('Чтото пошло не так')
            return [False, self.index, self.dat, self.komplekt, self.spisok_dla_mater]

    def welded_part(self, svar_det):
        print('РАСЧЕТ СВАРНОЙ ДЕТАЛИ', '| Обознач:', svar_det[0])
        self.index += 1
        index = self.index
        #print(svar_det)
        kol = int(svar_det[2]) * int(self.dat['количество'])
        #one_symbol = re.findall(r'\w+', svar_det[0])[0]
        last_symbol = re.findall(r'\w+', svar_det[0])[-1]
        W_line1 = []
        nominal = self.dat['In']

        # if one_symbol == 'К':
        #     oboznach = 'Крышка СБ'
        #     nominal = '-'
        # elif one_symbol == 'КВ':
        #     oboznach = 'Крышка с выступом СБ'
        #     nominal = '-'
        # elif one_symbol == 'С':
        #     oboznach = 'Стенка СБ'
        #     nominal = self.dat['In']
        # elif one_symbol == 'Ш':
        #     oboznach = 'Шина СБ'
        #     nominal = self.dat['In']
        # else:
        #     oboznach = 'Сварная деталь СБ'
        #     nominal = self.dat['In']

        if last_symbol == 'З':
            svar_det[0] = svar_det[0] + ' (Зеркальная)'

        A = '-'
        B = '-'
        C = '-'
        X = '-'
        Y = '-'
        L = '-'
        L1 = '-'

        if self.dat['Обозначение'] in ['тв', 'tv']:
            if svar_det[0] in ['С-СД14']:
                if self.dat['In'] in [3200, 4000, 5000]:
                    C = str(float(svar_det[3][2][0]) - float(self.dat['расстояние от оси до корпуса'])
                            - float(self.dat['ширина стенки']) - 1.5)
                else:
                    C = str(float(svar_det[3][2][0]) - float(self.dat['расстояние от оси до корпуса'])
                            - float(self.dat['ширина стенки']) / 2)
            elif svar_det[0] in ['Ш-СД22', 'Ш-СД22-З', 'Ш-СД21', 'Ш-СД21-З', 'Ш-СД15', 'Ш-СД15-З', 'Ш-СД16',
                                 'Ш-СД16-З']:
                if self.dat['In'] in [3200, 4000, 5000]:
                    C = str(float(svar_det[3][2][0]) - float(self.dat['расстояние от оси до шины'])
                            - float(self.dat['ширина шины']) - 3)
                else:
                    C = str(float(svar_det[3][2][0]) - float(self.dat['расстояние от оси до шины'])
                            - float(self.dat['ширина шины']) / 2)
            else:
                C = '-'
            L = str('*'.join(self.os))
        elif self.dat['Обозначение'] in ['тс', 'tsv']:
            L = self.dat['Обозначение'] + re.findall(r'[^\s]+', re.sub(r'[()]', ' ', self.dat['размер']))[0]
            C = '-'
        elif self.dat['Обозначение'] in ['ом', 'pr', 'омф', 'prf']:

            if int(self.tip[0]) in [1, 2]:
                A = str(svar_det[5][0])
            elif int(self.tip[0]) in [3, 4]:
                A = str(svar_det[5][0])
                B = str(svar_det[5][1])
            elif int(self.tip[0]) in [5, 6]:
                A = str(svar_det[5][0])
                B = str(svar_det[5][1])
                C = str(svar_det[5][1])

            del svar_det[5]
            #print(self.os)
            L = str(float(self.os[0]) - float(self.dat['расстояние от оси до шины']) * 2)
        elif self.dat['Обозначение'] in ['уг', 'ug']:
            C = self.C
        else:
            C = '-'

        if self.dat['Обозначение'] in ['п', 'уг', 'ув', 'зг', 'зв', 'кп', 'кл', 'згф', 'звф', 'увф', 'угф', 'тв', 'тс',
                                       'pt', 'ug', 'uv', 'zg', 'zv', 'kp', 'kl', 'zgf', 'zvf', 'uvf', 'ugf', 'tv',
                                       'tsv', 'sk']:
            nom_two = [A, B, C]
            nom_one = 0
            print(len(svar_det))

            for i in range(3, len(svar_det)):
                if svar_det[i][0] in ['u', 'ugol', 'ugol1', 'ugol2', 'ugol1_2', 'ugol_2', 'ugol2-z']:
                    result = self.detail(svar_det[i] + self.os, '')
                    W_line1.append(result)
                    continue
                else:
                    result = self.detail(svar_det[i], '')
                    nom_two[nom_one] = result[8]
                    W_line1.append(result)
                    nom_one += 1

            A = nom_two[0]
            B = nom_two[1]
            C = nom_two[2]
            print(A, B, C)

        else:   # для ОМ
            nom_one = 0

            for i in range(3, len(svar_det)):
                result = self.detail(svar_det[i], 's')
                W_line1.append(result)
                nom_one += 1

        W_line = [[index, self.dat['Серия'], self.dat['ip'], self.dat['Материал'], nominal,
                   self.dat['Кол. пров.'], svar_det[1], svar_det[0], L, L1, A, B, C, kol,
                   'ведомость']]
        W_line = W_line + W_line1
        #print('W_line', W_line)
        return W_line

    def detail(self, detal, coating):
        """ detal  это список атрибутов детали: [Обозначение, количество, раземр по осям]
            coating это атрибут покрытия (окрашенно "s", или не окрашено)."""
        print('РАСЧЕТ ДЕТАЛИ', '| Обознач:', str(detal[0]))

        if detal[0] in ['n', 'fl', 'zts', 'sux', 'mfazcentr', 'torcentr']:
            self.komplekt.append([self.dat['Кол. пров.'], self.dat['Материал'], self.dat['In'],
                                  detal[0], detal[1] * int(self.dat['количество'])])
            return 0
        else:
            #print(self.index)
            self.index = self.index + 1
            kol = detal[1] * self.dat['количество']
            print('detal', detal)
            itog = getattr(Detali(detal[2], self.dat, coating, kol, self.tip,
                                  [self.A, self.B, self.C], self.spis_kompl), detal[0])()
            print('itog', itog)
            itog.insert(0, self.index)
            itog.append(kol)
            itog.append('ведомость')
            #print('ИТОГ: ', itog)
            return itog

    # Вывод на печать
    def prints(self, itog):
        print('ЗАПИСЬ В СПИСОК')
        for i in itog:
            self.itog[i[0]] = {'Серия': i[1], 'ip': i[2], 'Материал': i[3], 'In': i[4], 'Кол. пров.': i[5],
                               'Наименование': i[6], 'Обозначение': i[7], 'Разм.L': i[8], 'Разм.L1': i[9],
                               'Разм.A': i[10], 'Разм.B': i[11], 'Разм.C': i[12], 'количество': i[13],
                               'тип': self.dat['тип'], 'стандарт': self.dat['стандарт'],
                               'категория': i[14]}

    # раысчет стыков
    def sb(self):
        #print(self.index)
        self.index += 1
        itog = [[self.index, self.dat['Серия'], self.dat['ip'], self.dat['Материал'], self.dat['In'],
                 self.dat['Кол. пров.'], self.dat['Наименование'], 'sb',
                 self.L, self.L1, self.A, self.B, self.C,
                 self.dat['количество'], 'спецификация']]
        detali = [['ss', 2, self.os],
                  ['tp', self.dat['количество токопроводящих пластин'], self.os],
                  ['vtulka', self.dat['количество втулок'], self.os],
                  ['ksb', 2, self.os],
                  ['dp', self.dat['количество демпферов'], self.os],
                  ['izol_k', 2, self.os],
                  ['izol_s', self.dat['количество средних изоляторов'], self.os]]

        if self.dat['In'] in [3200, 4000, 5000]:
            detali[5][1] = detali[5][1] * 2
            detali[6][1] = detali[6][1] * 2
        elif self.dat['In'] in [3200, 4000, 5000]:
            detali[5][1] = detali[5][1] * 3
            detali[6][1] = detali[6][1] * 3

        self.spisok_dla_mater['Nstik'] = self.spisok_dla_mater['Nstik'] + int(self.dat['количество'])
        self.spisok_dla_mater['KolProv'] = self.dat['Кол. пров.']

        for j in detali:
            itog_det = self.detail(j, '')
            itog.append(itog_det)
        self.prints(itog)
        return True

    # прямые и фланцы
    def p(self):
        #print('Расчет прямой секции:')
        self.L = self.os[0]
        self.index = self.index + 1

        self.spisok_dla_mater['dlina'] = round(self.spisok_dla_mater['dlina'] + int(self.dat['количество']) * int(self.L) / 1000, 0)
        self.spisok_dla_mater['Nsekc'] = self.spisok_dla_mater['Nsekc'] + int(self.dat['количество'])
        self.spisok_dla_mater['KolProv'] = self.dat['Кол. пров.']

        if (self.index) == 500:
            self.dat['тип'] = 0.5
        elif int(self.L) == 1000:
            self.dat['тип'] = 1.0
        elif int(self.L) == 1500:
            self.dat['тип'] = 1.5
        elif int(self.L) == 2000:
            self.dat['тип'] = 2.0
        elif int(self.L) == 2500:
            self.dat['тип'] = 2.5
        elif int(self.L) == 3000:
            self.dat['тип'] = 3.0
        elif int(self.L) > 500 and int(self.L) < 1000:
            self.dat['тип'] = 0.9
        elif int(self.L) > 1000 and int(self.L) < 1500:
            self.dat['тип'] = 1.4
        elif int(self.L) > 1500 and int(self.L) < 2000:
            self.dat['тип'] = 1.9
        elif int(self.L) > 2000 and int(self.L) < 2500:
            self.dat['тип'] = 2.4
        elif int(self.L) > 2500 and int(self.L) < 3000:
            self.dat['тип'] = 2.9

        itog = [[self.index, self.dat['Серия'], self.dat['ip'], self.dat['Материал'], self.dat['In'],
                 self.dat['Кол. пров.'], self.dat['Наименование'], 'pt',
                 self.L, self.L1, self.A, self.B, self.C,
                 self.dat['количество'], 'спецификация']]
#E3
        if self.dat['Серия'] in ['Е3', 'E3']:

            if str(self.dat['Кол. пров.']) in ['4', '3+1']:
                detali = [['kv', 2, self.os[0]], ['c', 2, self.os[0]], ['s1', 2, self.os[0]], ['s2', 2, self.os[0]],
                          ['n', 4], ['sux', 4]]

                if self.dat['Обозначение'] in ['пф', 'pf', 'pfk']:
                    self.spisok_dla_mater['Nflanc'] = self.spisok_dla_mater['Nflanc'] + int(self.dat['количество'])
                    itog[0][7] = 'pf'
                    detali[2][0] = 's17'
                    detali[3][0] = 's18'
                    detali[4][1] = 2
                    detali.append(['fl', 2])

                if self.dat['In'] in [2500]:
                    detali.pop(0)
                    detali.insert(0, ['k', 2, self.os[0]])
                elif self.dat['In'] in [2600, 3200, 4000, 5000]:
                    detali.pop(0)
                    detali.insert(0, ['k', 2, self.os[0]])
                    for i in [1, 2, 3]:
                        detali[i][1] = 4
                    detali.insert(1, ['kc', 1, self.os[0]])
                elif self.dat['In'] in [6400]:
                    detali.pop(0)
                    detali.insert(0, ['k', 2, self.os[0]])
                    for i in range(1, 4):
                        detali[i][1] = 6
                    detali.insert(1, ['kc', 2, self.os[0]])

            else:   # 3-х проводной
                detali = [['kv', 2, self.os[0]], ['c', 2, self.os[0]], ['s1', 2, self.os[0]], ['s', 1, self.os[0]],
                          ['n', 4], ['sux', 4]]

                if self.dat['Обозначение'] in ['пф', 'pf', 'pfk']:
                    self.spisok_dla_mater['Nflanc'] = self.spisok_dla_mater['Nflanc'] + int(self.dat['количество'])
                    itog[0][7] = 'pf'
                    detali[2][0] = 's17'
                    detali[4][1] = 2
                    detali.append(['fl', 2])
#CR
        elif self.dat['Серия'] in ['CR1', 'CR2']:

            if str(self.dat['Кол. пров.']) in ['4', '3+1']:
                detali = [['s_01', 4, self.os[0]], ['torcentr', 2], ['mfazcentr', round(int(self.L) / 400, 0)]]

                if self.dat['Обозначение'] in ['пф', 'pf', 'pfk']:
                    self.spisok_dla_mater['Nflanc'] = self.spisok_dla_mater['Nflanc'] + int(self.dat['количество'])
                    itog[0][7] = 'pf'
                    detali[0][0] = 's36'
                    detali[0][1] = 2
                    detali.append(['s37', 2, self.os[0]])
                    detali.append(['fl', 2])

                if self.dat['In'] in [3200, 4000, 5000]:
                    detali.insert(0, ['s_01', 8, self.os[0]])
                elif self.dat['In'] in [6400]:
                    detali.insert(0, ['s_01', 12, self.os[0]])

            else:  # 3-х проводной
                detali = [['s_01', 3, self.os[0]], ['torcentr', 2], ['mfazcentr', round(int(self.L) / 0.4)]]

                # нет чертежей для пф для заливки
                if self.dat['Обозначение'] in ['пф', 'pf', 'pfk']:
                    self.spisok_dla_mater['Nflanc'] = self.spisok_dla_mater['Nflanc'] + int(self.dat['количество'])
                    self.spisok_dla_mater['KolProv'] = self.dat['Кол. пров.']
                    itog[0][7] = 'pf'
                    detali[2][0] = 's17'
                    detali[4][1] = 2
                    detali.append(['fl', 2])

        for i in detali:
            itog_det = self.detail(i, 's_01')
            if itog_det == 0:   # только что расчитывали сухарь, направляющую или фланец
                continue
            else:
                itog.append(itog_det)
        self.prints(itog)

        line_raskroi.komlektuyushie(self.dat, self.length_OS, self.spis_kompl).standart_izdel()
        return True

    # сортировка словаря
    def sort(self, dict_list):
        dict_list_sort = {}
        for k in sorted(dict_list.keys()):
            dict_list_sort[k] = dict_list[k]
        return dict_list_sort

    def ug(self):
        self.A = self.os[0]
        self.B = self.os[1]

        self.spisok_dla_mater['dlina'] = round(self.spisok_dla_mater['dlina'] + int(self.dat['количество'])
                                               * (int(self.A) + int(self.B)) / 1000, 0)
        self.spisok_dla_mater['Nsekc'] = self.spisok_dla_mater['Nsekc'] + int(self.dat['количество'])
        self.spisok_dla_mater['Lsvar_izd'] = round(self.spisok_dla_mater['Lsvar_izd'] + int(self.dat['количество'])
                                                   * (int(self.A) + int(self.B)) / 1000, 0)
        self.spisok_dla_mater['KolProv'] = self.dat['Кол. пров.']

        # вычисляем угол горизонтального угла
        print("self.os", self.os, len(self.os))
        if self.dat['Обозначение'] in ['ugf', 'угф'] and len(self.os) == 3:
            self.os.append(90)
        elif self.dat['Обозначение'] in ['ug', 'уг'] and len(self.os) == 2:
            self.os.append(90)

        self.C = int(self.os[-1])
        self.index = self.index + 1
        itog = [[self.index, self.dat['Серия'], self.dat['ip'], self.dat['Материал'], self.dat['In'],
                 self.dat['Кол. пров.'], self.dat['Наименование'], 'ug',
                 self.L, self.L1, self.A, self.B, self.C,
                 self.dat['количество'], 'спецификация']]

        if str(self.dat['Кол. пров.']) in ['4', '3+1']:
            if self.C != 90:
                svar_det_one_floor = [['К-СД1', 'Крышка СБ', 1, ['k1', 1, self.A], ['k2', 1, self.B]],
                                      ['К-СД1', 'Крышка СБ', 1, ['k1', 1, self.B], ['k2', 1, self.A]],
                                      ['С-СД15', 'Стенка СБ', 1, ['c4', 1, self.A], ['c4', 1, self.B]],
                                      ['С-СД16', 'Стенка СБ', 1, ['c3', 1, self.A], ['c3', 1, self.B]]]
            else:
                svar_det_one_floor = [['К-СД1', 'Крышка СБ', 1, ['k1', 1, self.A], ['k2', 1, self.B]],
                                      ['К-СД1', 'Крышка СБ', 1, ['k1', 1, self.B], ['k2', 1, self.A]],
                                      ['С-СД12', 'Стенка СБ', 1, ['cB', 1, self.A], ['cB', 1, self.B], ['u', 1, 0]],
                                      ['С-СД2', 'Стенка СБ', 1, ['cA', 1, self.A], ['cA', 1, self.B], ['u', 1, 0]]]

            detali = [['n', 4], ['sux', 4],
                      ['s5', 1, [self.A, self.B]],
                      ['s6', 1, [self.A, self.B]],
                      ['s7', 1, [self.A, self.B]],
                      ['s8', 1, [self.A, self.B]]]

            if self.dat['In'] in [2600, 3200, 4000, 5000]:

                if self.C != 90:
                    svar_det_one_floor = [['К-СД1', 'Крышка СБ', 1, ['k1', 1, self.A], ['k2', 1, self.B]],
                                          ['К-СД1', 'Крышка СБ', 1, ['k1', 1, self.B], ['k2', 1, self.A]],
                                          ['С-СД15', 'Стенка СБ', 2, ['c4', 2, self.A], ['c4', 2, self.B]],
                                          ['С-СД16', 'Стенка СБ', 2, ['c3', 2, self.A], ['c3', 2, self.B]],
                                          ['К-СД14', 1, ['kc1', 1, self.A], ['kc1', 1, self.B]]]
                else:
                    svar_det_one_floor = [['К-СД1', 'Крышка СБ', 1, ['k1', 1, self.A], ['k2', 1, self.B]],
                                          ['К-СД1', 'Крышка СБ', 1, ['k1', 1, self.B], ['k2', 1, self.A]],
                                          ['С-СД12', 'Стенка СБ', 2, ['cB', 2, self.A], ['cB', 2, self.B], ['u', 2, 0]],
                                          ['С-СД2', 'Стенка СБ', 2, ['cA', 2, self.A], ['cA', 2, self.B], ['u', 2, 0]],
                                          ['К-СД14', 'Крышка СБ', 1, ['kc1', 1, self.A], ['kc1', 1, self.B]]]

                for i in [2, 3, 4, 5]:
                    detali[i][1] = 2

            elif self.dat['In'] in [4000, 5000]:

                if self.C != 90:
                    svar_det_one_floor = [['К-СД1', 'Крышка СБ', 1, ['k1', 1, self.A], ['k2', 1, self.B]],
                                          ['К-СД1', 'Крышка СБ', 1, ['k1', 1, self.B], ['k2', 1, self.A]],
                                          ['С-СД15', 'Стенка СБ', 2, ['c4', 2, self.A], ['c4', 2, self.B]],
                                          ['С-СД16', 'Стенка СБ', 2, ['c3', 2, self.A], ['c3', 2, self.B]],
                                          ['К-СД14', 'Крышка СБ', 1, ['kc1', 1, self.A], ['kc1', 1, self.B]]]
                else:
                    svar_det_one_floor = [['К-СД1', 'Крышка СБ', 1, ['k1', 1, self.A], ['k2', 1, self.B]],
                                          ['К-СД1', 'Крышка СБ', 1, ['k1', 1, self.B], ['k2', 1, self.A]],
                                          ['С-СД12', 'Стенка СБ', 2, ['cB', 2, self.A], ['cB', 2, self.B], ['u', 2, 0]],
                                          ['С-СД2', 'Стенка СБ', 2, ['cA', 2, self.A], ['cA', 2, self.B], ['u', 2, 0]],
                                          ['К-СД14', 'Крышка СБ', 1, ['kc1', 1, self.A], ['kc1', 1, self.B]]]

                for i in [2, 3, 4, 5]:
                    detali[i][1] = 2

            elif self.dat['In'] in [6400]:

                if self.C != 90:
                    svar_det_one_floor = [['К-СД1', 'Крышка СБ', 1, ['k1', 1, self.A], ['k2', 1, self.B]],
                                          ['К-СД1', 'Крышка СБ', 1, ['k1', 1, self.B], ['k2', 1, self.A]],
                                          ['С-СД15', 'Стенка СБ', 3, ['c4', 3, self.A], ['c4', 3, self.B]],
                                          ['С-СД16', 'Стенка СБ', 3, ['c3', 3, self.A], ['c3', 3, self.B]],
                                          ['К-СД14', 'Крышка СБ', 2, ['kc1', 2, self.A], ['kc1', 2, self.B]]]
                else:
                    svar_det_one_floor = [['К-СД1', 'Крышка СБ', 1, ['k1', 1, self.A], ['k2', 1, self.B]],
                                          ['К-СД1', 'Крышка СБ', 1, ['k1', 1, self.B], ['k2', 1, self.A]],
                                          ['С-СД12', 'Стенка СБ', 3, ['cB', 3, self.A], ['cB', 3, self.B], ['u', 3, 0]],
                                          ['С-СД2', 'Стенка СБ', 3, ['cA', 3, self.A], ['cA', 3, self.B], ['u', 3, 0]],
                                          ['К-СД14', 'Крышка СБ', 2, ['kc1', 2, self.A], ['kc1', 2, self.B]]]

                for i in [2, 3, 4, 5]:
                    detali[i][1] = 3

            if self.os[0] == self.os[1] and self.dat['Обозначение'] not in ['угф', 'ugf']:
                #print(' Симетричные оси')
                svar_det_one_floor.pop(0)           # удаляем первую крышку К-СД1
                svar_det_one_floor[0][2] *= 2       # умножаем на 2 К-СД1
                svar_det_one_floor[0][3][1] *= 2    # умножаем на 2 к1
                svar_det_one_floor[0][4][1] *= 2    # умножаем на 2 к2
                svar_det_one_floor[1].pop(3)        # удаляем стенку с3 в С-СД1
                svar_det_one_floor[1][3][1] *= 2    # умножаем на 2 c3
                svar_det_one_floor[2].pop(3)        # удаляем стенку сА в С-СД2
                svar_det_one_floor[2][3][1] *= 2    # умножаем на 2 c3

            if self.dat['Обозначение'] in ['угф', 'ugf']:
                self.spisok_dla_mater['Nflanc'] = self.spisok_dla_mater['Nflanc'] + int(self.dat['количество'])
                self.spisok_dla_mater['KolProv'] = self.dat['Кол. пров.']
                itog[0][7] = 'ugf'
                #print('УГФ')
                svar_det_one_floor[0][3][0] = 'k2f'
                svar_det_one_floor[1][4][0] = 'k1f'
                svar_det_one_floor[2][3][0] = 'cBf'
                svar_det_one_floor[3][3][0] = 'cAf'

                if len(svar_det_one_floor) == 5:    # для двухэтажек

                    for i in svar_det_one_floor:
                        print(i)
                    svar_det_one_floor[4][3][0] = 'kc1f'
                dictionary = {2: 's19', 3: 's20', 4: 's21', 5: 's22'}

                for i in dictionary:
                    detali[i][0] = dictionary[i]
                detali.append(['fl', 2])
                #print(detali)

#CR
            if self.dat['Серия'] in ['CR1', 'CR2']:

                if self.dat['Обозначение'] in ['угф', 'ugf']:
                    detali = [['s23', 1, [self.A, self.B, 1]],
                              ['s24', 1, [self.A, self.B, 2]],
                              ['s25', 1, [self.A, self.B, 3]],
                              ['s26', 1, [self.A, self.B, 4]],
                              ['torcentr', 2], ['mfazcentr', round((int(self.os[0]) + int(self.os[1])) / 200, 0)]]
                else:
                    detali = [['s41', 1, [self.A, self.B, 1]],
                              ['s41', 1, [self.A, self.B, 2]],
                              ['s41', 1, [self.A, self.B, 3]],
                              ['s41', 1, [self.A, self.B, 4]],
                              ['torcentr', 2], ['mfazcentr', round((int(self.os[0]) + int(self.os[1])) / 200, 0)]]

        else:
            svar_det_one_floor = [['К-СД1', 'Крышка СБ', 1, ['k1', 1, self.A], ['k2', 1, self.B]],
                                  ['К-СД1', 'Крышка СБ', 1, ['k1', 1, self.os[1]], ['k2', 1, self.A]],
                                  ['С-СД12', 'Стенка СБ', 1, ['cB', 1, self.A], ['cB', 1, self.B], ['u', 1, 0]],
                                  ['С-СД2', 'Стенка СБ', 1, ['cA', 1, self.A], ['cA', 1, self.B], ['u', 1, 0]]]
            detali = [['n', 4], ['sux', 4],
                      ['s5', 1, [self.A, self.B]],
                      ['s38', 1, [self.A, self.B]],
                      ['s8', 1, [self.A, self.B]]]

        if self.dat['Серия'] in ['CR1', 'CR2']:
            print('CR1 нет сварных деталей!!!')
        else:

            for i in svar_det_one_floor:
                itog_svar = self.welded_part(i)

                for j in itog_svar:
                    itog.append(j)

        for j in detali:
            itog_det = self.detail(j, '')

            if itog_det == 0:   # только что расчитывали сухарь, направляющую или фланец
                continue
            else:
                itog.append(itog_det)

        self.prints(itog)

        line_raskroi.komlektuyushie(self.dat, self.length_OS, self.spis_kompl).standart_izdel()
        return True

    def uv(self):
        self.A = self.os[0]
        self.B = self.os[1]

        self.spisok_dla_mater['dlina'] = round(self.spisok_dla_mater['dlina'] + int(self.dat['количество'])
                                               * (int(self.A) + int(self.B)) / 1000, 0)
        self.spisok_dla_mater['Nsekc'] = self.spisok_dla_mater['Nsekc'] + int(self.dat['количество'])
        self.spisok_dla_mater['Lsvar_izd'] = round(self.spisok_dla_mater['Lsvar_izd'] + int(self.dat['количество'])
                                                   * (int(self.A) + int(self.B)) / 1000, 0)
        self.spisok_dla_mater['KolProv'] = self.dat['Кол. пров.']

        self.index = self.index + 1

        itog = [[self.index, self.dat['Серия'], self.dat['ip'], self.dat['Материал'], self.dat['In'],
                 self.dat['Кол. пров.'], self.dat['Наименование'], 'uv',
                 self.L, self.L1, self.A, self.B, self.C,
                 self.dat['количество'], 'спецификация']]

        # CR
        if self.dat['Серия'] in ['CR1', 'CR2']:

            if self.dat['Обозначение'] in ["uvf", "увф"]:
                detali = [['torcentr', 2], ['mfazcentr', round((int(self.os[0]) + int(self.os[1])) / 200, 0)]]
                svar_det = [['Ш-СД31', 'Шина СБ', 4, ['s', 4, [self.A, 'x']], ['s', 4, [self.B, 'y']]]]
            else:
                detali = [['torcentr', 2], ['mfazcentr', round((int(self.os[0]) + int(self.os[1])) / 200, 0)]]
                svar_det = [['Ш-СД31', 'Шина СБ', 4, ['s', 4, [self.A, 'x']], ['s', 4, [self.B, 'y']]]]

            for i in svar_det:
                itog_svar = self.welded_part(i)

                for j in itog_svar:
                    itog.append(j)

            for j in detali:
                itog_det = self.detail(j, '')

                if itog_det == 0:  # только что расчитывали сухарь, направляющую или фланец
                    continue
                else:
                    itog.append(itog_det)

            self.prints(itog)
            return True
        #E3
        else:
            def one(x, y):

                if self.dat['Обозначение'] in ['увф', 'uvf']:
                    self.spisok_dla_mater['Nflanc'] = self.spisok_dla_mater['Nflanc'] + int(self.dat['количество'])
                    self.spisok_dla_mater['KolProv'] = self.dat['Кол. пров.']
                    itog[0][7] = 'uvf'
                    detali = [['n', 2], ['sux', 4], ['fl', 2]]
                    svar_det_one_floor = [['К-СД2', 'Крышка СБ', 1, ['k3f', 1, x], ['k3', 1, y]],
                                          ['К-СД3', 'Крышка СБ', 1, ['k4f', 1, x], ['k4', 1, y]],
                                          ['С-СД3', 'Стенка СБ', 1, ['c1f', 1, x], ['c2', 1, y]],
                                          ['С-СД3', 'Стенка СБ', 1, ['c1', 1, y], ['c2f', 1, x]],
                                          ['Ш-СД17', 'Шина СБ', 1, ['s36', 1, x], ['s3', 1, y]],
                                          ['Ш-СД17-З', 'Шина СБ', 1, ['s36', 1, x], ['s3', 1, y]],
                                          ['Ш-СД18', 'Шина СБ', 1, ['s37', 1, x], ['s4', 1, y]],
                                          ['Ш-СД18-З', 'Шина СБ', 1, ['s37', 1, x], ['s4', 1, y]]]
                else:
                    detali = [['n', 4], ['sux', 4]]
                    svar_det_one_floor = [['К-СД2', 'Крышка СБ', 1, ['k3', 1, x], ['k3', 1, y]],
                                          ['К-СД3', 'Крышка СБ', 1, ['k4', 1, x], ['k4', 1, y]],
                                          ['С-СД3', 'Стенка СБ', 1, ['c1', 1, x], ['c2', 1, y]],
                                          ['С-СД3', 'Стенка СБ', 1, ['c1', 1, y], ['c2', 1, x]],
                                          ['Ш-СД1', 'Шина СБ', 1, ['s3', 1, x], ['s3a', 1, y]],
                                          ['Ш-СД1-З', 'Шина СБ', 1, ['s3', 1, x], ['s3a', 1, y]],
                                          ['Ш-СД2', 'Шина СБ', 1, ['s4', 1, x], ['s4a', 1, y]],
                                          ['Ш-СД2-З', 'Шина СБ', 1, ['s4', 1, x], ['s4a', 1, y]]]

                for j in detali:
                    itog_det = self.detail(j, '')
                    if itog_det == 0:  # только что расчитывали сухарь, направляющую или фланец
                        continue
                    else:
                        itog.append(itog_det)

                return svar_det_one_floor

            def one_3(x, y):
                detali = [['n', 4], ['sux', 4]]
                for j in detali:
                    itog_det = self.detail(j, '')
                    if itog_det == 0:  # только что расчитывали сухарь, направляющую или фланец
                        continue
                    else:
                        itog.append(itog_det)

                svar_det_one_floor = [['К-СД2', 'Крышка СБ', 1, ['k3', 1, x], ['k3', 1, y]],
                                      ['К-СД3', 'Крышка СБ', 1, ['k4', 1, x], ['k4', 1, y]],
                                      ['С-СД3', 'Стенка СБ', 1, ['c1', 1, x], ['c2', 1, y]],
                                      ['С-СД3', 'Стенка СБ', 1, ['c1', 1, y], ['c2', 1, x]],
                                      ['Ш-СД1', 'Шина СБ', 1, ['s3', 1, x], ['s3a', 1, y]],
                                      ['Ш-СД31', 'Шина СБ', 1, ['s', 1, x], ['sa', 1, y]],
                                      ['Ш-СД1-З', 'Шина СБ', 1, ['s3', 1, x], ['s3a', 1, y]]]

                return svar_det_one_floor

            # если оси одинаковые
            def ayna(svar_det_one_floor):
                if x == y and self.dat['Обозначение'] not in ['увф', 'uvf']:
                    svar_det_one_floor.pop(3)       # С-СД3
                    svar_det_one_floor[2][2] *= 2
                    svar_det_one_floor[2][3][1] *= 2
                    svar_det_one_floor[2][4][1] *= 2

                    svar_det_one_floor[0].pop(3)    # К-СД2
                    svar_det_one_floor[0][3][1] = 2

                    svar_det_one_floor[1].pop(3)    # К-СД3
                    svar_det_one_floor[1][3][1] = 2
                    return svar_det_one_floor
                else:
                    return svar_det_one_floor

            if str(self.dat['Кол. пров.']) in ['4', '3+1']:
                if self.dat['In'] in [630, 800, 1000, 1250, 1600, 2000, 2500]:
                    svar_det_one_floor = one(self.A, self.B)
                    for i in svar_det_one_floor:
                        itog_svar = self.welded_part(i)
                        for j in itog_svar:
                            itog.append(j)

                elif self.dat['In'] in [2600, 3200, 4000, 5000]:
                    # первый этаж
                    x = int(self.A) + self.dat['разница между этажами']
                    y = int(self.B) + self.dat['разница между этажами']
                    svar_det_one_floor = one(x, y)
                    svar_det_one_floor[1][0] = 'К-СД13'

                    if self.dat['Обозначение'] in ['увф', 'uvf']:
                        self.spisok_dla_mater['Nflanc'] = self.spisok_dla_mater['Nflanc'] + int(self.dat['количество'])
                        self.spisok_dla_mater['KolProv'] = self.dat['Кол. пров.']
                        itog[0][7] = 'uvf'
                        svar_det_one_floor[1][3][0] = 'kc2f'
                    else:
                        svar_det_one_floor[1][3][0] = 'kc2'

                    svar_det_one_floor[1][4][0] = 'kc2'
                    svar_det_one_floor = ayna(svar_det_one_floor)
                    #   второй этаж
                    x = int(self.A) - self.dat['разница между этажами']
                    y = int(self.B) - self.dat['разница между этажами']
                    svar_det_two_floor = one(x, y)
                    svar_det_two_floor = ayna(svar_det_two_floor)
                    svar_det_two_floor.pop(0)
                    svar_det = svar_det_one_floor + svar_det_two_floor
                    for i in svar_det:
                        itog_svar = self.welded_part(i)
                        for j in itog_svar:
                            itog.append(j)

                #   elif self.dat['In'] in [6400]:
                else:
                    # первый этаж
                    x = int(self.A) + self.dat['разница между этажами']
                    y = int(self.B) + self.dat['разница между этажами']
                    svar_det_one_floor = one(x, y)
                    svar_det_one_floor[1][0] = 'К-СД13'

                    if self.dat['Обозначение'] in ['увф', 'uvf']:
                        self.spisok_dla_mater['Nflanc'] = self.spisok_dla_mater['Nflanc'] + int(self.dat['количество'])
                        self.spisok_dla_mater['KolProv'] = self.dat['Кол. пров.']
                        itog[0][7] = 'uvf'
                        svar_det_one_floor[1][3][0] = 'kc2f'
                    else:
                        svar_det_one_floor[1][3][0] = 'kc2'

                    svar_det_one_floor[1][3][0] = 'kc2'
                    svar_det_one_floor[1][4][0] = 'kc2'
                    #   второй этаж
                    svar_det_two_floor = one(self.A, self.B)
                    svar_det_two_floor[1][0] = 'К-СД13'

                    if self.dat['Обозначение'] in ['увф', 'uvf']:
                        self.spisok_dla_mater['Nflanc'] = self.spisok_dla_mater['Nflanc'] + int(self.dat['количество'])
                        self.spisok_dla_mater['KolProv'] = self.dat['Кол. пров.']
                        itog[0][7] = 'uvf'
                        svar_det_one_floor[1][3][0] = 'kc2f'
                    else:
                        svar_det_one_floor[1][3][0] = 'kc2'

                    svar_det_two_floor[1][3][0] = 'kc2'
                    svar_det_two_floor[1][4][0] = 'kc2'
                    svar_det_two_floor.pop(0)
                    #   третий этаж
                    x = int(self.A) - self.dat['разница между этажами']
                    y = int(self.B) - self.dat['разница между этажами']
                    svar_det_three_floor = one(x, y)
                    svar_det_three_floor.pop(0)
                    svar_det = svar_det_one_floor + svar_det_two_floor + svar_det_three_floor
                    for i in svar_det:
                        itog_svar = self.welded_part(i)
                        for j in itog_svar:
                            itog.append(j)
            else:               # 3-х проводной
                svar_det_one_floor = one_3(self.A, self.B)

                for i in svar_det_one_floor:
                    itog_svar = self.welded_part(i)
                    for j in itog_svar:
                        itog.append(j)

            self.prints(itog)
            line_raskroi.komlektuyushie(self.dat, self.length_OS, self.spis_kompl).standart_izdel()
            return True

    def z_g(self):      #!!!!! не доделан 3-х проводной

        self.A = self.os[0]
        self.B = self.os[1]
        self.C = self.os[2]

        self.spisok_dla_mater['dlina'] = round(self.spisok_dla_mater['dlina'] + int(self.dat['количество'])
                                               * (int(self.A) + int(self.B) + int(self.C)) / 1000, 0)
        self.spisok_dla_mater['Nsekc'] = self.spisok_dla_mater['Nsekc'] + int(self.dat['количество'])
        self.spisok_dla_mater['Lsvar_izd'] = round(self.spisok_dla_mater['Lsvar_izd'] + int(self.dat['количество'])
                                                   * (int(self.A) + int(self.B) + int(self.C)) / 1000, 0)
        self.spisok_dla_mater['KolProv'] = self.dat['Кол. пров.']

        self.index = self.index + 1
        itog = [[self.index, self.dat['Серия'], self.dat['ip'], self.dat['Материал'], self.dat['In'],
                 self.dat['Кол. пров.'], self.dat['Наименование'], 'zg',
                 self.L, self.L1, self.A, self.B, self.C,
                 self.dat['количество'], 'спецификация']]

        if str(self.dat['Кол. пров.']) in ['4', '3+1']:
            svar_det_one_floor = [['К-СД4', 'Крышка СБ', 1, ['k2', 1, self.A], ['k7', 1, self.B], ['k2', 1, self.C]],
                                  ['К-СД5', 'Крышка СБ', 1, ['k1', 1, self.A], ['k8', 1, self.B], ['k1', 1, self.C]],
                                  ['С-СД13', 'Стенка СБ', 1, ['cB', 1, self.A], ['u', 2, 0], ['cC', 1, self.B], ['cA', 1, self.C]],
                                  ['С-СД13', 'Стенка СБ', 1, ['cB', 1, self.C], ['u', 2, 0], ['cC', 1, self.B], ['cA', 1, self.A]]]
                                  #['С-СД4', 1, ['c3', 1, self.os[0]], ['c3a', 1, self.os[1]], ['u', 1], ['cA', 1, self.os[2]]],
                                  #['С-СД4', 1, ['c3', 1, self.os[2]], ['c3a', 1, self.os[1]], ['u', 1], ['cA', 1, self.os[0]]]]

            if self.dat['Серия'] in ['CR1', 'CR']:
                detali = [['torcentr', 2], ['mfazcentr', round((int(self.os[0]) + int(self.os[1]) +
                                                                int(self.os[2])) / 200, 0)],
                          ['s46_1', 1, [self.A, self.B, self.C]],
                          ['s46_2', 1, [self.A, self.B, self.C]],
                          ['s46_3', 1, [self.A, self.B, self.C]],
                          ['s46_4', 1, [self.A, self.B, self.C]]]
            else:
                detali = [['n', 4], ['sux', 4],
                          ['s13', 1, [self.A, self.B, self.C]],
                          ['s14', 1, [self.A, self.B, self.C]],
                          ['s15', 1, [self.A, self.B, self.C]],
                          ['s16', 1, [self.A, self.B, self.C]]]

            if self.dat['In'] in [2000, 2500]:
                svar_det_one_floor[2] = ['С-СД13', 'Стенка СБ', 1, ['cB', 1, self.A], ['u', 2, 0], ['cC', 1, self.B], ['cA', 1, self.C]]
                svar_det_one_floor[3] = ['С-СД13', 'Стенка СБ', 1, ['cB', 1, self.C], ['u', 2, 0], ['cC', 1, self.B], ['cA', 1, self.A]]
            elif self.dat['In'] in [2600, 3200]:
                svar_det_one_floor[2] = ['С-СД13', 'Стенка СБ', 2, ['cB', 2, self.A],  ['u', 2, 0], ['cC', 2, self.B], ['cA', 2, self.C]]
                svar_det_one_floor[3] = ['С-СД13', 'Стенка СБ', 2, ['cB', 2, self.C],  ['u', 2, 0], ['cC', 2, self.B], ['cA', 2, self.A]]
                svar_det_one_floor.append(['К-СД16', 'Крышка СБ', 1, ['kc1', 1, self.A], ['kc4', 1, self.B], ['kc1', 1, self.C]])
                for i in [2, 3, 4, 5]:
                    detali[i][1] = 2
            elif self.dat['In'] in [4000, 5000]:
                svar_det_one_floor[2] = ['С-СД13', 'Стенка СБ', 2, ['cB', 2, self.A], ['u', 2, 0], ['cC', 2, self.B], ['cA', 2, self.C]]
                svar_det_one_floor[3] = ['С-СД13', 'Стенка СБ', 2, ['cB', 2, self.C], ['u', 2, 0], ['cC', 2, self.B], ['cA', 2, self.A]]
                svar_det_one_floor.append(['К-СД16', 'Крышка СБ', 1, ['kc1', 1, self.A], ['kc4', 1, self.B], ['kc1', 1, self.C]])
                for i in [2, 3, 4, 5]:
                    detali[i][1] = 2
            elif self.dat['In'] in [6400]:
                svar_det_one_floor[2] = ['С-СД13', 'Стенка СБ', 3, ['cB', 3, self.A],  ['u', 3, 0], ['cC', 3, self.B], ['cA', 3, self.C]]
                svar_det_one_floor[3] = ['С-СД13', 'Стенка СБ', 3, ['cB', 3, self.C],  ['u', 3, 0], ['cC', 3, self.B], ['cA', 3, self.A]]
                svar_det_one_floor.append(['К-СД16', 'Крышка СБ', 3, ['kc1', 3, self.A], ['kc4', 3, self.B], ['kc1', 3, self.C]])
                for i in [2, 3, 4, 5]:
                    detali[i][1] = 3

            '''if self.os[0] == self.os[2] and self.dat['Обозначение'] not in ['згф', 'zgf']:
                svar_det_one_floor.pop(3)           # удаляем первую крышку К-СД4
                svar_det_one_floor[2][1] *= 2       # умножаем на 2 К-СД1
                svar_det_one_floor[2][2][1] *= 2    # умножаем на 2 с3
                svar_det_one_floor[2][3][1] *= 2    # умножаем на 2 с2а
                svar_det_one_floor[2][4][1] *= 2    # умножаем на 2 сВ'''

            if self.dat['Обозначение'] in ['згф', 'zgf']:
                self.spisok_dla_mater['Nflanc'] = self.spisok_dla_mater['Nflanc'] + int(self.dat['количество'])
                itog[0][7] = 'zgf'
                svar_det_one_floor[0][3][0] = 'k2f'
                svar_det_one_floor[1][3][0] = 'k1f'
                svar_det_one_floor[2][3][0] = 'cBf'
                svar_det_one_floor[3][6][0] = 'cAf'
                dictionary = {2: 's27', 3: 's28', 4: 's29', 5: 's30'}
                for i in dictionary:
                    detali[i][0] = dictionary[i]
                detali.append(['fl', 2])

        else:   # 3-х проводной
            svar_det_one_floor = [['К-СД4', 'Крышка СБ', 1, ['k2', 1, self.A], ['k7', 1, self.B], ['k2', 1, self.C]],
                                  ['К-СД5', 'Крышка СБ', 1, ['k1', 1, self.A], ['k8', 1, self.B], ['k1', 1, self.C]],
                                  ['С-СД13', 'Стенка СБ', 1, ['cB', 1, self.A], ['u', 2, 0], ['cC', 1, self.B],
                                   ['cA', 1, self.C]],
                                  ['С-СД13', 'Стенка СБ', 1, ['cB', 1, self.C], ['u', 2, 0], ['cC', 1, self.B],
                                   ['cA', 1, self.A]]]
            detali = [['n', 4], ['sux', 4],
                      ['s13', 1, [self.A, self.B, self.C]],
                      ['s14', 1, [self.A, self.B, self.C]],
                      ['s15', 1, [self.A, self.B, self.C]],
                      ['s16', 1, [self.A, self.B, self.C]]]

        if self.dat['Серия'] in ['CR1', 'CR']:
            print('Нет сварных детлей')
        else:

            for i in svar_det_one_floor:

                itog_svar = self.welded_part(i)
                for j in itog_svar:
                    itog.append(j)

        for j in detali:
            itog_det = self.detail(j, '')
            if itog_det == 0:   # только что расчитывали сухарь, направляющую или фланец
                continue
            else:
                itog.append(itog_det)

        self.prints(itog)
        line_raskroi.komlektuyushie(self.dat, self.length_OS, self.spis_kompl).standart_izdel()
        return True

    def z_v(self):

        self.A = self.os[0]
        self.B = self.os[1]
        self.C = self.os[2]

        self.spisok_dla_mater['dlina'] = round(self.spisok_dla_mater['dlina'] + int(self.dat['количество'])
                                               * (int(self.A) + int(self.B) + int(self.C)) / 1000, 0)
        self.spisok_dla_mater['Nsekc'] = self.spisok_dla_mater['Nsekc'] + int(self.dat['количество'])
        self.spisok_dla_mater['Lsvar_izd'] = round(self.spisok_dla_mater['Lsvar_izd'] + int(self.dat['количество'])
                                                   * (int(self.A) + int(self.B) + int(self.C)) / 1000,0)
        self.spisok_dla_mater['KolProv'] = self.dat['Кол. пров.']

        self.index = self.index + 1
        itog = [[self.index, self.dat['Серия'], self.dat['ip'], self.dat['Материал'], self.dat['In'],
                 self.dat['Кол. пров.'], self.dat['Наименование'], 'zv',
                 self.L, self.L1, self.A, self.B, self.C,
                 self.dat['количество'], 'спецификация']]

        def one(x, y, z):
            detali = [['n', 4], ['sux', 4]]
            svar_det_one_floor = [['К-СД6', 'Крышка СБ', 1, ['k3', 1, x], ['k9', 1, y], ['k4', 1, z]],
                                  ['К-СД6', 'Крышка СБ', 1, ['k3', 1, z], ['k9', 1, y], ['k4', 1, x]],
                                  ['С-СД5', 'Стенка СБ', 1, ['c2', 1, x], ['c7', 1, y], ['c2', 1, z]],
                                  ['С-СД6', 'Стенка СБ', 1, ['c1', 1, x], ['c8', 1, y], ['c1', 1, z]],
                                  ['Ш-СД3', 'Шина СБ', 1, ['s3', 1, x], ['s', 1, y], ['s3', 1, z]],
                                  ['Ш-СД3-З', 'Шина СБ', 1, ['s3', 1, x], ['s', 1, y], ['s3', 1, z]],
                                  ['Ш-СД4', 'Шина СБ', 1, ['s4', 1, x], ['s', 1, y], ['s4', 1, z]],
                                  ['Ш-СД4-З', 'Шина СБ', 1, ['s4', 1, x], ['s', 1, y], ['s4', 1, z]]]

            if self.dat['Обозначение'] in ['звф', 'zvf']:
                self.spisok_dla_mater['Nflanc'] = self.spisok_dla_mater['Nflanc'] + int(self.dat['количество'])
                itog[0][7] = 'zvf'
                detali = [['n', 4], ['sux', 4], ['fl', 2]]
                svar_det_one_floor = [['К-СД6', 'Крышка СБ', 1, ['k3f', 1, x], ['k9', 1, y], ['k4', 1, z]],
                                      ['К-СД6-З', 'Крышка СБ', 1, ['k3', 1, z], ['k9', 1, y], ['k4f', 1, x]],
                                      ['С-СД5', 'Стенка СБ', 1, ['c2f', 1, x], ['c7', 1, y], ['c2', 1, z]],
                                      ['С-СД6', 'Стенка СБ', 1, ['c1f', 1, x], ['c8', 1, y], ['c1', 1, z]],
                                      ['Ш-СД19', 'Шина СБ', 1, ['s37', 1, x], ['s', 1, y], ['s3', 1, z]],
                                      ['Ш-СД20', 'Шина СБ', 1, ['s36', 1, x], ['s', 1, y], ['s3', 1, z]],
                                      ['Ш-СД19-З', 'Шина СБ', 1, ['s37', 1, x], ['s', 1, y], ['s4', 1, z]],
                                      ['Ш-СД20-З', 'Шина СБ', 1, ['s36', 1, x], ['s', 1, y], ['s4', 1, z]]]

            for j in detali:
                itog_det = self.detail(j, '')
                if itog_det == 0:  # только что расчитывали сухарь, направляющую или фланец
                    continue
                else:
                    itog.append(itog_det)

            return svar_det_one_floor

        def one_3(x, y, z):
            detali = [['n', 4], ['sux', 4]]

            for j in detali:
                itog_det = self.detail(j, '')
                if itog_det == 0:  # только что расчитывали сухарь, направляющую или фланец
                    continue
                else:
                    itog.append(itog_det)

            svar_det_one_floor = [['К-СД6', 'Крышка СБ', 1, ['k3', 1, x], ['k9', 1, y], ['k4', 1, z]],
                                  ['К-СД6', 'Крышка СБ', 1, ['k3', 1, z], ['k9', 1, y], ['k4', 1, x]],
                                  ['С-СД5', 'Стенка СБ', 1, ['c2', 1, x], ['c7', 1, y], ['c2', 1, z]],
                                  ['С-СД6', 'Стенка СБ', 1, ['c1', 1, x], ['c8', 1, y], ['c1', 1, z]],
                                  ['Ш-СД3', 'Шина СБ', 1, ['s3', 1, x], ['s', 1, y], ['s3', 1, z]],
                                  ['Ш-СД3-З', 'Шина СБ', 1, ['s3', 1, x], ['s', 1, y], ['s3', 1, z]],
                                  ['Ш-СД30', 'Шина СБ', 1, ['s_3', 1, x], ['s', 1, y], ['s_3', 1, z]]]

            return svar_det_one_floor

        if str(self.dat['Кол. пров.']) in ['4', '3+1']:

            if self.dat['In'] in [630, 800, 1000, 1250, 1600, 2000, 2500]:
                svar_det_one_floor = one(self.A, self.B, self.C)

                for i in svar_det_one_floor:
                    itog_svar = self.welded_part(i)

                    for j in itog_svar:
                        itog.append(j)

            elif self.dat['In'] in [2600, 3200, 4000, 5000]:
                # первый этаж
                x = int(self.os[0]) + self.dat['разница между этажами']
                z = int(self.os[2]) - self.dat['разница между этажами']
                svar_det_one_floor = one(x, self.B, z)

                if self.dat['Обозначение'] in ['звф', 'zvf']:
                    self.spisok_dla_mater['Nflanc'] = self.spisok_dla_mater['Nflanc'] + int(self.dat['количество'])
                    itog[0][7] = 'zvf'
                    svar_det_one_floor[1] = ['К-СД15', 'Крышка СБ', 1, ['kc2f', 1, x], ['kc5', 1, self.B], ['kc2a', 1, z]]
                else:
                    svar_det_one_floor[1] = ['К-СД15', 'Крышка СБ', 1, ['kc2', 1, x], ['kc5', 1, self.B], ['kc2a', 1, z]]

                #   второй этаж
                x = int(self.os[0]) - self.dat['разница между этажами']
                z = int(self.os[2]) + self.dat['разница между этажами']
                svar_det_two_floor = one(x, self.B, z)
                svar_det_two_floor.pop(0)
                svar_det = svar_det_one_floor + svar_det_two_floor

                for i in svar_det:
                    itog_svar = self.welded_part(i)

                    for j in itog_svar:
                        itog.append(j)

            #   elif self.dat['In'] in [6400]:
            else:
                # первый этаж
                x = int(self.os[0]) + self.dat['разница между этажами']
                z = int(self.os[2]) - self.dat['разница между этажами']
                svar_det_one_floor = one(x, self.B, z)

                if self.dat['Обозначение'] in ['звф', 'zvf']:
                    self.spisok_dla_mater['Nflanc'] = self.spisok_dla_mater['Nflanc'] + int(self.dat['количество'])
                    itog[0][7] = 'zvf'
                    svar_det_one_floor[1] = ['К-СД15', 'Крышка СБ', 1, ['kc2f', 1, x], ['kc5', 1, self.B], ['kc2a', 1, z]]
                else:
                    svar_det_one_floor[1] = ['К-СД15', 'Крышка СБ', 1, ['kc2', 1, x], ['kc5', 1, self.B], ['kc2a', 1, z]]

                #   второй этаж
                svar_det_two_floor = one(self.A, self.B, self.C)

                if self.dat['Обозначение'] == 'звф':
                    svar_det_one_floor[1] = ['К-СД15', 'Крышка СБ', 1, ['kc2f', 1, x], ['kc5', 1, self.B], ['kc2a', 1, z]]
                else:
                    svar_det_one_floor[1] = ['К-СД15', 'Крышка СБ', 1, ['kc2', 1, x], ['kc5', 1, self.B], ['kc2a', 1, z]]

                svar_det_two_floor.pop(0)
                #   третий этаж
                x = int(self.os[0]) - self.dat['разница между этажами']
                z = int(self.os[2]) + self.dat['разница между этажами']
                svar_det_three_floor = one(x, self.B, z)
                svar_det_three_floor.pop(0)
                svar_det = svar_det_one_floor + svar_det_two_floor + svar_det_three_floor

                for i in svar_det_one_floor:
                    itog_svar = self.welded_part(i)

                    for j in itog_svar:
                        itog.append(j)
        else:
            x = self.A
            y = self.B
            z = self.C
            svar_det_one_floor = one_3(x, y, z)

            for i in svar_det_one_floor:
                itog_svar = self.welded_part(i)

                for j in itog_svar:
                    itog.append(j)

        self.prints(itog)
        line_raskroi.komlektuyushie(self.dat, self.length_OS, self.spis_kompl).standart_izdel()
        return True

    def k_p(self):

        self.A = self.os[0]
        self.B = self.os[1]
        self.C = self.os[2]

        self.spisok_dla_mater['dlina'] = round(self.spisok_dla_mater['dlina'] + int(self.dat['количество'])
                                               * (int(self.A) + int(self.B) + int(self.C)) / 1000, 0)
        self.spisok_dla_mater['Nsekc'] = self.spisok_dla_mater['Nsekc'] + int(self.dat['количество'])
        self.spisok_dla_mater['Lsvar_izd'] = round(self.spisok_dla_mater['Lsvar_izd'] + int(self.dat['количество'])
                                                   * (int(self.A) + int(self.B) + int(self.C)) / 1000, 0)
        self.spisok_dla_mater['KolProv'] = self.dat['Кол. пров.']

        self.index = self.index + 1

        itog = [[self.index, self.dat['Серия'], self.dat['ip'], self.dat['Материал'], self.dat['In'],
                 self.dat['Кол. пров.'], self.dat['Наименование'], 'kp',
                 self.L, self.L1, self.A, self.B, self.C,
                 self.dat['количество'], 'спецификация']]

        def one(x, y, z):


            if self.dat['Обозначение'] in ['kpfuv']:
                itog[0][7] = 'kpfuv'
                detali = [['n', 2], ['sux', 4], ['fl', 2]]
                svar_det_one_floor = [['К-СД9', 'Крышка СБ', 1, ['k3f', 1, x], ['k13', 1, y], ['k2', 1, z]],
                                      ['К-СД10', 'Крышка СБ', 1, ['k4f', 1, x], ['k16', 1, y], ['k1', 1, z]],
                                      ['С-СД9', 'Стенка СБ', 1, ['c2f', 1, x], ['c1a', 1, y], ['u', 1, 0], ['cB', 1, z]],
                                      ['С-СД10', 'Стенка СБ', 1, ['c1f', 1, x], ['c2a', 1, y], ['u', 1, 0], ['cA', 1, z]],
                                      ['Ш-СД39', 'Шина СБ', 1, ['s36', 1, x], ['s12', 1, [y, z]]],
                                      ['Ш-СД40', 'Шина СБ', 1, ['s36', 1, x], ['s11', 1, [y, z]]],
                                      ['Ш-СД41', 'Шина СБ', 1, ['s37', 1, x], ['s10', 1, [y, z]]],
                                      ['Ш-СД42', 'Шина СБ', 1, ['s37', 1, x], ['s9', 1, [y, z]]]]
            else:
                detali = [['n', 4], ['sux', 4]]
                svar_det_one_floor = [['К-СД9', 'Крышка СБ', 1, ['k3', 1, x], ['k13', 1, y], ['k2', 1, z]],
                                      ['К-СД10', 'Крышка СБ', 1, ['k4', 1, x], ['k16', 1, y], ['k1', 1, z]],
                                      ['С-СД9', 'Стенка СБ', 1, ['c2', 1, x], ['c1a', 1, y], ['u', 1, 0], ['cB', 1, z]],
                                      ['С-СД10', 'Стенка СБ', 1, ['c1', 1, x], ['c2a', 1, y], ['u', 1, 0], ['cA', 1, z]],
                                      ['Ш-СД11', 'Шина СБ', 1, ['s3', 1, x], ['s12', 1, [y, z]]],
                                      ['Ш-СД12', 'Шина СБ', 1, ['s3', 1, x], ['s11', 1, [y, z]]],
                                      ['Ш-СД13', 'Шина СБ', 1, ['s4', 1, x], ['s10', 1, [y, z]]],
                                      ['Ш-СД14', 'Шина СБ', 1, ['s4', 1, x], ['s9', 1, [y, z]]]]

            for j in detali:
                itog_det = self.detail(j, '')

                if itog_det == 0:  # только что расчитывали сухарь, направляющую или фланец
                    continue
                else:
                    itog.append(itog_det)

            return svar_det_one_floor

        def one_3(x, y, z):
            detali = [['n', 4], ['sux', 4]]

            for j in detali:
                itog_det = self.detail(j, '')

                if itog_det == 0:  # только что расчитывали сухарь, направляющую или фланец
                    continue
                else:
                    itog.append(itog_det)

            svar_det_one_floor = [['К-СД9', 'Крышка СБ', 1, ['k3', 1, x], ['k13', 1, y], ['k2', 1, z]],
                                  ['К-СД10', 'Крышка СБ', 1, ['k4', 1, x], ['k16', 1, y], ['k1', 1, z]],
                                  ['С-СД9', 'Стенка СБ', 1, ['c2', 1, x], ['c1a', 1, y], ['u', 1, 0], ['cB', 1, z]],
                                  ['С-СД10', 'Стенка СБ', 1, ['c1', 1, x], ['c2a', 1, y], ['u', 1, 0], ['cA', 1, z]],
                                  ['Ш-СД11', 'Шина СБ', 1, ['s3', 1, x], ['s12', 1, [y, z]]],
                                  ['Ш-СД32', 'Шина СБ', 1, ['s_3', 1, x], ['s38', 1, [y, z]]],  # нужен новый чертеж
                                  ['Ш-СД14', 'Шина СБ', 1, ['s3', 1, x], ['s9', 1, [y, z]]]]
            return svar_det_one_floor

        if str(self.dat['Кол. пров.']) in ['4', '3+1']:

            if self.dat['In'] in [630, 800, 1000, 1250, 1600, 2000, 2500]:
                x = self.os[0]
                y = self.os[1]
                z = self.os[2]
                svar_det_one_floor = one(x, y, z)

                for i in svar_det_one_floor:
                    itog_svar = self.welded_part(i)

                    for j in itog_svar:
                        itog.append(j)

            elif self.dat['In'] in [2600, 3200, 4000, 5000]:
                x = int(self.os[0]) + self.dat['разница между этажами']
                y = int(self.os[1]) + self.dat['разница между этажами']
                z = self.os[2]
                svar_det_one_floor = one(x, y, z)
                svar_det_one_floor[1] = ['К-СД12', 'Крышка СБ', 1, ['kc2', 1, x], ['kc9', 1, y], ['kc1', 1, z]]

                x = int(self.os[0]) - self.dat['разница между этажами']
                y = int(self.os[1]) - self.dat['разница между этажами']
                z = self.os[2]
                svar_det_two_floor = one(x, y, z)
                svar_det_two_floor.pop(0)
                svar_det = svar_det_one_floor + svar_det_two_floor

                for i in svar_det:
                    itog_svar = self.welded_part(i)

                    for j in itog_svar:
                        itog.append(j)

            elif self.dat['In'] in [6400]:
                x = int(self.os[0]) + self.dat['разница между этажами']
                y = int(self.os[1]) + self.dat['разница между этажами']
                z = int(self.os[2])
                svar_det_one_floor = one(x, y, z)
                svar_det_one_floor[1] = ['К-СД12', 'Крышка СБ', 1, ['kc2', 1, x], ['kc9', 1, y], ['kc1', 1, z]]

                x = int(self.os[0])
                y = int(self.os[1])
                z = int(self.os[2])
                svar_det_two_floor = one(x, y, z)
                svar_det_one_floor[1] = ['К-СД12', 'Крышка СБ', 1, ['kc2', 1, x], ['kc9', 1, y], ['kc1', 1, z]]

                x = int(self.os[0]) - self.dat['разница между этажами']
                y = int(self.os[1]) - self.dat['разница между этажами']
                z = int(self.os[2])
                svar_det_two_three = one(x, y, z)
                svar_det_two_three.pop(0)
                svar_det = svar_det_one_floor + svar_det_two_floor + svar_det_two_three

                for i in svar_det_one_floor:
                    itog_svar = self.welded_part(i)

                    for j in itog_svar:
                        itog.append(j)

        # для 3-проводного шинопровода
        else:

            if self.dat['In'] in [630, 800, 1000, 1250, 1600, 2000, 2500]:
                x = self.os[0]
                y = self.os[1]
                z = self.os[2]
                svar_det_one_floor = one_3(x, y, z)

                for i in svar_det_one_floor:
                    itog_svar = self.welded_part(i)

                    for j in itog_svar:
                        itog.append(j)

        self.prints(itog)
        line_raskroi.komlektuyushie(self.dat, self.length_OS, self.spis_kompl).standart_izdel()
        return True

    def k_l(self):

        self.A = self.os[0]
        self.B = self.os[1]
        self.C = self.os[2]

        self.spisok_dla_mater['dlina'] = round(self.spisok_dla_mater['dlina'] + int(self.dat['количество']) * (int(self.A) + int(self.B) + int(self.C)) / 1000, 0)
        self.spisok_dla_mater['Nsekc'] = self.spisok_dla_mater['Nsekc'] + int(self.dat['количество'])
        self.spisok_dla_mater['Lsvar_izd'] = round(self.spisok_dla_mater['Lsvar_izd'] + int(self.dat['количество']) * (int(self.A) + int(self.B) + int(self.C)) / 1000, 0)

        self.index = self.index + 1

        itog = [[self.index, self.dat['Серия'], self.dat['ip'], self.dat['Материал'], self.dat['In'],
                 self.dat['Кол. пров.'], self.dat['Наименование'], 'kl',
                 self.L, self.L1, self.A, self.B, self.C,
                 self.dat['количество'], 'спецификация']]

        def one(x, y, z):

            if self.dat['Обозначение'] in ['klfuv']:
                itog[0][7] = 'klfuv'
                detali = [['n', 2], ['sux', 4], ['fl', 2]]
                svar_det_one_floor = [['К-СД7', 'Крышка СБ', 1, ['k3f', 1, x], ['k14', 1, y], ['k2', 1, z]],
                                      ['К-СД8', 'Крышка СБ', 1, ['k4f', 1, x], ['k15', 1, y], ['k1', 1, z]],
                                      ['С-СД7', 'Стенка СБ', 1, ['c1f', 1, x], ['c2a', 1, y], ['u', 1, 0], ['cB', 1, z]],
                                      ['С-СД8', 'Стенка СБ', 1, ['c2f', 1, x], ['c1a', 1, y], ['u', 1, 0], ['cA', 1, z]],
                                      ['Ш-СД37', 'Шина СБ', 1, ['s36', 1, x], ['s9', 1, [y, z]]],
                                      ['Ш-СД38', 'Шина СБ', 1, ['s37', 1, x], ['s10', 1, [y, z]]],
                                      ['Ш-СД39', 'Шина СБ', 1, ['s37', 1, x], ['s11', 1, [y, z]]],
                                      ['Ш-СД40', 'Шина СБ', 1, ['s36', 1, x], ['s12', 1, [y, z]]]]
            else:
                detali = [['n', 4], ['sux', 4]]
                svar_det_one_floor = [['К-СД7', 'Крышка СБ', 1, ['k3', 1, x], ['k14', 1, y], ['k1', 1, z]],
                                      ['К-СД8', 'Крышка СБ', 1, ['k4', 1, x], ['k15', 1, y], ['k2', 1, z]],
                                      ['С-СД7', 'Стенка СБ', 1, ['c1', 1, x], ['c2a', 1, y], ['u', 1, 0], ['cB', 1, z]],
                                      ['С-СД8', 'Стенка СБ', 1, ['c2', 1, x], ['c1a', 1, y], ['u', 1, 0], ['cA', 1, z]],
                                      ['Ш-СД7', 'Шина СБ', 1, ['s3', 1, x], ['s12', 1, [y, z]]],
                                      ['Ш-СД8', 'Шина СБ', 1, ['s3', 1, x], ['s11', 1, [y, z]]],
                                      ['Ш-СД9', 'Шина СБ', 1, ['s4', 1, x], ['s10', 1, [y, z]]],
                                      ['Ш-СД10', 'Шина СБ', 1, ['s4', 1, x], ['s9', 1, [y, z]]]]
            for j in detali:
                itog_det = self.detail(j, '')
                if itog_det == 0:  # только что расчитывали сухарь, направляющую или фланец
                    continue
                else:
                    itog.append(itog_det)

            return svar_det_one_floor

        def one_3(x, y, z):
            detali = [['n', 4], ['sux', 4]]
            for j in detali:
                itog_det = self.detail(j, '')
                if itog_det == 0:  # только что расчитывали сухарь, направляющую или фланец
                    continue
                else:
                    itog.append(itog_det)
            svar_det_one_floor = [['К-СД7', 'Крышка СБ', 1, ['k3', 1, x], ['k14', 1, y], ['k1', 1, z]],
                                  ['К-СД8', 'Крышка СБ', 1, ['k4', 1, x], ['k15', 1, y], ['k2', 1, z]],
                                  ['С-СД7', 'Стенка СБ', 1, ['c1', 1, x], ['c2a', 1, y], ['u', 1, 0], ['cB', 1, z]],
                                  ['С-СД8', 'Стенка СБ', 1, ['c2', 1, x], ['c1a', 1, y], ['u', 1, 0], ['cA', 1, z]],
                                  ['Ш-СД7', 'Шина СБ', 1, ['s3', 1, x], ['s12', 1, [y, z]]],
                                  ['Ш-СД29', 'Шина СБ', 1, ['s_3', 1, x], ['s38', 1, [y, z]]],
                                  ['Ш-СД10', 'Шина СБ', 1, ['s4', 1, x], ['s9', 1, [y, z]]]]
            return svar_det_one_floor

        if str(self.dat['Кол. пров.']) in ['4', '3+1']:
            if self.dat['In'] in [630, 800, 1000, 1250, 1600, 2000, 2500]:
                x = self.os[0]
                y = self.os[1]
                z = self.os[2]
                svar_det_one_floor = one(x, y, z)
                for i in svar_det_one_floor:
                    itog_svar = self.welded_part(i)
                    for j in itog_svar:
                        itog.append(j)

            elif self.dat['In'] in [2600, 3200, 4000, 5000]:
                x = int(self.os[0]) + self.dat['разница между этажами']
                y = int(self.os[1]) + self.dat['разница между этажами']
                z = self.os[2]
                svar_det_one_floor = one(x, y, z)
                svar_det_one_floor[1] = ['КС-СД11', 'Крышка СБ', 1, ['kc2', 1, x], ['kc8', 1, y], ['kc1', 1, z]]

                x = int(self.os[0]) - self.dat['разница между этажами']
                y = int(self.os[1]) - self.dat['разница между этажами']
                z = self.os[2]
                svar_det_two_floor = one(x, y, z)
                svar_det_two_floor.pop(0)
                svar_det = svar_det_one_floor + svar_det_two_floor
                for i in svar_det:
                    itog_svar = self.welded_part(i)
                    for j in itog_svar:
                        itog.append(j)

            elif self.dat['In'] in [6400]:
                x = int(self.os[0]) + self.dat['разница между этажами']
                y = int(self.os[1]) + self.dat['разница между этажами']
                z = int(self.os[2])
                svar_det_one_floor = one(x, y, z)
                svar_det_one_floor[1] = ['К-СД11', 'Крышка СБ', 1, ['kc2', 1, x], ['kc8', 1, y], ['kc1', 1, z]]

                x = int(self.os[0])
                y = int(self.os[1])
                z = int(self.os[2])
                svar_det_two_floor = one(x, y, z)
                svar_det_one_floor[1] = ['К-СД11', 'Крышка СБ', 1, ['kc2', 1, x], ['kc8', 1, y], ['kc1', 1, z]]

                x = int(self.os[0]) - self.dat['разница между этажами']
                y = int(self.os[1]) - self.dat['разница между этажами']
                z = int(self.os[2])
                svar_det_two_three = one(x, y, z)
                svar_det_two_three.pop(0)
                svar_det = svar_det_one_floor + svar_det_two_floor + svar_det_two_three
                for i in svar_det:
                    itog_svar = self.welded_part(i)
                    for j in itog_svar:
                        itog.append(j)
        else:
            if self.dat['In'] in [630, 800, 1000, 1250, 1600, 2000, 2500]:
                x = self.os[0]
                y = self.os[1]
                z = self.os[2]
                svar_det_one_floor = one_3(x, y, z)
                for i in svar_det_one_floor:
                    itog_svar = self.welded_part(i)
                    for j in itog_svar:
                        itog.append(j)
        self.prints(itog)
        line_raskroi.komlektuyushie(self.dat, self.length_OS, self.spis_kompl).standart_izdel()
        return True

    def nestandart(self):
        print('Ошибка: нестандартная секция')
        self.dat['категория'] = 'спецификация'
        self.dat['стандарт'] = 'нестандарт'
        return False

    def om(self):
        self.L = self.os[0]

        self.spisok_dla_mater['dlina'] = round(self.spisok_dla_mater['dlina'] + int(self.dat['количество']) * int(self.L) / 1000, 0)
        self.spisok_dla_mater['Nsekc'] = self.spisok_dla_mater['Nsekc'] + int(self.dat['количество'])

        print('os', self.os)

        #print('Секция отбора мощности')
        def tipiz(os, calc, nominal):

            if self.tip == []:
                self.dat['Разм.L'] = self.dat['размер']
                calculation.nestandart(self)
                return False

            elif int(self.tip[0]) in [1, 2]:

                if len(os) <= 1:
                    A = int(os[0]) / 2
                else:
                    A = int(os[1])

                L = int(os[0])
                B = '-'
                C = '-'

                if nominal == 2500:

                    if int(self.tip[0]) in [1]:
                        detali = [['k', 1, L], ['k18', 1, L], ['c', 2, L], ['n', 4], ['sux', 4]]
                    else:
                        detali = [['k18', 1, L], ['k18', 1, L], ['c', 2, L], ['n', 4], ['sux', 4]]

                else:

                    if int(self.tip[0]) in [1]:
                        detali = [['kv', 1, L], ['kv18', 1, L], ['c', 2, L], ['n', 4], ['sux', 4]]
                    else:
                        detali = [['kv18', 1, L], ['kv18', 1, L], ['c', 2, L], ['n', 4], ['sux', 4]]

                if int(self.tip[0]) in [1]:
                    svar_det = [['Ш-СД33', 'Шина СБ', 1, ['s1_01', 1, L], ['stp09v', 1, 0],
                                 [float(L - A - calc['расстояние от оси до шины'] - 20 + 98)]],
                                ['Ш-СД34', 'Шина СБ', 1, ['s2_01', 1, L], ['stp09v', 1, 0],
                                 [float(L - A - calc['расстояние от оси до шины'] - 20 - 46)]],
                                ['Ш-СД34', 'Шина СБ', 1, ['s2_01', 1, L], ['stp09v', 1, 0],
                                 [float(A - calc['расстояние от оси до шины'] - 20 - 46)]],
                                ['Ш-СД33', 'Шина СБ', 1, ['s1_01', 1, L], ['stp09v', 1, 0],
                                 [float(A - calc['расстояние от оси до шины'] - 20 + 98)]]]
                else:
                    svar_det = [['Ш-СД33-01', 'Шина СБ', 1, ['s1_01', 1, L], ['stp09v', 2, 0],
                                 [float(L - A - calc['расстояние от оси до шины'] - 20 + 98)]],
                                ['Ш-СД34-01', 'Шина СБ', 1, ['s2_01', 1, L], ['stp09v', 2, 0],
                                 [float(L - A - calc['расстояние от оси до шины'] - 20 - 46)]],
                                ['Ш-СД34-01', 'Шина СБ', 1, ['s2_01', 1, L], ['stp09v', 2, 0],
                                 [float(A - calc['расстояние от оси до шины'] - 20 - 46)]],
                                ['Ш-СД33-01', 'Шина СБ', 1, ['s1_01', 1, L], ['stp09v', 2, 0],
                                 [float(A - calc['расстояние от оси до шины'] - 20 + 98)]]]

                return [detali, svar_det, A, B, C]

            #else:
                #calculation.nestandart(self)
                #return False

            elif int(self.tip[0]) in [3, 4]:

                if len(os[0]) <= 1:

                    if int(os[0]) == 2000:
                        A = 500
                        B = 1000
                    elif int(os[0]) == 2500:
                        A = 750
                        B = 1000
                    else:
                        A = 1000
                        B = 1000

                else:
                    A = int(os[1])
                    B = int(os[2])


                #if int(self.L) in [1000, 1500, 2000, 2500, 3000]:
                L = int(os[0])
                C = '-'

                if nominal == 2500:
                    if int(self.tip[0]) in [3]:
                        detali = [['k', 1, L], ['k18_01', 1, L], ['c', 2, L], ['n', 4], ['sux', 4]]
                    else:
                        detali = [['k18_01', 1, L], ['k18_01', 1, L], ['c', 2, L], ['n', 4], ['sux', 4]]
                else:
                    if int(self.tip[0]) in [3]:
                        detali = [['kv', 1, L], ['kv18_01', 1, L], ['c', 2, L], ['n', 4], ['sux', 4]]
                    else:
                        detali = [['kv18_01', 1, L], ['kv18_01', 1, L], ['c', 2, L], ['n', 4], ['sux', 4]]

                if int(self.tip[0]) in [3]:
                    svar_det = [['Ш-СД33-02', 'Шина СБ', 1, ['s1_01', 1, L], ['stp09v', 2, 0],
                                 [float(L - A - B - calc['расстояние от оси до шины'] - 20 + 98), B]],
                                ['Ш-СД34-02', 'Шина СБ', 1, ['s2_01', 1, L], ['stp09v', 2, 0],
                                 [float(L - A - calc['расстояние от оси до шины'] - 20 - 46 - B), B]],
                                ['Ш-СД34-02', 'Шина СБ', 1, ['s2_01', 1, L], ['stp09v', 2, 0],
                                 [float(A - calc['расстояние от оси до шины'] - 20 - 46), B]],
                                ['Ш-СД33-02', 'Шина СБ', 1, ['s1_01', 1, L], ['stp09v', 2, 0],
                                 [float(A - calc['расстояние от оси до шины'] - 20 + 98), B]]]
                else:
                    svar_det = [['Ш-СД33-03', 'Шина СБ', 1, ['s1_01', 1, L], ['stp09v', 4, 0],
                                 [float(L - A - B - calc['расстояние от оси до шины'] - 20 + 98), B]],
                                ['Ш-СД34-03', 'Шина СБ', 1, ['s2_01', 1, L], ['stp09v', 4, 0],
                                 [float(L - A - calc['расстояние от оси до шины'] - 20 - 46 - B), B]],
                                ['Ш-СД34-03', 'Шина СБ', 1, ['s2_01', 1, L], ['stp09v', 4, 0],
                                 [float(A - calc['расстояние от оси до шины'] - 20 - 46), B]],
                                ['Ш-СД33-03', 'Шина СБ', 1, ['s1_01', 1, L], ['stp09v', 4, 0],
                                 [float(A - calc['расстояние от оси до шины'] - 20 + 98), B]]]

                return [detali, svar_det, A, B, C]

            elif int(self.tip[0]) in [5, 6]:

                if len(os) <= 1:
                    A = 500
                    B = 1000
                    C = 1000
                else:
                    A = int(os[1])
                    B = int(os[2])
                    C = int(os[3])

                if int(self.L) in [3000]:
                    L = int(os[0])

                    if nominal == 2500:

                        if int(self.tip[0]) in [5]:
                            detali = [['k', 1, L], ['k18_02', 1, L], ['c', 2, L], ['n', 4], ['sux', 4]]
                        else:
                            detali = [['k18_02', 1, L], ['k18_02', 1, L], ['c', 2, L], ['n', 4], ['sux', 4]]

                    else:

                        if int(self.tip[0]) in [5]:
                            detali = [['kv', 1, L], ['kv18_02', 1, L], ['c', 2, L], ['n', 4], ['sux', 4]]
                        else:
                            detali = [['kv18_02', 1, L], ['kv18_02', 1, L], ['c', 2, L], ['n', 4], ['sux', 4]]

                    if int(self.tip[0]) in [5]:
                        svar_det = [['Ш-СД33-04', 'Шина СБ', 1, ['s1_01', 1, L], ['stp09v', 3, 0],
                                     [float(L - A - B - C - calc['расстояние от оси до шины'] - 20 + 98), B, C]],
                                    ['Ш-СД34-04', 'Шина СБ', 1, ['s2_01', 1, L], ['stp09v', 3, 0],
                                     [float(L - A - B - C - calc['расстояние от оси до шины'] - 20 - 46), B, C]],
                                    ['Ш-СД34-04', 'Шина СБ', 1, ['s2_01', 1, L], ['stp09v', 3, 0],
                                     [float(A - calc['расстояние от оси до шины'] - 20 - 46), B, C]],
                                    ['Ш-СД33-04', 'Шина СБ', 1, ['s1_01', 1, L], ['stp09v', 3, 0],
                                     [float(A - calc['расстояние от оси до шины'] - 20 + 98), B, C]]]
                    else:
                        svar_det = [['Ш-СД33-05', 'Шина СБ', 1, ['s1_01', 1, L], ['stp09v', 6, 0],
                                     [float(L - A - B - C - calc['расстояние от оси до шины'] - 20 + 98), B, C]],
                                    ['Ш-СД34-05', 'Шина СБ', 1, ['s2_01', 1, L], ['stp09v', 6, 0],
                                     [float(L - A - B - C - calc['расстояние от оси до шины'] - 20 - 46), B, C]],
                                    ['Ш-СД34-05', 'Шина СБ', 1, ['s2_01', 1, L], ['stp09v', 6, 0],
                                     [float(A - calc['расстояние от оси до шины'] - 20 - 46), B, C]],
                                    ['Ш-СД33-05', 'Шина СБ', 1, ['s1_01', 1, L], ['stp09v', 6, 0],
                                     [float(A - calc['расстояние от оси до шины'] - 20 + 98), B, C]]]

                    return [detali, svar_det, A, B, C]

            else:
                calculation.nestandart(self)
                return False

        itogo = tipiz(self.os, self.dat, self.dat['In'])

        if itogo == False:
            return False

        detali = itogo[0]
        svar_detali = itogo[1]

        self.A = itogo[2]
        self.B = itogo[3]
        self.C = itogo[4]
        self.index = self.index + 1

        itog = [[self.index, self.dat['Серия'], self.dat['ip'], self.dat['Материал'], self.dat['In'],
                 self.dat['Кол. пров.'], self.dat['Наименование'],
                 'pr' + self.dat['тип'],
                 self.L, self.L1, self.A, self.B,
                 self.C, self.dat['количество'], 'спецификация']]

        for i in svar_detali:
            itog_svar = self.welded_part(i)

            for j in itog_svar:
                itog.append(j)

        for i in detali:
            itog_det = self.detail(i, 's')

            if itog_det == 0:   # только что расчитывали сухарь, направляющую или фланец
                continue
            else:
                itog.append(itog_det)

        self.prints(itog)
        line_raskroi.komlektuyushie(self.dat, self.length_OS, self.spis_kompl).standart_izdel()
        return True

    def omf(self):    # Не доделано
        self.L = self.dat['размер']

        self.spisok_dla_mater['dlina'] = round(self.spisok_dla_mater['dlina'] + int(self.dat['количество'])
                                               * int(re.findall(r'\d+', self.L)[0]) / 1000, 0)
        self.spisok_dla_mater['Nsekc'] = self.spisok_dla_mater['Nsekc'] + int(self.dat['количество'])
        self.spisok_dla_mater['KolProv'] = self.dat['Кол. пров.']

        #print('Секция отбора мощности с фиксированным выводом')
        def tipiz(os, calc, nominal, tip):

            if int(tip[0]) in [1]:

                if len(re.findall(r'\d+', self.L)) > 1:
                    A = int(re.findall(r'\d+', self.L)[1])
                    B = '-'
                    C = '-'
                elif re.findall(r'\d+', self.L)[0] in [1500, 2000, 2500, 3000]:
                    A = 400
                    B = '-'
                    C = '-'

                else:
                    calculation.nestandart(self)
                    return False

                if nominal == 2500:
                    detali = [['k', 1, os], ['k20', 1, os], ['k21', 1, os], ['c', 2, os], ['n', 4], ['sux', 4]]
                else:
                    detali = [['kv', 1, os], ['kv20', 1, os], ['kv21', 1, os], ['c', 2, os], ['n', 4], ['sux', 4]]

                svar_det = [['Ш-СД35', 'Шина СБ', 1, ['s1', 1, os], ['stp026v', 1, 0], [A]],
                            ['Ш-СД36', 'Шина СБ', 1, ['s2_01', 1, os], ['stp09v', 1, 0], [A]],
                            ['Ш-СД36-З', 'Шина СБ', 1, ['s2_01', 1, os], ['stp09v', 1, 0], [A]],
                            ['Ш-СД35-З', 'Шина СБ', 1, ['s1_01', 1, os], ['stp09v', 1, 0], [A]]]
                return [detali, svar_det, A, B, C]

            elif int(tip[0]) in [3, 4]:

                if len(re.findall(r'\d+', self.L)) > 1:
                    A = int(re.findall(r'\d+', self.L)[1])
                    B = int(re.findall(r'\d+', self.L)[2])
                    C = '-'
                elif len(re.findall(r'\d+', self.L)) == 1:

                    if int(self.L) in [1000, 1500, 2000, 2500, 3000]:
                        C = '-'

                        if int(os) == 2000:
                            A = 500
                            B = 1000
                        elif int(os) == 2500:
                            A = 750
                            B = 1000
                        else:
                            A = 1000
                            B = 1000

                else:
                    calculation.nestandart(self)
                    return False

                if nominal == 2500:
                    if int(tip[0]) in [3]:
                        detali = [['k', 1, os], ['k18_01', 1, os], ['c', 2, os], ['n', 4], ['sux', 4]]
                    else:
                        detali = [['k18_01', 1, os], ['k18_01', 1, os], ['c', 2, os], ['n', 4], ['sux', 4]]
                else:
                    if int(tip[0]) in [3]:
                        detali = [['kv', 1, os], ['kv18_01', 1, os], ['c', 2, os], ['n', 4], ['sux', 4]]
                    else:
                        detali = [['kv18_01', 1, os], ['kv18_01', 1, os], ['c', 2, os], ['n', 4], ['sux', 4]]

                svar_det = [['Ш-СД33', 'Шина СБ', 1, ['s1_01', 1, os], ['stp09v', 1, 0], [float(os - A - B - calc['расстояние от оси до шины'] - 20 + 98), B]],
                            ['Ш-СД34', 'Шина СБ', 1, ['s2_01', 1, os], ['stp09v', 1, 0], [float(os - A - calc['расстояние от оси до шины'] - 20 - 46 - B), B]],
                            ['Ш-СД34', 'Шина СБ', 1, ['s2_01', 1, os], ['stp09v', 1, 0], [float(A - calc['расстояние от оси до шины'] - 20 - 46), B]],
                            ['Ш-СД33', 'Шина СБ', 1, ['s1_01', 1, os], ['stp09v', 1, 0], [float(A - calc['расстояние от оси до шины'] - 20 + 98), B]]]
                return [detali, svar_det, A, B, C]

            else:
                calculation.nestandart(self)
                return False

        itogo = tipiz(int(self.os[0]), self.dat, self.dat['In'], self.tip)
        print(itogo, self.tip)

        if itogo == False:
            return False

        detali = itogo[0]
        svar_detali = itogo[1]

        self.A = itogo[2]
        self.B = itogo[3]
        self.C = itogo[4]
        self.index = self.index + 1

        itog = [[self.index, self.dat['Серия'], self.dat['ip'], self.dat['Материал'], self.dat['In'],
                 self.dat['Кол. пров.'], self.dat['Наименование'],
                 str(self.dat['Обозначение'] + str('.'.join(self.tip))).upper(), self.L, self.L1, self.A, self.B,
                 self.C, self.dat['количество'], 'спецификация']]


        for i in svar_detali:
            itog_svar = self.welded_part(i)

            for j in itog_svar:
                itog.append(j)

        for i in detali:
            itog_det = self.detail(i, 's')
            if itog_det == 0:   # только что расчитывали сухарь, направляющую или фланец
                continue
            else:
                itog.append(itog_det)

        self.prints(itog)
        line_raskroi.komlektuyushie(self.dat, self.length_OS, self.spis_kompl).standart_izdel()
        return False

    def tv(self):  # не закончено

        self.A = x = self.os[0]
        self.B = y = self.os[1]
        self.C = z = self.os[2]

        self.spisok_dla_mater['dlina'] = round(self.spisok_dla_mater['dlina'] + int(self.dat['количество'])
                                               * (int(self.A) + int(self.B) + int(self.C)) / 1000, 0)
        self.spisok_dla_mater['Nsekc'] = self.spisok_dla_mater['Nsekc'] + int(self.dat['количество'])
        self.spisok_dla_mater['Lsvar_izd'] = round(self.spisok_dla_mater['Lsvar_izd'] + int(self.dat['количество'])
                                                   * (int(self.A) + int(self.B) + int(self.C)) / 1000, 0)
        self.spisok_dla_mater['KolProv'] = self.dat['Кол. пров.']

        #print(self.index)
        self.index += 1

        itog = [[self.index, self.dat['Серия'], self.dat['ip'], self.dat['Материал'], self.dat['In'],
                 self.dat['Кол. пров.'], self.dat['Наименование'], 'tv',
                 self.L, self.L1, self.A, self.B, self.C,
                 self.dat['количество'], 'спецификация']]

        if self.dat['In'] in [630, 800, 1000, 1250, 1600, 2000, 2500]:
            detali = [['k', 1, [x, y]], ['n', 8], ['sux', 8]]
            svar_det = [['К-СД3', 'Крышка СБ', 1, ['k4', 1, x], ['k4', 1, z]],
                        ['К-СД3', 'Крышка СБ', 1, ['k4', 1, x], ['k4', 1, z]],
                        ['С-СД11', 'Стенка СБ', 1, ['ct', 1, [x, y]], ['ctz', 1, z]],
                        ['С-СД11', 'Стенка СБ', 1, ['ct', 1, [y, x]], ['ctz', 1, z]],
                        ['Ш-СД15', 'Шина СБ', 1, ['s2t', 1, [x, y]], ['s4t', 1, z]],
                        ['Ш-СД15-З', 'Шина СБ', 1, ['s2t', 1, [y, x]], ['s4t', 1, z]],
                        ['Ш-СД16', 'Шина СБ', 1, ['s1t', 1, [x, y]], ['s3t', 1, z]],
                        ['Ш-СД16-З', 'Шина СБ', 1, ['s1t', 1, [y, x]], ['s3t', 1, z]]]

        elif self.dat['In'] in [2600, 3200, 4000, 5000]:
            detali = [['k', 2, [x, y]], ['n', 8], ['sux', 8]]
            svar_det = [['К-СД3', 'Крышка СБ', 1, ['k4t', 1, x], ['k4t', 1, z]],
                        ['К-СД3', 'Крышка СБ', 1, ['k4t', 1, y], ['k4t', 1, z]],
                        ['С-СД14', 'Стенка СБ', 1, ['ct', 2, [x, y]], ['ctz', 2, z]],
                        ['С-СД14', 'Стенка СБ', 1, ['ct', 2, [y, x]], ['ctz', 2, z]],
                        ['Ш-СД22', 'Шина СБ', 1, ['s2t', 2, [x, y]], ['s4t', 2, z]],
                        ['Ш-СД22-З', 'Шина СБ', 1, ['s2t', 2, [y, x]], ['s4t', 2, z]],
                        ['Ш-СД21', 'Шина СБ', 1, ['s1t', 2, [x, y]], ['s3t', 2, z]],
                        ['Ш-СД21-З', 'Шина СБ', 1, ['s1t', 2, [y, x]], ['s3t', 2, z]]]

        else:   # 6400
            detali = [['k', 1, [x, y]], ['n', 8], ['sux', 8]]
            svar_det = [['К-СД3', 'Крышка СБ', 1, ['k4', 1, x], ['k4', 1, z]],
                        ['С-СД11', 'Стенка СБ', 1, ['ct', 1, [x, y]], ['ctz', 1, z]],
                        ['С-СД11', 'Стенка СБ', 1, ['ct', 1, [y, x]], ['ctz', 1, z]],
                        ['Ш-СД15', 'Шина СБ', 1, ['s2t', 1, [x, y]], ['s4t', 1, z]],
                        ['Ш-СД15-З', 'Шина СБ', 1, ['s2t', 1, [y, x]], ['s4t', 1, z]],
                        ['Ш-СД16', 'Шина СБ', 1, ['s1t', 1, [x, y]], ['s3t', 1, z]],
                        ['Ш-СД16-З', 'Шина СБ', 1, ['s1t', 1, [y, x]], ['s3t', 1, z]]]

        for i in svar_det:
            itog_svar = self.welded_part(i)
            for j in itog_svar:
                itog.append(j)

        for i in detali:
            itog_det = self.detail(i, '')
            if itog_det == 0:   # только что расчитывали сухарь, направляющую или фланец
                continue
            else:
                itog.append(itog_det)

        self.prints(itog)
        line_raskroi.komlektuyushie(self.dat, self.length_OS, self.spis_kompl).standart_izdel()
        return True

    def tg(self):

        '''self.spisok_dla_mater['dlina'] = round(self.spisok_dla_mater['dlina'] + int(self.dat['количество']) * (int(self.A) + int(self.B) + int(self.C)) / 1000, 0)
        self.spisok_dla_mater['Nsekc'] = self.spisok_dla_mater['Nsekc'] + int(self.dat['количество'])
        self.spisok_dla_mater['Lsvar_izd'] = round(self.spisok_dla_mater['Lsvar_izd'] + int(self.dat['количество']) * (int(self.A) + int(self.B) + int(self.C)) / 1000, 0)'''

        self.nestandart()
        return False

    # Секция компенсации
    def sk(self):
        self.A = self.os[0]

        self.spisok_dla_mater['dlina'] = round(self.spisok_dla_mater['dlina'] + int(self.dat['количество'])
                                               * int(self.A) / 1000, 0)
        self.spisok_dla_mater['Nsekc'] = self.spisok_dla_mater['Nsekc'] + int(self.dat['количество'])
        self.spisok_dla_mater['Lsvar_izd'] = round(self.spisok_dla_mater['Lsvar_izd'] + int(self.dat['количество'])
                                                   * int(self.A) / 1000, 0)
        self.spisok_dla_mater['KolProv'] = self.dat['Кол. пров.']
        self.spisok_dla_mater['Nflanc'] = (self.spisok_dla_mater['Nflanc'] + int(self.dat['количество']) *2)

        self.index = self.index + 1

        itog = [[self.index, self.dat['Серия'], self.dat['ip'], self.dat['Материал'], self.dat['In'],
                 self.dat['Кол. пров.'], self.dat['Наименование'], 'sk',
                 self.L, self.L1, self.A, self.B, self.C,
                 self.dat['количество'], 'спецификация']]

        # CR  нестандарт не производим
        if self.dat['Серия'] in ['CR1', 'CR2']:
            self.nestandart()
            self.spisok_dla_mater['Nsekc'] = self.spisok_dla_mater['Nsekc'] + int(self.dat['количество'])

        #E3
        else:

            if str(self.dat['Кол. пров.']) in ['4', '3+1'] and self.dat['In'] < 2600:
                detali = [['n', 4], ['sux', 4], ['c', 4, self.A], ['k', 4, self.A], ['sk_tr', 4, 0],
                          ['A000_125', 1, 0], ['A000_125_01', 1, 0], ['A000_125_02', 1, 0], ['A000_125_03', 1, 0]]
                svar_det = [['000 777', 'Шина средняя Ск', 2, ['A000_120', 4, 0]],
                            ['000 776', 'Шина крайняя Ск', 2, ['A000_119', 4, 0]],
                            ['k_pe', 'Шина PE в сборе', 1, ['A000_128', 2, 0]],
                            ['ksm', 'Кожух СК -01', 1, ['lvn', 2, 0], ['klb', 2, 0]],
                            ['km', 'Каркас кожуха-01', 1, ['ugol2', 2, 0], ['ugol1', 2, 0], ['ugol2_z', 2, 0],
                             ['ugol', 2, 0]],
                            ['kcb', 'Кожух СК-02', 1, ['lvb', 2, 0], ['lbm', 2, 0]],
                            ['kb', 'Каркас кожуха-02', 1, ['ugol2', 2, 0], ['ugol1_2', 2, 0], ['ugol2_z', 2, 0],
                             ['ugol_2', 2, 0]],
                            ['000 124', 'Компенсационная шина СБ', 5, ['A000_108', 5 * 7, 0]]]

                if self.dat['In'] in [2500]:
                    svar_det[7][2][1] = 5 * 9

                for j in detali:
                    itog_det = self.detail(j, '')
                    if itog_det == 0:  # только что расчитывали сухарь, направляющую или фланец
                        continue
                    else:
                        itog.append(itog_det)

                for i in svar_det:
                    itog_svar = self.welded_part(i)
                    for j in itog_svar:
                        itog.append(j)

            # нестандарт. на двух этажные и трех этажные документы не разработаны на три и пять проводнико не разработано
            else:
                self.nestandart()
                self.spisok_dla_mater['Nsekc'] = self.spisok_dla_mater['Nsekc'] + int(self.dat['количество'])

            self.prints(itog)
            line_raskroi.komlektuyushie(self.dat, self.length_OS, self.spis_kompl).standart_izdel()
            return True

    def ts(self):
        print('5. Расчет трансформаторной секции:')

        tip1 = int(self.tip[0])
        tip2 = int(self.tip[1])
        text1 = re.findall(r'[^\s]+', re.sub(r'[()]', ' ', self.dat['размер']))
        #print('text1', text1)
        vivod = int(text1[2])
        #print('vivod', vivod)
        self.A = A = int(re.findall(r'[^-*+]+', text1[1])[0])
        self.B = B = int(re.findall(r'[^-*+]+', text1[1])[1])
        self.C = C = int(re.findall(r'[^-*+]+', text1[1])[2])
        self.L1 = L1 = int(re.findall(r'[^-*+]+', text1[1])[3])
        #print(str('L1=' + str(L1)), str('A=' + str(A)), str('B=' + str(B)), str('C=' + str(C)))

        A1 = C + B + A + L1
        A2 = B + C + L1
        A3 = C + L1
        A4 = L1
        # проверяем длину корпуса, достаточна ли она
        if int(text1[0]) < A1:
            razmer = A1 + 80
            #print('Длина по осии Х изменена на', razmer, 'мм.')
        else:
            razmer = text1[0]

        self.L = razmer
        self.spisok_dla_mater['dlina'] = round(self.spisok_dla_mater['dlina'] + int(self.dat['количество']) * int(self.L) / 1000, 0)
        self.spisok_dla_mater['Nsekc'] = self.spisok_dla_mater['Nsekc'] + int(self.dat['количество'])
        self.spisok_dla_mater['KolProv'] = self.dat['Кол. пров.']

        #print('Длина по X:', razmer, ' Тип:', str(str(tip1) + '.' + str(tip2)))
        os = [razmer, L1, A, B, C, tip1, tip2]

        trans_v = {1: {'A': A1, 'B': A2, 'C': A3, 'N': A4},
                   2: {'A': A1, 'B': A2, 'N': A3, 'C': A4},
                   3: {'A': A1, 'N': A2, 'B': A3, 'C': A4},
                   4: {'N': A1, 'A': A2, 'B': A3, 'C': A4},
                   5: {'C': A1, 'B': A2, 'A': A3, 'N': A4},
                   6: {'C': A1, 'B': A2, 'N': A3, 'A': A4},
                   7: {'C': A1, 'N': A2, 'B': A3, 'A': A4},
                   8: {'N': A1, 'C': A2, 'B': A3, 'A': A4}}

        ctp_v = {1: ['A', 'B', 'C', 'N'],
                 2: ['N', 'A', 'B', 'C'],
                 3: ['C', 'B', 'A', 'N'],
                 4: ['N', 'C', 'B', 'A']}
        detali = [['kv', 1, os], ['k19', 1, os], ['c', 2, os], ['n', 2], ['sux', 4], ['zts', 1], ['A000_774_01', 2, os],
                  ['A000_774_02', 2, os]]
        svar_det = [['Ш-СД25', 'Шина СБ', 1, ['s3', 1, trans_v[tip1][ctp_v[tip2][0]]], ['s33', 1, vivod]],
                    ['Ш-СД26', 'Шина СБ', 1, ['s4', 1, trans_v[tip1][ctp_v[tip2][1]]], ['s33', 1, vivod]],
                    ['Ш-СД27', 'Шина СБ', 1, ['s4', 1, trans_v[tip1][ctp_v[tip2][2]]], ['s33', 1, vivod]],
                    ['Ш-СД28', 'Шина СБ', 1, ['s3', 1, trans_v[tip1][ctp_v[tip2][3]]], ['s33', 1, vivod]]]

        if self.dat['In'] in [2500]:
            detali[0][0] = 'k'
        elif self.dat['In'] in [3200, 4000, 5000]:
            detali = [['kv', 1, os], ['k19', 1, os], ['c', 4, os], ['n', 2], ['sux', 4], ['zts', 1],
                      ['A000_774_01', 2, os], ['A000_774_02', 2, os]]
            svar_det = [['Ш-СД25', 'Шина СБ', 2, ['s3', 2, trans_v[tip1][ctp_v[tip2][0]]], ['s33', 1, vivod], ['s33i', 1, vivod]],
                        ['Ш-СД26', 'Шина СБ', 2, ['s4', 2, trans_v[tip1][ctp_v[tip2][1]]], ['s33', 1, vivod], ['s33i', 1, vivod]],
                        ['Ш-СД27', 'Шина СБ', 2, ['s4', 2, trans_v[tip1][ctp_v[tip2][2]]], ['s33', 1, vivod], ['s33i', 1, vivod]],
                        ['Ш-СД28', 'Шина СБ', 2, ['s3', 2, trans_v[tip1][ctp_v[tip2][3]]], ['s33', 1, vivod], ['s33i', 1, vivod]]]

        self.index = self.index + 1
        itog = [[self.index, self.dat['Серия'], self.dat['ip'], self.dat['Материал'], self.dat['In'],
                 self.dat['Кол. пров.'], self.dat['Наименование'], 'ts',
                 self.L, self.L1, self.A, self.B,
                 self.C, self.dat['количество'], 'спецификация']]

        for i in svar_det:
            itog_svar = self.welded_part(i)

            for j in itog_svar:
                itog.append(j)

        for i in detali:
            itog_det = self.detail(i, 's')

            if itog_det == 0:   # только что расчитывали сухарь, направляющую или фланец
                continue
            else:
                itog.append(itog_det)

        self.prints(itog)
        return True

    def kz(self):
        print('5. Расчет концевой заглушки:')
        self.index = self.index + 1
        self.A = 138
        self.B = 152
        detali = [['lb', 2, self.os], ['lv', 2, self.os], ['lt', 1, self.os]]

        if self.dat['In'] in [630]:
            self.C = 117
        elif self.dat['In'] in [800]:
            self.C = 132
        elif self.dat['In'] in [1000]:
            self.C = 157
        elif self.dat['In'] in [1250]:
            self.C = 187
        elif self.dat['In'] in [1600]:
            self.C = 237
        elif self.dat['In'] in [2000, 2500]:
            self.C = 277
        elif self.dat['In'] in [2600, 3200]:
            self.C = 403
        elif self.dat['In'] in [4000, 5000]:
            self.C = 483
        elif self.dat['In'] in [6400]:
            self.C = '-'

        self.spisok_dla_mater['Nkon_zag'] = self.spisok_dla_mater['Nkon_zag'] + int(self.dat['количество'])
        self.spisok_dla_mater['KolProv'] = self.dat['Кол. пров.']

        itog = [[self.index, self.dat['Серия'], self.dat['ip'], self.dat['Материал'], self.dat['In'],
                 self.dat['Кол. пров.'], self.dat['Наименование'], 'kz',
                 self.L, self.L1, self.A, self.B, self.C,
                 self.dat['количество'], 'спецификация']]

        for i in detali:
            itog_det = self.detail(i, 's')
            if itog_det == 0:  # только что расчитывали сухарь, направляющую или фланец
                continue
            else:
                itog.append(itog_det)
        self.prints(itog)

        line_raskroi.komlektuyushie(self.dat, self.length_OS, self.spis_kompl).standart_izdel()
        return True

    def pn(self):   # Перевод нейтрали
        self.nestandart()
        self.spisok_dla_mater['Nsekc'] = self.spisok_dla_mater['Nsekc'] + int(self.dat['количество'])
        self.spisok_dla_mater['KolProv'] = self.dat['Кол. пров.']

    def bom(self):
        self.nestandart()

    def ks(self):   # Крепежная скоба
        self.nestandart()

    def ksb(self):  # Крышка стыка
        self.nestandart()

    def pp(self):   # Пружинный подвес
        self.nestandart()


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    s = rashet('88 Сбербанк', 'D:/PycharmProjects/materials/пример.xlsx', 'Kama')
    #s = rashet(195, '/home/eva/PycharmProjects/materials/пример.xlsx', 'Solaris')
    #s = rashet(157, 'D:/PycharmProjects/materials/Технопарк доп заказ.xlsx')

    s.zapusk()