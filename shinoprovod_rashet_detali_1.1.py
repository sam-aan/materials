# coding^utf8
import re
import os

thisFile = "spisok_det.csv" #удаляем старый файл .csv
os.remove(thisFile)

p = open('spisok_det.txt', 'w') # создаем новй пустой файл
p.write('Обозначение;Длина L, мм.;Количество, шт.\n')
p.close()


def P (pr):#это для записи в текстовый файл новой строки
    pri = open('spisok_det.txt', 'a')
    pri.write(str(pr) + '\n')
    pri.close()


def P1 (pr, pr1, pr2):#это для записи в текстовый файл новой строки
    pri = open('spisok_det.txt', 'a')
    pri.write(str(pr) + ';' + str(pr1) + ';' + str(pr2) + ';' + '\n')
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
        kol = naz.kolichestvo
        razm = naz.razmer
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
            sec = Sekcii(os, kol)
            i = 0
            for i in nazvanie:
                if nazvanie == 'П':
                    print(sec.P())
                    break
                elif nazvanie == 'УГ':
                    print(sec.UG())
                    break
                elif nazvanie == 'УВ':
                    print(sec.UV())
                    break
                return
            return
        vib_sekc(naz.nazvanie, naz.razmer, naz.kolichestvo)

    f.close()     # закрывем файл
    return ()


