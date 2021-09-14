# coding^utf8
import re
from schet import schetchik
from detali import Detali
from prints import prints
import nominal

class Welded_part:


    def __init__(self, input_data ):
        self.A = 0  #
        self.B = 0  #
        self.C = 0  #
        self.H_stenka = 0  # высота стенки
        self.H = 0  # ширина шины
        self.nominal = input_data[0]
        self.index = schetchik()
        self.quantity = input_data[3]
        self.input_data = input_data
        self.os = []
        self.spisok_det = []

    def Many_det(self, razmer, nazv_weld_part, kol):  #
        spis_det = {'К-СД1': 'k1-k2', 'К-СД1-З': 'k2-k1', 'К-СД2': 'k3-k3', 'К-СД3': 'k4-k4', 'К-СД4': 'k2-k7-k2', 'К-СД5': 'k1-k8-k1',
                    'К-СД6': 'k3-k9-k4', 'К-СД6-З': 'k4-k9-k3', 'К-СД7': 'k3-k14-k1', 'К-СД8': 'k4-k15-k2', 'К-СД9': 'k3-k13-k2', 'К-СД10': 'k4-k16-k1',
                    'С-СД1': 'c3-c3', 'С-СД2': 'c4-c4', 'С-СД3': 'c1-c2', 'С-СД3-З': 'c2-c1', 'С-СД4': 'c3-c9-c4', 'С-СД4-З': 'c4-c9-c3', 'С-СД5': 'c2-c7-c2', 'С-СД6': 'c1-c8-c1',
                    'С-СД7': 'c3-c14-c1', 'С-СД8': 'c2-c15-c4', 'С-СД9': 'c2-c13-c3', 'С-СД10': 'c1-c16-c4',
                    'К-СД11': 'kc2-kc8-kc1', 'К-СД12': 'kc2-kc9-kc1', 'К-СД13': 'kc2-kc2', 'К-СД14': 'kc1-kc1',
                    'К-СД15': 'kc2-kc5-kc2', 'К-СД16': 'kc1-kc4-kc1',
                    'Ш-СД1': 's3-s3a', 'Ш-СД2': 's4-s4a', 'Ш-СД2-З': 's4a-s4', 'Ш-СД1-З': 's3a-s3', 'Ш-СД3': 's3-s-s3', 'Ш-СД4': 's4-s-s4'}

        for i in nazv_weld_part:
            value = spis_det[i]
            q = re.findall(r'[^-]+', value)
            w = 0
            b = self.index.shet3() # присваиваем индекс
            self.print2(i, b, kol)
            for j in razmer:
                det = Detali(j, self.H_stenka, self.H, self.A, self.B, self.C)
                t = getattr(det, q[w])()
                w = w + 1
                a = self.index.shet4()
                h = ';'.join(t)
                quantity = int(self.quantity) * int(kol)
                self.print(h, a, quantity)
                print(t)

    def Many_det3(self, razmer, nazv_weld_part, kol):  #
        spis_det = {'Ш-СД7': 's3-s12', 'Ш-СД8': 's4-s11', 'Ш-СД9': 's4-s10', 'Ш-СД10': 's3-s9', 'Ш-СД11': 's3-s12',
                    'Ш-СД12': 's4-s11', 'Ш-СД13': 's4-s10', 'Ш-СД14': 's3-s9'}

        for i in nazv_weld_part:
            a = self.index.shet3()
            quantity = int(self.quantity) * int(kol)
            self.print(i, a, quantity)
            value = spis_det[i]
            q = re.findall(r'[^-]+', value)
            det = Detali(razmer[0], self.H_stenka, self.H, self.A, self.B, self.C)
            t = getattr(det, q[0])()
            print(t)
            a = self.index.shet4()
            self.print2(q[0], a, quantity)
            det = Detali(0, self.H_stenka, self.H, self.A, self.B, self.C)
            t = getattr(det, q[1])()
            print(t)
            a = self.index.shet4()
            self.print2(q[1], a, quantity)


    def Many_det2(self, razmer, nazv_weld_part, kol):  #
        for i in nazv_weld_part:
            det = Detali(razmer[0], self.H_stenka, self.H, self.A, self.B, self.C)
            t = getattr(det, i)()
            a = self.index.shet4()
            h = ';'.join(t)
            quantity = int(self.quantity) * int(kol)
            self.print(h, a, quantity)
            print(t)

    def ABC(self, input_data):
        self.os = re.findall(r'[^xXхХ*]+', input_data[2])
        if len(self.os) == 2:
            self.A = self.os[0]
            self.B = self.os[1]
            self.C = None

        elif len(self.os) == 3:
            self.A = self.os[0]
            self.B = self.os[1]
            self.C = self.os[2]
        else:
            return False

    def nominal(self, input_data):
        vibor_nominal = nominal.vvod_znach(self.nominal)
        self.H = vibor_nominal[0]
        self.H_stenka = vibor_nominal[1]



    def print(self, a, b, quantity): # a-значение которое нужно записать b-на каком уровне счетчик
        per = open('spisok_det.txt', 'a')
        print(str(b) + ';' + str(self.nom) + ';' + str(a) + ';-;' + str(quantity), file=per)
        #print(str(b) + ';' + str(self.nom) + ';' + str(a))
        per.close()

    def print2(self, a, b, quantity):  # a-значение которое нужно записать b-на каком уровне счетчик
        per = open('spisok_det.txt', 'a')
        print(str(b) + ';' + str(self.nom) + ';' + str(a) + ';-;-;-;-;-;' + str(quantity), file=per)
        # print(str(b) + ';' + str(self.nom) + ';' + str(a))
        per.close()

    '''def vibor(self, razmer, nazv_weld_part):
        spis_det = {'К-СД1': 'k1-k2', 'К-СД1-З': 'k2-k1', 'К-СД2': 'k3-k3', 'К-СД3': 'k4-k4', 'К-СД4': 'k2-k7-k2',
                    'К-СД5': 'k1-k8-k1',
                    'К-СД6': 'k3-k9-k4', 'К-СД6-З': 'k4-k9-k3', 'К-СД7': 'k3-k14-k1', 'К-СД8': 'k4-k15-k2',
                    'К-СД9': 'k3-k13-k2', 'К-СД10': 'k4-k16-k1',
                    'С-СД1': 'c3-c3', 'С-СД2': 'c4-c4', 'С-СД3': 'c1-c2', 'С-СД3-З': 'c2-c1', 'С-СД4': 'c3-c9-c4',
                    'С-СД4-З': 'c4-c9-c3', 'С-СД5': 'c2-c7-c2', 'С-СД6': 'c1-c8-c1',
                    'С-СД7': 'c3-c14-c1', 'С-СД8': 'c2-c15-c4', 'С-СД9': 'c2-c13-c3', 'С-СД10': 'c1-c16-c4',
                    'К-СД11': 'kc2-kc8-kc1', 'К-СД12': 'kc2-kc9-kc1', 'К-СД13': 'kc2-kc2', 'К-СД14': 'kc1-kc1',
                    'К-СД15': 'kc2-kc5-kc2', 'К-СД16': 'kc1-kc4-kc1',
                    'Ш-СД1': 's3-s3a', 'Ш-СД2': 's4-s4a', 'Ш-СД2-З': 's4a-s4', 'Ш-СД1-З': 's3a-s3', 'Ш-СД3': 's3-s-s3',
                    'Ш-СД4': 's4-s-s4', 'Ш-СД7': 's3-s12', 'Ш-СД8': 's4-s11', 'Ш-СД9': 's4-s10', 'Ш-СД10': 's3-s9', 'Ш-СД11': 's3-s12',
                    'Ш-СД12': 's4-s11', 'Ш-СД13': 's4-s10', 'Ш-СД14': 's3-s9'}

        shini_2_os = ['Ш-СД1','Ш-СД2']
        shini_3_os = ['Ш-СД3', 'Ш-СД4', 'Ш-СД7', 'Ш-СД8', 'Ш-СД9', 'Ш-СД10', 'Ш-СД11', 'Ш-СД12', 'Ш-СД13', 'Ш-СД14']
        shini_3_det = ['Ш-СД7', 'Ш-СД8', 'Ш-СД9', 'Ш-СД10', 'Ш-СД11', 'Ш-СД12', 'Ш-СД13', 'Ш-СД14']

        for a in nazv_weld_part:    # из списка делателй для секции выбираем по очереди название каждой
            if any('Ш' in s for s in a):     # если это шины
                value = spis_det[a]  # "value" - это перечень деталей в сварной детали "a"  выбранный из списка
                q = re.findall(r'[^-]+', value)  # разбираем перечень "value" на список  "q"

                if a in shini_2_os:         # если это две оси шины "a"-это название сварной детали
                    if razmer[0] == razmer[1]:
                        det = Detali(razmer[0], self.H_stenka, self.H, self.A, self.B, self.C)
                        t = getattr(det, q[0])()  # запрашиваем нужную деталь
                        a = self.index.shet4()  # присваиеваем номер
                        h = ';'.join(t)  # делаем строку с разделением ;
                        quantity = int(self.quantity) * 2  # умножаем на 2 все детали в проекте
                        self.print(h, a, quantity)
                        print(t)
                    else:
                        w = 0
                        for b in q: # пока "b" в списке "q"
                            det = Detali(razmer[w], self.H_stenka, self.H, self.A, self.B, self.C)
                            t = getattr(det, b[w])()    #запрашиваем нужную деталь
                            a = self.index.shet4()      #присваиеваем номер
                            h = ';'.join(t)             #делаем строку с разделением ;
                            self.print(h, a, self.quantity)
                            print(t)
                            w = w + 1

                elif a in shini_3_os:  # если это три оси шины "a"-это название сварной детали
                    if a in shini_3_det:
                        for b in q:  # пока "b" в списке "q" "b" - это название детали
                            det = Detali(razmer[0], self.H_stenka, self.H, self.A, self.B, self.C)
                            t = getattr(det, b[0])()  # запрашиваем нужную деталь
                            a = self.index.shet4()  # присваиеваем номер
                            h = ';'.join(t)  # делаем строку с разделением ;
                            self.print(h, a, self.quantity)
                            print(t)
                            det = Detali(razmer[0], self.H_stenka, self.H, self.B, self.C, 0)
                            t = getattr(det, b[0])()  # запрашиваем нужную деталь
                            a = self.index.shet4()  # присваиеваем номер
                            h = ';'.join(t)  # делаем строку с разделением ;
                            self.print(h, a, self.quantity)
                            print(t)
                    else:
                        w = 0
                        for b in q:  # пока "b" в списке "q"
                            det = Detali(razmer[w], self.H_stenka, self.H, self.A, self.B, self.C)
                            t = getattr(det, b[w])()  # запрашиваем нужную деталь
                            a = self.index.shet4()  # присваиеваем номер
                            h = ';'.join(t)  # делаем строку с разделением ;
                            self.print(h, a, self.quantity)
                            print(t)
                            w = w + 1'''

    def slovar_spisok(self, nazv_svar_det): #выбор из словаря нужный список деталей
        slovar = {'К-СД1': 'k1-k2', 'К-СД1-З': 'k2-k1', 'К-СД2': 'k3-k3', 'К-СД3': 'k4-k4', 'К-СД4': 'k2-k7-k2',
                    'К-СД5': 'k1-k8-k1',
                    'К-СД6': 'k3-k9-k4', 'К-СД6-З': 'k4-k9-k3', 'К-СД7': 'k3-k14-k1', 'К-СД8': 'k4-k15-k2',
                    'К-СД9': 'k3-k13-k2', 'К-СД10': 'k4-k16-k1',
                    'С-СД1': 'c3-c3', 'С-СД2': 'c4-c4', 'С-СД3': 'c1-c2', 'С-СД3-З': 'c2-c1', 'С-СД4': 'c3-c9-c4',
                    'С-СД4-З': 'c4-c9-c3', 'С-СД5': 'c2-c7-c2', 'С-СД6': 'c1-c8-c1',
                    'С-СД7': 'c3-c14-c1', 'С-СД8': 'c2-c15-c4', 'С-СД9': 'c2-c13-c3', 'С-СД10': 'c1-c16-c4',
                    'К-СД11': 'kc2-kc8-kc1', 'К-СД12': 'kc2-kc9-kc1', 'К-СД13': 'kc2-kc2', 'К-СД14': 'kc1-kc1',
                    'К-СД15': 'kc2-kc5-kc2', 'К-СД16': 'kc1-kc4-kc1',
                    'Ш-СД1': 's3-s3a', 'Ш-СД2': 's4-s4a', 'Ш-СД2-З': 's4a-s4', 'Ш-СД1-З': 's3a-s3', 'Ш-СД3': 's3-s-s3',
                    'Ш-СД4': 's4-s-s4', 'Ш-СД7': 's3-s12', 'Ш-СД8': 's4-s11', 'Ш-СД9': 's4-s10', 'Ш-СД10': 's3-s9',
                    'Ш-СД11': 's3-s12',
                    'Ш-СД12': 's4-s11', 'Ш-СД13': 's4-s10', 'Ш-СД14': 's3-s9'}
        value = slovar[nazv_svar_det]  # "value" - это перечень деталей в сварной детали "a"  выбранный из списка
        self.spisok_det = re.findall(r'[^-]+', value)  # разбираем перечень "value" на список  "self.slovar_spisok"

    def vid(self, nazv_sv_det): # выбор что это шины или корпуса
        shini = ['Ш']
        korpus = ['К', 'С']
        pervaiya_bukva = re.findall(r'[^-]+', nazv_sv_det)[0]
        if pervaiya_bukva == shini[0]:
            return 'шины'
        elif pervaiya_bukva == korpus[0] or korpus[1]:
            return 'корпус'
        else:
            return 'ошибка'

    def osi(self, razmer):  # выбор сколько осей в детали
        a = len(razmer)
        if a == 2:
            return 2    # 2 оси
        elif a == 3:
            return 3    # 3 оси
        else:
            return False #ошибка

    def odinakovie_os(self, razmer):    # одинаковый ли размер осей (симметричная ли деталь)
        if razmer[0] == razmer[1]:
            return True    # одинаковый размер
        else:
            return False    # разные размеры

    def kol_det(self, nazv_sv_det):
        l = [7, 8, 9, 10, 11, 12, 13, 14]
        poslednyai_cifra = re.findall(r'[^-]+', nazv_sv_det)[-1]
        for poslednyai_cifra in l:
            return 1    #2 детали
        else:
            return 0    #3 детали

    def zapusk(self, spisok_svar_det):
        self.ABC(self.input_data)
        kol_os = self.osi(self.os)
        print('размер: ', self.os)
        print('кол-во осей: ', kol_os)
        print('список сварных деталей: ', spisok_svar_det)
        for svar_det in spisok_svar_det:
            print('обозначение сврной детали: ', svar_det)
            self.slovar_spisok(svar_det)
            print('список деталей: ', self.spisok_det)
            for det in self.spisok_det:
                tip = self.vid(det)  #получаем значение какой типа деталей 1-шины 2-корпус 3-ошибка
                print('тип детали: ', tip)
                if tip == 
                if kol_os == 2:
                    simetria = self.odinakovie_os(self.os)
                    print('симетрия: ', simetria)
                    if simetria == True:
                        det = Detali(self.A, self.H_stenka, self.H, self.A, self.B, self.C)
                        t = getattr(det, self.spisok_det[0])()  # запрашиваем нужную деталь
                        print(t, '\n')


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    f = Welded_part(['1600', 'УВ', '300х300', '2'])
    f.zapusk(['К-СД2', 'К-СД3', 'С-СД3', 'С-СД3-З', 'Ш-СД1', 'Ш-СД2', 'Ш-СД2-З', 'Ш-СД1-З'])