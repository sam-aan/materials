# coding^utf8
from detali import Detali
import re
from schet import schetchik
import nominal

class calculation:
    def __init__(self, input_data, floor):
        self.input_data = input_data
        self.spisok_det = []
        self.slovar_detali = {}
        self.slovar_svar_det = {}
        self.detail = Detali
        self.os = []
        self.slovar = {}
        self.kol_os = 0
        self.index = schetchik()
        self.kol_stikov = 0
        self.razmer_rozetki = 0
        self.nominal = 0
        self.slovar_svar_det_one_floor = {}
        self.slovar_svar_det_two_floor = {}
        self.floor_os = []
        self.floor = floor

    def choice(self):
        global ctik
        print('НАЧАЛО РАСЧЕТА СЕКЦИИ: ', self.input_data[0], self.input_data[1], self.input_data[2], self.input_data[3])
        self.nominal = self.input_data[0]   # вычислили номинал
        self.os = re.findall(r'[^xXхХ*+]+', self.input_data[2])  # список размеров по осям
        self.kol_os = len(self.os)  # вычисляем количество осей
        slovar_old = {'К-СД6': 'k3-k9-k4',
                      'К-СД6-З': 'k4-k9-k3',
                      'К-СД15': 'kc2-kc5-kc2a',
                      'С-СД6': 'c1-c8-c1',
                      'С-СД5': 'c2-c7-c2',
                      'Ш-СД3': 's3-s-s3',
                      'Ш-СД4': 's4-s-s4',
                      'К-СД4': 'k2-k7-k2',
                      'К-СД5': 'k1-k8-k1',
                      'К-СД4Ф': 'k2f-k7-k2',
                      'К-СД5Ф': 'k1f-k8-k1',
                      'К-СД16': 'kc1-kc4-kc1',
                      'С-СД4': 'c3-c9-c4',
                      'С-СД4-З': 'c4-c9-c3',
                      'С-СД4Ф': 'c3f-c9-c4',
                      'С-СД4-ЗФ': 'c4f-c9-c3',
                      'К-СД7': 'k3-k14-k1',
                      'К-СД8': 'k4-k15-k2',
                      'К-СД11': 'kc2-kc8-kc1',
                      'С-СД7': 'c1-c14-c3',
                      'С-СД8': 'c2-c15-c4',
                      'Ш-СД10': 's3-s9',
                      'Ш-СД9': 's4-s10',
                      'Ш-СД7': 's3-s12',
                      'Ш-СД8': 's4-s11',
                      'К-СД9': 'k3-k13-k2',
                      'К-СД10': 'k4-k16-k1',
                      'К-СД12': 'kc2-kc9-kc1',
                      'С-СД9': 'c2-c13-c3',
                      'С-СД10': 'c1-c16-c4',
                      'Ш-СД14': 's3-s9',
                      'Ш-СД13': 's4-s10',
                      'Ш-СД11': 's3-s12',
                      'Ш-СД12': 's4-s11',
                      'К-СД2': 'k3-k3',
                      'К-СД3': 'k4-k4',
                      'К-СД13': 'kc2-kc2',
                      'С-СД3': 'c1-c2',
                      'С-СД3-З': 'c2-c1',
                      'Ш-СД1': 's3-s3a',
                      'Ш-СД1-З': 's3a-s3',
                      'Ш-СД2': 's4-s4a',
                      'Ш-СД2-З': 's4a-s4',
                      'К-СД14': 'kc1-kc1',
                      'К-СД1': 'k1-k2',
                      'К-СД1-З': 'k2-k1',
                      'С-СД1': 'c3-c3',
                      'С-СД2': 'c4-c4'
                      }
        slovar_new = {'К-СД15': 'kc2-kc5-kc2', 'КВ-СД6': 'kv3-kv9-kv4_1', 'КВ-СД6-З': 'kv4_1-kv9-kv3',
                      'С-СД5': 'c2-c7-c2', 'С-СД6': 'c1-c8-c1',
                      'Ш-СД3': 's3-s-s3', 'Ш-СД4': 's4-s-s4',
                      'К-СД16': 'kc1-kc4-kc1', 'КВ-СД4': 'kv2-kv7-kv1-1', 'КВ-СД5': 'kv2_1-kv8-kv1',
                      'С-СД4': 'c3-c9-c4', 'С-СД4-З': 'c4-c9-c3',
                      'К-СД11': 'kc2-kc8-kc1', 'КВ-СД7': 'kv3-kv14-kv2_1', 'КВ-СД8': 'kv4_1-kv20-kv2',
                      'С-СД7': 'c3-c14-c1', 'С-СД8': 'c2-c15-c4',
                      'Ш-СД10': 's3-s9',
                      'Ш-СД7': 's3-s12',
                      'Ш-СД8': 's4-s11',
                      'Ш-СД9': 's4-s10',
                      'КВ-СД10': 'kv4_1-kv19-kv1', 'К-СД12': 'kc2-kc9-kc1', 'КВ-СД9': 'kv3-kv13-kv1_1',
                      'С-СД10': 'c1-c16-c4', 'С-СД9': 'c2-c13-c3',
                      'Ш-СД11': 's3-s12',
                      'Ш-СД12': 's4-s11',
                      'Ш-СД13': 's4-s10',
                      'Ш-СД14': 's3-s9',
                      'К-СД13': 'kc2-kc2', 'КВ-СД2': 'kv3-kv3_1', 'КВ-СД3': 'kv4_1-kv4',
                      'С-СД3': 'c1-c2', 'С-СД3-З': 'c2-c1',
                      'Ш-СД1': 's3-s3a', 'Ш-СД1-З': 's3a-s3', 'Ш-СД2': 's4-s4a', 'Ш-СД2-З': 's4a-s 4',
                      'КВ-СД1': 'kv2-kv2_1', 'К-СД14': 'kc1-kc1', 'КВ-СД1-З': 'kv2_1-kv2',
                      'С-СД1': 'c3-c3', 'С-СД2': 'c4-c4'}
        self.slovar = slovar_old
        bukva = re.findall(r'^\w+', self.input_data[1])  # список букв в обозначении детали нас интересует
        if bukva[0] == 'ОМ' or bukva[0] == 'ОМФ':
            self.razmer_rozetki = re.search(r'\((.*?)\)', self.input_data[2]).group(1)  # убираем все что за скобками
            #print('razmer_rozetki=', self.razmer_rozetki)
            self.input_data[2] = re.sub(r'\([^()]*\)', '', self.input_data[2])  # убираем скобки и все что в них вложено
            #print('self.input_data[2]=', self.input_data[2])
        elif bukva[0].lower() == 'сб':
            self.input_data[2] = '1'
            self.floor = '0'

        if self.floor == '2':
            self.two_floor()
        elif self.floor == '0':
            self.SB(int(self.input_data[3]))
        else:
            self.one_floor()
        print('ЗАВЕРШЕНИЕ РАСЧЕТА СЕКЦИИ')

    def xyz(self, floor):
        c = nominal.vvod_znach(self.nominal)
        c = c.calc_nom()
        os = re.findall(r'[^xXхХ*+]+', self.input_data[2])  # список размеров по осям
        if floor[1] == 1:  # Этаж: 1 (первый)
            floor_os = c[2]
        elif floor[1] == 2:  # Этаж: 2 (второй)
            floor_os = c[2] * -1
        else:
            floor_os = 0
        x = 0
        y = 0
        z = 0
        xyz = []
        if len(os) == 1:
            x = int(os[0])
            y = None
            z = None
            xyz = [x]
        elif len(os) == 2:
            if self.input_data[1] == '2ув':
                x = float(os[0]) + floor_os
                y = float(os[1]) + floor_os
                z = None
            else:
                x = float(os[0])
                y = float(os[1])
                z = None
            xyz = [x, y]
        elif len(os) == 3:
            if self.input_data[1] == '2зв':
                x = float(os[0]) + floor_os
                y = float(os[1])
                z = float(os[2]) - floor_os
            elif self.input_data[1] == '2зг':
                x = float(os[0])
                y = float(os[1])
                z = float(os[2])
            else:
                x = float(os[0]) + floor_os
                y = float(os[1]) + floor_os
                z = float(os[2]) + floor_os
            xyz = [x, y, z]
        print('x=', x, 'y=', y, 'z=', z)
        return xyz

    def one_floor(self):
        print('ЗАПУСК РАСЧЕТА ОДНОЭТАЖНОЙ СЕКЦИИ')
        self.floor_os = [1, 0]  # так мы сообщяем что у нас одноэтажная секция и один этаж
        xyz = self.xyz(self.floor_os)
        spisok_nominalov = ['630', '800', '1000', '1250', '1600', '2000', '2500']
        sekciay_one = {'п': 'p', 'уг': 'ug', 'ув': 'uv', 'зг': 'z_g', 'зв': 'z_v', 'кп': 'k_p', 'кл': 'k_l',
                       'ом': 'om', 'омф': 'omf', 'пф': 'fb', 'згф': 'z_g_f'}
        if self.nominal in spisok_nominalov:    # проверям одноэтажка ли это
            section = sekciay_one[self.input_data[1].lower()]  # вычисляем секцию
            choice = getattr(calculation, section)  # запускаем выбранную секцию
            print(choice(self))  # выводим на печать название
            spisok_svar_det = self.slovar_svar_det.keys()  # ДЕЛАЕМ СПИСОК сварных деталей ИЗ СЛОВАРЯ
            self.detail = Detali(0, self.input_data, xyz)
            for i in spisok_svar_det:
                one_symbol = re.findall(r'\w+', i)[0]
                if one_symbol == 'К':
                    self.oboznach = 'Крышка СБ'
                elif one_symbol == 'КВ':
                    self.oboznach = 'Крышка с выступом СБ'
                elif one_symbol == 'С':
                    self.oboznach = 'Стенка СБ'
                elif one_symbol == 'Ш':
                    self.oboznach = 'Шина СБ'
                else:
                    print('Ошибка выбора сборочной детали')
                nomer = self.index.shet1()
                kol = int(self.slovar_svar_det[i]) * int(self.input_data[3])
                f = open('spisok_det.txt', 'a')
                tz = ';'
                print('Сварная деталь: ', self.oboznach + tz + i + tz + str(
                        self.input_data[2]) + ' Кол-во: ' + str(kol))
                if self.oboznach == 'Крышка СБ' or self.oboznach == 'Крышка с выступом СБ': # не пишем в файл номинал,
                    f.write(str(nomer) + ';-;' + self.oboznach + tz + i + tz + str(         # потому что крышка без номинала
                        self.input_data[2]) + ';-;-;-;-;' + str(kol) + '\n')
                    #print('\n', 'Номер: ', nomer, 'Сварная деталь: ', i, ' Кол-во: ', kol, '\n')
                    f.close()
                else:
                    f.write(str(nomer) + tz + str(self.input_data[0]) + tz + self.oboznach + tz + i + tz + str(
                        self.input_data[2]) + ';-;-;-;-;' + str(kol) + '\n')
                    #print('\n', 'Номер: ', nomer, 'Сварная деталь: ', i, ' Кол-во: ', kol, '\n')
                    f.close()
                w = 0
                spisok_det = self.slovar_spisok(i)  # теперь список деталей в "self.spisok_det"
    # Для уголв
                if self.kol_os == 2 and self.spisok_det[0] == self.spisok_det[1] and self.os[0] == self.os[1]:
                    nomer = self.index.shet1()
                    det = getattr(self.detail, self.spisok_det[0])
                    kol = int(kol) * 2
                    self.prints(det, nomer, kol)
    # для Z
                elif self.input_data[1] == 'зв' or self.input_data[1] == 'зг' or self.input_data[1] == 'згф' \
                        or self.input_data[1] == 'звф' or self.input_data[1] == 'згф':
                    if self.spisok_det[0] == self.spisok_det[2] and self.os[0] == self.os[2]:
                        nomer = self.index.shet1()  # присваиваем новый номер
                        det = getattr(self.detail, self.spisok_det[0])  # запускаем модуль в деталях из списка деталей
                        kol_odinak = int(kol) * 2   # вычисляем количество
                        self.prints(det, nomer, kol_odinak)     # выводим на печать
                        nomer = self.index.shet1()  # присваиваем следующий номер
                        detail_sredii = Detali(1, self.input_data, xyz)
                        det = getattr(detail_sredii, self.spisok_det[1])
                        kol_razn = int(kol)
                        self.prints(det, nomer, kol_razn)

                    else:
                        while w < len(self.os):
                            for j in self.os:  # начинаем перебор по осям
                                nomer = self.index.shet1()
                                self.detail = Detali(w, self.input_data, xyz)
                                det = getattr(self.detail, self.spisok_det[w])
                                w = w + 1
                                self.prints(det, nomer, kol)
    # комбинированные
                elif self.input_data[1] == 'кп' or self.input_data[1] == 'кл':
                    nomer = self.index.shet1()  # вертикальный угол
                    self.detail = Detali(0, self.input_data, xyz)
                    det = getattr(self.detail, self.spisok_det[0])
                    self.prints(det, nomer, kol)
                    first_letter = re.findall(r'\D+', self.spisok_det[1])
                    if first_letter[0] == 's':  # считаем одинаковые шины для комбинированных углов
                        # считаем только шины и сразу по Y и по Z
                        nomer = self.index.shet1()  # горизонтальный угол
                        self.detail = Detali(1, self.input_data, xyz)
                        det = getattr(self.detail, self.spisok_det[1])
                        self.prints(det, nomer, kol)

                    else:
                        # считаем корпус для комбинированной секции сначала по Y потом по Z
                        nomer = self.index.shet1()  # горизонтальный угол
                        self.detail = Detali(1, self.input_data, xyz)
                        det = getattr(self.detail, self.spisok_det[1])
                        self.prints(det, nomer, kol)
                        # по Z
                        nomer = self.index.shet1()  # горизонтальный угол
                        self.detail = Detali(2, self.input_data, xyz)
                        det = getattr(self.detail, self.spisok_det[2])
                        self.prints(det, nomer, kol)
                #elif self.input_data[1] == 'тв' or self.input_data[1] == 'кл':
    # все остальное что не попало под требования
                else:
                    while w < len(self.os):
                        for j in self.os:  # начинаем перебор по осям
                            nomer = self.index.shet1()
                            self.detail = Detali(w, self.input_data, xyz)
                            #print(w)
                            det = getattr(self.detail, self.spisok_det[w])
                            w = w + 1
                            self.prints(det, nomer, kol)
            self.detali_()
            '''spisok_det = self.slovar_detali.keys()  # ДЕЛАЕМ СПИСОК сварных деталей ИЗ СЛОВАРЯ
            print('spisok detaley: ', spisok_det)
            for i in spisok_det:
                nomer = self.index.shet1()  # присваеваем порядковый номер
                kol = int(self.slovar_detali[i]) * int(self.input_data[3])
                det = getattr(self.detail, i)
                self.prints(det, nomer, kol)'''
        else:
            print('Ошибка')
            return False
    def two_floor(self):
        print('ЗАПУСК РАСЧЕТА ДВУХЭТАЖНОЙ СЕКЦИИ')
        global spisok_svar_det, xyz
        spisok_nominalov = ['3200', '4000', '5000']
        sekciay = {'2п': 'two_p', '2уг': 'two_ug', '2ув': 'two_uv', '2зг': 'two_z_g', '2зв': 'two_z_v',
                   '2кп': 'two_k_p', '2кл': 'two_k_l',
                   '2ом': 'two_om', '2омф': 'two_omf', '2пф': 'two_f_b', '2пф100': 'two_f_b100'}
        if self.nominal in spisok_nominalov:  # проверям одноэтажка ли это
            section = sekciay[self.input_data[1]]  # вычисляем секцию
            choice = getattr(calculation, section)  # запускаем выбранную секцию
            print(choice(self))
            spisok_os_floor = [[2, 1], [2, 2]]
            # начинаем перебор по списку этажей spisok_os_floor
            for self.floor_os in spisok_os_floor:
                # в зависимости от того какой этаж считаем, выбираем список делатей сварных
                if self.floor_os[1] == 1:
                    spisok_svar_det = self.slovar_svar_det_one_floor.keys()  # ДЕЛАЕМ СПИСОК сварных деталей ИЗ СЛОВАРЯ
                    self.slovar_svar_det = self.slovar_svar_det_one_floor
                    xyz = self.xyz(self.floor_os)
                elif self.floor_os[1] == 2:
                    if self.slovar_svar_det_two_floor == None:
                        xyz = self.xyz(self.floor_os)
                        break
                    else:
                        spisok_svar_det = self.slovar_svar_det_two_floor.keys()  # ДЕЛАЕМ СПИСОК сварных деталей ИЗ СЛОВАРЯ
                        self.slovar_svar_det = self.slovar_svar_det_two_floor
                        xyz = self.xyz(self.floor_os)
                # Сборки
                for i in spisok_svar_det:
                    one_symbol = re.findall(r'\w+', i)[0]
                    if one_symbol == 'К':
                        self.oboznach = 'Крышка СБ'
                    elif one_symbol == 'КВ':
                        self.oboznach = 'Крышка с выступом СБ'
                    elif one_symbol == 'С':
                        self.oboznach = 'Стенка СБ'
                    elif one_symbol == 'Ш':
                        self.oboznach = 'Шина СБ'
                    else:
                        print('Ошибка 0001')
                    nomer = self.index.shet1()
                    kol = int(self.slovar_svar_det[i]) * int(self.input_data[3])
                    f = open('spisok_det.txt', 'a')
                    tz = ';'
                    if self.oboznach == 'Крышка СБ' or self.oboznach == 'Крышка с выступом СБ':
                        f.write(str(nomer) + ';-;' + str(self.oboznach) + tz + i + tz + str(
                            self.input_data[2]) + ';-;-;-;-;' + str(kol) + '\n')
                        print('\n', 'Номер: ', nomer, 'Сварная деталь: ', i, ' Кол-во: ', kol, '\n')
                        f.close()
                    else:
                        f.write(str(nomer) + tz + str(self.input_data[0]) + tz + str(self.oboznach)
                                + tz + i + tz + str(self.input_data[2]) + ';-;-;-;-;' + str(kol) + '\n')
                        print('\n', 'Номер: ', nomer, 'Сварная деталь: ', i, ' Кол-во: ', kol, '\n')
                        f.close()
                    w = 0
                    self.slovar_spisok(i)  # теперь список деталей в "self.spisok_det"
