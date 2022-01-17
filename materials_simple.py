 # coding:utf8

import math

class vvod:
    def __init__(self, seria, material, nominal, dlina, Nstik, Nsekc, Nkon_zag, Nflanc, Lsvar_izd):
        self.seria = seria
        self.material = material
        self.nominal = int(nominal)
        self.nominal_2 = 0      # нужен для медного шинопровода для стенок
        self.dlina = int(dlina)
        self.Nstik = int(Nstik)
        self.Nsekc = int(Nsekc)
        self.Nkon_zag = int(Nkon_zag)
        self.Nflanc = int(Nflanc)
        self.Lsvar_izd = int(Lsvar_izd)
        self.kr = 2.82
        self.nkr = 3
        self.v_st = 0
        self.s = 0  # s это ширина шины
        self.pet = 0    #ширина пленки пэт
        self.H_zag_tor = 0
        self.ves_zag_tor = 0
        self.H_zag_bok = 0
        self.ves_zag_bok = 0
        self.zaglushka1 = ''
        self.ves_flanca = 0
        self.stenka_2500 = 2000
        self.S_sh = 0   # Площадь сечения шины
        self.itog = []

    def fg(self):
        print("Расчет материалов\n")
        print('\nНоминал/длина/стыки/секции/заглушки/фланцы/сварные\n', self.nominal, '/', self.dlina, '/', self.Nstik,
              '/', self.Nsekc, '/', self.Nkon_zag, '/', self.Nflanc, '/', self.Lsvar_izd)

        print("Материал", self.material)
        if self.material in ['Алюминий', 'Al']:
            self.vibor()
        else:
            self.vibor_2()

        if self.seria in ['E3']:
            print('крышка и стенка крашенная')
            self.kr_st_kraska(int(self.dlina) - int(self.Lsvar_izd))  # крышка и стенка крашенная
            print('крышка и стенка некрашенная')
            self.kr_st(self.Lsvar_izd)  # крышка и стенка некрашенная
            print('шина')
            self.sh(self.dlina)  # шина
            print('сухарь')
            self.sux(self.Nsekc)  # сухарь
            print('направляющие')
            self.napr(self.Nsekc)  # направляющие
            print('пленка')
            self.plenka(self.dlina)  # пленка
            print('изоляция')
            self.zel(self.nominal, self.dlina)  # изоляция
            print('порошок ПОС')
            self.pos(self.Nstik)  # порошок ПОС
            print('стыки')
            self.stik(self.Nstik)  # стыки
            print('крышки стыка количество')
            self.krishka(self.Nstik)  # крышки стыка количество
            print('концевые заглушк')
            self.zaglishka(self.Nkon_zag)  # концевые заглушки

            if int(self.Nflanc) == 0:
                print('Без фланца')
            else:
                print('расчет веса листа для фланцев')
                self.flanec(self.Nflanc)  # расчет веса листа для фланцев

            print('расчет количества герметика')
            self.germetik(self.dlina)  # расчет количества герметика
            print('заклепки')
            self.zak(self.dlina)  # заклепки
            print('количесвто болтов м6')
            self.bolt_m6(self.Nsekc)  # количесвто болтов м6
            print('Конец')
            return self.itog
        else:
            self.stik(self.Nstik)  # стыки
            self.pos(self.Nstik)  # порошок ПОС
            self.sh(self.dlina)  # шина
            self.kompaund(self.dlina)   # Расчет компаунда и наполнителей
            return self.itog

    def vibor(self):
        '''для алюминиевого шинопровода'''
        print(self.nominal, self.dlina, self.Nstik, self.Nsekc, self.Nkon_zag, self.Nflanc, self.Lsvar_izd)
        if self.nominal == 250:
            self.nominal_2 = 630
            print(self.nominal)
            self.s = 40
            self.S_sh = 232.3   # площадь сечения
            self.v_sh = 0.63  # вес шины
            self.v_st = 0.92  # вес стенки
            self.pet = str('пленка ПЭТ ширина 40 мм.')
            self.H_zag_tor = 117  # размер заглушки торцевой
            self.ves_zag_tor = 0.25  # вес заглушки торцевой
            self.H_zag_bok = 113  # размер заглушки боковой
            self.ves_zag_bok = 0.26  # вес заглушки боковой
            self.zaglushka1 = 'Лист боковой 630'  # название листа бокового
            self.ves_flanca = 0.18
        elif self.nominal == 400:
            self.nominal_2 = 630
            print(self.nominal)
            self.s = 40
            self.S_sh = 232.3  # площадь сечения
            self.v_sh = 0.63  # вес шины
            self.v_st = 0.92  # вес стенки
            self.pet = str('пленка ПЭТ ширина 40 мм.')
            self.H_zag_tor = 117  # размер заглушки торцевой
            self.ves_zag_tor = 0.25  # вес заглушки торцевой
            self.H_zag_bok = 113  # размер заглушки боковой
            self.ves_zag_bok = 0.26  # вес заглушки боковой
            self.zaglushka1 = 'Лист боковой 630'  # название листа бокового
            self.ves_flanca = 0.18
        elif self.nominal == 630:
            self.nominal_2 = 630
            print(self.nominal)
            self.s = 40
            self.S_sh = 232.3   # площадь сечения
            self.v_sh = 0.63  # вес шины
            self.v_st = 0.92  # вес стенки
            self.pet = str('пленка ПЭТ ширина 40 мм.')
            self.H_zag_tor = 117  # размер заглушки торцевой
            self.ves_zag_tor = 0.25  # вес заглушки торцевой
            self.H_zag_bok = 113  # размер заглушки боковой
            self.ves_zag_bok = 0.26  # вес заглушки боковой
            self.zaglushka1 = 'Лист боковой 630'  # название листа бокового
            self.ves_flanca = 0.18
        elif self.nominal == 800:
            self.nominal_2 = 800
            self.s = 55
            self.S_sh = 322.3 # площадь сечения
            self.v_sh = 0.873
            self.v_st = 1.046
            self.pet = str('пленка ПЭТ ширина 55 мм.')
            self.H_zag_tor = 132
            self.ves_zag_tor = 0.28
            self.H_zag_bok = 128
            self.ves_zag_bok = 0.3
            self.ves_flanca = 0.2
        elif self.nominal == 1000:
            self.nominal_2 = 1000
            self.s = 80
            self.S_sh = 502.3 # площадь сечения
            self.v_sh = 1.28
            self.v_st = 1.249
            self.pet = str('пленка ПЭТ ширина 80 мм.')
            self.H_zag_tor = 157
            self.ves_zag_tor = 0.34
            self.H_zag_bok = 153
            self.ves_zag_bok = 0.36
            self.ves_flanca = 0.21
        elif self.nominal == 1250:
            self.nominal_2 = 1250
            self.s = 110
            self.S_sh = 652.3 # площадь сечения
            self.v_sh = 1.77
            self.v_st = 1.14
            self.pet = str('пленка ПЭТ ширина 110 мм.')
            self.H_zag_tor = 187
            self.ves_zag_tor = 0.4
            self.H_zag_bok = 183
            self.ves_zag_bok = 0.43
            self.ves_flanca = 0.23
        elif self.nominal in [1600, 3200]:
            if self.seria in ['E3']:
                self.nominal_2 = 1600
                self.s = 160
                self.S_sh = 952.3 # площадь сечения
                self.v_sh = 2.58
                self.v_st = 1.83
                self.pet = str('пленка ПЭТ ширина 160 мм.')
                self.vH_zag_tor = 235
                self.ves_zag_tor = 0.51
                self.H_zag_bok = 231
                self.ves_zag_bok = 0.55
                self.ves_flanca = 0.65
            else:
                self.nominal_2 = 1601
                self.s = 130
                self.S_sh = 1026.3 # площадь сечения
                self.v_sh = 2.77
                self.ves_flanca = 0.65
        elif self.nominal in [2000, 4000]:
            if self.seria in ['E3']:
                self.nominal_2 = 2000
                self.s = 200
                self.S_sh = 1192.3 # площадь сечения
                self.v_sh = 3.231
                self.v_st = 2.225
                self.pet = str('пленка ПЭТ ширина 200 мм.')
                self.H_zag_tor = 237
                self.ves_zag_tor = 0.6
                self.H_zag_bok = 233
                self.ves_zag_bok = 0.64
                self.ves_flanca = 0.75
            else:
                self.nominal_2 = 2001
                self.s = 160
                self.S_sh = 1266.3   # площадь сечения
                self.v_sh = 3.2
                self.ves_flanca = 0.65
        elif self.nominal in [2500, 5000, 6300]:
            self.nominal_2 = 2500
            self.stenka_2500 = 2000
            self.s = 200
            self.S_sh = 1586.3 # площадь сечения
            self.v_sh = 4.299   # вес шины
            self.v_st = 2.225   # вес стенки
            self.pet = str('пленка ПЭТ ширина 200 мм.')
            self.H_zag_tor = 237
            self.ves_zag_tor = 0.6
            self.H_zag_bok = 233
            self.ves_zag_bok = 0.64
            self.ves_flanca = 0.75
        else:
            print("такого номинала нет, введите другое значение")
            exit()

    def vibor_2(self):
        '''для медного шинопровода'''
        print(self.nominal, self.dlina, self.Nstik, self.Nsekc, self.Nkon_zag, self.Nflanc, self.Lsvar_izd)
        if self.nominal == 630:  # не утверждено по идее такого номинала нет
            print(self.nominal)
            self.nominal_2 = 630
            self.s = 40
            self.S_sh = 232.3                       # площадь сечения
            self.v_sh = 2.1                         # вес шины
            self.v_st = 0.92                        # вес стенки
            self.pet = str('пленка ПЭТ ширина 40 мм.')
            self.H_zag_tor = 117                    # размер заглушки торцевой
            self.ves_zag_tor = 0.25                 # вес заглушки торцевой
            self.H_zag_bok = 113                    # размер заглушки боковой
            self.ves_zag_bok = 0.26                 # вес заглушки боковой
            self.zaglushka1 = 'Лист боковой 630'    # название листа бокового
            self.ves_flanca = 0.18
        elif self.nominal == 800:
            print(self.nominal)
            self.nominal_2 = 630
            self.s = 40
            self.S_sh = 232.3                       # площадь сечения
            self.v_sh = 2.1                         # вес шины
            self.v_st = 0.92                        # вес стенки
            self.pet = str('пленка ПЭТ ширина 40 мм.')
            self.H_zag_tor = 117                    # размер заглушки торцевой
            self.ves_zag_tor = 0.25                 # вес заглушки торцевой
            self.H_zag_bok = 113                    # размер заглушки боковой
            self.ves_zag_bok = 0.26                 # вес заглушки боковой
            self.zaglushka1 = 'Лист боковой 630'    # название листа бокового
            self.ves_flanca = 0.18
        elif self.nominal == 1000:
            self.nominal_2 = 800
            self.s = 55
            self.S_sh = 322.3                       # площадь сечения
            self.v_sh = 2.9
            self.v_st = 1.046
            self.pet = str('пленка ПЭТ ширина 55 мм.')
            self.H_zag_tor = 132
            self.ves_zag_tor = 0.28
            self.H_zag_bok = 128
            self.ves_zag_bok = 0.3
            self.ves_flanca = 0.2
        elif self.nominal in [1250]:
            self.nominal_2 = 1000
            self.s = 80
            self.S_sh = 502.3 # площадь сечения
            self.v_sh = 4.2
            self.v_st = 1.249
            self.pet = str('пленка ПЭТ ширина 80 мм.')
            self.H_zag_tor = 157
            self.ves_zag_tor = 0.34
            self.H_zag_bok = 153
            self.ves_zag_bok = 0.36
            self.ves_flanca = 0.21
        elif self.nominal in [1600, 3200]:
            self.nominal_2 = 1250
            self.s = 110
            self.S_sh = 652.3   # площадь сечения
            self.v_sh = 5.8
            self.v_st = 1.14
            self.pet = str('пленка ПЭТ ширина 110 мм.')
            self.H_zag_tor = 187
            self.ves_zag_tor = 0.4
            self.H_zag_bok = 183
            self.ves_zag_bok = 0.43
            self.ves_flanca = 0.23
        elif self.nominal in [2000, 4000]:
            self.nominal_2 = 1600
            self.s = 160
            self.S_sh = 952.3 # площадь сечения
            self.v_sh = 8.5
            self.v_st = 1.83
            self.pet = str('пленка ПЭТ ширина 160 мм.')
            self.vH_zag_tor = 235
            self.ves_zag_tor = 0.51
            self.H_zag_bok = 231
            self.ves_zag_bok = 0.55
            self.ves_flanca = 0.65
        elif self.nominal in [2500, 5000, 6300]:
            self.stenka_2500 = 1600
            self.nominal_2 = '2500 (160x8)'
            self.s = 160
            self.S_sh = 1266.3 # площадь сечения
            self.v_sh = 11.3  # вес шины
            self.v_st = 1.83  # вес стенки
            self.pet = str('пленка ПЭТ ширина 200 мм.')
            self.H_zag_tor = 237
            self.ves_zag_tor = 0.6
            self.H_zag_bok = 233
            self.ves_zag_bok = 0.64
            self.ves_flanca = 0.75
        else:
            print("такого номинала нет, введите другое значение")
            exit()

    def kompaund(self, os):
        '''Для получения 1 литра компаунда необходимо смешать следующие компоненты:
                    -0,49 кг. эпоксидной смолы,
                    - 0,10 кг отвердителя 0903,
                    -0,07 кг. отвердителя 0590,
                    -0,91 кг кварцевого песка. '''
        if self.nominal in [3200, 4000, 5000, 6300]:
            gabarit = [0.1, (self.s * 2 + 50) / 1000]   # габарит шинопрвода в метрах
        else:
            gabarit = [0.1, (self.s + 40) / 1000]   # габарит шинопрвода в метрах
        os2 = os - self.Nsekc * 0.275   # объем с вычетом длины торцов без компаунда
        obem_shin = self.S_sh * os * 4 / 1000000    # объем шин
        print(obem_shin, 'obem shin')

        if self.nominal in [3200, 4000, 5000, 6300]:
            obem = round(gabarit[0] * gabarit[1] * os2 - obem_shin * 2, 5)   # объем шинопровода в м3 для двухэтажек
        else:
            obem = round(gabarit[0] * gabarit[1] * os2 - obem_shin, 5)   # объем шинопровода в м3
        print(obem, 'obem')

        '''Расчитываем эпоксидку'''
        epoxy = round(obem / 0.001 * 0.49, 2)
        print('epoxy', epoxy)
        self.itog.append(['М', 'Смола CHS-Epoxy 520', epoxy, 'кг.'])
        '''расчитываем отвердитель'''
        otverd_0903 = round(obem / 0.001 * 0.1, 2)
        print('otverd0903', otverd_0903)
        self.itog.append(['М', 'Отвердитель Telalit 0903', otverd_0903, 'кг.'])
        '''расчитываем отвердитель'''
        otverd_0590 = round(obem / 0.001 * 0.07, 2)
        print('otverd0590', otverd_0590)
        self.itog.append(['М', 'Отвердитель Telalit 0590', otverd_0590, 'кг.'])
        '''расчитываем наполнитель'''
        kv_pes = round(obem / 0.001 * 0.91, 2)
        print('kv pesok', kv_pes)
        self.itog.append(['М', 'Кварцевая мука', kv_pes, 'кг.'])

    def kr_st_kraska(self, os):     # расчет крышки и стенки крашенной
        print(os, 'os')
        L = round(os * 2 / 3, 0)
        V = L * 3 * self.v_sh
        L1 = round(os * 2 / 3, 0)
        V1 = L1 * 3 * self.v_st
        print('Крышка с выступом окрашенная 2.82м.', L, ' шт.\n', 'стенка крашенная', L1, ' шт.', )
        if self.nominal in [2500]:
            self.itog.append(['П', 'Крышка окрашенная 2.82м.', L, 'шт.'])
            self.itog.append(['П', 'Стенка ' + str(self.stenka_2500) + ' окрашенный 2.82м.', L1, 'шт.'])
        elif self.nominal in [3200, 4000]:
            self.itog.append(['П', 'Крышка с выступом окрашенная 2.82м.', L, 'шт.'])
            self.itog.append(['П', 'Крышка средняя окрашенная 2.82м.', L / 2, 'шт.'])
            self.itog.append(['П', 'Стенка ' + str(self.nominal_2) + ' окрашенный 2.82м.', L1 * 2, 'шт.'])
        elif self.nominal in [5000]:
            self.itog.append(['П', 'Крышка окрашенная 2.82м.', L, 'шт.'])
            self.itog.append(['П', 'Крышка средняя окрашенная 2.82м.', L / 2, 'шт.'])
            self.itog.append(['П', 'Стенка ' + str(self.stenka_2500) + ' окрашенный 2.82м.', L1 * 2, 'шт.'])
        elif self.nominal in [6300]:
            self.itog.append(['П', 'Крышка окрашенная 2.82м.', L, 'шт.'])
            self.itog.append(['П', 'Крышка средняя окрашенная 2.82м.', L, 'шт.'])
            self.itog.append(['П', 'Стенка ' + str(self.stenka_2500) + ' окрашенный 2.82м.', L1 * 3, 'шт.'])
        else:
            self.itog.append(['П', 'Крышка с выступом окрашенная 2.82м.', L, 'шт.'])
            self.itog.append(['П', 'Стенка ' + str(self.nominal_2) + ' окрашенный 2.82м.', L1, 'шт.'])

    def kr_st(self, os):    # расчет не крашенной крышки
        L = round(math.ceil(os * 2 / 3), 0)
        L1 = round(math.ceil(os * 2 / 3), 0)
        print('Крышка без покрытия 3м. ', L, ' шт.\n')
        if self.nominal in [2500]:
            self.itog.append(['П', 'Крышка без покрытия 3м.', L, 'шт.'])
            self.itog.append(['П', 'Стенка ' + str(self.stenka_2500) + ' без покрытия 3м.', L, 'шт.'])
        elif self.nominal in [3200, 4000]:
            self.itog.append(['П', 'Крышка без покрытия 3м.', L, 'шт.'])
            self.itog.append(['П', 'Стенка ' + str(self.nominal_2) + ' без покрытия 3м.', L * 2, 'шт.'])
            self.itog.append(['П', 'Крышка средняя без покрытия 3м.', L, 'шт.'])
        elif self.nominal in [5000]:
            self.itog.append(['П', 'Крышка без покрытия 3м.', L, 'шт.'])
            self.itog.append(['П', 'Стенка ' + str(self.stenka_2500) + ' без покрытия 3м.', L * 2, 'шт.'])
            self.itog.append(['П', 'Крышка средняя без покрытия 3м.', L, 'шт.'])
        elif self.nominal in [6300]:
            self.itog.append(['П', 'Крышка без покрытия 3м.', L, 'шт.'])
            self.itog.append(['П', 'Стенка ' + str(self.stenka_2500) + ' без покрытия 3м.', L * 3, 'шт.'])
            self.itog.append(['П', 'Крышка средняя без покрытия 3м.', L * 2, 'шт.'])
        else:
            self.itog.append(['П', 'Крышка без покрытия 3м.', L, 'шт.'])
            self.itog.append(['П', 'Стенка ' + str(self.nominal_2) + ' без покрытия 3м.', L, 'шт.'])

    def sh(self, os):   #расчет шины
        L = round(math.ceil(os * 4 / 3), 2)
        if self.material in ['Алюминий', 'Al']:
            name = 'Шина ' + str(self.nominal_2)
        else:
            name = 'Шина медная ' + str(self.nominal)
        if self.nominal in [3200, 4000, 5000]:
            self.itog.append(['П', name, L * 2, 'шт.'])
        elif self.nominal in [6300]:
            self.itog.append(['П', name, L * 3, 'шт.'])
        else:
            self.itog.append(['П', name, L, 'шт.'])

    def sux(self, kol):     # сухари
        sux_kol = int(kol) * 4
        self.itog.append(['заг', 'Сухарь (Деталь)', sux_kol, 'шт.'])
        self.itog.append(['ст',
                          'Заклепка вытяжная 4,8х12 мм Сталь/Сталь, стандартный бортик ZAC', sux_kol * 2 / 1000, 'тыс. шт.'])

    def napr(self, kol):    # направляющиеа расчитываем из количества секций

        if self.nominal in [3200, 4000, 5000]:
            L = round(math.ceil((self.s * 2 + 66 + 5 + 3 + 3) * 4 * kol / 3000), 2)
        elif self.nominal in [6300]:
            L = round(math.ceil((self.s * 3 + 66 + 5 + 6 + 3) * 4 * kol / 3000), 2)
        else:
            L = round(math.ceil((self.s + 66 + 5 + 3) * 4 * kol / 3000), 2)
        print('Направляющая', L, 'шт.')

        if self.nominal in [2500, 5000, 6300]:
            self.itog.append(['П', 'Направляющая ' + str(self.nominal), L, 'шт.'])
        else:
            self.itog.append(['П', 'Направляющая', L, 'шт.'])

        epdm3 = (25 + L * 2) * 2
        self.itog.append(['М', 'Уплотнитель из пористой резины "EPDM 150" с клеевым слоем, 5 мм х25 мм (цвет чёрный)',
                          epdm3, 'м.п.'])
        self.itog.append(['Пи', 'Силикагель фасованный (20 гр)', kol * 2, 'шт.'])

    def krishka(self, kol_kr_st):   # крышка стыка
        kol_kr_st = kol_kr_st * 2
        epdm3 = kol_kr_st * 250 / 1000
        self.itog.append(['Пи', 'Крышка защитная верхняя 000 034 RAL 7035, с уплотнителем EPDM', kol_kr_st, 'шт.'])
        self.itog.append(['М', 'Уплотнитель из пористой резины "EPDM 150" с клеевым слоем, 5 мм х125 мм (цвет чёрный)',
                          epdm3, 'м.п.'])

    # нужно пересчитать премикс для изоляторов и вообще выделить расчет всех материалов в отдельный расчет в конце модуля
    def stik(self, kol):    # стыки
        print('nominal', self.nominal)
        L_stenka = round(kol * (self.s + 66 + 5) * 2 / 3000, 2)  # расчет стенки стыка
        #print(str(kol), str(self.s))
        L_skotch_dvoinoi = round(kol * (self.s + 30) * 4 * 8 / 1000, 2)  # расчет двойного скотча
        L_epdm = kol * 0.25 * 2  # расчет EPDM уплотнителя
        razmer_dempf = 35
        razmer_list_sil = 500
        procent_dempf = (razmer_dempf ** 2) * 100 / (razmer_list_sil ** 2)

        if self.nominal in [2000]:
            kol_plast = kol * 8
            L_plastina = round(kol_plast * (self.s + 30 + 5) / 3000, 2)  # расчет пластины токопроводящей
            kol_b = kol * 2
            ves_vtul = round(kol * 2 * 0.05075, 2)  # вес втулки расчет
            kol_demp = kol_b * 4  # количество демпферов
            #self.itog.append(['заг', 'Демпфер 25-35мм 8мм', kol_demp, 'шт.'])
            ves_demp = round(kol_demp * 0.008085, 2)  # вес всех демпферов
            itog_dempf = kol_demp * procent_dempf
            isol_sr = kol * 3  # количество изоляторов средних
            isol_kr = kol * 2  # количество изоляторов крайних
            ves_izol_sr = 0.24
            ves_izol_kr = 0.235
            naz_sr = 'Изолятор 2000А  (Ср.)'  # название изолятора
            naz_kr = 'Изолятор 2000А  (Кр.)'  # название изолятора
        elif self.nominal in [2500]:
            kol_plast = kol * 8
            L_plastina = round(kol_plast * (self.s + 30 + 5) / 3000, 2)  # расчет пластины токопроводящей
            kol_b = kol * 2
            ves_vtul = round(kol * 2 * 0.05075, 2)  # вес втулки расчет
            kol_demp = kol_b * 4  # количество демпферов
            # self.itog.append(['заг', 'Демпфер 25-35мм 8мм', kol_demp, 'шт.'])
            ves_demp = round(kol_demp * 0.008085, 2)  # вес всех демпферов
            itog_dempf = kol_demp * procent_dempf
            isol_sr = kol * 3  # количество изоляторов средних
            isol_kr = kol * 2  # количество изоляторов крайних
            ves_izol_sr = 0.24
            ves_izol_kr = 0.235
            naz_sr = 'Изолятор 2000А  (Ср.)'  # название изолятора
            naz_kr = 'Изолятор 2000А  (Кр.)'  # название изолятора
        elif self.nominal in [1600]:
            kol_plast = kol * 8
            L_plastina = round(kol_plast * (self.s + 30 + 5) / 3000, 2)  # расчет пластины токопроводящей
            kol_b = kol * 2
            ves_vtul = round(kol * 2 * 0.05075, 2)  # вес втулки расчет
            kol_demp = kol_b * 4  # количество демпферов
            itog_dempf = kol_demp * procent_dempf
            #self.itog.append(['заг', 'Демпфер 20-30мм 4мм', kol_demp, 'шт.'])
            ves_demp = round(kol_demp * 0.008085, 2)  # вес всех демпферов
            isol_sr = kol * 3  # количество изоляторов средних
            isol_kr = kol * 2  # количество изоляторов крайних
            ves_izol_sr = 0.205
            ves_izol_kr = 0.195
            naz_sr = 'Изолятор 1600А  (Ср.)'  # название изолятора
            naz_kr = 'Изолятор 1600А  (Кр.)'  # название изолятора
        elif self.nominal in [3200]:
            kol_plast = kol * 8
            L_plastina = round(kol_plast  * (self.s * 2 + 30 + 5) / 3000, 2)  # расчет пластины токопроводящей
            kol_b = kol * 4
            print('rolichestvo boltov', kol_b)
            ves_vtul = round(kol * 2 * 0.05075, 2)  # вес втулки расчет
            kol_demp = kol_b * 4  # количество демпферов
            itog_dempf = kol_demp * procent_dempf
            #self.itog.append(['заг', 'Демпфер 20-30мм 4мм', kol_demp, 'шт.'])
            ves_demp = round(kol_demp * 0.008085, 2)  # вес всех демпферов
            isol_sr = kol * 6  # количество изоляторов средних
            isol_kr = kol * 4  # количество изоляторов крайних
            ves_izol_sr = 0.205
            ves_izol_kr = 0.195
            naz_sr = 'Изолятор 1600А  (Ср.)'  # название изолятора
            naz_kr = 'Изолятор 1600А  (Кр.)'  # название изолятора
        elif self.nominal in [4000]:
            kol_plast = kol * 8
            L_plastina = round(kol_plast * (self.s * 2 + 30 + 5) / 3000, 2)  # расчет пластины токопроводящей
            kol_b = kol * 4
            ves_vtul = round(kol * 2 * 0.05075, 2)  # вес втулки расчет
            kol_demp = kol_b * 4  # количество демпферов
            itog_dempf = kol_demp * procent_dempf
            #self.itog.append(['заг', 'Демпфер 20-30мм 4мм', kol_demp, 'шт.'])
            ves_demp = round(kol_demp * 0.008085, 2)  # вес всех демпферов
            isol_sr = kol * 6  # количество изоляторов средних
            isol_kr = kol * 4  # количество изоляторов крайних
            ves_izol_sr = 0.24
            ves_izol_kr = 0.235
            naz_sr = 'Изолятор 2000А  (Ср.)'  # название изолятора
            naz_kr = 'Изолятор 2000А  (Кр.)'  # название изолятора
        elif self.nominal in [5000]:
            kol_plast = kol * 8
            L_plastina = round(kol_plast * (self.s * 2 + 30 + 5) / 3000, 2)  # расчет пластины токопроводящей
            kol_b = kol * 4
            ves_vtul = round(kol * 2 * 0.05075, 2)  # вес втулки расчет
            kol_demp = kol_b * 4  # количество демпферов
            itog_dempf = kol_demp * procent_dempf
            #self.itog.append(['заг', 'Демпфер 20-30мм 4мм', kol_demp, 'шт.'])
            ves_demp = round(kol_demp * 0.008085, 2)  # вес всех демпферов
            isol_sr = kol * 6  # количество изоляторов средних
            isol_kr = kol * 4  # количество изоляторов крайних
            ves_izol_sr = 0.24
            ves_izol_kr = 0.235
            naz_sr = 'Изолятор 2000А  (Ср.)'  # название изолятора
            naz_kr = 'Изолятор 2000А  (Кр.)'  # название изолятора
        elif self.nominal in [630]:
            kol_plast = kol * 8
            L_plastina = round(kol_plast * (self.s + 30 + 5) / 3000, 2)  # расчет пластины токопроводящей
            kol_b = kol
            ves_vtul = round(kol * 0.05075, 2)  # вес втулки расчет
            kol_demp = kol_b * 4  # количество демпферов
            itog_dempf = kol_demp * procent_dempf
            #self.itog.append(['заг', 'Демпфер 20-30мм 4мм', kol_demp, 'шт.'])
            ves_demp = round(kol_demp * 0.008085, 2)  # вес всех демпферов
            isol_sr = kol * 3  # количество изоляторов средних
            isol_kr = kol * 2  # количество изоляторов крайних
            ves_izol_sr = 0.11
            ves_izol_kr = 0.105
            naz_sr = 'Изолятор 630А  (Ср.)'  # название изолятора
            naz_kr = 'Изолятор 630А  (Кр.)'  # название изолятора
        elif self.nominal in [1250]:
            kol_plast = kol * 8
            L_plastina = round(kol_plast * (self.s + 30 + 5) / 3000, 2)  # расчет пластины токопроводящей
            kol_b = kol * 2
            ves_vtul = round(kol * 2 * 0.05075, 2)  # вес втулки расчет
            kol_demp = kol_b * 4  # количество демпферов
            itog_dempf = kol_demp * procent_dempf
            # self.itog.append(['заг', 'Демпфер 20-30мм 4мм', kol_demp, 'шт.'])
            ves_demp = round(kol_demp * 0.008085, 2)  # вес всех демпферов
            isol_sr = kol * 3  # количество изоляторов средних
            isol_kr = kol * 2  # количество изоляторов крайних
            ves_izol_sr = 0.16
            ves_izol_kr = 0.15
            naz_sr = 'Изолятор 1250А  (Ср.)'  # название изолятора
            naz_kr = 'Изолятор 1250А  (Кр.)'  # название изолятора
        elif self.nominal in [1250]:
            kol_plast = kol * 8
            L_plastina = round(kol_plast * (self.s + 30 + 5) / 3000, 2)  # расчет пластины токопроводящей
            kol_b = kol * 2
            ves_vtul = round(kol * 2 * 0.05075, 2)  # вес втулки расчет
            kol_demp = kol_b * 4  # количество демпферов
            itog_dempf = kol_demp * procent_dempf
            # self.itog.append(['заг', 'Демпфер 20-30мм 4мм', kol_demp, 'шт.'])
            ves_demp = round(kol_demp * 0.008085, 2)  # вес всех демпферов
            isol_sr = kol * 3  # количество изоляторов средних
            isol_kr = kol * 2  # количество изоляторов крайних
            ves_izol_sr = 0.105
            ves_izol_kr = 0.115
            naz_sr = 'Изолятор 800А  (Ср.)'  # название изолятора
            naz_kr = 'Изолятор 800А  (Кр.)'  # название изолятора
        elif self.nominal in [6300]:
            # 6300
            kol_plast = kol * 8
            L_plastina = round(kol_plast * (self.s * 3 + 30 + 5) / 3000, 2)  # расчет пластины токопроводящей
            kol_b = kol * 6
            ves_vtul = round(kol * 0.05075, 2)  # вес втулки расчет
            kol_demp = kol_b * 4  # количество демпферов
            itog_dempf = kol_demp * procent_dempf
            #self.itog.append(['заг', 'Демпфер 20-30мм 4мм', kol_demp, 'шт.'])
            ves_demp = round(kol_demp * 0.008085, 2)  # вес всех демпферов
            isol_sr = kol * 9  # количество изоляторов средних
            isol_kr = kol * 6  # количество изоляторов крайних
            ves_izol_sr = 0.24
            ves_izol_kr = 0.235
            naz_sr = 'Изолятор 2000А  (Ср.)'  # название изолятора
            naz_kr = 'Изолятор 2000А  (Кр.)'  # название изолятора
        else:
            kol_plast = kol * 8
            L_plastina = round(kol_plast * (self.s + 30 + 5) / 3000, 2)  # расчет пластины токопроводящей
            kol_b = kol
            ves_vtul = round(kol * 0.05075, 2)  # вес втулки расчет
            kol_demp = kol_b * 4  # количество демпферов
            itog_dempf = kol_demp * procent_dempf
            #self.itog.append(['заг', 'Демпфер 20-30мм 4мм', kol_demp, 'шт.'])
            ves_demp = round(kol_demp * 0.008085, 2)  # вес всех демпферов
            isol_sr = kol * 3  # количество изоляторов средних
            isol_kr = kol * 2  # количество изоляторов крайних
            ves_izol_sr = 0.105
            ves_izol_kr = 0.115
            naz_sr = 'изолятор 1600 средний'  # название изолятора
            naz_kr = 'изолятор 1600 крайний'  # название изолятора

        self.itog.append(['Пи', 'Наклейки на стыки ШП', kol * 2, 'шт.'])
        self.itog.append(['П', 'Стенка стыка', L_stenka, 'шт.'])

        if self.material in ['Алюминий', 'Al']:
            name_L_plastina = ''
        else:
            name_L_plastina = ' медная'

        if self.nominal in [2500, 5000, 6300]:
            self.itog.append(['П', 'Пластина токопроводящая 2500' + name_L_plastina, L_plastina, 'шт.'])
            self.itog.append(['Пи', 'Болт М12 со срывной головкой (номинал 2500) по чертежу 000 031-01', kol_b, 'шт.'])
            self.itog.append(['заг', 'Силикон листовой толщина 8 мм 500х500мм', itog_dempf, 'шт.'])
        else:
            self.itog.append(['П', 'Пластина токопроводящая' + name_L_plastina, L_plastina, 'шт.'])
            self.itog.append(['Пи', 'болт со срывной головкой', kol_b, 'шт.'])
            self.itog.append(['М', 'Силикон листовой 6мм, 500х500мм', itog_dempf, 'шт.'])
            self.itog.append(['Пи', 'Втулка двухсоставная', kol_b, 'шт.'])

        #self.p('М', 'капролон листовой толщина 25 мм.', ves_vtul, 'шт.')
        #self.itog.append(['Пи', naz_sr, isol_sr, 'шт.'])
        #self.itog.append(['Пи', naz_kr, isol_kr, 'шт.'])
        self.itog.append(['М', 'Прессматериал полиэфирный TNPC BMC 200.20.1', isol_sr * ves_izol_sr + isol_kr * ves_izol_kr, 'шт.'])
        #print('Уплотнитель из пористой резины "EPDM 150" с клеевым слоем, 5 мм х125 мм (цвет чёрный) ', L_epdm, ' м.п.')
        self.itog.append(['ст', 'Гайка М12 шестигранная, цинк DIN934', kol_b * 0.01567, 'кг.'])
        self.itog.append(['Пи', 'держатель гайки', kol_b, 'шт.'])
        self.itog.append(['Пи', 'Индикатор температуры', kol, 'шт.'])
        '''print('шайба пружинная ', kol_b * 2, 'шт.')'''
        self.itog.append(['Пи', 'пружина тарельчатая', kol_b * 2, 'шт.'])
        self.itog.append(['М', 'Лента клеевая 2-х сторонняя 15мм*50м 90080', L_skotch_dvoinoi, 'м.п.'])
        self.itog.append(['Пи', 'Силикагель фасованный (20 гр)', kol, 'шт.'])

        if self.seria in ['CR1'] and self.nominal in [3200, 4000, 1600, 2500]:

            if self.material in ['Алюминий', 'Al']:
                obem_nominal = {'4000': 18, '3200': 14, '1600': 9.6, '2500': 10.5}
            else:   #медь
                obem_nominal = {'2500': 10.5}

            obem = obem_nominal[str(self.nominal)] * self.Nstik  # объем компаунда в стыке в литрах
            print(obem, 'obem')
            '''Для получения 1 литра компаунда необходимо смешать следующие компоненты: 
                -0,49 кг. эпоксидной смолы,
                - 0,10 кг отвердителя 0903, 
                -0,07 кг. отвердителя 0590, 
                -0,91 кг кварцевого песка. '''

            '''Расчитываем эпоксидку'''
            epoxy = round(obem * 0.49, 2)
            print('epoxy', epoxy)
            self.itog.append(['М стык', 'Смола CHS-Epoxy 520', epoxy, 'кг.'])
            '''расчитываем отвердитель'''
            otverd_0903 = round(obem * 0.1, 2)
            print('otverd0903', otverd_0903)
            self.itog.append(['М стык', 'Отвердитель Telalit 0903', otverd_0903, 'кг.'])
            '''расчитываем отвердитель'''
            otverd_0590 = round(obem * 0.07, 2)
            print('otverd0590', otverd_0590)
            self.itog.append(['М стык', 'Отвердитель Telalit 0590', otverd_0590, 'кг.'])
            '''расчитываем наполнитель'''
            kv_pes = round(obem * 0.91, 2)
            print('kv pesok', kv_pes)
            self.itog.append(['М стык', 'Кварцевая мука', kv_pes, 'кг.'])

    def pos(self, pl):#ПОС порошок
        plosh = self.s * 40 * pl * 16 + (self.s + 30) * 40 * pl * 16
        rash = round(plosh / 1000000 * 0.5, 2)
        self.itog.append(['М', 'Порошковый материал ТР-63-25', rash, 'кг.'])

    def zel(self, nominal, os):#расчет эпоксидной изоляции
        per = self.s * 2 + 6
        plosh = per * 0.001 * os * 4
        ves = round(plosh * 0.35, 2)
        self.itog.append(['М', 'Краска порошковая ОХТЭК - 3ГЛ RAL 6024 ТР9 (для шин, зеленая)', ves, 'кг.'])

    def plenka(self, os):   # пленка
        L1 = round(self.s * 0.001 * os * 5 * 0.000125 * 1380, 2)
        L2 = round(40 * 0.001 * os * 2 * 0.000125 * 1380, 2)
        self.itog.append(['М', self.pet, L1, 'кг.'])
        self.itog.append(['М', 'пленка ПЭТ ширина 40 мм.', L2, 'кг.'])

    def zaglishka(self, kol):
        zaglushka1 = self.ves_zag_tor * 2 * kol  # расчетвеса торцевой заглушки
        zaglushka2 = self.ves_zag_bok * 2 * kol  # расчет боковой заглушки
        zaglushka3 = 0.32 * 2 * kol  # расчет верхнего листа
        vse_ves = round(zaglushka1 + zaglushka2 + zaglushka3, 2)  # расчет веса всего листа толщиной 2 мм.
        name_torc = 'Лист торцевой' + str(self.nominal)
        name_bok = 'Лист боковой' + str(self.nominal)
        self.itog.append(['заг', name_torc, zaglushka1, 'кг.'])
        self.itog.append(['заг', name_bok, zaglushka2, 'кг.'])
        self.itog.append(['заг', 'Лист верхний', zaglushka3, 'кг.'])
        self.itog.append(['М', 'Лист А5М 2х1200х3000 ГОСТ 21631-76', vse_ves, 'кг.'])

    def flanec(self, kol):
        ves_flancev = self.ves_flanca * 2
        kol_boltm8x65 = kol * 2
        ves_boltm8x65 = round(kol_boltm8x65 * 0.03094, 3)
        if self.nominal < 2500:
            kol_boltm8x35 = kol * 4
        else:
            kol_boltm8x35 = kol * 6
        ves_boltm8x35 = round(kol_boltm8x35 * 0.01909, 3)
        kol_gaikam8_flanec = kol_boltm8x35 + kol_boltm8x65
        ves_shaiba8 = round(kol_gaikam8_flanec * 0.00232, 3)
        trubka = round(kol * 2 * 30 / 950, 3)
        self.itog.append(['М', 'Лист АМГ6М 4х1200х3000  ГОСТ 21631-76', ves_flancev, 'кг.'])
        self.itog.append(['ст', 'Болт шестигранный М8х65 8.8 DIN 933', ves_boltm8x65, 'кг.'])
        self.itog.append(['ст', 'Болт М8х35 DIN 933 Zn. 8.8', ves_boltm8x35, 'кг.'])
        self.itog.append(['ст', 'Гайка шестигранная с фланцем М8 DIN 6923 Zn', kol_gaikam8_flanec, 'шт.'])
        self.itog.append(['ст', 'шайба плоская С.8', ves_shaiba8, 'кг.'])
        self.itog.append(['М', 'Трубка ТСЭФ 10х14х950', trubka, 'шт.'])

    def germetik(self, D):
        '''L1 = self.s * 2 + 60  # расчет герметика на выводах
        L = D * 4 + L1
        V = 0.75 * 2 * 3.14 * L / 1000000
        ves = V * 1300'''
        ves = D * 0.011     # вычисляем вес в килограммах
        kol_ger = round(ves / 0.65, 1)
        self.itog.append(['М', 'Герметик полиуретановый "Соудал "Соудафлекс 40 FC" 600 мл, серый', kol_ger, 'шт.'])

    def zak(self, L):
        if self.nominal in [630, 800, 1000, 1250, 1600, 2000]:
            k_zak = round(L / 150 * 2, 2)
        elif self.nominal in [2500, 3200, 4000]:
            k_zak = round(L / 150 * 4, 1)
        elif self.nominal in [5000]:
            k_zak = round(L / 150 * 6, 1)
        #6300
        else:
            k_zak = round(L / 150 * 3 / 1000, 1)
        self.itog.append(['ст', 'Заклепка вытяжная AFT 4,8х12 мм Алюм/Сталь станд.бортик (0,5/5,0zac) ZAC', k_zak, 'тыс. шт.'])

    def bolt_m6(self, kol):
        if self.nominal > 2500:
            kol_boltm6x25 = round(self.dlina * 1000 / 200 * 2 * 1.1)
        else:
            kol_boltm6x25 = 0
        kol_boltm6x10 = kol * 8
        kol_boltm6x16 = kol * 16 + kol_boltm6x10
        kol_klips = math.ceil(kol / 3 * 4)
        self.itog.append(['ст', 'Винт самонарезной полуцилиндр. гол., М6х16 DIN 7500С  TORX ', kol_boltm6x16, 'шт.'])
        #self.itog.append(['ст', 'Винт самонарезной М6х12 DIN7500М потай гол. оцинк. TORX', kol_boltm6x10, 'шт.'])
        self.itog.append(
            ['ст', 'Винт с цилин.гол. внутр.шестигр.М6х25 DIN912, 8,8', kol_boltm6x25 * 0.00666, 'кг.'])
        self.itog.append(['ст', 'Болт М10х25 8.8 DIN 933', kol_klips * 0.025, 'кг.'])
        self.itog.append(['ст', 'шайба гровер 10', kol_klips * 0.00194, 'кг.'])
        self.itog.append(['ст', 'гайка шестигранная М10', kol_klips, 'шт.'])
        self.itog.append(['ст', 'шайба плоская С.10', kol_klips * 2 * 0.00408, 'кг.'])
        self.itog.append(['ПИ', 'кронштейн', kol_klips, 'шт.'])

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    a = vvod('CR1', 'Алюминий', 2500, 135, 70, 70, 0, 32, 135)
    print(a.fg())
