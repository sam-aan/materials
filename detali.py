import re
import math


class Detali:
    def __init__(self, os, input_data, coating, kol, tip, ABC, spis_kompl):
        self.name = input_data['Обозначение']    # Обозначение
        self.os = os  # Размер по осям
        self.material = input_data['Материал']
        self.seria = input_data['Серия']
        self.ip = input_data['ip']
        self.nominal = int(input_data['In'])  # вычислили номинал
        self.H_stenka = input_data['ширина стенки']  # ширина стенки
        self.H = input_data['ширина шины']  # ширина шины
        self.H_paketa = input_data['толщина пакета']  # толщина пакета
        self.S_sh = input_data['толщина шины']  # Толщина шины по умолчанию 6 мм.
        # расстояние развертки двойного гиба
        self.L1_sh_m = input_data['малый гиб']  # развертка малого гиба
        self.L1_sh_b = input_data['большой гиб']  # развертка большого гиба
        self.stp_L1 = input_data['СТП край вывод']
        self.stp_L2 = input_data['СТП центр вывод']
        self.L1Edge = input_data['фланец край']  # развертка крайней шины фланца
        self.L1Centre = input_data['фланец центр']  # развертка средней шины гиба
        self.StpEdge = input_data['СТП край']
        self.SptCentre = input_data['СТП центр']
        self.S_stenka = input_data['толщина стенки']
        self.S_sh_izol = input_data['толщина изоляции']
        self.H_krishka = input_data['ширина крышки']
        self.S_krishka = input_data['толщина крышки']
        self.S_krishka_sred = input_data['толщина крышки средней']
        self.R_sh = input_data['расстояние от оси до шины']
        self.R_kor = input_data['расстояние от оси до корпуса']
        # переменные для работы
        self.oboznachenie = ''
        self.naimenovanie = ''
        self.L = '-'
        self.L1 = '-'
        self.A = ABC[0]  #
        self.B = ABC[1]  #
        self.C = ABC[2]  #
        self.X = '-'
        self.Y = '-'
        self.Z = '-'
        self.a = []  # Возврать результата
        self.Nprov = input_data['Кол. пров.']
        self.Ka = input_data['K']       # К-фактор для гибов
        self.R = input_data['R']
        self.coating = coating          # цвет открашивания профиля
        self.kolN = kol                  # количество деталей в расчете
        self.tip = tip
        self.spis_kompl = spis_kompl        # словарь со списком комплектующих

    # Лист боковой
    def lb(self):
        nominal = {'630': 113, '800': 128, '1000': 153, '1250': 183,
                   '1600': 233, '2000': 273, '2500': 273, '2600': 299,
                   '3200': 399, '4000': 479, '5000': 479, '6300': '-'}
        self.A = 150
        self.B = nominal[str(self.nominal)]
        self.C = '-'
        self.oboznachenie = 'ЛБ'
        self.naimenovanie = 'Лист боковой'
        self.print_rezult()
        return self.a

    # Лист Верхний
    def lv(self):
        self.A = 150
        self.B = 138
        self.C = '-'
        self.oboznachenie = 'ЛВ'
        self.naimenovanie = 'Лист верхний'
        self.print_rezult()
        return self.a

    # Лист торцевой
    def lt(self):
        nominal = {'630': 117, '800': 132, '1000': 153, '1250': 187,
                   '1600': 237, '2000': 277, '2500': 277, '2600': 303, '3200': 403, '4000': 483, '5000': 483, '6300': '-'}
        self.A = 138
        self.B = nominal[str(self.nominal)]
        self.C = '-'
        self.oboznachenie = 'ЛТ'
        self.naimenovanie = 'Лист торцевой'
        self.print_rezult()
        return self.a

    # заглушки  !!! для 2500 неверная !!!
    def A000_774_01(self):
        if self.material == 'Al':
            nominal = {'630': [70, 56, 42], '800': [85, 71, 57], '1000': [110, 96, 82], '1250': [140, 126, 112],
                       '1600': [190, 176, 162], '2000': [230, 216, 202], '2500': [240, 220, 202], '2600': [240, 220, 202]}
        else:
            nominal = {'800': [70, 56, 42], '1000': [85, 71, 57], '1250': [110, 96, 82], '1600': [140, 126, 112],
                       '2000': [190, 176, 162], '2500': [200, 180, 162]}
        self.A = nominal[str(self.nominal)][0]
        self.B = nominal[str(self.nominal)][1]
        self.C = nominal[str(self.nominal)][2]
        self.oboznachenie = '000 774-01'
        self.naimenovanie = 'Заглушка для шины ТМ'
        self.print_rezult()
        return self.a

    # заглушки  !!! для 2500 неверная !!!
    def A000_774_02(self):
        if self.material == 'Al':
            nominal = {'630': [70, 56, 42], '800': [85, 71, 57], '1000': [110, 96, 82], '1250': [140, 126, 112],
                       '1600': [190, 176, 162], '2000': [230, 216, 202], '2500': [240, 220, 202], '2600': [240, 220, 202]}
        else:
            nominal = {'800': [70, 56, 42], '1000': [85, 71, 57], '1250': [110, 96, 82], '1600': [140, 126, 112],
                       '2000': [190, 176, 162], '2500': [200, 180, 162]}
        self.A = nominal[str(self.nominal)][0]
        self.B = nominal[str(self.nominal)][1]
        self.C = nominal[str(self.nominal)][2]
        self.oboznachenie = '000 774-02'
        self.naimenovanie = 'Заглушка для шины ТМ'
        self.print_rezult()
        return self.a

    # Уголок
    def u(self):
        self.L = float(self.H_stenka)
        self.oboznachenie = 'У'
        self.naimenovanie = 'Уголок_25х25х3'
        self.A = '-'  #
        self.B = '-'  #
        self.C = '-'  #
        self.print_rezult()
        return self.a

    # фланец
    def fl(self):
        if self.material == 'Al':  # алюминий
            L = {'630': [182, 200], '800': [200, 200], '1000': [226, 200], '1250': [249, 200], '1600': [305, 200],
                 '2000': [351, 200], '2500': [351, 245], '3200': [504, 245], '3201': [504, 245], '2600': [504, 245],
                 '4000': [596, 245], '5000': [596, 245], '6300': [763, 245]}
        else:
            L = {'630': ['X', 'Y'], '1000': [200, 200], '1250': [226, 200], '1600': [249, 200], '2000': [305, 200],
                 '2500': [305, 200], '3200': ['X', 'Y'], '3201': ['X', 'Y'], '4000': [504, 245], '5000': [504, 245], '6300': ['X', 'Y']}
        self.A = L[str(self.nominal)][0]
        self.B = L[str(self.nominal)][1]
        self.oboznachenie = '000 168'
        self.naimenovanie = 'Фланец'
        self.print_rezult()
        return self.a

    # Токопроводящая пластина
    def tp(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.oboznachenie = 'ТП'
        self.naimenovanie = 'Пластина токопроводящая'
        if self.material == 'Al':  # алюминий
            L = {'250': 30, '400': 68, '630': 66, '800': 80, '1000': 108, '1250': 138, '1600': 185, '2000': 226,
                 '2500': 226, '2600': 226, '3200': 360, '3201': 360,
                 '4000': 434, '5000': 434, '6300': 660}
            if str(self.nominal) == '2500' or str(self.nominal) == '5000':
                self.profil(['профиль', self.naimenovanie + ' 2500', self.oboznachenie + '_2500', '90 90'], L[str(self.nominal)])
            else:
                self.profil(['профиль', self.naimenovanie, self.oboznachenie, '90 90'], L[str(self.nominal)])
        else:
            L = {'630': 66, '800': 66, '1000': 80, '1250': 108, '1600': 138, '2000': 185, '2500': 185, '3200': 234,
                 '4000': 360, '5000': 360, '6300': 540}
            if str(self.nominal) == '2500' or str(self.nominal) == '5000':
                self.profil(['профиль', self.naimenovanie + ' медная 2500', self.oboznachenie + '_2500', '90 90'], L[str(self.nominal)])
            else:
                self.profil(['профиль', self.naimenovanie + ' медная', self.oboznachenie, '90 90'], L[str(self.nominal)])
        self.L = L[str(self.nominal)]
        self.print_rezult()
        return self.a

    def vtulka(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        if self.nominal != 2500 or self.nominal != 6300:
            self.L = 72
        else:
            self.L = 86
        self.oboznachenie = 'В'
        self.naimenovanie = 'Втулка'
        self.print_rezult()
        return self.a

    def ksb(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.oboznachenie = 'КСБ'
        self.naimenovanie = 'Крышка стыка'
        self.print_rezult()
        return self.a

    def dp(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.oboznachenie = 'Д'
        self.naimenovanie = 'Демпфер'
        self.print_rezult()
        return self.a

    def izol_k(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.oboznachenie = 'ИК'
        self.naimenovanie = 'Изолятор крайний'
        self.print_rezult()
        return self.a

    def izol_s(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.oboznachenie = 'ИС'
        self.naimenovanie = 'Изолятор средний'
        self.print_rezult()
        return self.a

    # Стенка стыка
    def ss(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'

        if self.nominal < 2500:
            self.L = self.H_stenka + self.S_krishka * 2
        elif self.nominal > 2500 and self.nominal < 6300:
            self.L = self.H_stenka * 2 + 3 + self.S_krishka * 2
        else:   # для 6300
            self.L = self.H_stenka * 3 + 6 + self.S_krishka * 2

        self.oboznachenie = 'СС'
        self.naimenovanie = 'Стенка стыка'
        self.profil(['профиль', 'Стенка стыка (Заготовка)', self.oboznachenie, '90 90'], self.L)
        self.print_rezult()
        return self.a

    # Сухарь
    def sux(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = 40
        self.oboznachenie = 'СУ'
        self.naimenovanie = 'Сухарь'
        self.print_rezult()
        self.profil(['профиль', 'Сухарь (Заготовка)', self.oboznachenie, '90 90'], self.L)
        return self.a

    # Направляющая
    def n(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'

        if self.nominal <= 2500:
            self.L = self.H_stenka + self.S_krishka * 2
        elif self.nominal > 2500 and self.nominal < 6300:
            self.L = self.H_stenka * 2 + 3 + self.S_krishka * 2
        else:   # для 6300
            self.L = self.H_stenka * 3 + 6 + self.S_krishka * 2

        self.oboznachenie = 'Н'
        self.naimenovanie = 'Направляющая'

        if self.nominal in [2500, 5000]:
            s = ['профиль', self.naimenovanie + '2500(Заготовка)', self.oboznachenie + '_2500', '90 90']
        else:
            s = ['профиль', self.naimenovanie, self.oboznachenie, '90 90']

        self.print_rezult()
        self.profil(s, self.L)
        return self.a

    # Заглушка для трансформаторной секции
    def zts(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        if self.material == 'Al':  # алюминий
            L = {'630': 109, '800': 124, '1000': 149, '1250': 179, '1600': 229, '2000': 269, '2500': 269, '3200': 395,
                 '4000': 475, '5000': 475, '6300': 681}
        else:
            L = {'630': 109, '800': 124, '1000': 149, '1250': 149, '1600': 179, '2000': 229, '2500': 229, '3200': 295,
                 '4000': 395, '5000': 395, '6300': 561}
        self.L1 = '-'
        self.L = L[str(self.nominal)]
        self.oboznachenie = 'З-ТС'
        self.naimenovanie = 'Заглушка'
        self.print_rezult()
        return self.a

    # Центователи для CR1
    def torcentr(self):
        self.L = float(self.H) + 40
        self.L1 = 100
        self.oboznachenie = 'ТЦ'
        self.naimenovanie = 'Торцевой центрователь'
        self.A = '-'  #
        self.B = '-'  #
        self.C = '-'  #
        self.print_rezult()
        return self.a

    def mfazcentr(self):
        self.L = 40
        self.L1 = 90
        self.oboznachenie = 'МЦ'
        self.naimenovanie = 'Межфазный центрователь'
        self.A = '-'  #
        self.B = '-'  #
        self.C = '-'  #
        self.print_rezult()
        return self.a

    def k(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'

        if self.name in ['тв', 'tv']:
            self.L = float(self.os[0]) + float(self.os[1]) - float(self.R_kor) * 2
        elif self.name in ['пф', 'pf']:
            self.L = float(self.os) - float(self.R_kor) - 4
        elif self.name in ['тс', 'tsv']:
            self.L = float(self.os[0]) - float(self.R_kor)
        else:
            self.L = float(self.os) - float(self.R_kor) * 2

        if self.coating == 's':
            self.naimenovanie = 'Крышка крашенная'
            self.oboznachenie = 'К-кр'
            s = ['профиль', 'Крышка окрашенная 2.82м.', 'К_к_2.82', '90 90']
        else:
            self.naimenovanie = 'Крышка'
            self.oboznachenie = 'К'
            s = ['профиль', 'Крышка без покрытия 3м.', 'К_нк_3', '90 90']

        self.print_rezult()
        self.profil(s, self.L)
        return self.a

    def k1(self):
        self.A = '-'
        self.B = '-'

        if self.name in ['ug', 'uv', 'uvf', 'ugf']:
            Alfa = (180 - int(self.C)) / 2
        else:
            Alfa = 45
            self.C = '-'

        self.L = round(float(self.os) - float(self.R_kor) + float(self.H_krishka) / 2 * math.tan(math.radians(Alfa)), 1)
        self.oboznachenie = 'К1'
        self.naimenovanie = 'Крышка'
        self.print_rezult()
        self.profil(['профиль', 'Крышка без покрытия 3м.', 'К_нк_3', '90 +45'], self.L)
        return self.a

    def k1f(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.H_krishka) / 2 - 4
        self.oboznachenie = 'К1'
        self.naimenovanie = 'Крышка'
        self.print_rezult()
        self.profil(['профиль', 'Крышка без покрытия 3м.', 'К_нк_3', '90 +45'], self.L)
        return self.a

    def k2(self):
        self.A = '-'
        self.B = '-'

        if self.name in ['ug', 'uv', 'uvf', 'ugf']:
            Alfa = (180 - int(self.C)) / 2
        else:
            Alfa = 45
            self.C = '-'

        self.L = round(float(self.os) - float(self.R_kor) + float(self.H_krishka) / 2 * math.tan(math.radians(Alfa)), 1)
        self.oboznachenie = 'К2'
        self.naimenovanie = 'Крышка'
        self.print_rezult()
        self.profil(['профиль', 'Крышка без покрытия 3м.', 'К_нк_3', '90 -45'], self.L)
        return self.a

    def k2f(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.H_krishka) / 2 - 4
        self.oboznachenie = 'К2'
        self.naimenovanie = 'Крышка'
        self.print_rezult()
        self.profil(['профиль', 'Крышка без покрытия 3м.', 'К_нк_3', '90 -45'], self.L)
        return self.a

    def k3(self):
        self.A = '-'
        self.B = '-'

        if self.name in ['ug', 'ugf']:
            Alfa = int(self.C) / 2
        else:
            Alfa = 45
            self.C = '-'

        if int(self.nominal) >= 1600:
            self.L = float(self.os) - float(self.R_kor) + float(self.H_stenka) / 2 / math.tan(math.radians(Alfa)) + float(self.S_krishka) + 1
        else:
            self.L = float(self.os) - float(self.R_kor) + float(self.H_stenka) / 2 / math.tan(math.radians(Alfa)) + float(self.S_krishka)
        #print(str(self.os) + '-' + str(self.R_kor) + '+' + str(self.H_stenka) + '/2+' + str(self.S_krishka) + '=' + str(self.L))
        self.oboznachenie = 'К3'
        self.naimenovanie = 'Крышка'
        self.print_rezult()
        self.profil(['профиль', 'Крышка без покрытия 3м.', 'К_нк_3', '90 +45s'], self.L)
        return self.a

    # для УВФ и ЗВФ
    def k3f(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        #print('угол вертикальный крыка')
        self.L = float(self.os) + float(self.H_stenka) / 2 + float(self.S_krishka) - 4
        #print(str(self.os) + '-' + str(self.R_kor) + '+' + str(self.H_stenka) + '/2+' + str(self.S_krishka) + '=' + str(self.L))
        self.oboznachenie = 'К3'
        self.naimenovanie = 'Крышка'
        self.print_rezult()
        self.profil(['профиль', 'Крышка без покрытия 3м.', 'К_нк_3', '90 +45s'], self.L)
        return self.a

    def k4(self):
        self.A = '-'
        self.B = '-'

        if self.name in ['ug', 'ugf']:
            Alfa = int(self.C) / 2
        else:
            Alfa = 45
            self.C = '-'

        self.L = round(float(self.os) - float(self.R_kor) - float(self.H_stenka) / 2 / math.tan(math.radians(Alfa)), 1)
        #print(str(float(self.os)) + '-' + str(float(self.R_kor))  + '-' + str(float(self.H_stenka)) + '/' + '2' + '=' + str(self.L))
        self.oboznachenie = 'К4'
        self.naimenovanie = 'Крышка'
        self.print_rezult()
        self.profil(['профиль', 'Крышка без покрытия 3м.', 'К_нк_3', '90 -45s'], self.L)
        return self.a

    # для УВФ и ЗВФ
    def k4f(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - float(self.H_stenka) / 2 - 4
        #print(str(float(self.os)) + '-' + str(float(self.R_kor)) + '-' + str(float(self.H_stenka)) + '/' + '2' + '=' + str(self.L))
        self.oboznachenie = 'К4'
        self.naimenovanie = 'Крышка'
        self.print_rezult()
        self.profil(['профиль', 'Крышка без покрытия 3м.', 'К_нк_3', '90 -45s'], self.L)
        return self.a

    # для ТВ двухэтажной
    def k4t(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - float(self.R_kor) - float(self.H_stenka) - 1.5
        # print(str(float(self.os)) + '-' + str(float(self.R_kor))  + '-' + str(float(self.H_stenka)) + '/' + '2' + '=' + str(self.L))
        self.oboznachenie = 'К4'
        self.naimenovanie = 'Крышка'
        self.print_rezult()
        self.profil(['профиль', 'Крышка без покрытия 3м.', 'К_нк_3', '90 -45s'], self.L)
        return self.a

    def k5(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.H_krishka)
        self.oboznachenie = 'К5'
        self.naimenovanie = 'Крышка'
        self.print_rezult()
        self.profil(['профиль', 'Крышка без покрытия 3м.', 'К_нк_3', '-45 +45'], self.L)
        return self.a

    def k7(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.H_krishka)
        self.oboznachenie = 'К7'
        self.naimenovanie = 'Крышка'
        self.print_rezult()
        self.profil(['профиль', 'Крышка без покрытия 3м.', 'К_нк_3', '+45 +45'], self.L)
        return self.a

    def k8(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.H_krishka)
        self.oboznachenie = 'К8'
        self.naimenovanie = 'Крышка'
        self.print_rezult()
        self.profil(['профиль', 'Крышка без покрытия 3м.', 'К_нк_3', '-45 -45'], self.L)
        return self.a

    def k9(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.S_krishka)
        self.oboznachenie = 'К9'
        self.naimenovanie = 'Крышка'
        self.print_rezult()
        self.profil(['профиль', 'Крышка без покрытия 3м.', 'К_нк_3', '+45s -45s'], self.L)
        return self.a

    def k11(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.H_stenka) + float(self.S_krishka) * 2
        self.oboznachenie = 'К11'
        self.naimenovanie = 'Крышка'
        self.print_rezult()
        self.profil(['профиль', 'Крышка без покрытия 3м.', 'К_нк_3', '+45s +45s'], self.L)
        return self.a

    def k12(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.H_stenka)
        self.oboznachenie = 'К12'
        self.naimenovanie = 'Крышка'
        self.print_rezult()
        self.profil(['профиль', 'Крышка без покрытия 3м.', 'К_нк_3', '-45s -45s'], self.L)
        return self.a

    def k13(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.H_krishka) / 2 + float(self.H_stenka) / 2 + float(self.S_krishka)
        self.oboznachenie = 'К13'
        self.naimenovanie = 'Крышка'
        self.print_rezult()
        self.profil(['профиль', 'Крышка без покрытия 3м.', 'К_нк_3', '+45s +45'], self.L)
        return self.a

    def k14(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.H_krishka) / 2 + float(self.H_stenka) / 2 + float(self.S_krishka)
        self.oboznachenie = 'К14'
        self.naimenovanie = 'Крышка'
        self.print_rezult()
        self.profil(['профиль', 'Крышка без покрытия 3м.', 'К_нк_3', '+45s -45'], self.L)
        return self.a

    def k15(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.H_krishka) / 2 - float(self.H_stenka) / 2
        self.oboznachenie = 'К15'
        self.naimenovanie = 'Крышка'
        self.print_rezult()
        self.profil(['профиль', 'Крышка без покрытия 3м.', 'К_нк_3', '-45s +45'], self.L)
        return self.a

    def k16(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.H_krishka) / 2 - float(self.H_stenka) / 2
        self.oboznachenie = 'К16'
        self.naimenovanie = 'Крышка'
        self.print_rezult()
        self.profil(['профиль', 'Крышка без покрытия 3м.', 'К_нк_3', '-45s -45'], self.L)
        return self.a

    # крышка с отверситем для втычной розетки для типов 1 и 2
    def k18(self):
        if int(self.tip[0]) in [1, 2]:
            self.B = '-'
            self.C = '-'
            self.L = float(self.os) - float(self.R_kor) * 2
            self.A = str(float(self.A) - float(self.R_kor))
        self.naimenovanie = 'Крышка крашенная'
        self.oboznachenie = 'К18'
        self.print_rezult()
        self.profil(['профиль', 'Крышка окрашенная 2.82м.', 'К_к_2.82', '90 90'], self.L)
        return self.a

    # крышка с отверситем для втычной розетки для типов 3 и 4
    def k18_01(self):
        self.C = '-'
        self.L = float(self.os) - float(self.R_kor) * 2
        self.A = str(float(self.A) - float(self.R_kor))
        self.naimenovanie = 'Крышка крашенная'
        self.oboznachenie = 'К18-01'
        self.print_rezult()
        self.profil(['профиль', 'Крышка окрашенная 2.82м.', 'К_к_2.82', '90 90'], self.L)
        return self.a

    # крышка с отверситем для втычной розетки для типов 5 и 6
    def k18_02(self):
        self.C = '-'
        self.L = float(self.os) - float(self.R_kor) * 2
        self.A = str(float(self.A) - float(self.R_kor))
        self.naimenovanie = 'Крышка крашенная'
        self.oboznachenie = 'К18-02'
        self.print_rezult()
        self.profil(['профиль', 'Крышка окрашенная 2.82м.', 'К_к_2.82', '90 90'], self.L)
        return self.a

    def k19(self):      # крышка для трансформаторной секции
        #print('self.os', self.os)
        self.L = float(self.os[0]) - float(self.R_kor)
        self.L1 = float(self.os[1]) - float(self.R_kor)
        self.A = float(self.os[2])
        self.B = float(self.os[3])
        self.C = float(self.os[4])
        self.oboznachenie = 'К19'
        self.naimenovanie = 'Крышка'
        self.print_rezult()
        self.profil(['профиль', 'Крышка окрашенная 2.82м.', 'К_к_2.82', '90 90'], self.L)
        return self.a

    def k20(self):      # крышка для отбора мощности с фиксированным выводом
        #print('self.os', self.os)
        self.L = float(self.os[0]) - float(self.R_kor)
        self.L1 = float(self.os[1]) - float(self.R_kor)
        self.A = float(self.os[2])
        self.B = float(self.os[3])
        self.C = float(self.os[4])
        self.oboznachenie = 'К19'
        self.naimenovanie = 'Крышка'
        self.print_rezult()
        self.profil(['профиль', 'Крышка окрашенная 2.82м.', 'К_к_2.82', '90 90'], self.L)
        return self.a

    def k21(self):      # крышка для отбора мощности с фиксированным выводом
        #print('self.os', self.os)
        self.L = float(self.os[0]) - float(self.R_kor)
        self.L1 = float(self.os[1]) - float(self.R_kor)
        self.A = float(self.os[2])
        self.B = float(self.os[3])
        self.C = float(self.os[4])
        self.oboznachenie = 'К19'
        self.naimenovanie = 'Крышка'
        self.print_rezult()
        self.profil(['профиль', 'Крышка окрашенная 2.82м.', 'К_к_2.82', '90 90'], self.L)
        return self.a

    # крышка с выступом
    def kv(self):  # N это длина по оси КРЫШКИ
        self.A = '-'
        self.B = '-'
        self.C = '-'
        if self.name in ['тв', 'tv']:
            self.L = float(self.os[0]) + float(self.os[1]) - float(self.R_kor) * 2
        elif self.name in ['пф', 'pf', 'pfk']:
            self.L = float(self.os) - float(self.R_kor) - 4
        elif self.name in ['тс', 'tsv']:
            self.L = float(self.os[0]) - float(self.R_kor)
        else:
            self.L = float(self.os) - float(self.R_kor) * 2
        if self.coating == 's':
            self.naimenovanie = 'Крышка с выступом крашенная'
            self.oboznachenie = 'КВ-кр'
            s = ['профиль', 'Крышка с выступом окрашенная 2.82м.', 'КВ_к_2.82', '90 90']
        else:
            self.naimenovanie = 'Крышка с выступом'
            self.oboznachenie = 'КВ'
            s = ['профиль', 'Крышка с выступом 2.82м.', 'КВ_нк_2.82', '90 90']
        self.print_rezult()
        self.profil(s, self.L)
        return self.a

    # для фланца крышка с вычетом плюс 118.5
    def kva(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - float(self.R_kor) - 4
        self.oboznachenie = 'КВ'
        self.naimenovanie = 'Крышка с выступом крашенная'
        self.print_rezult()
        self.profil(['профиль', 'Крышка с выступом окрашенная 2.82м.', 'КВ_к_2.82', '90 90'], self.L)
        return self.a

    # крышка с выступом с отверситем для втычной розетки для типов 1 и 2
    def kv18(self):
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - float(self.R_kor) * 2
        self.A = str(float(self.A) - float(self.R_kor))
        self.naimenovanie = 'Крышка с выступом крашенная'
        self.oboznachenie = 'КВ18'
        self.print_rezult()
        self.profil(['профиль', 'Крышка с выступом окрашенная 2.82м.', 'КВ_к_2.82', '90 90'], self.L)
        return self.a

    # крышка с выступом с отверситем для втычной розетки для типов 3 и 4
    def kv18_01(self):
        self.C = '-'
        self.L = float(self.os) - float(self.R_kor) * 2
        self.A = str(float(self.A) - float(self.R_kor))
        self.naimenovanie = 'Крышка с выступом крашенная'
        self.oboznachenie = 'КВ18-01'
        self.print_rezult()
        self.profil(['профиль', 'Крышка с выступом окрашенная 2.82м.', 'КВ_к_2.82', '90 90'], self.L)
        return self.a

    # крышка с выступом с отверситем для втычной розетки для типов 5 и 6
    def kv18_02(self):
        self.C = '-'
        self.L = float(self.os) - float(self.R_kor) * 2
        self.A = str(float(self.A) - float(self.R_kor))
        self.naimenovanie = 'Крышка с выступом крашенная'
        self.oboznachenie = 'КВ18-02'
        self.print_rezult()
        self.profil(['профиль', 'Крышка с выступом окрашенная 2.82м.', 'КВ_к_2.82', '90 90'], self.L)
        return self.a

    # крышка с выступом для отбора мощности с фиксированным выводом
    def kv20(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        if self.name in ['тв', 'tv']:
            self.L = float(self.os[0]) + float(self.os[1]) - float(self.R_kor) * 2
        elif self.name in ['пф', 'pf', 'pfk']:
            self.L = float(self.os) - float(self.R_kor) - 4
        elif self.name in ['тс', 'tsv']:
            self.L = float(self.os[0]) - float(self.R_kor)
        else:
            self.L = float(self.os) - float(self.R_kor) * 2
        if self.coating == 's':
            self.naimenovanie = 'Крышка с выступом крашенная'
            self.oboznachenie = 'КВ-кр'
            s = ['профиль', 'Крышка с выступом окрашенная 2.82м.', 'КВ_к_2.82', '90 90']
        else:
            self.naimenovanie = 'Крышка с выступом'
            self.oboznachenie = 'КВ'
            s = ['профиль', 'Крышка с выступом 2.82м.', 'КВ_нк_2.82', '90 90']
        self.print_rezult()
        self.profil(s, self.L)
        return self.a

    # крышка с выступом для отбора мощности с фиксированным выводом
    def kv21(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        if self.name in ['тв', 'tv']:
            self.L = float(self.os[0]) + float(self.os[1]) - float(self.R_kor) * 2
        elif self.name in ['пф', 'pf', 'pfk']:
            self.L = float(self.os) - float(self.R_kor) - 4
        elif self.name in ['тс', 'tsv']:
            self.L = float(self.os[0]) - float(self.R_kor)
        else:
            self.L = float(self.os) - float(self.R_kor) * 2
        if self.coating == 's':
            self.naimenovanie = 'Крышка с выступом крашенная'
            self.oboznachenie = 'КВ-кр'
            s = ['профиль', 'Крышка с выступом окрашенная 2.82м.', 'КВ_к_2.82', '90 90']
        else:
            self.naimenovanie = 'Крышка с выступом'
            self.oboznachenie = 'КВ'
            s = ['профиль', 'Крышка с выступом 2.82м.', 'КВ_нк_2.82', '90 90']
        self.print_rezult()
        self.profil(s, self.L)
        return self.a

    # стенка
    # стенка крашенная используется для прямых секций
    def c(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        if self.name in ['пф', 'pf', 'pfk']:
            self.L = float(self.os) - float(self.R_kor) - 4
        elif self.name in ['п', 'тг', 'ом', 'pt', 'tg']:
            self.L = float(self.os) - float(self.R_kor) * 2 - 1
        elif self.name in ['уг', 'угф', 'ug', 'ugf']:
            self.L = float(self.os) - float(self.R_kor) + float(self.H_paketa) / 2
        elif self.name in ['тс', 'tsv']:
            self.L = float(self.os[0]) - float(self.R_kor)
        else:
            self.L = 'неизветсно'
        if self.coating == 's':
            self.oboznachenie = 'С-кр'
            self.naimenovanie = 'Стенка крашенная'
            nominal = self.print_rezult()
            self.profil(['профиль', 'Стенка ' + str(nominal) + ' окрашенный 2.82м.', 'С_' + str(nominal) + '_к_2.82', '90 90'], self.L)
        else:
            self.oboznachenie = 'С'
            self.naimenovanie = 'Стенка'
            nominal = self.print_rezult()
            self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' + str(nominal) + '_нк_3', '90 90'], self.L)
        return self.a

    # стенка для С-СД2. то же что и С4 минус 25 мм. ВНУТРЕНЯЯ
    def cA(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - float(self.R_kor) - float(self.H_paketa) / 2 - self.S_stenka
        #print('!!!!!!!!', self.os, self.R_kor, self.H_paketa)
        self.oboznachenie = 'С'
        self.naimenovanie = 'Стенка'
        nominal = self.print_rezult()
        self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' + str(nominal) + '_нк_3', '90 90'], self.L)
        return self.a

    # стенка для С-СД2. то же что и С4 минус 25 мм. ВНУТРЕНЯЯ ДЛЯ ФЛАНЦЕВ!
    def cAf(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - float(self.H_paketa) / 2 - self.S_stenka - 4
        #print('!!!!!!!!', self.os, self.R_kor, self.H_paketa)
        self.oboznachenie = 'С'
        self.naimenovanie = 'Стенка'
        nominal = self.print_rezult()
        self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' + str(nominal) + '_нк_3', '90 90'], self.L)
        return self.a

    # стенка для замены С-СД3 для номинала 2000А. то же что и С3 без ширины стенки ВНЕШНЯЯ
    def cB(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - float(self.R_kor) + float(self.H_paketa) / 2
        self.oboznachenie = 'С'
        self.naimenovanie = 'Стенка'
        nominal = self.print_rezult()
        self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' + str(nominal) + '_нк_3', '90 90'], self.L)
        return self.a

    # стенка для замены С-СД3 для номинала 2000А. то же что и С3 без ширины стенки ВНЕШНЯЯ ДЛЯ ФЛАНЦЕВ!
    def cBf(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.H_paketa) / 2 - 4
        self.oboznachenie = 'С'
        self.naimenovanie = 'Стенка'
        nominal = self.print_rezult()
        self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' + str(nominal) + '_нк_3', '90 90'], self.L)
        return self.a

    # стенка для Z горизонтальной для оси Y внешняя
    def cC(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - self.S_stenka
        self.oboznachenie = 'С'
        self.naimenovanie = 'Стенка'
        nominal = self.print_rezult()
        self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' + str(nominal) + '_нк_3', '90 90'], self.L)
        return self.a

    # для ТВ
    def ct(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os[0]) + float(self.os[1]) - float(self.R_kor) * 2
        self.oboznachenie = 'С'
        self.naimenovanie = 'Стенка'
        nominal = self.print_rezult()
        self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' + str(nominal) + '_нк_3', '90 90'], self.L)
        return self.a

    # для ТВ по оси Z
    def ctz(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        if self.nominal in [3200, 4000, 5000]:      # для ТВ по оси Z для двухэтажной секции
            self.L = float(self.os) - float(self.R_kor) - float(self.H_stenka) - 1.5
        else:
            self.L = float(self.os) - float(self.R_kor) - float(self.H_stenka) / 2
        self.oboznachenie = 'С'
        self.naimenovanie = 'Стенка'
        nominal = self.print_rezult()
        self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' + str(nominal) + '_нк_3', '90 90'], self.L)
        return self.a

    def c1(self):
        self.A = '-'
        self.B = '-'

        if self.name in ['ug', 'ugf']:
            Alfa = int(self.C) / 2
        else:
            Alfa = 45
            self.C = '-'

        self.L = float(self.os) - float(self.R_kor) + float(self.H_stenka) / 2 / math.tan(math.radians(Alfa))
        self.oboznachenie = 'С1'
        self.naimenovanie = 'Стенка'
        nominal = self.print_rezult()
        self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' + str(nominal) + '_нк_3', '90 +45'], self.L)
        return self.a

    # для УВФ и ЗВФ
    def c1f(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.H_stenka) / 2 - 4
        self.oboznachenie = 'С1'
        self.naimenovanie = 'Стенка'
        nominal = self.print_rezult()
        self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' + str(nominal) + '_нк_3', '90 +45'], self.L)
        return self.a

    # Для средней оси "y" комбинированной секции
    def c1a(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        if self.name in ['кп', 'kp']:
            self.L = float(self.os) + float(self.H_stenka) / 2 + float(self.H_paketa) / 2
        elif self.name in ['кл', 'kl']:
            self.L = float(self.os) + float(self.H_stenka) / 2 - float(self.H_paketa) / 2 - float(self.S_stenka)
        self.oboznachenie = 'С1'
        self.naimenovanie = 'Стенка'
        nominal = self.print_rezult()
        self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' + str(nominal) + '_нк_3', '90 +45'], self.L)
        return self.a

    def c2(self):
        self.A = '-'
        self.B = '-'

        if self.name in ['ug', 'ugf']:
            Alfa = int(self.C) / 2
        else:
            Alfa = 45
            self.C = '-'

        self.L = float(self.os) - float(self.R_kor) + float(self.H_stenka) / 2 / math.tan(math.radians(Alfa))
        self.oboznachenie = 'С2'
        self.naimenovanie = 'Стенка'
        nominal = self.print_rezult()
        self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' + str(nominal) + '_нк_3', '90 -45'], self.L)
        return self.a

    # для УВФ и ЗВФ
    def c2f(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.H_stenka) / 2 - 4
        self.oboznachenie = 'С2'
        self.naimenovanie = 'Стенка'
        nominal = self.print_rezult()
        self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' + str(nominal) + '_нк_3', '90 -45'], self.L)
        return self.a

    # Для средней оси "y" комбинированной секции
    def c2a(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        if self.name in ['кп', 'kp']:
            self.L = float(self.os) + float(self.H_stenka) / 2 - float(self.H_paketa) / 2 - float(self.S_stenka)
        elif self.name in ['кл', 'kl']:
            self.L = float(self.os) + float(self.H_stenka) / 2 + float(self.H_paketa) / 2
        self.oboznachenie = 'С2'
        self.naimenovanie = 'Стенка'
        nominal = self.print_rezult()
        self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' + str(nominal) + '_нк_3', '90 -45'], self.L)
        return self.a

    def c3(self):
        self.A = '-'
        self.B = '-'
        Alfa = (180 - int(self.C)) / 2

        if self.seria in ['CR1', 'CR2']:
            self.L = round(float(self.os) - float(self.R_kor) + (float('100') / 2 + float(self.S_stenka)) * math.tan(math.radians(Alfa)), 1)
        else:
            self.L = round(float(self.os) - float(self.R_kor) + (float(self.H_paketa) / 2 + float(self.S_stenka)) * math.tan(math.radians(Alfa)), 1)

        self.oboznachenie = 'С3'
        self.naimenovanie = 'Стенка'
        nominal = self.print_rezult()
        self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' + str(nominal) + '_нк_3', '90 +45s'], self.L)
        return self.a

    # Стенка для С-СД4 замена С9
    def c3a(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os)
        self.oboznachenie = 'С3'
        self.naimenovanie = 'Стенка'
        nominal = self.print_rezult()
        self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' + str(nominal) + '_нк_3', '90 +45s'], self.L)
        return self.a

    def c4(self):
        self.A = '-'
        self.B = '-'
        Alfa = (180 - int(self.C)) / 2

        if self.seria in ['CR1', 'CR2']:
            self.L = round(float(self.os) - float(self.R_kor) - 100 / 2 * math.tan(math.radians(Alfa)), 1)
        else:
            self.L = round(float(self.os) - float(self.R_kor) - float(self.H_paketa) / 2 * math.tan(math.radians(Alfa)), 1)

        self.oboznachenie = 'С4'
        self.naimenovanie = 'Стенка'
        nominal = self.print_rezult()
        self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' + str(nominal) + '_нк_3', '90 -45s'], self.L)
        return self.a

    # для Z-горизонтальной с фланцем
    def c3f(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.H_paketa) / 2 + float(self.S_stenka) - 4
        self.oboznachenie = 'С3'
        self.naimenovanie = 'Стенка'
        nominal = self.print_rezult()
        self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' + str(nominal) + '_нк_3', '90 +45s'], self.L)
        return self.a

    def c4f(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - float(self.H_paketa) / 2 - 4
        self.oboznachenie = 'С4'
        self.naimenovanie = 'Стенка'
        nominal = self.print_rezult()
        self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' + str(nominal) + '_нк_3', '90 -45s'], self.L)
        return self.a

    def c5(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.H_stenka)
        self.oboznachenie = 'С5'
        self.naimenovanie = 'Стенка'
        nominal = self.print_rezult()
        self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' + str(nominal) + '_нк_3', '-45 +45'], self.L)
        return self.a

    def c7(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.H_stenka)
        # print(str(self.os) + ' + ' + str(self.H_stenka) + ' = ' + str(self.L))
        self.oboznachenie = 'С7'
        self.naimenovanie = 'Стенка'
        nominal = self.print_rezult()
        self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' +str(nominal) + '_нк_3', '+45 +45'], self.L)
        return self.a

    def c8(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.H_stenka)
        self.oboznachenie = 'С8'
        self.naimenovanie = 'Стенка'
        nominal = self.print_rezult()
        self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' + str(nominal) + '_нк_3', '-45 -45'], self.L)
        return self.a

    def c9(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.S_stenka)
        self.oboznachenie = 'С9'
        self.naimenovanie = 'Стенка'
        nominal = self.print_rezult()
        self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' + str(nominal) + '_нк_3', '-45s -45s'], self.L)
        return self.a

    def c11(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.S_stenka) * 2 + float(self.H_paketa)
        self.oboznachenie = 'С11'
        self.naimenovanie = 'Стенка'
        nominal = self.print_rezult()
        self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' + str(nominal) + '_нк_3', '-45s +45s'], self.L)
        return self.a

    def c12(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - float(self.H_paketa)
        self.oboznachenie = 'С12'
        self.naimenovanie = 'Стенка'
        nominal = self.print_rezult()
        self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' + str(nominal) + '_нк_3', '+45s -45s'], self.L)
        return self.a

    def c13(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.H_stenka) / 2 + float(self.S_stenka) + float(self.H_paketa) / 2
        self.oboznachenie = 'С13'
        self.naimenovanie = 'Стенка'
        nominal = self.print_rezult()
        self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' + str(nominal) + '_нк_3', '+45s +45'], self.L)
        return self.a

    def c14(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.H_stenka) / 2 + float(self.S_stenka) + float(self.H_paketa) / 2
        self.oboznachenie = 'С14'
        self.naimenovanie = 'Стенка'
        nominal = self.print_rezult()
        self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' + str(nominal) + '_нк_3', '+45s -45'], self.L)
        return self.a

    def c15(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.H_stenka) / 2 - float(self.H_paketa) / 2
        self.oboznachenie = 'С15'
        self.naimenovanie = 'Стенка'
        nominal = self.print_rezult()
        self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' + str(nominal) + '_нк_3', '-45s +45'], self.L)
        return self.a

    def c16(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.H_stenka) / 2 - float(self.H_paketa) / 2
        self.oboznachenie = 'С16'
        self.naimenovanie = 'Стенка'
        nominal = self.print_rezult()
        self.profil(['профиль', 'Стенка ' + str(nominal) + 'без покрытия 3м.', 'С_' + str(nominal) + '_нк_3', '-45s -45'], self.L)
        return self.a

    # крышка средняя
    def kc(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        if self.name in ['тв', 'tv']:
            self.L = float(self.A) + float(self.B) - float(self.R_kor) * 2
        elif self.name in ['пф', 'pf', 'pfk']:
            self.L = float(self.os) - float(self.R_kor) - 4
        else:
            self.L = float(self.os) - float(self.R_kor) * 2
        if self.coating == 's':
            self.oboznachenie = 'КС-кр'
            self.naimenovanie = 'Крышка средняя крашенная'
            s = ['профиль', 'Крышка средняя окрашенная 2.82м.', 'КС_к_2.82', '90 90']
        else:
            self.oboznachenie = 'КС'
            self.naimenovanie = 'Крышка средняя'
            s = ['профиль', 'Крышка средняя без покрытия 3м.', 'КС_нк_3', '90 90']
        self.print_rezult()
        self.profil(s, self.L)
        return self.a

    # для угф стенка с вычетом плюс 118.5 - 4
    def kca(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.H_krishka) / 2 - 4
        self.oboznachenie = 'КС'
        self.naimenovanie = 'Крышка средняя'
        self.print_rezult()
        self.profil(['профиль', 'Крышка средняя без покрытия 3м.', 'КС_нк_3', '90 90'], self.L)
        return self.a

    def kc1(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - float(self.R_kor) + float(self.H_krishka) / 2
        self.oboznachenie = 'КС1'
        self.naimenovanie = 'Крышка средняя'
        self.print_rezult()
        self.profil(['профиль', 'Крышка средняя без покрытия 3м.', 'КС_нк_3', '90 +45'], self.L)
        return self.a

    # для УГФ
    def kc1f(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.H_krishka) / 2 - 4
        self.oboznachenie = 'КС1'
        self.naimenovanie = 'Крышка средняя'
        self.print_rezult()
        self.profil(['профиль', 'Крышка средняя без покрытия 3м.', 'КС_нк_3', '90 +45'], self.L)
        return self.a

    def kc2(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - float(self.R_kor) - float(self.H_stenka) / 2 + 18.5   # 18.5-потому что по центру
        self.oboznachenie = 'КС2'
        #print(str(self.L), '=', str(float(self.os)), '-', str(float(self.R_kor)), '-', str(float(str(self.H_stenka))),
             # '/ 2 + 18.5')
        self.naimenovanie = 'Крышка средняя'
        self.print_rezult()
        self.profil(['профиль', 'Крышка средняя без покрытия 3м.', 'КС_нк_3', '90 +45s'], self.L)
        return self.a

    def kc2a(self):     # для Z-вертикальной по оси Z
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - float(self.R_kor) + float(self.H_stenka) / 2 + 21.5
        #print(str(self.L), '=', str(float(self.os)), '-', str(float(self.R_kor)), '+', str(float(str(self.H_stenka))),
            #  '/ 2 + 21.5')
        self.oboznachenie = 'КС2'
        self.naimenovanie = 'Крышка средняя'
        self.print_rezult()
        self.profil(['профиль', 'Крышка средняя без покрытия 3м.', 'КС_нк_3', '90 +45s'], self.L)
        return self.a

    # для УВФ
    def kc2f(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - float(self.H_stenka) / 2 + 18.5 - 4
        self.oboznachenie = 'КС2'
        #print(str(self.L), '=', str(float(self.os)), '-', str(float(self.R_kor)), '-', str(float(str(self.H_stenka))),
              #'/ 2 + 18.5')
        self.naimenovanie = 'Крышка средняя'
        self.print_rezult()
        self.profil(['профиль', 'Крышка средняя без покрытия 3м.', 'КС_нк_3', '90 +45s'], self.L)
        return self.a

    def kc3(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.H_krishka) * 2
        self.oboznachenie = 'КС3'
        self.naimenovanie = 'Крышка средняя'
        self.print_rezult()
        self.profil(['профиль', 'Крышка средняя без покрытия 3м.', 'КС_нк_3', '+45 -45'], self.L)
        return self.a

    def kc4(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.H_krishka)
        self.oboznachenie = 'КС4'
        self.naimenovanie = 'Крышка средняя'
        self.print_rezult()
        self.profil(['профиль', 'Крышка средняя без покрытия 3м.', 'КС_нк_3', '+45 +45'], self.L)
        return self.a

    def kc5(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + 40
        self.oboznachenie = 'КС5'
        self.naimenovanie = 'Крышка средняя'
        self.print_rezult()
        self.profil(['профиль', 'Крышка средняя без покрытия 3м.', 'КС_нк_3', '+45s +45s'], self.L)
        return self.a

    def kc6(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) + float(self.H_krishka) * 2
        self.oboznachenie = 'КС6'
        self.naimenovanie = 'Крышка средняя'
        self.print_rezult()
        self.profil(['профиль', 'Крышка средняя без покрытия 3м.', 'КС_нк_3', '+45s +45s'], self.L)
        return self.a

    def kc8(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - float(self.H_stenka) / 2 + 18.5 + float(self.H_krishka) / 2
        self.oboznachenie = 'КС8'
        self.naimenovanie = 'Крышка средняя'
        self.print_rezult()
        self.profil(['профиль', 'Крышка средняя без покрытия 3м.', 'КС_нк_3', '+45 +45s'], self.L)
        return self.a

    def kc9(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - float(self.H_stenka) / 2 + 18.5 + float(self.H_krishka) / 2
        # print(str(self.L), '=', str(float(self.os)), '-', str(float(self.H_stenka)),  '/2 +18.5',  '+', str(float(self.H_krishka)), '/ 2')
        self.oboznachenie = 'КС9'
        self.naimenovanie = 'Крышка средняя'
        self.print_rezult()
        self.profil(['профиль', 'Крышка средняя без покрытия 3м.', 'КС_нк_3', '+45 +45s'], self.L)
        return self.a

    # проставок | для 3-х проводных П и УВ
    def stp09v(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = 23
        self.oboznachenie = 'СТП 09 В'
        self.naimenovanie = 'Зубчатый вывод'
        self.print_rezult()
        self.profil(['профиль', 'Шина 630', 'Ш_630', '90 90'], self.L)
        #print(self.a)
        return self.a

    # проставок | для 3-х проводных П и УВ
    def s(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        if self.seria in ['CR1']:
            if self.name in ['ув', 'uv']:
                if self.os[1] == 'x':
                    self.L = float(self.os[0]) - self.R_sh - self.H / 2
                else:
                    self.L = float(self.os[0]) - self.R_sh + self.H / 2
            elif self.name in ['п', 'pt']:
                self.L = float(self.os) - float(self.R_sh) * 2
        else:
            if str(self.Nprov) in ['4', '3+1']:
                self.L = float(self.os) - float(self.H)
            else:   # 3-х проводной
                if self.name in ['п', 'pt']:
                    self.L = float(self.os) - float(self.R_sh) * 2
                elif self.name in ['пф', 'pf', 'pfk']:
                    self.L = float(self.os) - float(self.R_sh) + self.L1Centre
                elif self.name in ['зв', 'звф', 'zv', 'zvf']:
                    self.L = float(self.os) - float(self.H)
                else:   # УВ
                    self.L = float(self.os) + float(self.H) / 2 - float(self.R_sh)
        self.oboznachenie = 'Ш'
        self.naimenovanie = 'Шина'
        sI = self.print_rezult()
        self.profil(['профиль', 'Шина ' + sI, 'Ш_' + sI, '90 90'], self.L)
        return self.a

    # для 3-х проводных УВ
    def sa(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - float(self.H) / 2 - float(self.R_sh)
        self.oboznachenie = 'Ш'
        self.naimenovanie = 'Шина'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L)
        return self.a

    # для прямых секций
    def s1(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - float(self.R_sh) * 2
        self.L1 = float(self.L) + self.L1_sh_b * 2
        self.oboznachenie = 'Ш1'
        self.naimenovanie = 'Шина (' + str(self.stp_L1) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    # для отбора мощности
    def s1_01(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        print(self.os)
        self.L = float(self.os) - float(self.R_sh) * 2
        self.L1 = float(self.L) + self.L1_sh_b * 2
        self.oboznachenie = 'Ш1-01'
        self.naimenovanie = 'Шина (' + str(self.stp_L1) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    # для ТВ
    def s1t(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os[0]) + float(self.os[1]) - float(self.R_sh) * 2
        self.L1 = float(self.L) + self.L1_sh_b * 2
        self.oboznachenie = 'Ш1'
        self.naimenovanie = 'Шина'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    # для прямых секций
    def s2(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - float(self.R_sh) * 2
        self.L1 = float(self.L) + self.L1_sh_m * 2
        self.oboznachenie = 'Ш2'
        self.naimenovanie = 'Шина (' + str(self.stp_L2) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    # для отбора мощности
    def s2_01(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - float(self.R_sh) * 2
        self.L1 = float(self.L) + self.L1_sh_m * 2
        self.oboznachenie = 'Ш2-01'
        self.naimenovanie = 'Шина (' + str(self.stp_L2) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    # для ТВ
    def s2t(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os[0]) + float(self.os[1]) - float(self.R_sh) * 2
        self.L1 = float(self.L) + self.L1_sh_m * 2
        self.oboznachenie = 'Ш2'
        self.naimenovanie = 'Шина'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    # для отбора мощьности
    def s1om1(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - float(self.R_sh) * 2
        self.L1 = float(self.L) + self.L1_sh_b * 2
        self.oboznachenie = 'Ш1'
        self.naimenovanie = 'Шина'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    def s1om4(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - float(self.R_sh) * 2
        self.L1 = float(self.L) + self.L1_sh_b * 2
        self.oboznachenie = 'Ш1'
        self.naimenovanie = 'Шина'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    def s2om2(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - float(self.R_sh) * 2
        self.L1 = float(self.L) + self.L1_sh_m
        self.oboznachenie = 'Ш2'
        self.naimenovanie = 'Шина'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    def s2om3(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - float(self.R_sh) * 2
        self.L1 = float(self.L) + self.L1_sh_m
        self.oboznachenie = 'Ш2'
        self.naimenovanie = 'Шина'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    # для вертикального угла и Z в том числе на 3- х проводной
    def s3(self):  # для углов вертикальных с плюсом
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - float(self.R_sh) + float(self.H) / 2
        # print('s3: ' + str(self.os) + ' - ' + str(self.R_sh) + ' + ' + str(self.H) + ' / 2 = ' + str(self.L))
        self.L1 = float(self.L) + self.L1_sh_b
        self.oboznachenie = 'Ш3'
        self.naimenovanie = 'Шина (' + str(self.stp_L1) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    # для Z 3- х проводной
    def s_3(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - float(self.R_sh) + float(self.H) / 2
        # print('s3: ' + str(self.os) + ' - ' + str(self.R_sh) + ' + ' + str(self.H) + ' / 2 = ' + str(self.L))
        self.L1 = float(self.L)
        self.oboznachenie = 'Ш'
        self.naimenovanie = 'Шина'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    # для ТВ
    def s3t(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        if self.nominal in [3200, 4000, 5000]:
            self.L = float(self.os) - float(self.R_sh) - float(self.H) - 3
        else:
            self.L = float(self.os) - float(self.R_sh) - float(self.H) / 2
        # print('s3: ' + str(self.os) + ' - ' + str(self.R_sh) + ' + ' + str(self.H) + ' / 2 = ' + str(self.L))
        self.L1 = float(self.L) + self.L1_sh_b
        self.oboznachenie = 'Ш3'
        self.naimenovanie = 'Шина'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    # та же шина что и Ш3 но для углов вертикальных с минусом
    def s3a(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - float(self.R_sh) - float(self.H) / 2
        # print('s3a: ' + str(self.os) + ' - ' + str(self.R_sh) + ' - ' + str(self.H) + ' / 2 = ' + str(self.L))
        self.L1 = float(self.L) + self.L1_sh_b
        self.oboznachenie = 'Ш3'
        self.naimenovanie = 'Шина (' + str(self.stp_L1) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    def s4(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - float(self.R_sh) + float(self.H) / 2
        # print('s4: ' + str(self.os) + ' - ' + str(self.R_sh) + ' +  ' + str(self.H) + ' / 2 = ' + str(self.L))
        self.L1 = float(self.L) + self.L1_sh_m
        self.oboznachenie = 'Ш4'
        self.naimenovanie = 'Шина (' + str(self.stp_L2) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    # та же шина что и Ш4 но для углов вертикальных с минусом
    def s4a(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = float(self.os) - float(self.R_sh) - float(self.H) / 2
        # print('s4a: ' + str(self.os) + ' - ' + str(self.R_sh) + ' -  ' + str(self.H) + ' / 2 = ' + str(self.L))
        self.L1 = float(self.L) + self.L1_sh_m
        self.oboznachenie = 'Ш4'
        self.naimenovanie = 'Шина (' + str(self.stp_L2) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    # для ТВ
    def s4t(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        if self.nominal in [3200, 4000, 5000]:
            self.L = float(self.os) - float(self.R_sh) - float(self.H) - 3
        else:
            self.L = float(self.os) - float(self.R_sh) - float(self.H) / 2
        # print('s3: ' + str(self.os) + ' - ' + str(self.R_sh) + ' + ' + str(self.H) + ' / 2 = ' + str(self.L))
        self.L1 = float(self.L) + self.L1_sh_m
        self.oboznachenie = 'Ш4'
        self.naimenovanie = 'Шина (' + str(self.stp_L2) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    # для горизонтального угла
    def s5(self):  # шина гнутая внешняя большой гиб

        beta = (180 - int(self.C)) / 2

        if str(self.Nprov) in ['4', '3+1']:
            self.X = float(float(self.os[0]) - float(self.R_sh) + (float(self.S_sh_izol) * 3 + int(self.S_sh) * 2) * (math.tan(math.radians(beta))))
            self.Y = float(float(self.os[1]) - float(self.R_sh) + (float(self.S_sh_izol) * 3 + int(self.S_sh) * 2) * (math.tan(math.radians(beta))))
        else:       # 3-х проводной
            self.X = float(float(self.os[0]) - float(self.R_sh) + float(self.S_sh_izol) * 2 + int(self.S_sh) * 1.5 * (math.tan(math.radians(beta))))
            self.Y = float(float(self.os[1]) - float(self.R_sh) + float(self.S_sh_izol) * 2 + int(self.S_sh) * 1.5 * (math.tan(math.radians(beta))))

        BD = self.razvertka_XY(beta * 2, self.R, self.Ka, self.S_sh)
        self.A = round(float(self.X) - BD / 2 + self.L1_sh_b, 1)
        self.B = round(float(self.Y) - BD / 2 + self.L1_sh_b, 1)
        self.L = '-'
        self.L1 = round(float(self.A) + float(self.B), 1)
        self.oboznachenie = 'Ш5'
        self.naimenovanie = 'Шина (' + str(self.stp_L1) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    def s6(self):  # шина гнутая внешняя малый гиб

        beta = (180 - int(self.C)) / 2

        self.X = float(float(self.os[0]) - float(self.R_sh) + (float(self.S_sh_izol) + int(self.S_sh)) * (math.tan(math.radians(beta))))
        self.Y = float(float(self.os[1]) - float(self.R_sh) + (float(self.S_sh_izol) + int(self.S_sh)) * (math.tan(math.radians(beta))))
        BD = self.razvertka_XY(beta * 2, self.R, self.Ka, self.S_sh)
        self.A = round(float(self.X) - BD / 2 + self.L1_sh_m, 1)
        self.B = round(float(self.Y) - BD / 2 + self.L1_sh_m, 1)
        self.L = '-'
        self.L1 = round(float(self.A) + float(self.B), 1)
        self.oboznachenie = 'Ш6'
        self.naimenovanie = 'Шина (' + str(self.stp_L2) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    def s7(self):  # шина гнутая внутренняя малый гиб

        beta = (180 - int(self.C)) / 2

        self.X = float(float(self.os[0]) - float(self.R_sh) - (float(self.S_sh_izol)) * (math.tan(math.radians(beta))))
        self.Y = float(float(self.os[1]) - float(self.R_sh) - (float(self.S_sh_izol)) * (math.tan(math.radians(beta))))
        BD = self.razvertka_XY(beta * 2, self.R, self.Ka, self.S_sh)
        self.A = round(float(self.X) - BD / 2 + self.L1_sh_m, 1)
        self.B = round(float(self.Y) - BD / 2 + self.L1_sh_m, 1)
        self.L = '-'
        self.L1 = round(float(self.A) + float(self.B), 1)
        self.oboznachenie = 'Ш7'
        self.naimenovanie = 'Шина (' + str(self.stp_L2) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    def s8(self):  # шина гнутая внутренняя большой гиб (с припуском)

        beta = (180 - int(self.C)) / 2

        if str(self.Nprov) in ['4', '3+1']:
            self.X = float(float(self.os[0]) - float(self.R_sh) - (float(self.S_sh_izol) * 3 + int(self.S_sh)) * (math.tan(math.radians(beta))))
            self.Y = float(float(self.os[1]) - float(self.R_sh) - (float(self.S_sh_izol) * 3 + int(self.S_sh)) * (math.tan(math.radians(beta))))
        else:
            self.X = float(float(self.os[0]) - float(self.R_sh) - (float(self.S_sh_izol) * 2 + int(self.S_sh) / 2) * (math.tan(math.radians(beta))))
            self.Y = float(float(self.os[1]) - float(self.R_sh) - (float(self.S_sh_izol) * 2 + int(self.S_sh) / 2) * (math.tan(math.radians(beta))))

        BD = self.razvertka_XY(beta * 2, self.R, self.Ka, self.S_sh)

        # для 6мм. шины создаем припуск, для 8мм. припуска нет
        if self.S_sh in [6, '6']:
            self.A = round(float(self.X) - BD / 2 + self.L1_sh_b, 1)    # технологический допуск
            self.B = round(float(self.Y) - BD / 2 + self.L1_sh_b, 1)    # технологический допуск
        else:
            self.A = round(float(self.X) - BD / 2 + self.L1_sh_b, 1)
            self.B = round(float(self.Y) - BD / 2 + self.L1_sh_b, 1)

        self.L = '-'
        self.L1 = round(float(self.A) + float(self.B), 1)
        self.oboznachenie = 'Ш8'
        self.naimenovanie = 'Шина (' + str(self.stp_L1) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    # для комбинированных секций

    def s9(self):  # Шина гнутая внешняя крайняя с одним выводом
        self.C = '-'
        if str(self.Nprov) in ['4', '3+1']:
            self.X = float(self.os[0]) + float(self.S_sh_izol) * 3 + int(self.S_sh) * 2 - float(self.H) / 2
            self.Y = float(self.os[1]) - float(self.R_sh) + float(self.S_sh_izol) * 3 + int(self.S_sh) * 2
        else:   # 3-х проводной
            self.X = float(self.os[0]) + float(self.S_sh_izol) * 2 + int(self.S_sh) * 1.5 - float(self.H) / 2
            self.Y = float(self.os[1]) - float(self.R_sh) + float(self.S_sh_izol) * 2 + int(self.S_sh) * 1.5
        BD = self.razvertka_XY(90, self.R, self.Ka, self.S_sh)
        self.A = round(float(self.X) - BD / 2, 1)
        self.B = round(float(self.Y) - BD / 2 + self.L1_sh_b, 1)
        self.L = '-'
        self.L1 = round(float(self.A) + float(self.B), 1)

        self.oboznachenie = 'Ш9'
        self.naimenovanie = 'Шина (' + str(self.stp_L1) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    def s10(self):  # Шина гнутая внешняя средняя  с одним выводом
        self.C = '-'

        self.X = float(float(self.os[0]) + float(self.S_sh_izol) + int(self.S_sh)) - float(self.H) / 2
        self.Y = float(float(self.os[1]) - float(self.R_sh) + float(self.S_sh_izol) + int(self.S_sh))
        BD = self.razvertka_XY(90, self.R, self.Ka, self.S_sh)
        self.A = round(float(self.X) - BD / 2, 1)
        self.B = round(float(self.Y) - BD / 2 + self.L1_sh_m, 1)
        self.L = '-'
        self.L1 = round(float(self.A) + float(self.B), 1)
        self.oboznachenie = 'Ш10'
        self.naimenovanie = 'Шина (' + str(self.stp_L2) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    def s11(self):  # Шина гнутая внутреняя средняя с одним выводом
        self.C = '-'
        self.X = float(float(self.os[0]) - float(self.S_sh_izol)) - float(self.H) / 2
        self.Y = float(float(self.os[1]) - float(self.R_sh) - float(self.S_sh_izol))
        BD = self.razvertka_XY(90, self.R, self.Ka, self.S_sh)
        self.A = round(float(self.X) - BD / 2, 1)
        self.B = round(float(self.Y) - BD / 2 + self.L1_sh_m, 1)
        self.L = '-'
        self.L1 = round(float(self.A) + float(self.B), 1)
        self.oboznachenie = 'Ш11'
        self.naimenovanie = 'Шина (' + str(self.stp_L2) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    def s12(self):  # Шина гнутая, внутреняя, крайняя, стандартный выыод с одной стороны.
        self.C = '-'
        if str(self.Nprov) in ['4', '3+1']:
            self.X = float(float(self.os[0]) - float(self.S_sh_izol) * 3 - int(self.S_sh)) - float(self.H) / 2
            self.Y = float(float(self.os[1]) - float(self.R_sh) - float(self.S_sh_izol) * 3 - int(self.S_sh))
        else:
            X = float(float(self.os[0]) - float(self.S_sh_izol) * 2 - int(self.S_sh) / 2) - float(self.H) / 2
            Y = float(float(self.os[1]) - float(self.R_sh) - float(self.S_sh_izol) * 2 - int(self.S_sh) / 2)

        BD = self.razvertka_XY(90, self.R, self.Ka, self.S_sh)
        self.A = round(float(self.X) - BD / 2, 1)
        self.B = round(float(self.Y) - BD / 2 + self.L1_sh_b, 1) - 3    # технологический допуск
        self.L = '-'
        self.L1 = round(float(self.A) + float(self.B), 1)
        self.oboznachenie = 'Ш12'
        self.naimenovanie = 'Шина (' + str(self.stp_L1) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    # для Z-образной

    def s13(self):  # Шина с двойным гибом внешняя крайняя
        self.X = float(float(self.os[0]) - float(self.R_sh) + float(self.S_sh_izol) * 3 + int(self.S_sh) * 2)
        self.Y = float(float(self.os[2]) - float(self.R_sh) - float(self.S_sh_izol) * 3 - int(self.S_sh))
        BD = self.razvertka_XY(90, self.R, self.Ka, self.S_sh)
        self.A = round(float(self.X) - BD / 2 + self.L1_sh_b, 1)
        self.B = round(float(self.os[1]) + int(self.S_sh) - BD, 1)
        self.C = round(float(self.Y) - BD / 2 + self.L1_sh_b, 1)
        self.L = '-'
        self.L1 = round(float(self.A) + float(self.B) + float(self.C), 1)
        self.oboznachenie = 'Ш13'
        self.naimenovanie = 'Шина (' + str(self.stp_L1) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    def s14(self):  # Шина с двойным гибом внешняя средняя
        self.X = float(float(self.os[0]) - float(self.R_sh) + float(self.S_sh_izol) + int(self.S_sh))
        self.Y = float(float(self.os[2]) - float(self.R_sh) - float(self.S_sh_izol))
        BD = self.razvertka_XY(90, self.R, self.Ka, self.S_sh)
        self.A = round(float(self.X) - BD / 2 + self.L1_sh_m, 1)
        self.B = round(float(self.os[1]) + int(self.S_sh) - BD, 1)
        self.C = round(float(self.Y) - BD / 2 + self.L1_sh_m, 1)
        self.L = '-'
        self.L1 = round(float(self.A) + float(self.B) + float(self.C), 1)
        self.oboznachenie = 'Ш14'
        self.naimenovanie = 'Шина (' + str(self.stp_L2) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    def s15(self):  # Шина с двойным гибом внутреняя средняя
        self.X = float(float(self.os[0]) - float(self.R_sh) - float(self.S_sh_izol))
        self.Y = float(float(self.os[2]) - float(self.R_sh) + float(self.S_sh_izol) + int(self.S_sh))
        BD = self.razvertka_XY(90, self.R, self.Ka, self.S_sh)
        self.A = round(float(self.X) - BD / 2 + self.L1_sh_m, 1)
        self.B = round(float(self.os[1]) + int(self.S_sh) - BD, 1)
        self.C = round(float(self.Y) - BD / 2 + self.L1_sh_m, 1)
        self.L = '-'
        self.L1 = round(float(self.A) + float(self.B) + float(self.C), 1)
        self.oboznachenie = 'Ш15'
        self.naimenovanie = 'Шина (' + str(self.stp_L2) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    def s16(self):  # Шина с двойным гибом внутреняя крайняя
        self.X = float(float(self.os[0]) - float(self.R_sh) - float(self.S_sh_izol) * 3 - int(self.S_sh))
        self.Y = float(float(self.os[2]) - float(self.R_sh) + float(self.S_sh_izol) * 3 + int(self.S_sh) * 2)
        BD = self.razvertka_XY(90, self.R, self.Ka, self.S_sh)
        self.A = round(float(self.X) - BD / 2 + self.L1_sh_b, 1)
        self.B = round(float(self.os[1]) + int(self.S_sh) - BD, 1)
        self.C = round(float(self.Y) - BD / 2 + self.L1_sh_b, 1)
        self.L = '-'
        self.L1 = round(float(self.A) + float(self.B) + float(self.C), 1)
        self.oboznachenie = 'Ш16'
        self.naimenovanie = 'Шина (' + str(self.stp_L1) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a


# шины для прямой с фланцем по новому чертежу СТП 01Ф
    def stp01f_01(self):
        razmery = [210, 100]

        self.A = '-'    # не должен быть меньше 100 мм.
        self.B = '-'
        self.C = '-'
        self.L = '-'
        self.L1 = 1
        #print(float(self.os), float(self.R_sh), self.L1Edge, self.L1_sh_b)
        self.oboznachenie = 'Ш17'
        self.naimenovanie = 'Шина (' + str(self.StpEdge) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        print(self.a)

    # для фланцев
    # для номинала от 630 до 2000 включительно
    def s17(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = '-'
        self.L1 = round(float(self.os) - float(self.R_sh) + self.L1Edge + self.L1_sh_b, 1)
        #print(float(self.os), float(self.R_sh), self.L1Edge, self.L1_sh_b)
        self.oboznachenie = 'Ш17'
        self.naimenovanie = 'Шина (' + str(self.StpEdge) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    # для номинала от 630 до 2000 включительно
    def s18(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = '-'
        self.L1 = round(float(self.os) - float(self.R_sh) + self.L1Centre + self.L1_sh_m, 1)
        #print(float(self.os), float(self.R_sh), self.L1Centre, self.L1_sh_m)
        self.oboznachenie = 'Ш18'
        self.naimenovanie = 'Шина (' + str(self.SptCentre) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    # для угф
    def s19(self):  # шина гнутая внешняя большой гиб
        self.C = '-'
        self.X = float(float(self.os[0]) + float(self.S_sh_izol) * 3 + int(self.S_sh) * 2)
        self.Y = float(float(self.os[1]) - float(self.R_sh) + float(self.S_sh_izol) * 3 + int(self.S_sh) * 2)
        BD = self.razvertka_XY(90, self.R, self.Ka, self.S_sh)
        self.B = round(float(self.Y) - BD / 2 + self.L1_sh_b, 1)
        self.A = round(float(self.X) - BD / 2 + self.L1Edge + 4, 1)
        self.L = '-'
        self.L1 = round(float(self.A) + float(self.B), 1)
        self.oboznachenie = 'Ш19'
        self.naimenovanie = 'Шина'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    def s20(self):  # шина гнутая внешняя малый гиб
        self.C = '-'
        self.X = float(float(self.os[0]) + float(self.S_sh_izol) + int(self.S_sh))
        self.Y = float(float(self.os[1]) - float(self.R_sh) + float(self.S_sh_izol) + int(self.S_sh))
        BD = self.razvertka_XY(90, self.R, self.Ka, self.S_sh)
        self.A = round(float(self.X) - BD / 2 + self.L1Centre + 4, 1)
        self.B = round(float(self.Y) - BD / 2 + self.L1_sh_m, 1)
        self.L = '-'
        self.L1 = round(float(self.A) + float(self.B), 1)
        self.oboznachenie = 'Ш20'
        self.naimenovanie = 'Шина'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    def s21(self):  # шина гнутая внутренняя малый гиб
        self.C = '-'
        self.X = float(float(self.os[0]) - float(self.S_sh_izol))
        self.Y = float(float(self.os[1]) - float(self.R_sh) - float(self.S_sh_izol))
        BD = self.razvertka_XY(90, self.R, self.Ka, self.S_sh)
        self.A = round(float(self.X) - BD / 2 + self.L1Centre + 4, 1)
        self.B = round(float(self.Y) - BD / 2 + self.L1_sh_m, 1)
        self.L = '-'
        self.L1 = round(float(self.A) + float(self.B), 1)
        self.oboznachenie = 'Ш21'
        self.naimenovanie = 'Шина'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    def s22(self):  # шина гнутая внутренняя большой гиб
        self.C = '-'
        self.X = float(float(self.os[0]) - float(self.S_sh_izol) * 3 - int(self.S_sh))
        self.Y = float(float(self.os[1]) - float(self.R_sh) - float(self.S_sh_izol) * 3 - int(self.S_sh))
        BD = self.razvertka_XY(90, self.R, self.Ka, self.S_sh)
        self.A = round(float(self.X) - BD / 2 + self.L1Edge + 4, 1)
        self.B = round(float(self.Y) - BD / 2 + self.L1_sh_b, 1)
        self.L = '-'
        self.L1 = round(float(self.A) + float(self.B), 1)
        self.oboznachenie = 'Ш22'
        self.naimenovanie = 'Шина'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    # для комбинированных и для CR
    def s23(self):  # шина гнутая внутренняя большой гиб
        beta = (180 - int(self.C)) / 2
        self.X = float(float(self.os[0]) + (float(self.S_sh_izol) * 3 + int(self.S_sh) * 2) * (math.tan(math.radians(beta))))
        self.Y = float(float(self.os[1]) - float(self.R_sh) + (float(self.S_sh_izol) * 3 + int(self.S_sh) * 2) * (math.tan(math.radians(beta))))
        print(self.Y, (float(self.S_sh_izol) * 3 + int(self.S_sh) * 2) * (math.tan(math.radians(beta))))
        BD = self.razvertka_XY(beta * 2, self.R, self.Ka, self.S_sh)
        self.B = round(float(self.Y) - BD / 2 + self.L1_sh_b, 1)
        self.A = round(float(self.X) - BD / 2 + self.L1Edge + 4, 1)
        self.L = '-'
        self.L1 = round(float(self.A) + float(self.B), 1)
        self.oboznachenie = 'Ш23'
        self.naimenovanie = 'Шина'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    def s24(self):  # шина гнутая внешняя малый гиб
        beta = (180 - int(self.C)) / 2
        self.X = float(float(self.os[0]) + (float(self.S_sh_izol) + int(self.S_sh)) * (math.tan(math.radians(beta))))
        self.Y = float(float(self.os[1]) - float(self.R_sh) + (float(self.S_sh_izol) + int(self.S_sh)) * (math.tan(math.radians(beta))))
        print(self.Y, (float(self.S_sh_izol) + int(self.S_sh)) * (math.tan(math.radians(beta))))
        BD = self.razvertka_XY(beta * 2, self.R, self.Ka, self.S_sh)
        self.A = round(float(self.X) - BD / 2 + self.L1Centre + 4, 1)
        self.B = round(float(self.Y) - BD / 2 + self.L1_sh_m, 1)
        self.L = '-'
        self.L1 = round(float(self.A) + float(self.B), 1)
        self.oboznachenie = 'Ш24'
        self.naimenovanie = 'Шина'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    def s25(self):  # шина гнутая внутренняя малый гиб
        beta = (180 - int(self.C)) / 2
        self.X = float(float(self.os[0]) - (float(self.S_sh_izol)) * (math.tan(math.radians(beta))))
        self.Y = float(float(self.os[1]) - float(self.R_sh) - (float(self.S_sh_izol)) * (math.tan(math.radians(beta))))
        print(self.Y, float(self.S_sh_izol) * (math.tan(math.radians(beta))))
        BD = self.razvertka_XY(beta * 2, self.R, self.Ka, self.S_sh)
        self.A = round(float(self.X) - BD / 2 + self.L1Centre + 4, 1)
        self.B = round(float(self.Y) - BD / 2 + self.L1_sh_m, 1)
        self.L = '-'
        self.L1 = round(float(self.A) + float(self.B), 1)
        self.oboznachenie = 'Ш25'
        self.naimenovanie = 'Шина'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    def s26(self):  # шина гнутая внутренняя большой гиб
        beta = (180 - int(self.C)) / 2
        self.X = float(float(self.os[0]) - (float(self.S_sh_izol) * 3 - int(self.S_sh)) * (math.tan(math.radians(beta))))
        self.Y = float(float(self.os[1]) - float(self.R_sh) - (float(self.S_sh_izol) * 3 + int(self.S_sh)) * (math.tan(math.radians(beta))))
        #print(self.Y, (float(self.S_sh_izol) * 3 + int(self.S_sh)) * (math.tan(math.radians(beta))))
        BD = self.razvertka_XY(beta * 2, self.R, self.Ka, self.S_sh)
        self.A = round(float(self.X) - BD / 2 + self.L1Edge + 4, 1)
        self.B = round(float(self.Y) - BD / 2 + self.L1_sh_b, 1)
        self.L = '-'
        self.L1 = round(float(self.A) + float(self.B), 1)
        self.oboznachenie = 'Ш26'
        self.naimenovanie = 'Шина'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    # для Z-образной с фланцем

    def s27(self):  # шина гнутая внешняя большой гиб
        self.X = float(float(self.os[0]) + float(self.S_sh_izol) * 3 + int(self.S_sh) * 2)
        self.Y = float(float(self.os[2]) - float(self.R_sh) - float(self.S_sh_izol) * 3 - int(self.S_sh))
        BD = self.razvertka_XY(90, self.R, self.Ka, self.S_sh)
        self.A = round(float(self.X) - BD / 2 + self.L1Edge + 4, 1)
        self.B = round(float(self.os[1]) + int(self.S_sh) - BD, 1)
        self.C = round(float(self.Y) - BD / 2 + self.L1_sh_b, 1)
        self.L = '-'
        self.L1 = round(float(self.A) + float(self.B) + float(self.C), 1)
        self.oboznachenie = 'Ш27'
        self.naimenovanie = 'Шина (' + str(self.StpEdge) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    def s28(self):  # шина гнутая внешняя малый гиб
        self.X = float(float(self.os[0]) + float(self.S_sh_izol) + int(self.S_sh))
        self.Y = float(float(self.os[2]) - float(self.R_sh) - float(self.S_sh_izol))
        BD = self.razvertka_XY(90, self.R, self.Ka, self.S_sh)
        self.A = round(float(self.X) - BD / 2 + self.L1Centre + 4, 1)
        self.B = round(float(self.os[1]) + int(self.S_sh) - BD, 1)
        self.C = round(float(self.Y) - BD / 2 + self.L1_sh_m, 1)
        self.L = '-'
        self.L1 = round(float(self.A) + float(self.B) + float(self.C), 1)
        self.oboznachenie = 'Ш28'
        self.naimenovanie = 'Шина (' + str(self.SptCentre) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    def s29(self):  # шина гнутая внутренняя малый гиб
        self.X = float(float(self.os[0]) - float(self.S_sh_izol))
        self.Y = float(float(self.os[2]) - float(self.R_sh) + float(self.S_sh_izol) + int(self.S_sh))
        BD = self.razvertka_XY(90, self.R, self.Ka, self.S_sh)
        self.A = round(float(self.X) - BD / 2 + self.L1Centre + 4, 1)
        self.B = round(float(self.os[1]) + int(self.S_sh) - BD, 1)
        self.C = round(float(self.Y) - BD / 2 + self.L1_sh_m, 1)
        self.L = '-'
        self.L1 = round(float(self.A) + float(self.B) + float(self.C), 1)
        self.oboznachenie = 'Ш29'
        self.naimenovanie = 'Шина (' + str(self.SptCentre) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    def s30(self):  # шина гнутая внутренняя большой гиб
        self.X = float(float(self.os[0]) - float(self.S_sh_izol) * 3 - int(self.S_sh))
        self.Y = float(float(self.os[2]) - float(self.R_sh) + float(self.S_sh_izol) * 3 + int(self.S_sh) * 2)
        BD = self.razvertka_XY(90, self.R, self.Ka, self.S_sh)
        self.A = round(float(self.X) - BD / 2 + self.L1Edge + 4, 1)
        self.B = round(float(self.os[1]) + int(self.S_sh) - BD, 1)
        self.C = round(float(self.Y) - BD / 2 + self.L1_sh_b, 1)
        self.L = '-'
        self.L1 = round(float(self.A) + float(self.B) + float(self.C), 1)
        self.oboznachenie = 'Ш30'
        self.naimenovanie = 'Шина (' + str(self.StpEdge) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    # для трансформаторной секции
    def s33(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = round(float(self.os) + float(self.S_krishka) + 1.5, 1)
        self.oboznachenie = 'Ш33'
        self.naimenovanie = 'Шина (Ш-ФБ)'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L)
        return self.a

    # для трансформаторной секции
    def s33i(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        self.L = round(float(self.os) + float(self.H) * 2 + float(self.S_krishka) + 7.5, 1)
        self.oboznachenie = 'Ш33'
        self.naimenovanie = 'Шина (Ш-ФБ)'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L)
        return self.a

    # шина с фланцем крайняя с минусом половины ширины шины. (Ш3 с плюсом)
    def s36(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'

        if self.seria in ['CR1']:
            self.L = round(float(self.os) + 210 - self.R_sh, 1)
            self.L1 = round(float(self.os) + self.L1Edge - self.R_sh, 1)
        else:
            if self.name in ['kpfuv', 'klfuv']:
                self.L = round(float(self.os) + float(self.H) / 2 + 210, 1)  # 210 это длина вывода фланца
                self.L1 = round(float(self.os) + float(self.H) / 2 + self.L1Edge, 1)
            else:
                self.L = round(float(self.os) - float(self.H) / 2 + 210, 1)  # 210 это длина вывода фланца
                self.L1 = round(float(self.os) - float(self.H) / 2 + self.L1Edge, 1)
        self.oboznachenie = 'Ш36'
        self.naimenovanie = 'Шина (' + str(self.StpEdge) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    # шина с фланцем средняя с минусом половины ширины шины. (Ш4 с плюсом)
    def s37(self):
        self.A = '-'
        self.B = '-'
        self.C = '-'
        if self.seria in ['CR1']:
            self.L = round(float(self.os) + 210 - self.R_sh, 1)
            self.L1 = round(float(self.os) + self.L1Centre - self.R_sh, 1)
        else:
            if self.name in ['kpfuv', 'klfuv']:
                self.L = round(float(self.os) + float(self.H) / 2 + 210, 1)
                self.L1 = round(float(self.os) + float(self.H) / 2 + self.L1Centre, 1)
            else:
                self.L = round(float(self.os) - float(self.H) / 2 + 210, 1)
                self.L1 = round(float(self.os) - float(self.H) / 2 + self.L1Centre, 1)
        self.oboznachenie = 'Ш37'
        self.naimenovanie = 'Шина (' + str(self.SptCentre) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    # шина с фланцем средняя с минусом половины ширины шины. (Ш4 с плюсом)
    def s38(self):
        self.C = '-'
        BD = self.razvertka_XY(90, self.R, self.Ka, self.S_sh)
        if self.name in ['ув', 'uv']:
            self.X = float(self.os[0]) - float(self.R_sh) + float(self.S_sh) / 2
            self.Y = float(self.os[1]) - float(self.R_sh) + float(self.S_sh) / 2
        else:   # Для КП КЛ 3-х проводников
            if self.name in ['кп', 'кл']:
                self.X = float(self.os[0]) + int(self.S_sh) / 2 - float(self.H) / 2
                self.Y = float(self.os[1]) - float(self.R_sh) + int(self.S_sh) / 2
            else:    # если это уг
                self.X = float(self.os[0]) - float(self.R_sh) + int(self.S_sh) / 2
                self.Y = float(self.os[1]) - float(self.R_sh) + int(self.S_sh) / 2
        self.A = round(float(self.X) - BD / 2, 1)
        self.B = round(float(self.Y) - BD / 2, 1)
        self.L = '-'
        self.L1 = round(float(self.A) + float(self.B), 1)
        self.oboznachenie = 'Ш38'
        self.naimenovanie = 'Шина (' + str(self.stp_L1) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    def s41(self):

        beta = (180 - int(self.C)) / 2

        if self.os[2] == 1:
            if str(self.Nprov) in ['4', '3+1']:
                self.X = float(float(self.os[0]) - float(self.R_sh) + (float(self.S_sh_izol) * 3 + int(self.S_sh) * 2) * (math.tan(math.radians(beta))))
                self.Y = float(float(self.os[1]) - float(self.R_sh) + (float(self.S_sh_izol) * 3 + int(self.S_sh) * 2) * (math.tan(math.radians(beta))))
            else:       # 3-х проводной
                self.X = float(float(self.os[0]) - float(self.R_sh) + float(self.S_sh_izol) * 2 + int(self.S_sh) * 1.5 * (math.tan(math.radians(beta))))
                self.Y = float(float(self.os[1]) - float(self.R_sh) + float(self.S_sh_izol) * 2 + int(self.S_sh) * 1.5 * (math.tan(math.radians(beta))))
        elif self.os[2] == 2:
                self.X = float(float(self.os[0]) - float(self.R_sh) + (float(self.S_sh_izol) + int(self.S_sh)) * (math.tan(math.radians(beta))))
                self.Y = float(float(self.os[1]) - float(self.R_sh) + (float(self.S_sh_izol) + int(self.S_sh)) * (math.tan(math.radians(beta))))
        elif self.os[2] == 3:
                self.X = float(
                    float(self.os[0]) - float(self.R_sh) - (float(self.S_sh_izol)) * (math.tan(math.radians(beta))))
                self.Y = float(
                    float(self.os[1]) - float(self.R_sh) - (float(self.S_sh_izol)) * (math.tan(math.radians(beta))))
        elif self.os[2] == 4:
                if str(self.Nprov) in ['4', '3+1']:
                    self.X = float(
                        float(self.os[0]) - float(self.R_sh) - (float(self.S_sh_izol) * 3 + int(self.S_sh)) * (math.tan(math.radians(beta))))
                    self.Y = float(
                        float(self.os[1]) - float(self.R_sh) - (float(self.S_sh_izol) * 3 + int(self.S_sh)) * (math.tan(math.radians(beta))))
                else:
                    self.X = float(
                        float(self.os[0]) - float(self.R_sh) - (float(self.S_sh_izol) * 2 + int(self.S_sh) / 2) * (math.tan(math.radians(beta))))
                    self.Y = float(
                        float(self.os[1]) - float(self.R_sh) - (float(self.S_sh_izol) * 2 + int(self.S_sh) / 2) * (math.tan(math.radians(beta))))

        BD = self.razvertka_XY(beta * 2, self.R, self.Ka, self.S_sh)
        self.A = round(float(self.X) - BD / 2, 1)
        self.B = round(float(self.Y) - BD / 2, 1)
        self.L = '-'
        self.L1 = round(float(self.A) + float(self.B), 1)
        self.oboznachenie = 'Ш41'
        self.naimenovanie = 'Шина (' + str(self.stp_L1) + ')'
        s = self.print_rezult()
        self.profil(['профиль', 'Шина ' + s, 'Ш_' + s, '90 90'], self.L1)
        return self.a

    def print_rezult(self):

        if self.naimenovanie in ['Крышка', 'Сухарь', 'Крышка средняя', 'Уголок_25х25х3', 'Крышка с выступом крашенная',
                                 'Втулка', 'Крышка стыка', 'Демпфер']:
            nominal = '-'
        elif self.nominal > 2500 and self.naimenovanie in ['Стенка', 'Стенка крашенная', 'Изолятор крайний',
                                                           'Изолятор средний', 'Направляющая']:

            if self.material in ['Al']:
                nominalus = {3200: 1600, 2600: 1250, 4000: 2000, 5000: 2000, 6300: 2000, 3201: 2000}
                nominal = nominalus[self.nominal]
            else:
                nominalus = {3200: 1250, 4000: 1600, 5000: 1600, 6300: 1600}
                nominal = nominalus[self.nominal]

            if self.naimenovanie in ['Стенка', 'Стенка крашенная']:
                self.oboznachenie = str(self.oboznachenie) + '-01'

        elif re.findall(r'.', self.oboznachenie)[0] in ['Ш'] or self.oboznachenie in ['ТП']:

            if self.material in ['Al']:

                if self.nominal > 2500 and re.findall(r'\w*', self.naimenovanie)[0] in ['Шина']:
                    nominalus = {3200: 1600, 3201: 1600, 2600: 1250, 4000: 2000, 5000: 2500, 6300: 2500}
                    nominal = str(nominalus[self.nominal]) + ' (Алюм)'
                else:
                    nominal = str(self.nominal) + ' (Алюм)'

            else:  # self.material in ['Cu']:

                if self.nominal > 2500 and re.findall(r'\w*', self.naimenovanie)[0] in ['Шина', 'Пластина']:
                    nominalus = {3200: 1600, 4000: 2000, 5000: 2500, 6300: 2500}
                    nominal = str(nominalus[self.nominal]) + ' (Медь)'
                else:
                    nominal = str(self.nominal) + ' (Медь)'

        elif self.nominal < 3200 and self.naimenovanie in ['Стенка', 'Стенка крашенная', 'Стенка стыка',
                                                           'Пластина токопроводящая',
                                                           'Изолятор крайний', 'Изолятор средний',
                                                           'Направляющая'] and self.material in ['Cu']:
            nominalus = {400: 630, 630: 630, 800: 630, 1000: 800, 1250: 1000, 1600: 1250, 2000: 1600, 2500: 1600}
            nominal = nominalus[self.nominal]
        else:
            nominal = str(self.nominal)

        self.a = [self.seria, self.ip, self.material, nominal, self.Nprov, self.naimenovanie, self.oboznachenie, self.L,
                  self.L1, self.A, self.B, self.C]

        return nominal

    def razvertka_XY(self, fi, r, k, S):
        # Где s_izol – толщина изоляции, N – номер шины от центра осуи сверху вниз, Y2, X2 – полки, fi – внешний угол,
        # r – внутренний радиус гибки, k – коэффициент положения нейтральной линии (К-фактор), S – толщина металла.
        # OS - это внешняя граница гибки
        OS = 2 * (math.tan(math.radians(fi / 2))) * (int(r) + int(S))
        # BD - это вычет
        BD = OS - float(math.pi) * float(fi) / 180 * (int(r) + float(k) * int(S))
        print('Dano: ', fi, r, k, S, BD)
        return BD

    def profil(self, s, znachenie):
            i = 1

            while i <= int(self.kolN):
                self.spis_kompl['profil'].append([str(s[0]) + ';' + str(s[1]) + ';' + str(s[2]) + ';'
                                                  + str(s[3]) + ';' + str(znachenie) + ';' + str(self.name)])
                i += 1