# углы горизонтальные и вертикальные
                    if self.kol_os == 2:
                        print('Расчет двухэтажного угла')
                        if self.spisok_det[0] == self.spisok_det[1] and self.os[0] == self.os[1]:
                            nomer = self.index.shet1()
                            self.detail = Detali(0, self.input_data, xyz)
                            det = getattr(self.detail, self.spisok_det[0])
                            kol = int(kol) * 2
                            self.prints(det, nomer, kol)
                        else:
                            while w < self.kol_os:  # изначально w=0 пока количество осей больше 'w'
                                for j in xyz:  # начинаем перебор по осям
                                    nomer = self.index.shet1()
                                    self.detail = Detali(w, self.input_data, xyz)
                                    det = getattr(self.detail, self.spisok_det[w])
                                    w = w + 1
                                    self.prints(det, nomer, kol)
# комбинированные углы
                    elif self.input_data[1] == '2кп' or self.input_data[1] == '2кл':
                        nomer = self.index.shet1()  # вертикальный угол
                        self.detail = Detali(0, self.input_data, xyz)
                        det = getattr(self.detail, self.spisok_det[0])
                        self.prints(det, nomer, kol)
                        first_letter = re.findall(r'\D+', self.spisok_det[1])
                        if first_letter[0] == 's':
                            # считаем только шины и сразу по Y и по Z
                            nomer = self.index.shet1()  # горизонтальный угол
                            self.detail = Detali(1, self.input_data, xyz)
                            det = getattr(self.detail, self.spisok_det[1])
                            self.prints(det, nomer, kol)
                        else:
                            # считаем корпус для комбинированной секции сначала по Y потом по Z
                            nomer = self.index.shet1()  # горизонтальный угол
                            self.detail = Detali(1, self.input_data, xyz)
                            det = getattr(self.detail, self.spisok_det[1])
                            self.prints(det, nomer, kol)
                            # по Z
                            nomer = self.index.shet1()  # горизонтальный угол
                            self.detail = Detali(2, self.input_data, xyz)
                            det = getattr(self.detail, self.spisok_det[2])
                            self.prints(det, nomer, kol)
