 # coding:utf8

import math
import time
from datetime import datetime, timedelta, date, time as dt_time
now = datetime.today()
datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
print(now)
print ( "                                                  Расчет материалов\n" )
itog = open('itog_kol.txt', 'w')
itog.close()

class vvod:
    dlina: object

    def __init__(self, nominal, dlina, Nstik, Nsekc, Nkon_zag, Nflanc, Lsvar_izd):
        self.nominal = int(nominal)
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

    def fg(self):
        itog = open('itog_kol.txt', 'w')
        itog.close()
        print('\nНоминал/длина/стыки/секции/заглушки/фланцы/сварные\n', self.nominal, '/', self.dlina, '/', self.Nstik,
              '/', self.Nsekc, '/', self.Nkon_zag, '/', self.Nflanc, '/', self.Lsvar_izd)
        self.vibor()
        self.kr_st_kraska(self.dlina)  # крышка и стенка крашенная
        self.kr_st(self.Lsvar_izd)  # крышка и стенка некрашенная
        self.sh(self.dlina)  # шина
        self.sux(self.Nsekc)  # сухарь
        self.napr(self.Nstik)  # направляющие
        self.plenka(self.dlina)  # пленка
        self.zel(self.nominal, self.dlina)  # изоляция
        self.pos(self.Nstik)  # порошок ПОС
        self.stik(self.Nstik)  # стыки
        self.krishka(self.Nstik)  # крышки стыка количество
        self.zaglishka(self.Nkon_zag)  # концевые заглушки
        self.flanec(self.Nflanc)  # расчет веса листа для фланцев
        self.germetik(self.dlina)  # расчет количества герметика
        self.zak(self.dlina)  # заклепки
        self.bolt_m6(self.Nsekc)  # количесвто болтов м6  # количесвто болтов м6


    def vibor(self):
        nom = 1  # nom нужна для проверки условия выбора ширины шины
        nom_nominal = int(0)  # тоже самое что и nom
        while nom >= nom_nominal:
            if self.nominal == 630:
                self.s = 40
                self.v_sh = 0.63  # вес шины
                self.v_st = 0.92  # вес стенки
                self.pet = str('пленка ПЭТ ширина 40 мм.')
                self.H_zag_tor = 117  # размер заглушки торцевой
                self.ves_zag_tor = 0.25  # вес заглушки торцевой
                self.H_zag_bok = 113  # размер заглушки боковой
                self.ves_zag_bok = 0.26  # вес заглушки боковой
                self.zaglushka1 = 'Лист боковой 630'  # название листа бокового
                nom_nominal = 1
                self.ves_flanca = 0.18
                break

            elif self.nominal == 800:
                self.s = 55
                self.v_sh = 0.873
                self.v_st = 1.046
                self.pet = str('пленка ПЭТ ширина 55 мм.')
                self.H_zag_tor = 132
                self.ves_zag_tor = 0.28
                self.H_zag_bok = 128
                self.ves_zag_bok = 0.3
                nom_nominal = 1
                self.ves_flanca = 0.2
                break

            elif self.nominal == 1000:
                self.s = 80
                self.v_sh = 1.28
                self.v_st = 1.249
                self.pet = str('пленка ПЭТ ширина 80 мм.')
                self.H_zag_tor = 157
                self.ves_zag_tor = 0.34
                self.H_zag_bok = 153
                self.ves_zag_bok = 0.36
                nom_nominal = 1
                self.ves_flanca = 0.21
                break

            elif self.nominal == 1250:
                self.s = 110
                self.v_sh = 1.77
                self.v_st = 1.14
                self.pet = str('пленка ПЭТ ширина 110 мм.')
                self.H_zag_tor = 187
                self.ves_zag_tor = 0.4
                self.H_zag_bok = 183
                self.ves_zag_bok = 0.43
                nom_nominal = 1
                self.ves_flanca = 0.23
                break

            elif self.nominal == 1600:
                self.s = 160
                self.v_sh = 2.58
                self.v_st = 1.83
                self.pet = str('пленка ПЭТ ширина 160 мм.')
                self.vH_zag_tor = 235
                self.ves_zag_tor = 0.51
                self.H_zag_bok = 231
                self.ves_zag_bok = 0.55
                nom_nominal = 1
                self.ves_flanca = 0.65
                break

            elif self.nominal == 2000:
                self.s = 200
                self.v_sh = 3.231
                self.v_st = 2.225
                self.pet = str('пленка ПЭТ ширина 200 мм.')
                self.H_zag_tor = 237
                self.ves_zag_tor = 0.6
                self.H_zag_bok = 233
                self.ves_zag_bok = 0.64
                nom_nominal = 1
                self.ves_flanca = 0.75
                break

            elif self.nominal == 2500:
                self.s = 200
                self.v_sh = 4.299  # вес шины
                self.v_st = 2.225  # вес стенки
                self.pet = str('пленка ПЭТ ширина 200 мм.')
                self.H_zag_tor = 237
                self.ves_zag_tor = 0.6
                self.H_zag_bok = 233
                self.ves_zag_bok = 0.64
                self.ves_flanca = 0.75
                nom_nominal = 1
                break

            else:
                print("такого номинала нет, введите другое значение")
                nom_nominal = 0


    def kr_st_kraska(self, os):#расчет крышки и стенки крашенной
        L = round(math.ceil(os * 2 / self.kr), 2)
        L1 = round(math.ceil(os * 2 / self.kr), 2)
        print('\nкрышка крашенная', L, ' шт.')
        print('стенка крашенная', L1, ' шт.')
        itog = open('itog_kol.txt', 'a')
        if self.nominal == 2500:
            itog.write('крышка крашенная;' + str(L) + ';шт.\n' + 'стенка 2000 крашенная;' + str(
                L1) + ';шт.\n')
            itog.close()
        else:
            itog.write('крышка крашенная;' + str(L) + ';шт.\n' + 'стенка ' + str(self.nominal) + ' крашенная;' + str(
                L1) + ';шт.\n')
        itog.close()
        return L, L1

    def kr_st(self, os):#расчет не крашенной крышки
        L = round(math.ceil(os * 2 / self.nkr), 2)
        L1 = round(math.ceil(os * 2 / self.nkr), 2)
        print('крышка ', L, ' шт.')
        itog = open('itog_kol.txt', 'a')
        if self.nominal == 2500:
            itog.write('крышка;' + str(L) + ';шт.\n' + 'стенка 2000;' + str(L) + ';шт.\n')
        else:
            itog.write('крышка;' + str(L) + ';шт.\n' + 'стенка ' + str(self.nominal) + ';' + str(L) + ';шт.\n')
        itog.close()

    def sh(self, os):#расчет шины
        L = round(math.ceil(os * 4 / self.nkr), 2)
        print('шина ', self.nominal, ' ', L, ' шт.')
        itog = open('itog_kol.txt', 'a')
        itog.write('шина ' + str(self.nominal) + ';' + str(L) + ';шт.\n')
        itog.close()

    def sux(self, kol):#сухари
        sux_kol = int(kol) * 4
        L = round(math.ceil(sux_kol * 0.045 / self.nkr), 2)
        print('сухарь ', L, ' шт.')
        itog = open('itog_kol.txt', 'a')
        itog.write('сухарь;' + str(L) + ';шт.\n')
        itog.close()

    def napr(self, kol):    #направляющие
        L = round(math.ceil((self.s + 66 + 5) * 4 * kol / 3000), 2)
        print('направляющая ', L, ' шт.\n')
        itog = open('itog_kol.txt', 'a')
        if self.nominal == 2500:
            itog.write('направляющая ' + str(self.nominal) + ';' + str(L) + ';шт.\n')
        else:
            itog.write('направляющая;' + str(L) + ';шт.\n')
        itog.close()

    def krishka(self, kol_kr_st):#крышка стыка
        kol_kr_st = kol_kr_st * 2
        print('крышка стыка ', kol_kr_st, 'шт.')
        itog = open('itog_kol.txt', 'a')
        itog.write('крышка стыка;' + str(kol_kr_st) + ';шт.\n')
        itog.close()

    def stik(self, kol):#стыки
        L_stenka = round(kol * (self.s + 66 + 5) * 2 / 3000, 2)  # расчет стенки стыка
        L_plastina = round(kol * (self.s + 30 + 5) * 8 / 3000, 2)  # расчет пластины токопроводящей
        L_epdm = kol * 0.25 * 2  # расчет EPDM уплотнителя
        L_skotch_dvoinoi = round(kol * (self.s + 30) * 4 * 8 / 1000 / 50, 2)  # расчет двойного скотча
        if self.nominal == 2000 or self.nominal == 2500:
            kol_b = kol * 2
            ves_vtul = round(kol * 2 * 0.05075, 2)  # вес втулки расчет
            kol_demp = kol * 8 * 2  # количество демпферов
            ves_demp = round(kol_demp * 0.008085, 2)  # вес всех демпферов
            isol_sr = kol * 3  # количество изоляторов средних
            isol_kr = kol * 2  # количество изоляторов крайних
            naz_sr = 'изолятор 2000 средний'  # название изолятора
            naz_kr = 'изолятор 2000 крайний'  # название изолятора
        else:
            kol_b = kol
            ves_vtul = round(kol * 0.05075, 2)  # вес втулки расчет
            kol_demp = kol * 8  # количество демпферов
            ves_demp = round(kol_demp * 0.008085, 2)  # вес всех демпферов
            isol_sr = kol * 3  # количество изоляторов средних
            isol_kr = kol * 2  # количество изоляторов крайних
            naz_sr = 'изолятор 1600 средний'  # название изолятора
            naz_kr = 'изолятор 1600 крайний'  # название изолятора
        print('стенка стыка ', L_stenka, ' шт.')
        print('пластина ', L_plastina, ' шт.')
        print('втулка ', ves_vtul, ' шт.')
        print('силикон листовой толщина 6 мм.(демпфер);', ves_demp, ' кг.')
        print(str(naz_sr), isol_sr, ' шт.\n', str(naz_kr), isol_kr, ' шт.\n')
        print('Уплотнитель из пористой резины "EPDM 150" с клеевым слоем, 5 мм х125 мм (цвет чёрный) ', L_epdm, ' м.п.')
        print('болт со срывной головкой ', kol_b, 'шт.')
        print('держатель гайки ', kol_b, 'шт.')
        print('индикатор температуры ', kol, 'шт.')
        print('пружина тарельчатая ', kol_b * 2, 'шт.')
        print('двойной скотч', L_skotch_dvoinoi, 'шт.')
        itog = open('itog_kol.txt', 'a')
        itog.write('стенка стыка;' + str(L_stenka) + ';шт.\n')
        if self.nominal == 2500:
            itog.write('пластина ' + str(self.nominal) + ';' + str(L_plastina) + ';шт.\n')
        else:
            itog.write('пластина;' + str(L_plastina) + ';шт.\n')
        itog.write('капролон листовой толщина 25 мм.;' + str(ves_vtul) + ';кг.\n')
        itog.write('демпфер;' + str(kol_demp) + ';шт.\n')
        itog.write('Уплотнитель из пористой резины "EPDM 150" с клеевым слоем, 5 мм х125 мм (цвет чёрный);' + str(
            L_epdm) + ';м.п.\n')
        itog.write(str(naz_sr) + ';' + str(isol_sr) + ';шт.\n' + str(naz_kr) + ';' + str(isol_kr) + ';шт.\n')
        itog.write('болт со срывной головкой;' + str(kol_b) + ';шт.\n')
        itog.write('держатель гайки;' + str(kol_b) + ';шт.\n')
        itog.write('индикатор температуры;' + str(kol) + ';шт.\n')
        itog.write('шайба пружинная;' + str(kol_b * 2) + ';шт.\n')
        itog.write('пружина тарельчатая;' + str(kol_b * 2) + ';шт.\n')
        itog.write('двойной скотч;' + str(L_skotch_dvoinoi) + ';шт.\n')
        itog.close()

    def pos(self, pl):#ПОС порошок
        plosh = self.s * 40 * pl * 16 + (self.s + 30) * 40 * pl * 16
        rash = round(plosh / 1000000 * 0.5, 2) * 2
        print('Порошковый материал ТР-63-25 ', rash, ' кг.')
        itog = open('itog_kol.txt', 'a')
        itog.write('Порошковый материал ТР-63-25;' + str(rash) + ';кг.\n')
        itog.close()

    def zel(self, nominal, os):#расчет эпоксидной изоляции
        per = self.s * 2 + 6
        plosh = per * 0.001 * os * 4
        ves = round(plosh * 0.35 * 2, 2)
        print('Порошковое эпоксидное покрытие Scotchcast 6233E ', ves, ' кг.')
        itog = open('itog_kol.txt', 'a')
        itog.write('Порошковое эпоксидное покрытие Scotchcast 6233E;' + str(ves) + ';кг.\n')
        itog.close()

    def plenka(self, os):#пленка
        L1 = round(self.s * 0.001 * os * 5 * 0.000125 * 1380, 2)
        L2 = round(40 * 0.001 * os * 2 * 0.000125 * 1380, 2)
        print(str(self.pet), L1, ' кг.')
        print('пленка ПЭТ ширина 40 мм.;', L2, ';кг.')
        itog = open('itog_kol.txt', 'a')
        itog.write('пленка ПЭТ ширина 40 мм.;' + str(L2) + ';кг.\n')
        itog.write(str(self.pet) + ';' + str(L1) + ';кг.\n')
        itog.close()

    def zaglishka(self, kol):
        zaglushka1 = self.ves_zag_tor * 2 * kol  # расчетвеса торцевой заглушки
        zaglushka2 = self.ves_zag_bok * 2 * kol  # расчет боковой заглушки
        zaglushka3 = 0.32 * 2 * kol  # расчет верхнего листа
        vse_ves = round(zaglushka1 + zaglushka2 + zaglushka3, 2)  # расчет веса всего листа толщиной 2 мм.
        print('Лист торцевой ', str(self.nominal), str(zaglushka1), ' кг.')
        print('Лист боковой ', str(self.nominal), str(zaglushka2), ' кг.')
        print('Лист верхний ', str(zaglushka3), ' кг.')
        print('Лист А5М 2х1200х3000  ГОСТ 21631-76 ', str(vse_ves), ' кг.')
        itog = open('itog_kol.txt', 'a')
        # itog.write('Лист торцевой;' + str(zaglushka1) + ';кг.\n')
        # itog.write('Лист боковой;' + str(zaglushka2) + ';кг.\n')
        # itog.write('Лист верхний;' + str(zaglushka3) + ';кг.\n')
        itog.write('Лист А5М 2х1200х3000 ГОСТ 21631-76;' + str(vse_ves) + ';кг.\n')
        itog.close()

    def flanec(self, kol):
        ves_flancev = self.ves_flanca * 2
        print('Лист АМГ6М 4х1200х3000  ГОСТ 21631-76 ', str(ves_flancev), ' кг.')
        itog = open('itog_kol.txt', 'a')
        itog.write('Лист АМГ6М 4х1200х3000  ГОСТ 21631-76;' + str(ves_flancev) + ';кг.\n')
        itog.close()

    def germetik(self, D):#расчет герметика на выводах
        L1 = self.s * 2 + 60
        L = D * 4 + L1
        V = 1.5 ** 2 * 3.14 * L / 1000000
        ves = V * 1300
        kol_ger = round(ves / 0.65, 1)
        print('Герметик полиуретановый "Соудал "Соудафлекс 40 FC" 600 мл, серый ', str(kol_ger), ' шт.')
        itog = open('itog_kol.txt', 'a')
        itog.write('Герметик полиуретановый "Соудал "Соудафлекс 40 FC" 600 мл, серый;' + str(kol_ger) + ';шт.\n')
        itog.close()

    def zak(self, L):
        k_zak = math.ceil(L * 1000 / 150 * 4)
        print('заклепка вытяжная 4.8х12  ', str(k_zak), ' шт.')
        itog = open('itog_kol.txt', 'a')
        itog.write('заклепка вытяжная 4.8х12;' + str(k_zak) + ';шт.\n')
        itog.close()
        return k_zak

    def bolt_m6(self, kol):
        kol_boltm6x16 = kol * 16
        kol_boltm6x10 = kol * 8
        kol_shaib = kol_boltm6x16 + kol_boltm6x10
        kol_klips = math.ceil(self.dlina / 3 * 4)
        kol_shaib = kol_klips * 2
        kol_shaibm6 = kol_boltm6x10 + kol_boltm6x16
        print('винт с цилиндрической головкой и внyтренним шестигранником М6х16  ', str(kol_boltm6x16), ' шт.')
        print('винт с цилиндрической головкой и внутренним шестигранником М6х10  ', str(kol_boltm6x10), ' шт.')
        print('винт с потайной головкой и внутренним шестигранником М6х16  ', str(kol_boltm6x10), ' шт.')
        print('шайба гровер 6  ', str(kol_shaibm6), ' шт.')
        print('винт с шестигранной головкой М10х25  ', str(kol_klips), ' шт.')
        print('шайба гровер 10  ', str(kol_klips), ' шт.')
        print('гайка шестигранная М10  ', str(kol_klips), ' шт.')
        print('шайба плоская С.10  ', str(kol_shaib), ' шт.')
        print('кронштейн  ', str(kol_klips), ' шт.')
        itog = open('itog_kol.txt', 'a')
        itog.write('винт с цилиндрической головкой и внутренним шестигранником М6х16;' + str(kol_boltm6x16) + ';шт.\n')
        itog.write('винт с цилиндрической головкой и внутренним шестигранником М6х10;' + str(kol_boltm6x10) + ';шт.\n')
        itog.write('винт с потайной головкой и внутренним шестигранником М6х16;' + str(kol_boltm6x10) + ';шт.\n')
        itog.write('шайба гровер 6;' + str(kol_shaibm6) + ';шт.\n')
        itog.write('винт с шестигранной головкой М10х25;' + str(kol_klips) + ';шт.\n')
        itog.write('шайба гровер 10;' + str(kol_klips) + ';шт.\n')
        itog.write('гайка шестигранная М10;' + str(kol_klips) + ';шт.\n')
        itog.write('шайба плоская С.10;' + str(kol_shaib) + ';шт.\n')
        itog.write('кронштейн;' + str(kol_klips) + ';шт.\n')
        itog.close()

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    a = vvod(2500, 48, 17, 17, 2, 2, 8)
    a.fg()