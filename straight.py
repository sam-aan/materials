# coding^utf8
import re
from schet import schetchik
from detali import Detali
import nominal


class straight:
    def __init__(self, razmer, nazvanie, proekt, kol, nom,  ssh, ss):
        self.razmer = razmer
        self.osx = 0
        self.osy = 0
        self.osz = 0
        self.nazvanie = nazvanie
        self.proekt = proekt
        self.ssh =ssh
        self.ss = ss
        self.kol = kol
        self.nom = nom
        self.indeks = schetchik(0, 0)
        self.etag = 0

    def calculation(self, os, d):
        det = Detali(os, self.ssh, self.ss, self.osx, self.osy, self.osz)
        per = open('specifikaciya.txt', 'a')
        print('\nДетали\n')
        print('Детали', file=per)
        per.close()
        z = 0
        for i in d:
            t = getattr(det, d[z])()
            itog = str(str(self.indeks.shet4()) + ';' + str(self.nom) + ';' + str(';'.join(t)) + ';' + str(self.kol))
            per = open('specifikaciya.txt', 'a')
            per1 = open('spisok_det.txt', 'a')
            print(itog)
            print(itog, file=per)
            print(itog, file=per1)
            per.close()
            per1.close()

            z = z + 1


    def calculation_sh(self, os, d):    #длина по оси и os и список деталей d
        q = re.findall(r'[^хХxX*]+', self.razmer)
        per = open('specifikaciya.txt', 'a')
        print('\nДетали\n')
        print('Детали', file=per)
        per.close()
        z = 0
        for i in d:
            det = Detali(os, self.ssh, self.ss, self.osx, self.osy, self.osz)
            t = getattr(det, d[z])()
            itog = str(str(self.indeks.shet4()) + ';' + str(self.nom) + ';' + str(';'.join(t)) + ';' + str(self.kol))
            per = open('specifikaciya.txt', 'a')
            per1 = open('spisok_det_sh.txt', 'a')
            print(itog)
            print(itog, file=per)
            print(itog, file=per1)
            per.close()
            per1.close()
            z = z + 1

    def vibor(self):

        vv = nominal.vvod_znach(self.nom)
        self.etag = vv.calc_nom_2_etag() #это разница между этажами
        q = re.findall(r'\d+', self.razmer)

        if self.nazvanie == 'П':
            self.osx = q[0]
            d = ['c', 'c', 'k', 'k']
            s = ['s1', 's1', 's2', 's2']
            self.calculation(self.osx, d)
            self.calculation_sh(self.osx, s)

        elif self.nazvanie == 'УГ':
            self.osx = q[0]
            self.osy = q[1]
            self.razmer = self.osx + self.osy
            s = ['s7', 's8', 's9', 's10']
            self.calculation_sh(s)

        elif self.nazvanie == '2УВ':
            print('***Верх шины***')
            self.osx = float(q[0]) + self.etag
            self.osy = float(q[1]) + self.etag
            spis_det = ['s3.s3a', 's4.s4a', 's4a.s4', 's3a.s3']
            self.calculation_sh(spis_det)       #не водим размер оси, он зашит в self.razmer

            print('***Низ шины***')
            self.osx = float(p[0]) - self.etag
            self.osy = float(p[1]) - self.etag
            spis_det = ['k4.k4', 'c1.c2', 'c2.c1', 's3.s3a', 's4.s4a', 's4a.s4', 's3a.s3']
            self.calculation_sh(0, spis_det)

        else:
            return 0