# Z-образные углы
                    # для одинаковых осей X и Z
                    elif self.kol_os == 3:
                        if all([(self.input_data[1] == '2зв' or '2зг'), (self.kol_os == 3),
                                (self.spisok_det[0] == self.spisok_det[2]), (xyz[0] == xyz[2])]):
                            nomer = self.index.shet1()
                            self.detail = Detali(0, self.input_data, xyz)
                            det = getattr(self.detail, self.spisok_det[0])
                            kol = int(kol) * 2
                            self.prints(det, nomer, kol)
                            self.detail = Detali(1, self.input_data, xyz)
                            det = getattr(self.detail, self.spisok_det[1])
                            kol = int(self.slovar_svar_det[i]) * int(self.input_data[3])
                            self.prints(det, nomer, kol)
                    # для разных осей X и Z
                        else:
                            while w < self.kol_os:
                                for j in xyz:  # начинаем перебор по осям
                                    nomer = self.index.shet1()
                                    self.detail = Detali(w, self.input_data, xyz)
                                    det = getattr(self.detail, self.spisok_det[w])
                                    w = w + 1
                                    self.prints(det, nomer, kol)
                self.detali_()
        else:
            print('Ошибка 002')
            return False
    def detali_(self):
        # детали
        print(' РАСЧЕТ ДЕТАЛЕЙ', self.slovar_detali.keys())
        spisok_det = self.slovar_detali.keys()  # ДЕЛАЕМ СПИСОК сварных деталей ИЗ СЛОВАРЯ
        for i in spisok_det:
            if i == 'n':
                s = open('счетчик1.txt', 'a')
                s.write(str(self.slovar_detali[i] * int(self.input_data[3])) + '\n')
                s.close()
            elif i == 'sux':
                s = open('счетчик2.txt', 'a')
                s.write(str(self.slovar_detali[i] * int(self.input_data[3])) + '\n')
                s.close()
            else:
                nomer = self.index.shet1()
                kol = int(self.slovar_detali[i]) * int(self.input_data[3])
                det = getattr(self.detail, i)
                self.prints(det, nomer, kol)
