# coding^utf8
import re
import os
import datetime

series_nomber = input('Введите номер заказа ')
print(series_nomber)
now = datetime.datetime.today().strftime("%Y")
print(now)
arr = os.listdir()  # читаем что находится в директории
q = 0
thisFile = "spisok_det.csv"
thisFile2 = "spisok_shin.csv"
for j in arr:
    if arr[q] == thisFile: #удаляем старый файл .csv
        print(arr[q])
        os.remove(thisFile)
        q = q + 1
    elif arr[q] == thisFile2: #удаляем старый файл .csv
        print(arr[q])
        os.remove(thisFile2)
        q = q + 1
    else:
        q = q + 1

p_korpus = open('spisok_det.txt', 'w') # создаем новй пустой файл для корпусов
p_korpus.write('Серийный номер;Обозначение;Длина L, мм.;Количество, шт.\n')
p_korpus.close()

p_shina = open('spisok_shin.txt', 'w') # создаем новй пустой файл для шин
p_shina.write('Серийный номер;Обозначение;Длина L, мм.;Размер L1, мм.;Размер А, мм.;Размер Б, мм.;Количество, шт.\n')
p_shina.close()


def P (pr):#это для записи в текстовый файл новой строки
    pri = open('spisok_det.txt', 'a')
    pri.write(str(pr) + '\n')
    pri.close()


def P1 (pr, pr1, pr2, pr3):#это для записи в текстовый файл новой строки
    pri = open('spisok_det.txt', 'a')
    pri.write(str(pr) + ';' + str(pr1) + ';' + str(pr2) + ';' + str(pr3) + ':' + '\n')
    pri.close()

def P2 (pr1, pr2, pr3, pr4, pr5, pr6, pr7, pr8):#это для записи в текстовый файл новой строки
    pri = open('spisok_shin.txt', 'a')
    pri.write(str(pr1) + ';' + str(pr2) + ';' + str(pr3) + ';' + str(pr4) + ';' + str(pr5) + ';' + str(pr6) + ';' + str(pr7) + ';' + str(pr8) + ':' + '\n')
    pri.close()

class Nazvanie:
    def __init__(self, nominal, nazvanie, razmer, kolichestvo):
        self.nominal = nominal
        self.nazvanie = nazvanie
        self.razmer = razmer
        self.kolichestvo = kolichestvo


class Razmer:
    def __init__(self, H_stenka, S_stenka, H_krishka, S_krishka, H, S, H_paketa, R_sh, R_kor):
        self.H_stenka = H_stenka    # ширина стенки
        self.S_stenka = S_stenka    # высота стенки
        self.H_krishka = H_krishka  # ширина крышки
        self.S_krishka = S_krishka  # высота крышки
        self.H = H                  # ширина шины
        self.S = S                  # толщина шины
        self.H_paketa = H_paketa    # толщина пакета
        self.R_sh = R_sh            # растояние от оси до шины
        self.R_kor = R_kor          # растояние от оси до корпуса

raz = Razmer(0, 25, 125, 33, 0, 6, 27, 20.5, 118.5)  # присваиваем значения из списка в класс


