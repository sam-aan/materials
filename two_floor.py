# coding^utf8
from detali import Detali
import re
from schet import schetchik

class calculation:
    def __init__(self, input_data):
        self.input_data = input_data
        self.spisok_det = []
        self.slovar_detali = {}
        self.slovar_svar_det = {}
        self.detail = Detali
        self.os = []
        self.kol_os = 0
        self.index = schetchik()
        self.slovar_svar_det_one_floor = {}
        self.slovar_svar_det_two_floor = {}
        self.os_floor = 0

    def choice(self):
        slovar_old = {'К-СД1': 'k1-k2',
                      'К-СД1-З': 'k2-k1',
                      'К-СД2': 'k3-k3',
                      'К-СД3': 'k4-k4',
                      'К-СД4': 'k2-k7-k2',
                      'К-СД5': 'k1-k8-k1',
                      'К-СД6': 'k3-k9-k4',
                      'К-СД6-З': 'k4-k9-k3',
                      'К-СД7': 'k3-k14-k1',
                      'К-СД8': 'k4-k15-k2',
                      'К-СД9': 'k3-k13-k2',
                      'К-СД10': 'k4-k16-k1',
                      'С-СД1': 'c3-c3',
                      'С-СД2': 'c4-c4',
                      'С-СД3': 'c1-c2',
                      'С-СД3-З': 'c2-c1',
                      'С-СД4': 'c3-c9-c4',
                      'С-СД4-З': 'c4-c9-c3',
                      'С-СД5': 'c2-c7-c2',
                      'С-СД6': 'c1-c8-c1',
                      'С-СД7': 'c1-c14-c3',
                      'С-СД8': 'c2-c15-c4',
                      'С-СД9': 'c2-c13-c3',
                      'С-СД10': 'c1-c16-c4',
                      'К-СД11': 'kc2-kc8-kc1',
                      'К-СД12': 'kc2-kc9-kc1',
                      'К-СД13': 'kc2-kc2',
                      'К-СД14': 'kc1-kc1',
                      'К-СД15': 'kc2-kc5-kc2a',
                      'К-СД16': 'kc1-kc4-kc1',
                      'Ш-СД1': 's3-s3a',
                      'Ш-СД1-З': 's3a-s3',
                      'Ш-СД2': 's4-s4a',
                      'Ш-СД2-З': 's4a-s4',
                      'Ш-СД3': 's3-s-s3',
                      'Ш-СД4': 's4-s-s4',
                      'Ш-СД7': 's3-s12',
                      'Ш-СД8': 's4-s11',
                      'Ш-СД9': 's4-s10',
                      'Ш-СД10': 's3-s9',
                      'Ш-СД11': 's3-s12',
                      'Ш-СД12': 's4-s11',
                      'Ш-СД13': 's4-s10',
                      'Ш-СД14': 's3-s9'}
        slovar_new = {'К-СД15': 'kc2-kc5-kc2', 'КВ-СД6': 'kv3-kv9-kv4_1', 'КВ-СД6-З': 'kv4_1-kv9-kv3',
                      'С-СД5': 'c2-c7-c2', 'С-СД6': 'c1-c8-c1', 'Ш-СД3': 's3-s-s3', 'Ш-СД4': 's4-s-s4',
                      'К-СД16': 'kc1-kc4-kc1', 'КВ-СД4': 'kv2-kv7-kv1-1',
                      'КВ-СД5': 'kv2_1-kv8-kv1', 'С-СД4': 'c3-c9-c4', 'С-СД4-З': 'c4-c9-c3',
                      'К-СД11': 'kc2-kc8-kc1', 'КВ-СД7': 'kv3-kv14-kv2.1', 'КВ-СД8': 'kv4_1-kv20-kv2',
                      'С-СД7': 'c3-c14-c1', 'С-СД8': 'c2-c15-c4', 'Ш-СД10': 's3-s9', 'Ш-СД7': 's3-s12',
                      'Ш-СД8': 's4-s11', 'Ш-СД9': 's4-s10', 'КВ-СД10': 'kv4_1-kv19-kv1', 'К-СД12': 'kc2-kc9-kc1',
                      'КВ-СД9': 'kv3-kv13-kv1_1', 'С-СД10': 'c1-c16-c4', 'С-СД9': 'c2-c13-c3', 'Ш-СД11': 's3-s12',
                      'Ш-СД12': 's4-s11', 'Ш-СД13': 's4-s10', 'Ш-СД14': 's3-s9', 'К-СД13': 'kc2-kc2',
                      'КВ-СД2': 'kv3-kv3_1', 'КВ-СД3': 'kv4_1-kv4', 'С-СД3': 'c1-c2', 'С-СД3-З': 'c2-c1',
                      'Ш-СД1': 's3-s3a', 'Ш-СД1-З': 's3a-s3', 'Ш-СД2': 's4-s4a', 'Ш-СД2-З': 's4-s4',
                      'КВ-СД1': 'kv2-kv2_1', 'К-СД14': 'kc1-kc1', 'КВ-СД1-З': 'kv2_1-kv2', 'С-СД1': 'c3-c3',
                      'С-СД2': 'c4-c4'}
        self.slovar = slovar_old
        f = open('spisok_det.txt', 'a')
        tz = ';'
        nov_str = '\n'
        self.os = re.findall(r'[^xXхХ*+]+', self.input_data[2])  # список размеров по осям
        nominal = self.input_data[0]    # вычислили номинал
        rated_current = vvod_znach(nominal)
        spisok_nominalov_two_floor = ['3200', '4000', '5000']
        sekciay_two_floor = {'2П': 'p', '2УГ': 'ug', '2УВ': 'uv', '2Z-Г': 'z_g', '2Z-В': 'z_v', '2К-П': 'k_p', '2К-Л': 'k_l',
                   '2ОМ': 'om2', '2ОМФ': 'omf2', '2ПФ': 'f_b', '2ПФ100': 'f_b100'}
        os_p = self.os  #Для прямой!
        if nominal in spisok_nominalov_two_floor:             #проверям одноэтажка ли это
            section = sekciay_two_floor[self.input_data[1]]   # вычисляем секцию
            #print(section)
            choice = getattr(calculation, section) # запускаем выбранную секцию
            print(choice(self))