# Вывод на печать
    def prints(self, det, nomer, kol):
        f = open('spisok_det.txt', 'a')
        tz = ';'
        f.write(str(nomer) + tz + str(';'.join(det())) + tz + str(kol) + '\n')
        print('Деталь: ', ';'.join(det()), ' Кол-во: ', kol)
        f.close()

    def SB(self, kol):
        kol_vtulka = nominal.vvod_znach(self.nominal).calc_nom()[7]
        spis = {'ss': 2, 'tp': 8, 'vtulka': kol_vtulka}
        for i in spis.keys():
            #print('i=', i)
            self.detail = Detali(0, self.input_data, [100, 100, 100])
            kol_i = kol * spis[i]
            nomer = self.index.shet1()  # присваеваем порядковый номер
            det = getattr(self.detail, i)
            self.prints(det, nomer, kol_i)

    def p(self):
        if self.nominal == 2500:
            self.slovar_detali = {'n': 4, 'sux': 4, 'k': 2, 'c': 2, 's1': 2, 's2': 2}
            self.kol_stikov = 1
        else:
            self.slovar_detali = {'n': 4, 'sux': 4, 'kv': 2, 'c': 2, 's1': 2, 's2': 2}
            self.kol_stikov = 1

    def fb(self):
        if int(self.input_data[0]) < 2000:
            self.slovar_detali = {'kva': 2, 'ca': 2, 's17': 2, 's18': 2, 'n': 2, 'sux': 4}
        else:
            self.slovar_detali = {'n': 2, 'sux': 4, 'kva': 2, 'ca': 2, 's17': 2, 's18': 2}
        self.kol_stikov = 1

    def ug(self):
        if self.os[0] == self.os[1]:
            self.slovar_svar_det = {'К-СД1': 2, 'С-СД1': 1, 'С-СД2': 1}
        else:
            self.slovar_svar_det = {'К-СД1': 1, 'К-СД1-З': 1, 'С-СД1': 1, 'С-СД2': 1}

        self.slovar_detali = {'n': 4, 'sux': 4, 's5': 1, 's6': 1, 's7': 1, 's8': 1}
        self.kol_stikov = 1

    def uv(self):
        if self.os[0] == self.os[1]:
            self.slovar_svar_det = {'К-СД2': 1, 'К-СД3': 1, 'С-СД3': 2, 'Ш-СД1': 2, 'Ш-СД2': 2}
        else:
            self.slovar_svar_det = {'К-СД2': 1, 'К-СД3': 1, 'С-СД3': 1, 'С-СД3-З': 1, 'Ш-СД1': 1, 'Ш-СД2': 1,
                                    'Ш-СД1-З': 1, 'Ш-СД2-З': 1}
        self.slovar_detali = {'n': 4, 'sux': 4}
        self.kol_stikov = 1

    def z_g(self):
        if self.os[0] == self.os[2]:
            self.slovar_svar_det = {'К-СД4': 1, 'К-СД5': 1, 'С-СД4': 2}
        else:
            self.slovar_svar_det = {'К-СД4': 1, 'К-СД5': 1, 'С-СД4': 1, 'С-СД4-З': 1}
        self.slovar_detali = {'s13': 1, 's14': 1, 's15': 1, 's16': 1, 'n': 4, 'sux': 4}
        self.kol_stikov = 1

    def z_g_f(self):
        if self.os[0] == self.os[2]:
            self.slovar_svar_det = {'К-СД4Ф': 1, 'К-СД5Ф': 1, 'С-СД4Ф': 2}
        else:
            self.slovar_svar_det = {'К-СД4Ф': 1, 'К-СД5Ф': 1, 'С-СД4Ф': 1, 'С-СД4-ЗФ': 1}
        self.slovar_detali = {'s27': 1, 's28': 1, 's29': 1, 's30': 1, 'n': 4, 'sux': 4}
        self.kol_stikov = 1

    def z_v(self):
        if self.os[0] == self.os[2]:
            self.slovar_svar_det = {'К-СД6': 2, 'С-СД5': 1, 'С-СД6': 1, 'Ш-СД3': 2, 'Ш-СД4': 2}
        else:
            self.slovar_svar_det = {'К-СД6': 1, 'К-СД6-З': 1, 'С-СД5': 1, 'С-СД6': 1, 'Ш-СД3': 2, 'Ш-СД4': 2}
        self.slovar_detali = {'n': 4, 'sux': 4}
        self.kol_stikov = 1

    def k_p(self):
        self.slovar_svar_det = {'К-СД9': 1, 'К-СД10': 1, 'С-СД9': 1, 'С-СД10': 1, 'Ш-СД11': 1, 'Ш-СД12': 1,
                                'Ш-СД13': 1, 'Ш-СД14': 1}
        self.slovar_detali = {'n': 4, 'sux': 4}
        self.kol_stikov = 1

    def k_l(self):
        self.slovar_svar_det = {'К-СД7': 1, 'К-СД8': 1, 'С-СД7': 1, 'С-СД8': 1, 'Ш-СД7': 1, 'Ш-СД8': 1, 'Ш-СД9': 1,
                                'Ш-СД10': 1}
        self.slovar_detali = {'n': 4, 'sux': 4}
        self.kol_stikov = 1

    def om(self):
        self.slovar_detali = {'n': 4, 'sux': 4, 'k': 1, 'k19': 1, 'c': 2, 's1': 2, 's2': 2}
        self.kol_stikov = 1

    def omf(self):
        self.slovar_detali = {'n': 4, 'sux': 4, 'k': 2, 'c': 2, 's1': 2, 's2': 2}
        self.kol_stikov = 1


    def slovar_spisok(self, nazv_svar_det):  # выбор из словаря нужный список деталей
        value = self.slovar[nazv_svar_det]  # "value" - это перечень деталей в сварной детали "a"  выбранный из списка
        self.spisok_det = re.findall(r'[^-]+', value)  # разбираем перечень "value" на список  "self.slovar_spisok"


    def two_p(self):
        self.slovar_detali = {'n': 4, 'sux': 4, 'k': 2, 'c': 4, 's1': 4, 's2': 4, 'kc': 1}
        self.kol_stikov = 1

    def two_om(self):
        self.slovar_detali = {'n': 4, 'sux': 4, 'k': 2, 'c': 4, 's1': 4, 's2': 4, 'kc': 1}
        self.kol_stikov = 1

    def two_omf(self):
        self.slovar_detali = {'n': 4, 'sux': 4, 'k': 2, 'c': 4, 's1': 4, 's2': 4, 'kc': 1}
        self.kol_stikov = 1


    def two_ug(self):
        if self.os[0] == self.os[1]:
            print('Равнополчная секция')
            self.slovar_svar_det_one_floor = {'К-СД1': 2, 'С-СД1': 2, 'С-СД2': 2, 'К-СД14': 1}
            self.slovar_svar_det_two_floor = None
        else:
            print('Разнополчная секция')
            self.slovar_svar_det_one_floor = {'К-СД1': 1, 'К-СД1-З': 1, 'С-СД1': 2, 'С-СД2': 2, 'К-СД14': 1}
            self.slovar_svar_det_two_floor = None
        self.slovar_detali = {'n': 4, 'sux': 4, 's5': 2, 's6': 2, 's7': 2, 's8': 2}
        self.kol_stikov = 1

    def two_uv(self):
        if self.os[0] == self.os[1]:
            self.slovar_svar_det_one_floor = {'К-СД2': 1, 'К-СД13': 1, 'С-СД3': 2, 'Ш-СД1': 2, 'Ш-СД2': 2}
            self.slovar_svar_det_two_floor = {'К-СД3': 1, 'С-СД3': 2, 'Ш-СД1': 2, 'Ш-СД2': 2}
        else:
            self.slovar_svar_det_one_floor = {'К-СД2': 1, 'К-СД13': 1, 'С-СД3': 1, 'С-СД3-З': 1, 'Ш-СД1': 1,
                                              'Ш-СД2': 1, 'Ш-СД1-З': 1, 'Ш-СД2-З': 1}
            self.slovar_svar_det_two_floor = {'К-СД3': 1, 'С-СД3': 1, 'С-СД3-З': 1, 'Ш-СД1': 1, 'Ш-СД2': 1,
                                              'Ш-СД1-З': 1, 'Ш-СД2-З': 1}
        self.slovar_detali = {'n': 4, 'sux': 4}
        self.kol_stikov = 1

    def two_z_g(self):
        if self.os[0] == self.os[2]:
            self.slovar_svar_det_one_floor = {'К-СД4': 1, 'К-СД5': 1, 'К-СД16': 1, 'С-СД4': 4}
            self.slovar_svar_det_two_floor = None
        else:
            self.slovar_svar_det_one_floor = {'К-СД4': 1, 'К-СД5': 1, 'К-СД16': 1, 'С-СД4': 2, 'С-СД4-З': 2}
            self.slovar_svar_det_two_floor = None
        self.slovar_detali = {'n': 4, 'sux': 4, 's13': 2, 's14': 2, 's15': 2, 's16': 2}
        self.kol_stikov = 1

    def two_z_v(self):
        if self.os[0] == self.os[2]:
            self.slovar_svar_det_one_floor = {'К-СД6': 1, 'К-СД15': 1, 'С-СД5': 1, 'С-СД6': 1, 'Ш-СД3': 2, 'Ш-СД4': 2}
            self.slovar_svar_det_two_floor = {'К-СД6-З': 1, 'С-СД5': 1, 'С-СД6': 1, 'Ш-СД3': 2, 'Ш-СД4': 2}
        else:
            self.slovar_svar_det_one_floor = {'К-СД6': 1, 'К-СД15': 1, 'С-СД5': 1, 'С-СД6': 1, 'Ш-СД3': 2, 'Ш-СД4': 2}
            self.slovar_svar_det_two_floor = {'К-СД6-З': 1, 'С-СД5': 1, 'С-СД6': 1, 'Ш-СД3': 2, 'Ш-СД4': 2}
        self.slovar_detali = {'n': 4, 'sux': 4}
        self.kol_stikov = 1

    def two_k_p(self):
        self.slovar_svar_det_one_floor = {'К-СД8': 1, 'К-СД10': 1, 'С-СД8': 1, 'С-СД9': 1, 'Ш-СД11': 1, 'Ш-СД12': 1, 'Ш-СД13': 1, 'Ш-СД14': 1}
        self.slovar_svar_det_two_floor = {'К-СД9': 1, 'С-СД8': 1, 'С-СД9': 1, 'Ш-СД11': 1, 'Ш-СД12': 1, 'Ш-СД13': 1, 'Ш-СД14': 1}
        self.slovar_detali = {'n': 4, 'sux': 4}
        self.kol_stikov = 1

    def two_k_l(self):
        self.slovar_svar_det_one_floor = {'К-СД6': 1, 'К-СД11': 1, 'С-СД6': 1, 'С-СД7': 1, 'Ш-СД7': 1, 'Ш-СД8': 1, 'Ш-СД9': 1, 'Ш-СД10': 1}
        self.slovar_svar_det_two_floor = {'К-СД7': 1, 'С-СД6': 1, 'С-СД7': 1, 'Ш-СД7': 1, 'Ш-СД8': 1,
                                          'Ш-СД9': 1, 'Ш-СД10': 1}
        self.slovar_detali = {'n': 4, 'sux': 4}
        self.kol_stikov = 1

    def two_f_b(self):
        print('Прямая секция с фланцем')
        self.slovar_detali = {'n': 4, 'sux': 4, 'kva': 2, 'ca': 4, 's17a': 4, 's18a': 4, 'kca': 1}
        self.kol_stikov = 1

    def two_f_b100(self):
        print('Прямая секция с фланцем')
        self.slovar_detali = {'n': 4, 'sux': 4, 'kva': 2, 'ca': 4, 's17': 4, 's18': 4, 'kca': 1}
        self.kol_stikov = 1