def V_nom():
    f = open('wod_det.txt')  # отркываем и читаем файл
    line = (f.readline().rstrip())  # начинаем читать построчно
    counter_sekc = 0
    while line:    # начинаем перебор построчно
        result = re.findall(r'\S+', line) #создаем список из строки
        print('\n', result)
        naz = Nazvanie(result[0], result[1], result[2], result[3])  # присваиваем значения из списка в класс
        print('Номинальный ток ', naz.nominal)
        print('Обозначение секции ', naz.nazvanie)
        print('Габариты секции ', naz.razmer)
        print('Количество секций ', naz.kolichestvo)
        def vibor_nominala(i):
            if i == '630':
                raz.H = 40
                raz.S = 6
            elif i == '800':
                raz.H = 55
                raz.S = 6
            elif i == '1000':
                raz.H = 80
                raz.S = 6
            elif i == '1250':
                raz.H = 110
                raz.S = 6
            elif i == '1600':
                raz.H = 160
                raz.S = 6
            elif i == '2000':
                raz.H = 200
                raz.S = 6
            elif i == '2500':
                raz.H = 110
                raz.S = 6
            elif i == '3200':
                raz.H = 160
                raz.S = 6
            elif i == '4000':
                raz.H = 200
                raz.S = 6
            else:
                print("Ошибка")
            return(i)
        vibor_nominala(naz.nominal) # запускаем выбор номинала для опредеоения ширины шины
        line = f.readline()    # присваем значению line следующую строку
        raz.H_stenka = raz.H + 3    # расчет ширины стенки
        bh = raz.H  # ширина шины
        bs = raz.S  # толщина шины
        kh = raz.H_krishka  # ширина крышки
        ks = raz.S_krishka  # высоты крышки
        sh = raz.H_stenka   # ширина стенки
        ss = raz.S_stenka   # высота стенки
        hp = raz.H_paketa # толщина пакета
        osk = raz.R_kor # растояние от корпуса до оси
        oss = raz.R_sh  # растояние от шины до оси
        index_s = "%03d" % counter_sekc
        ser_nom_sekc = (str(index_s) + '.' + str(series_nomber) + '-' + str(naz.nominal) + '-' + str(naz.nazvanie) + '-' + str(naz.razmer))
        print(ser_nom_sekc)
        counter_sekc = counter_sekc + 1
        counter_det = 0
        print('Ширина шины ', bh)
        print('Толщина шины ', bs)
        print('Ширина крышки ', kh)
        print('Высота крышки ', ks)
        print('Ширина стенки ', sh)
        print('Высота стенки ', ss)
        print('Толщина пакета ', hp)
        print('Растояние от корпуса до оси ', osk)
        print('Растояние от шины до оси ', oss)


        def vib_sekc(nazvanie, os, kol):   #выбираем какая у нас будет секция и вызываем метод из класса
            i = 0
            for i in nazvanie:
                if nazvanie == 'П':
                    korpus = ['k', 'k', 'c', 'c']
                    shini = ['s1', 's2']
                    sec = Sekcii(os, kol, korpus, shini, 0, 0, 0, index_s)
                    print(sec.K())
                    print(sec.S_P())
                    break
                elif nazvanie == 'УГ':
                    pattern = re.compile('[\d]+')
                    oss = re.findall(pattern, os)
                    X = oss[0]
                    Y = oss[1]
                    korpus = ['k1', 'k2', 'c3', 'c4']
                    shini = ['s7', 's8', 's9', 's10']
                    sec = Sekcii(X, kol, korpus, shini, X, Y, 0, index_s)
                    print(sec.K())
                    sec = Sekcii(Y, kol, korpus, shini, X, Y, 0, index_s)
                    print(sec.S_G())
                    break
                elif nazvanie == 'УВ':
                    pattern = re.compile('[\d]+')
                    oss = re.findall(pattern, os)
                    X = oss[0]
                    Y = oss[1]
                    korpus = ['k3', 'k4', 'c1', 'c2']
                    shini = ['s3', 's4', 's5', 's6']
                    sec = Sekcii(X, kol, korpus, shini, X, Y, 0, index_s)
                    print(sec.K())
                    sec = Sekcii(Y, kol, korpus, shini, X, Y, 0, index_s)
                    print(sec.S_P())
                    break
                return
            return
        vib_sekc(naz.nazvanie, naz.razmer, naz.kolichestvo)

    f.close()     # закрывем файл
    return ()