# вычисление параметров осей
            one_floor = rated_current.calc_nom()[2]
            two_floor = rated_current.calc_nom()[2] * -1
            spisok_os_floor = [one_floor, two_floor]
#начинаем перебор по списку этажей spisok_os_floor
            for floor_os in spisok_os_floor:
                if len(self.os) == 1:
                    A = float(self.os[0])
                    B = 0
                    C = 0
                    self.kol_os = 1
                    print('Количество осей в секции ', self.kol_os)
                    self.os_floor = [A]

                elif len(self.os) == 2:
                    if self.input_data[1] == '2УВ':
                        A = float(self.os[0]) + floor_os
                        B = float(self.os[1]) + floor_os
                        C = 0
                        print(A, B, C)
                    elif self.input_data[1] == '2УГ':
                        A = float(self.os[0])
                        B = float(self.os[1])
                        C = 0
                    else:
                        print('что то пошло нетак ...', self.input_data[1])
                    self.kol_os = 2
                    print('Количество осей в секции ', self.kol_os)
                    self.os_floor = [A, B]

                elif len(self.os) == 3:
                    if self.input_data[1] == '2Z-В':
                        A = float(self.os[0]) + floor_os
                        print(A)
                        B = float(self.os[1])
                        print(B)
                        C = float(self.os[2]) - floor_os
                        print(C)
                    elif self.input_data[1] == '2Z-Г':
                        A = float(self.os[0])
                        B = float(self.os[1])
                        C = float(self.os[2])
                    else:
                        A = float(self.os[0]) + floor_os
                        B = float(self.os[1]) + floor_os
                        C = float(self.os[2]) + floor_os
                    self.kol_os = 3
                    print('Количество осей в секции ', self.kol_os)
                    self.os_floor = [A, B, C]
                else:
                    print("Ошибка: не указаны оси, или их больше трех")
# в зависимости от того какой этаж считаем, выбираем список делатей сварных
                if floor_os == one_floor:
                    spisok_svar_det = self.slovar_svar_det_one_floor.keys()  # ДЕЛАЕМ СПИСОК сварных деталей ИЗ СЛОВАРЯ
                    self.slovar_svar_det = self.slovar_svar_det_one_floor
                    print(spisok_svar_det)
                elif floor_os == two_floor:
                    if self.slovar_svar_det_two_floor == None:
                        break
                    else:
                        spisok_svar_det = self.slovar_svar_det_two_floor.keys()  # ДЕЛАЕМ СПИСОК сварных деталей ИЗ СЛОВАРЯ
                        self.slovar_svar_det = self.slovar_svar_det_two_floor
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
                        print('Ошибка 1000')
                    print(i)
                    nomer = self.index.shet1()
                    kol = int(self.slovar_svar_det[i]) * int(self.input_data[3])
                    if self.oboznach == 'Крышка СБ' or self.oboznach == 'Крышка с выступом СБ':
                        f.write(str(nomer) + ';-;' + str(self.oboznach) + tz + i + tz + str(
                            self.input_data[2]) + ';-;-;-;-;' + str(kol) + nov_str)
                        print('\n', 'Номер: ', nomer, 'Сварная деталь: ', i, ' Кол-во: ', kol, '\n')
                    else:
                        f.write(str(nomer) + tz + str(self.input_data[0]) + tz + str(self.oboznach)
                                + tz + i + tz + str(self.input_data[2]) + ';-;-;-;-;' + str(kol) + nov_str)
                        print('\n', 'Номер: ', nomer, 'Сварная деталь: ', i, ' Кол-во: ', kol, '\n')
                    w = 0
                    self.slovar_spisok(i) # теперь список деталей в "self.spisok_det"