class Sekcii:
    def __init__(self, os, kol):
        self.os = os
        self.kol = kol

    def P(self):    #расчет прямой
        self.kol = int(self.kol) * 2
        det = Detali(int(self.os), 0, 0, 0, 0)
        det1 = ['К', det.k(), self.kol]
        det2 = ['С', det.k(), self.kol]
        det3 = ['Н', int(raz.S_krishka * 2 + raz.H_krishka), 4]
        det4 = ['C', 40, 4]
        det5 = ['Ш1', det.S1(), self.kol]
        det6 = ['Ш2', det.S2(), self.kol]
        P1(det1[0], det1[1], det1[2])   #записываем в файл данные о детали
        P1(det2[0], det2[1], det2[2])
        P1(det3[0], det3[1], det3[2])
        P1(det4[0], det4[1], det4[2])
        P1(det5[0], det5[1], det5[2])
        P1(det6[0], det6[1], det6[2])
        return det1, det2, det3, det4, det5, det6


    def UG(self):
        self.kol = int(self.kol)  # вычисляем количесвто секций
        pattern = re.compile('[\d]+')
        oss = re.findall(pattern, self.os)

        X = oss[0]
        Y = oss[1]
        s_det1 = Detali(X, 0, 0, X, Y)    # krishka x1
        s_det2 = Detali(Y, 0, 0, X, Y)   # krishka y1
        s_det3 = Detali(X, 0, 0, X, Y)   # stenka x1
        s_det4 = Detali(Y, 0, 0, X, Y)   # stenka y1
        s_det5 = Detali(X, 0, 0, X, Y)   # krishka x2
        s_det6 = Detali(Y, 0, 0, X, Y)   # krishka y2
        s_det7 = Detali(X, 0, 0, X, Y)   # stenka x2
        s_det8 = Detali(Y, 0, 0, X, Y)   # stenka y2
        s_det9 = Detali(X, 0, 0, X, Y)   # shina x1
        s_det10 = Detali(X, 0, 0, X, Y)  # shina x2
        s_det11 = Detali(X, 0, 0, X, Y)  # shina x3
        s_det12 = Detali(X, 0, 0, X, Y)  # shina x4
        s_det13 = Detali(Y, 0, 0, X, Y)  # shina y1
        s_det14 = Detali(Y, 0, 0, X, Y)  # shina y2
        s_det15 = Detali(Y, 0, 0, X, Y)  # shina y3
        s_det16 = Detali(Y, 0, 0, X, Y)  # shina y4
        if X == Y:
            det1 = ['К2', s_det1.k2(), self.kol * 2]    # XY krishka
            det2 = ['К1', s_det2.k1(), self.kol * 2]    # XY krishka
            det3 = ['С3', s_det3.C3(), self.kol * 2]    # XY stenka
            det4 = ['С4', s_det4.C4(), self.kol * 2]    # XY stenka
            det5 = ['Ш3', s_det9.S3(), self.kol * 2]    # XY shina
            det6 = ['Ш4', s_det10.S4(), self.kol * 2]   # XY shina
            det7 = ['Ш5', s_det11.S5(), self.kol * 2]   # XY shina
            det8 = ['Ш6', s_det12.S6(), self.kol * 2]   # XY shina
            P1(det1[0], det1[1], det1[2])   #записываем в файл данные о детали
            P1(det2[0], det2[1], det2[2])
            P1(det3[0], det3[1], det3[2])
            P1(det4[0], det4[1], det4[2])
            P1(det5[0], det5[1], det5[2])
            P1(det6[0], det6[1], det6[2])
            P1(det7[0], det7[1], det7[2])
            P1(det8[0], det8[1], det8[2])
            return det1, det2, det3, det4, det5, det6, det7, det8
        else:
            det1 = ['К1', s_det1.k1(), self.kol]        #X krishka x1
            det2 = ['К2', s_det2.k2(), self.kol]         #Y krishka y1
            det3 = ['С3', s_det3.C3(), self.kol]        #X stenka x1
            det4 = ['С4', s_det4.C4(), self.kol]        #Y stenka y1
            det5 = ['К1', s_det5.k1(), self.kol]        #X krishka x2
            det6 = ['К2', s_det6.k2(), self.kol]        #Y krishka y2
            det7 = ['С3', s_det7.C3(), self.kol]        #X stenka x2
            det8 = ['С4', s_det8.C4(), self.kol]        #Y stenka y2
            det9 = ['Ш3', s_det9.S3(), self.kol * 2]    # X1 shina
            det10 = ['Ш4', s_det10.S4(), self.kol * 2]  # X2 shina
            det11 = ['Ш5', s_det11.S5(), self.kol * 2]  # X3 shina
            det12 = ['Ш6', s_det12.S6(), self.kol * 2]  # X4 shina
            det13 = ['Ш3', s_det13.S3(), self.kol * 2]  # Y1 shina
            det14 = ['Ш4', s_det14.S4(), self.kol * 2]  # Y2 shina
            det15 = ['Ш5', s_det15.S5(), self.kol * 2]  # Y3 shina
            det16 = ['Ш6', s_det16.S6(), self.kol * 2]  # Y4 shina
            P1(det1[0], det1[1], det1[2])
            P1(det2[0], det2[1], det2[2])
            P1(det3[0], det3[1], det3[2])
            P1(det4[0], det4[1], det4[2])
            P1(det5[0], det5[1], det5[2])
            P1(det6[0], det6[1], det6[2])
            P1(det7[0], det7[1], det7[2])
            P1(det8[0], det8[1], det8[2])
            P1(det9[0], det9[1], det9[2])
            P1(det10[0], det10[1], det10[2])
            P1(det11[0], det11[1], det11[2])
            P1(det12[0], det12[1], det12[2])
            P1(det13[0], det13[1], det13[2])
            P1(det14[0], det14[1], det14[2])
            P1(det15[0], det15[1], det15[2])
            P1(det16[0], det16[1], det16[2])
        return det1, det2, det3, det4, det5, det6, det7, det8, det9, det10, det11, det12, det13, det14, det15, det16


    def UV(self):
        self.kol = int(self.kol)  # вычисляем количесвто прямых секций
        pattern = re.compile('[\d]+')
        oss = re.findall(pattern, self.os)

        X = oss[0]
        Y = oss[1]
        s_det1 = Detali(X, 0, 0, 0, 0)   # krishka x1
        s_det2 = Detali(Y, 0, 0, 0, 0)   # krishka y1
        s_det3 = Detali(X, 0, 0, 0, 0)   # stenka x1
        s_det4 = Detali(Y, 0, 0, 0, 0)   # stenka y1
        s_det5 = Detali(X, 0, 0, 0, 0)   # krishka x2
        s_det6 = Detali(Y, 0, 0, 0, 0)   # krishka y2
        s_det7 = Detali(X, 0, 0, 0, 0)   # stenka x2
        s_det8 = Detali(Y, 0, 0, 0, 0)   # stenka y2
        s_det9 = Detali(X, 0, 0, X, Y)   # shina xy1
        s_det10 = Detali(X, 0, 0, X, Y)  # shina xy2
        s_det11 = Detali(X, 0, 0, X, Y)  # shina xy3
        s_det12 = Detali(X, 0, 0, X, Y)  # shina xy4
        if X == Y:
            det1 = ['К3', s_det1.k3(), self.kol * 2]    #XY krishka
            det2 = ['К4', s_det2.k4(), self.kol * 2]    #XY krishka
            det3 = ['С1', s_det3.C1(), self.kol * 2]    #XY stenka
            det4 = ['С2', s_det4.C2(), self.kol * 2]    #XY stenka
            det5 = ['Ш7', s_det9.S7(), self.kol * 2]    # XY shina 1
            det6 = ['Ш8', s_det10.S8(), self.kol * 2]    # XY shina 2
            det7 = ['Ш9', s_det11.S9(), self.kol * 2]    # XY shina 3
            det8 = ['Ш10', s_det12.S10(), self.kol * 2]    # XY shina 4
            P1(det1[0], det1[1], det1[2])  # записываем в файл данные о детали
            P1(det2[0], det2[1], det2[2])
            P1(det3[0], det3[1], det3[2])
            P1(det4[0], det4[1], det4[2])
            P1(det5[0], det5[1], det5[2])
            P1(det6[0], det6[1], det6[2])
            P1(det7[0], det7[1], det7[2])
            P1(det8[0], det8[1], det8[2])
            return det1, det2, det3, det4, det5, det6, det7, det8
        else:
            det1 = ['К3', s_det1.k3(), self.kol]     #X krishka
            det2 = ['К4', s_det2.k4(), self.kol]     #Y krishka
            det3 = ['С1', s_det3.C1(), self.kol]    #X stenka
            det4 = ['С2', s_det4.C2(), self.kol]    #Y stenka
            det5 = ['К3', s_det5.k1(), self.kol]    #X krishka
            det6 = ['К4', s_det6.k2(), self.kol]    #Y krishka
            det7 = ['С1', s_det7.C1(), self.kol]    #X stenka
            det8 = ['С2', s_det8.C2(), self.kol]    #Y stenka
            det9 = ['Ш7', s_det9.S7(), self.kol * 2]  # XY shina 1
            det10 = ['Ш8', s_det10.S8(), self.kol * 2]  # XY shina 2
            det11 = ['Ш9', s_det11.S9(), self.kol * 2]  # XY shina 3
            det12 = ['Ш10', s_det12.S10(), self.kol * 2]  # XY shina 4
            P1(det1[0], det1[1], det1[2])
            P1(det2[0], det2[1], det2[2])
            P1(det3[0], det3[1], det3[2])
            P1(det4[0], det4[1], det4[2])
            P1(det5[0], det5[1], det5[2])
            P1(det6[0], det6[1], det6[2])
            P1(det7[0], det7[1], det7[2])
            P1(det8[0], det8[1], det8[2])
            P1(det9[0], det9[1], det9[2])
            P1(det10[0], det10[1], det10[2])
            P1(det11[0], det11[1], det11[2])
            P1(det12[0], det12[1], det12[2])
        return det1, det2, det3, det4, det5, det6, det7, det8, det9, det10, det11, det12