class Sekcii:
    def __init__(self, os, kol, korpus, shini, X, Y, c_det, c_cek):
        self.os = os
        self.kol = kol
        self.korpus = korpus
        self.shini = shini
        self.X = X
        self.Y = Y
        self.c_det = c_det  # счетчик деталей
        self.c_cek = c_cek  # счетчик секций


    def K(self):    #расчет корпусов
        det = Detali(int(self.os), 0, 0, self.X, self.Y, 0)
        spisok = self.korpus
        z = 0
        for counter_det, i in enumerate(spisok):
            a = getattr(det, spisok[z])()
            korp = [spisok[z], a, self.kol]
            print(korp)
            index_d = "%04d" % counter_det
            self.c_det = index_d
            ser_nom_det = (str(self.c_det) + '.' + str(self.c_cek) + '.' + str(series_nomber))
            print(ser_nom_det)
            P1(ser_nom_det, korp[0], korp[1], korp[2])
            self.c_det = int(self.c_det) + 1
            z = z + 1

    def S_P(self):  # расчет шины прямые
        det = Detali(int(self.os), 0, 0, 0, 0, 0)
        spisok2 = self.shini
        d = 0
        for i in spisok2:
            b = getattr(det, spisok2[d])()
            korp2 = [spisok2[d], b[0], b[1], self.kol]
            print(korp2)
            ser_nom_det = (str(self.c_cek) + '-' + str(self.c_det) + '-' + str(spisok2[d]) + '-' + str(b))
            print(ser_nom_det)
            P2(ser_nom_det, korp2[0], korp2[1], korp2[2], '', '', '', korp2[3])
            self.c_det = int(self.c_det) + 1
            d = d + 1

    def S_G(self):  # расчет шины гнутые
        det = Detali(int(self.os), 0, 0, self.X, self.Y, 0)
        spisok3 = self.shini
        e = 0
        for i in spisok3:
            b = getattr(det, spisok3[e])()
            korp2 = [spisok3[e], b[0], b[1], b[2], self.kol]
            print(korp2)
            ser_nom_det = (str(self.c_cek) + '-' + str(self.c_det) + '-' + str(spisok3[e]) + '-' + str(b))
            print(ser_nom_det)
            P2(ser_nom_det, korp2[0], '', korp2[1], korp2[2], korp2[3], '', korp2[4])
            self.c_det = int(self.c_det) + 1
            e = e + 1


