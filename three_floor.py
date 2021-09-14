# coding^utf8

from detali import Detali
from nominal import vvod_znach
import re
from schet import schetchik

class calculation:
    def __init__(self, input_data, a):
        self.input_data = input_data
        self.H = 0
        self.H_stenka =0
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
        self.a = a
        self.L1_sh = 0
        self.L2_sh = 0
        self.S_sh = 0


    def choice(self):

        slovar_old = {'К-СД1': 'k1-k2', 'К-СД1-З': 'k2-k1', 'К-СД2': 'k3-k3', 'К-СД3': 'k4-k4', 'К-СД4': 'k2-k7-k2',
                    'К-СД5': 'k1-k8-k1', 'К-СД6': 'k3-k9-k4', 'К-СД6-З': 'k4-k9-k3', 'К-СД7': 'k3-k14-k1', 'К-СД8': 'k4-k15-k2',
                    'К-СД9': 'k3-k13-k2', 'К-СД10': 'k4-k16-k1',
                    'С-СД1': 'c3-c3', 'С-СД2': 'c4-c4', 'С-СД3': 'c1-c2', 'С-СД3-З': 'c2-c1', 'С-СД4': 'c3-c9-c4',
                    'С-СД4-З': 'c4-c9-c3', 'С-СД5': 'c2-c7-c2', 'С-СД6': 'c1-c8-c1', 'С-СД7': 'c3-c14-c1', 'С-СД8': 'c2-c15-c4',
                    'С-СД9': 'c2-c13-c3', 'С-СД10': 'c1-c16-c4',
                    'К-СД11': 'kc2-kc8-kc1', 'К-СД12': 'kc2-kc9-kc1', 'К-СД13': 'kc2-kc2', 'К-СД14': 'kc1-kc1',
                    'К-СД15': 'kc2-kc5-kc2a', 'К-СД16': 'kc1-kc4-kc1',
                    'Ш-СД1': 's3-s3a', 'Ш-СД1-З': 's3a-s3', 'Ш-СД2': 's4-s4a', 'Ш-СД2-З': 's4a-s4', 'Ш-СД3': 's3-s-s3',
                    'Ш-СД4': 's4-s-s4', 'Ш-СД7': 's3-s12', 'Ш-СД8': 's4-s11', 'Ш-СД9': 's4-s10', 'Ш-СД10': 's3-s9',
                    'Ш-СД11': 's3-s12', 'Ш-СД12': 's4-s11', 'Ш-СД13': 's4-s10', 'Ш-СД14': 's3-s9'}


        if self.a == 0:
            self.slovar = slovar_old
        elif self.a == 1:
            self.slovar = slovar_new
        else:
            print('Ошибка 101')