class Detali:
    def __init__(self, os, L, L1, A, B):
        self.os = os
        self.L = L
        self.L1 = L1
        self.A = A
        self.B = B


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


    def C1(self):
        self.L = float(self.os) - float(raz.R_kor) + float(raz.H_stenka) / 2
        return self.L


    def C2(self):
        self.L = float(self.os) - float(raz.R_kor) + float(raz.H_stenka) / 2
        return self.L


    def C3(self):
        self.L = float(self.os) - float(raz.R_kor) - float(raz.H_paketa) / 2
        return self.L


    def C4(self):
        self.L = float(self.os) - float(raz.R_kor) - float(raz.H_paketa) / 2
        return self.L


    def C5(self):
        self.L = float(self.os) + float(raz.H_stenka)
        return self.L


    def C7(self):
        self.L = float(self.os) + float(raz.H_stenka)
        return self.L


    def C8(self):
        self.L = float(self.os) + float(raz.H_stenka)
        return self.L


    def C9(self):
        self.L = float(self.os) + float(raz.S_stenka)
        return self.L


    def C11(self):
        self.L = float(self.os) + float(raz.S_stenka) * 2 + float(raz.H_paketa)
        return self.L


    def C12(self):
        self.L = float(self.os) - float(raz.H_paketa)
        return self.L


    def C13(self):
        self.L = float(self.os) + float(raz.H_stenka) / 2 + float(raz.S_stenka) + float(raz.H_paketa) / 2
        return self.L


    def C14(self):
        self.L = float(self.os) + float(raz.H_stenka) / 2 + float(raz.S_stenka) + float(raz.H_paketa) / 2
        return self.L


    def C15(self):
        self.L = float(self.os) + float(raz.H_stenka) / 2 + float(raz.H_paketa) / 2
        return self.L


    def C16(self):
        self.L = float(self.os) + float(raz.H_stenka) / 2 + float(raz.H_paketa) / 2
        return self.L

    def S1(self):
        self.L = float(self.os) - float(raz.R_sh) * 2
        self.L1 = float(self.L) + 4.6
        return self.L, self.L1

    def S2(self):
        self.L = float(self.os) - float(raz.R_sh) * 2
        self.L1 = float(self.L) + 0.4
        return self.L, self.L1

    def S3(self):
        self.L = float(self.os) - float(raz.R_sh) + float(raz.H) / 2
        self.L1 = float(self.L) + 4.6
        return self.L, self.L1

    def S4(self):
        self.L = float(self.os) - float(raz.R_sh) + float(raz.H) / 2
        self.L1 = float(self.L) + 4.6
        return self.L, self.L1

    def S5(self):
        self.L = float(self.os) - float(raz.R_sh) + float(raz.H) / 2
        self.L1 = float(self.L) + 0.4
        return self.L, self.L1

    def S6(self):
        self.L = float(self.os) - float(raz.R_sh) + float(raz.H) / 2
        self.L1 = float(self.L) + 0.4
        return self.L, self.L1

    def S7(self):
        self.A = float(self.A) - 11.25
        self.B = float(self.B) - 11.25
        self.L1 = float(self.A) + float(self.B)
        return self.L1, self.A, self.B

    def S8(self):
        self.A = float(self.A) - 20.7
        self.B = float(self.B) - 20.7
        self.L1 = float(self.A) + float(self.B)
        return self.L1, self.A, self.B

    def S9(self):
        self.A = float(self.A) - 26.57
        self.B = float(self.B) - 26.57
        self.L1 = float(self.A) + float(self.B)
        return self.L1, self.A, self.B

    def S10(self):
        self.A = float(self.A) - 30.99
        self.B = float(self.B) - 30.99
        self.L1 = float(self.A) + float(self.B)
        return self.L1, self.A, self.B

V_nom()
thisFile = "spisok_det.txt"
base = os.path.splitext(thisFile)[0]
os.rename(thisFile, base + ".csv")