# углы горизонтальные и вертикальные
                    if self.kol_os == 2:
                        print('Расчет двухэтажного угла')
                        if self.spisok_det[0] == self.spisok_det[1] and self.os_floor[0] == self.os_floor[1]:
                            nomer = self.index.shet1()
                            self.detail = Detali(self.os[0], self.H, self.H_stenka, A, B, C, self.input_data[0],
                                                 self.L2_sh, self.L1_sh, self.S_sh, self.H_paketa)
                            det = getattr(self.detail, self.spisok_det[0])
                            kol = int(kol) * 2

                            f.write(str(nomer) + tz + str(';'.join(det())) + tz + str(kol) + nov_str)
                            print('Номер: ', nomer, 'Детали: ', ';'.join(det()), ' Кол-во: ', kol)

                        else:
                            while w < len(self.os_floor):   #  изначально w=0 пока количество осей больше 'w'
                                for j in self.os_floor:   #начинаем перебор по осям
                                    nomer = self.index.shet1()
                                    self.detail = Detali(self.os_floor[w], self.H, self.H_stenka, A, B, C,
                                                         self.input_data[0], self.L2_sh, self.L1_sh, self.S_sh, self.H_paketa)
                                    det = getattr(self.detail, self.spisok_det[w])
                                    w = w + 1

                                    f.write(str(nomer) + tz + str(';'.join(det())) + tz + str(kol) + nov_str)
                                    print('Номер: ', nomer, 'Детали: ', ';'.join(det()), ' Кол-во: ', kol)

# комбинированные углы

                    elif self.input_data[1] == '2К-П' or self.input_data[1] == '2К-Л':
                        nomer = self.index.shet1()  # вертикальный угол
                        self.detail = Detali(self.os_floor[0], self.H, self.H_stenka, A, B, C, self.input_data[0],
                                             self.L2_sh, self.L1_sh, self.S_sh, self.H_paketa)
                        det = getattr(self.detail, self.spisok_det[0])

                        f.write(str(nomer) + tz + str(';'.join(det())) + tz + str(kol) + nov_str)
                        print('Номер: ', nomer, 'Детали: ', ';'.join(det()), ' Кол-во: ', kol)

                        first_letter = re.findall(r'\D+', self.spisok_det[1])
                        if first_letter[0] == 's':
                            # считаем только шины и сразу по Y и по Z
                            nomer = self.index.shet1()  # горизонтальный угол
                            self.detail = Detali(self.os_floor[1], self.H, self.H_stenka, A, B, C, self.input_data[0],
                                                 self.L2_sh, self.L1_sh, self.S_sh, self.H_paketa)
                            det = getattr(self.detail, self.spisok_det[1])

                            f.write(str(nomer) + tz + str(';'.join(det())) + tz + str(kol) + nov_str)
                            print('Номер: ', nomer, 'Детали: ', ';'.join(det()), ' Кол-во: ', kol)

                        else:
                            # считаем корпус для комбинированной секции сначала по Y потом по Z
                            nomer = self.index.shet1()  # горизонтальный угол
                            self.detail = Detali(self.os_floor[1], self.H, self.H_stenka, A, B, C, self.input_data[0],
                                                 self.L2_sh, self.L1_sh, self.S_sh, self.H_paketa)
                            det = getattr(self.detail, self.spisok_det[1])

                            f.write(str(nomer) + tz + str(';'.join(det())) + tz + str(kol) + nov_str)
                            print('Номер: ', nomer, 'Детали: ', ';'.join(det()), ' Кол-во: ', kol)

                            # по Z
                            nomer = self.index.shet1()  # горизонтальный угол
                            self.detail = Detali(self.os_floor[2], self.H, self.H_stenka, A, B, C, self.input_data[0],
                                                 self.L2_sh, self.L1_sh, self.S_sh, self.H_paketa)
                            det = getattr(self.detail, self.spisok_det[2])

                            f.write(str(nomer) + tz + str(';'.join(det())) + tz + str(kol) + nov_str)
                            print('Номер: ', nomer, 'Детали: ', ';'.join(det()), ' Кол-во: ', kol)
                        print('2К-П(Л)')