class Detali:
    def __init__(self, os, L, L1, A, B, C):
        self.os = os
        self.L = L
        self.L1 = L1
        self.A = A
        self.B = B
        self.C = C


    def k(self):  # N это длина по оси КРЫШКИ
        self.L = float(self.os) - float(raz.R_kor) * 2
        return self.L


    def k1(self):
        self.L = float(self.os) - float(raz.R_kor) + float(raz.H_krishka) / 2
        return self.L


    def k2(self):
        self.L = float(self.os) - float(raz.R_kor) + float(raz.H_krishka) / 2
        return self.L


    def k3(self):
        self.L = float(self.os) - float(raz.R_kor) + float(raz.H_stenka) / 2 + float(raz.H_krishka)
        return self.L


    def k4(self):
        self.L = float(self.os) - float(raz.R_kor) + float(raz.H_stenka) / 2 + float(raz.H_krishka)
        return self.L


    def k5(self):
        self.L = float(self.os) + float(raz.H_krishka)
        return self.L


    def k7(self):
        self.L = float(self.os) + float(raz.H_krishka)
        return self.L


    def k8(self):
        self.L = float(self.os) + float(raz.H_krishka)
        return self.L


    def k9(self):
        self.L = float(self.os) + float(raz.S_krishka)
        return self.L


    def k11(self):
        self.L = float(self.os) + float(raz.S_krishka) + float(raz.H_krishka)
        return self.L


    def k12(self):
        self.L = float(self.os) + float(raz.H_krishka) / 2 + float(raz.H_stenka) / 2 + float(raz.S_krishka)
        return self.L


    def k13(self):
        self.L = float(self.os) + float(raz.H_krishka) / 2 + float(raz.H_stenka) / 2 + float(raz.S_krishka)
        return self.L


    def k14(self):
        self.L = float(self.os) + float(raz.H_krishka) / 2 + float(raz.H_stenka) / 2 + float(raz.S_krishka)
        return self.L

    def k15(self):
        self.L = float(self.os) + float(raz.H_krishka) / 2 - float(raz.H_stenka) / 2
        return self.L


    def k16(self):
        self.L = float(self.os) + float(raz.H_krishka) / 2 - float(raz.H_stenka) / 2
        return self.L


    def c(self):  # N это длина по оси КРЫШКИ
        self.L = float(self.os) - float(raz.R_kor) * 2
        return self.L


    def c1(self):
        self.L = float(self.os) - float(raz.R_kor) + float(raz.H_stenka) / 2
        return self.L


    def c2(self):
        self.L = float(self.os) - float(raz.R_kor) + float(raz.H_stenka) / 2
        return self.L


    def c3(self):
        self.L = float(self.os) - float(raz.R_kor) - float(raz.H_paketa) / 2
        return self.L


    def c4(self):
        self.L = float(self.os) - float(raz.R_kor) - float(raz.H_paketa) / 2
        return self.L


    def c5(self):
        self.L = float(self.os) + float(raz.H_stenka)
        return self.L


    def c7(self):
        self.L = float(self.os) + float(raz.H_stenka)
        return self.L


    def c8(self):
        self.L = float(self.os) + float(raz.H_stenka)
        return self.L


    def c9(self):
        self.L = float(self.os) + float(raz.S_stenka)
        return self.L


    def c11(self):
        self.L = float(self.os) + float(raz.S_stenka) * 2 + float(raz.H_paketa)
        return self.L


    def c12(self):
        self.L = float(self.os) - float(raz.H_paketa)
        return self.L


    def c13(self):
        self.L = float(self.os) + float(raz.H_stenka) / 2 + float(raz.S_stenka) + float(raz.H_paketa) / 2
        return self.L


    def c14(self):
        self.L = float(self.os) + float(raz.H_stenka) / 2 + float(raz.S_stenka) + float(raz.H_paketa) / 2
        return self.L


    def c15(self):
        self.L = float(self.os) + float(raz.H_stenka) / 2 + float(raz.H_paketa) / 2
        return self.L


    def c16(self):
        self.L = float(self.os) + float(raz.H_stenka) / 2 + float(raz.H_paketa) / 2
        return self.L


    def s1(self):
        self.L = float(self.os) - float(raz.R_sh) * 2
        self.L1 = float(self.L) + 4.6
        return [self.L, self.L1]

    def s2(self):
        self.L = float(self.os) - float(raz.R_sh) * 2
        self.L1 = float(self.L) + 0.4
        return [self.L, self.L1]

    def s3(self):
        self.L = float(self.os) - float(raz.R_sh) + float(raz.H) / 2
        self.L1 = float(self.L) + 4.6
        return [self.L, self.L1]

    def s4(self):
        self.L = float(self.os) - float(raz.R_sh) + float(raz.H) / 2
        self.L1 = float(self.L) + 4.6
        return [self.L, self.L1]

    def s5(self):
        self.L = float(self.os) - float(raz.R_sh) + float(raz.H) / 2
        self.L1 = float(self.L) + 0.4
        return [self.L, self.L1]

    def s6(self):
        self.L = float(self.os) - float(raz.R_sh) + float(raz.H) / 2
        self.L1 = float(self.L) + 0.4
        return [self.L, self.L1]

    def s7(self):
        self.A = round(float(self.A) - 11.25, 1)
        self.B = round(float(self.B) - 11.25, 1)
        self.L1 = float(self.A) + float(self.B)
        return [self.L1, self.A, self.B]

    def s8(self):
        self.A = round(float(self.A) - 20.7, 1)
        self.B = round(float(self.B) - 20.7, 1)
        self.L1 = float(self.A) + float(self.B)
        return [self.L1, self.A, self.B]

    def s9(self):
        self.A = round(float(self.A) - 26.57, 1)
        self.B = round(float(self.B) - 26.57, 1)
        self.L1 = float(self.A) + float(self.B)
        return [self.L1, self.A, self.B]

    def s10(self):
        self.A = round(float(self.A) - 30.99, 1)
        self.B = round(float(self.B) - 30.99, 1)
        self.L1 = float(self.A) + float(self.B)
        return [self.L1, self.A, self.B]

V_nom()

thisFile = "spisok_det.txt"
base = os.path.splitext(thisFile)[0]
os.rename(thisFile, base + ".csv")

thisFile2 = "spisok_shin.txt"
base = os.path.splitext(thisFile2)[0]
os.rename(thisFile2, base + ".csv")