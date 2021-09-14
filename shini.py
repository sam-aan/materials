# coding^utf8
import re
from schet import schetchik
from detali import Detali

class shini:
    def __init__(self, razmer, nazvanie, proekt, kol, nom,  ssh, ss):
        self.razmer = razmer
        self.nazvanie = nazvanie
        self.proekt = proekt
        self.osx = 0
        self.osy = 0
        self.osz = 0
        self.ssh =ssh
        self.ss =ss
        self.nomberS = 0
        self.kol = kol
        self.nom = nom
        self.indeks = schetchik(0, 0)


    def calculation(self, d):
        q = re.findall(r'\d+', self.razmer)
        l = 0
        per = open('specifikaciya.txt', 'a')
        print('Детали сборки шины', file=per)
        per.close()
        print('\nДетали сборки шины\n')
        for i in q:
            os = q[l]
            det = Detali(os, self.ssh, self.ss, self.osx, self.osy, self.osz)
            t = getattr(det, d[l])()
            itog = str(str(self.indeks.shet4()) + ';' + str(self.nom) + ';' + str(';'.join(t)) + ';' + str(self.kol))
            sofe = open('spisok_det_sh.txt', 'a')
            print(str(itog), file= sofe)
            per = open('specifikaciya.txt', 'a')
            print(itog)
            print(itog, file=per)
            per.close()
            sofe.close()
            l = l + 1


    def vibor(self):
        if self.nazvanie == 'УВ':
            q = re.findall(r'\d+', self.razmer)
            self.osx = q[0]
            print(self.osx)
            self.osy = q[1]
            spis_det = ['s3.s3', 's4.s3', 's6.s5', 's5.s6']
            self.sborka(spis_det)
        else:
            return 0

    def sborka(self, spis_det):
        r = 0
        for i in spis_det:
            s = spis_det[r]
            df = re.findall(r'[^.]+', s)
            itog_s = str(self.indeks.shet3()) + ';' + str(self.nom) + ';' + '-'.join(df) + ';' + str(self.kol)
            sof = open('spisok_sborok.txt', 'a')
            print(itog_s, file=sof)
            sof.close()
            per = open('specifikaciya.txt', 'a')
            print(itog_s)
            print(itog_s, file=per)
            per.close()

            self.calculation(df)
            print('.' * 15)
            r = r + 1