# Z-образные углы
                    # для одинаковых осей X и Z
                    elif self.kol_os == 3:
                        if all([(self.input_data[1] == '2Z-В' or '2Z-Г'), (self.kol_os == 3),
                              (self.spisok_det[0] == self.spisok_det[2]), (self.os_floor[0] == self.os_floor[2])]):
                            nomer = self.index.shet1()
                            self.detail = Detali(self.os_floor[0], self.H, self.H_stenka, A, B, C, self.input_data[0],
                                                 self.L2_sh, self.L1_sh, self.S_sh, self.H_paketa)
                            det = getattr(self.detail, self.spisok_det[0])
                            kol = int(kol) * 2

                            f.write(str(nomer) + tz + str(';'.join(det())) + tz + str(kol) + nov_str)
                            print('Номер: ', nomer, 'Детали: ', ';'.join(det()), ' Кол-во: ', kol)

                            self.detail = Detali(self.os_floor[1], self.H, self.H_stenka, A, B, C, self.input_data[0],
                                                 self.L2_sh, self.L1_sh, self.S_sh, self.H_paketa)
                            det = getattr(self.detail, self.spisok_det[1])
                            kol = int(self.slovar_svar_det[i]) * int(self.input_data[3])

                            f.write(str(nomer) + tz + str(';'.join(det())) + tz + str(kol) + nov_str)
                            print('Номер: ', self.index.shet1(), 'Детали: ', ';'.join(det()), ' Кол-во: ', kol)

                    # для разных осей X и Z
                        else:
                            while w < len(self.os_floor):
                                for j in self.os_floor:   #начинаем перебор по осям
                                    nomer = self.index.shet1()
                                    self.detail = Detali(self.os_floor[w], self.H, self.H_stenka, A, B, C,
                                                         self.input_data[0], self.L2_sh, self.L1_sh, self.S_sh, self.H_paketa)
                                    det = getattr(self.detail, self.spisok_det[w])
                                    w = w + 1

                                    f.write(str(nomer) + tz + str(';'.join(det())) + tz + str(kol) + nov_str)
                                    print('Номер: ', nomer, 'Детали: ', ';'.join(det()), ' Кол-во: ', kol)


# детали
            spisok_det = self.slovar_detali.keys()  # ДЕЛАЕМ СПИСОК сварных деталей ИЗ СЛОВАРЯ
            for i in spisok_det:
                if self.input_data[1] == '2П' or self.input_data[1] == '2ПФ' or self.input_data[1] == '2ПФ100' \
                        or self.input_data[1] == '2УГ' or self.input_data[1] == '2Z-Г' or self.input_data[1] == '2ОМ':
                    self.os = os_p
                else:
                    continue
                nomer = self.index.shet1()
                kol = int(self.slovar_detali[i]) * int(self.input_data[3])
                print(i)
                self.detail = Detali(self.os[0], self.H, self.H_stenka, A, B, C, self.input_data[0], self.L2_sh, self.L1_sh, self.S_sh, self.H_paketa)
                det = getattr(self.detail, i)
                print(det())

                f.write(str(nomer) + tz + str(';'.join(det())) + tz + str(kol) + nov_str)
                print('Номер: ', nomer, 'Детали: ', ';'.join(det()), ' Кол-во: ', kol)
        else:
            print('Ошибка')
            return False

        f.close()

    def prints(self, det, nomer, kol):

        f = open('spisok_det.txt', 'a')
        tz = ';'

        f.write(str(nomer) + tz + str(';'.join(det())) + tz + str(kol) + '\n')
        print('Деталь: ', ';'.join(det()), ' Кол-во: ', kol)
        f.close()

    def SB(self, kol):
        spis = {'ss': 2, 'tp': 8}
        for i in spis.keys():
            #print('i=', i)
            self.detail = Detali(self.os[0], self.H, self.H_stenka, 0, 0, 0, self.input_data[0], self.L2_sh, self.L1_sh,
                                 self.S_sh, self.H_paketa)
            kol_i = kol * spis[i]
            nomer = self.index.shet1()  # присваеваем порядковый номер
            det = getattr(self.detail, i)
            self.prints(det, nomer, kol_i)

    def two_p(self):
        self.slovar_detali = {'n': 4, 'sux': 4, 'kv': 2, 'c': 4, 's1': 4, 's2': 4, 'kc': 1}
        self.kol_stikov = 1

    def two_om2(self):
        self.slovar_detali = {'n': 4, 'sux': 4, 'kv': 2, 'c': 4, 's1': 4, 's2': 4, 'kc': 1}
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

    def two_slovar_spisok(self, nazv_svar_det): #выбор из словаря нужный список деталей
        value = self.slovar[nazv_svar_det]  # "value" - это перечень деталей в сварной детали "a"  выбранный из списка
        self.spisok_det = re.findall(r'[^-]+', value)  # разбираем перечень "value" на список  "self.slovar_spisok"
        print(self.spisok_det)
