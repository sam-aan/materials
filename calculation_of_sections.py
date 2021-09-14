# coding^utf8
import re
from welded_part import Welded_part
import nominal

class welded_parts:
    def __init__(self, input_data):
        self.input_data = input_data    # 0-номинал 1-название 2- размер 3-кол-во
        self.razmer = 0
        self.nazvanie = ''
        self.osx = 0
        self.osy = 0
        self.osz = 0
        self.ssh = 0    #   размер "H" стенки
        self.ss = 0     #   размер "H" шины
        self.nomberS = 0
        self.kol = 0
        self.nom = 0
        self.etag = 0
        self.itog = ''

    def vibor(self):

        vv = nominal.vvod_znach(int(self.input_data[0]))    # ввод данных для вычисления размера стенок и шин
        self.etag = vv.calc_nom()[2]                        # вычисляем разницу между этажами исходя из номинала
        self.ssh = vv.calc_nom()[0]
        self.ss = vv.calc_nom()[1]

        size_axis = re.findall(r'[^хХxX*]+', self.input_data[2])   #записываем размер осей в список. Пример: ['300', '300']

        if self.input_data[1] == 'П':

            part_list = ['c', 'k', 's1', 's2']    #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, 0, 0, 0, self.input_data[3])
            output = v.Many_det2(size_axis, part_list, 2)   # размер осей и список деталей
            print(output)

        elif self.input_data[1] == '2П':

            part_list = ['c', 'k', 's1', 's2']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, 0, 0, 0, self.input_data[3])
            output = v.Many_det2(size_axis, part_list, 2)  # размер осей и список деталей
            print(output)

            part_list = ['kc']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, 0, 0, 0, self.input_data[3])
            output = v.Many_det2(size_axis, part_list, 1)  # размер осей и список деталей
            print(output)

        if self.input_data[1] == 'ОМ':

            part_list = ['c', 'k', 's1', 's2']    #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, 0, 0, 0, self.input_data[3])
            output = v.Many_det2(size_axis, part_list, 2)   # размер осей и список деталей
            print(output)

        elif self.input_data[1] == '2ОМ':

            part_list = ['c', 'k', 's1', 's2']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, 0, 0, 0, self.input_data[3])
            output = v.Many_det2(size_axis, part_list, 2)  # размер осей и список деталей
            print(output)

            part_list = ['kc']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, 0, 0, 0, self.input_data[3])
            output = v.Many_det2(size_axis, part_list, 1)  # размер осей и список деталей
            print(output)

        elif self.input_data[1] == 'УГ':
            part_list = ['К-СД1', 'К-СД1-З', 'С-СД1', 'С-СД2']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis[0], size_axis[1], 0, self.input_data[3])
            output = v.Many_det(size_axis, part_list, 1)
            print(output)

            part_list2 = ['s5', 's6', 's7', 's8']
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis[0], size_axis[1], 0, self.input_data[3])
            output = v.Many_det2(size_axis, part_list2, 1)  # размер осей и список деталей
            print(output)

        elif self.input_data[1] == '2УГ':
            part_list = ['С-СД1', 'С-СД2']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis[0], size_axis[1], 0, self.input_data[3])
            output = v.Many_det(size_axis, part_list, 1)
            print(output)

            part_list = ['К-СД1', 'К-СД1-З', 'К-СД13']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis[0], size_axis[1], 0, self.input_data[3])
            output = v.Many_det(size_axis, part_list, 1)
            print(output)

            part_list2 = ['s5', 's6', 's7', 's8']
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis[0], size_axis[1], 0, self.input_data[3])
            output = v.Many_det2(size_axis, part_list2, 1)  # размер осей и список деталей
            print(output)

        elif self.input_data[1] == 'УВ':
            part_list = ['К-СД2', 'К-СД3', 'С-СД3', 'С-СД3-З', 'Ш-СД1', 'Ш-СД2', 'Ш-СД2-З', 'Ш-СД1-З']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis[0], size_axis[1], 0, self.input_data[3])
            output = v.Many_det(size_axis, part_list, 1)
            print(output)

        elif self.input_data[1] == '2УВ':

            print('***ВЕРХ***')
            size_axis1 = int(size_axis[0]) + int(self.etag)
            size_axis2 = int(size_axis[1]) + int(self.etag)
            size_axis3 = [size_axis1, size_axis2]
            part_list = ['К-СД2', 'С-СД3', 'С-СД3-З', 'Ш-СД1', 'Ш-СД2', 'Ш-СД2-З', 'Ш-СД1-З']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis3[0], size_axis3[1], 0, self.input_data[3])
            output = v.Many_det(size_axis3, part_list, 1)
            print(output)

            part_list = ['К-СД13']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis[0], size_axis[1], 0, self.input_data[3])
            output = v.Many_det(size_axis, part_list, 1)
            print(output)

            print('***НИЗ***')
            size_axis1 = int(size_axis[0]) - int(self.etag)
            size_axis2 = int(size_axis[1]) - int(self.etag)
            size_axis3 = [size_axis1, size_axis2]
            part_list = ['К-СД3', 'С-СД3', 'С-СД3-З', 'Ш-СД1', 'Ш-СД2', 'Ш-СД2-З', 'Ш-СД1-З']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis3[0], size_axis3[1], 0, self.input_data[3])
            output = v.Many_det(size_axis3, part_list, 1)
            print(output)

        elif self.input_data[1] == 'Z-Г':

            part_list = ['К-СД4', 'К-СД5', 'С-СД4', 'С-СД4-З']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis[0], size_axis[1], size_axis[2], self.input_data[3])
            output = v.Many_det(size_axis, part_list, 1)
            print(output)

            part_list2 = ['s5', 's6', 's7', 's8']
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis[0], size_axis[1], size_axis[2], self.input_data[3])
            output = v.Many_det2(size_axis, part_list2, 1)  # размер осей и список деталей
            print(output)

        elif self.input_data[1] == '2Z-Г':

            part_list = ['С-СД4', 'С-СД4-З', 'С-СД4', 'С-СД4-З']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis[0], size_axis[1], size_axis[2], self.input_data[3])
            output = v.Many_det(size_axis, part_list, 2)
            print(output)

            part_list = ['К-СД4', 'К-СД5', 'К-СД16']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis[0], size_axis[1], size_axis[2], self.input_data[3])
            output = v.Many_det(size_axis, part_list, 1)
            print(output)

            part_list2 = ['s5', 's6', 's7', 's8']
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis[0], size_axis[1], size_axis[2], self.input_data[3])
            output = v.Many_det2(size_axis, part_list2, 2)  # размер осей и список деталей
            print(output)

        elif self.input_data[1] == 'Z-В':

            part_list = ['К-СД6', 'К-СД6-З', 'С-СД5', 'С-СД6', 'Ш-СД3', 'Ш-СД4', 'Ш-СД3', 'Ш-СД4']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis[0], size_axis[1], 0, self.input_data[3])
            output = v.Many_det(size_axis, part_list, 1)
            print(output)

        elif self.input_data[1] == '2Z-В':

            print('***ВЕРХ***')
            size_axis1 = int(size_axis[0]) + int(self.etag)
            size_axis2 = int(size_axis[1]) + int(self.etag)
            size_axis3 = int(size_axis[2]) + int(self.etag)
            size_axis4 = [size_axis1, size_axis2, size_axis3]
            part_list = ['К-СД6', 'С-СД5', 'С-СД6', 'Ш-СД3', 'Ш-СД4', 'Ш-СД3', 'Ш-СД4']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis4[0], size_axis4[1], 0, self.input_data[3])
            output = v.Many_det(size_axis4, part_list, 1)
            print(output)

            part_list = ['К-СД15']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis[0], size_axis[1], 0, self.input_data[3])
            output = v.Many_det(size_axis, part_list, 1)
            print(output)

            print('***НИЗ***')
            size_axis1 = int(size_axis[0]) - int(self.etag)
            size_axis2 = int(size_axis[1]) - int(self.etag)
            size_axis3 = int(size_axis[2]) - int(self.etag)
            size_axis4 = [size_axis1, size_axis2, size_axis3]
            part_list = ['К-СД6-З', 'С-СД5', 'С-СД6', 'Ш-СД3', 'Ш-СД4', 'Ш-СД3', 'Ш-СД4']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis4[0], size_axis4[1], 0, self.input_data[3])
            output = v.Many_det(size_axis4, part_list, 1)
            print(output)

        elif self.input_data[1] == 'К-П':

            part_list = ['К-СД9', 'К-СД10', 'С-СД9', 'С-СД10']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis[0], size_axis[1], 0, self.input_data[3])
            output = v.Many_det(size_axis, part_list, 1)
            print(output)

            part_list = ['Ш-СД11', 'Ш-СД12', 'Ш-СД13', 'Ш-СД14']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis[0], size_axis[1], 0, self.input_data[3])
            output = v.Many_det3(size_axis, part_list, 1)
            print(output)

        elif self.input_data[1] == 'К-Л':

            part_list = ['К-СД7', 'К-СД8', 'С-СД7', 'С-СД8']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis[0], size_axis[1], 0, self.input_data[3])
            output = v.Many_det(size_axis, part_list, 1)
            print(output)

            part_list = ['Ш-СД7', 'Ш-СД8', 'Ш-СД9', 'Ш-СД10']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis[0], size_axis[1], 0, self.input_data[3])
            output = v.Many_det3(size_axis, part_list, 1)
            print(output)

        elif self.input_data[1] == '2К-Л':

            print('***Верх***')
            size_axis1 = int(size_axis[0]) + int(self.etag)
            size_axis2 = int(size_axis[1]) + int(self.etag)
            size_axis3 = [size_axis1, size_axis2, size_axis[2]]
            part_list = ['К-СД7', 'С-СД7', 'С-СД18']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis3[1], size_axis3[2], 0, self.input_data[3])
            output = v.Many_det(size_axis3, part_list, 1)
            print(output)

            part_list = ['Ш-СД7', 'Ш-СД8', 'Ш-СД9', 'Ш-СД10']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis[1], size_axis[2], 0, self.input_data[3])
            output = v.Many_det3(size_axis3, part_list, 1)
            print(output)

            part_list = ['К-СД12']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, 0, 0, 0, self.input_data[3])
            output = v.Many_det(size_axis, part_list, 1)
            print(output)

            print('***Верх***')
            size_axis1 = int(size_axis[0]) - int(self.etag)
            size_axis2 = int(size_axis[1]) - int(self.etag)
            size_axis3 = [size_axis1, size_axis2, size_axis[2]]
            part_list = ['К-СД8', 'С-СД7', 'С-СД8']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, 0, 0, 0, self.input_data[3])
            output = v.Many_det(size_axis3, part_list, 1)
            print(output)

            part_list = ['Ш-СД7', 'Ш-СД8', 'Ш-СД9', 'Ш-СД10']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis3[1], size_axis3[2], 0, self.input_data[3])
            output = v.Many_det3(size_axis3, part_list, 1)
            print(output)

        elif self.input_data[1] == '2К-П':

            print('***ВЕРХ***')
            size_axis1 = int(size_axis[0]) + int(self.etag)
            size_axis2 = int(size_axis[1]) + int(self.etag)
            size_axis3 = [size_axis1, size_axis2, size_axis[2]]
            part_list = ['К-СД9', 'С-СД9', 'С-СД10']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis3[0], size_axis3[1], 0, self.input_data[3])
            output = v.Many_det(size_axis3, part_list, 1)
            print(output)

            part_list = ['Ш-СД11', 'Ш-СД12', 'Ш-СД13', 'Ш-СД14']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis3[1], size_axis3[2], 0, self.input_data[3])
            output = v.Many_det3(size_axis3, part_list, 1)
            print(output)

            part_list = ['К-СД12']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis[0], size_axis[1], 0, self.input_data[3])
            output = v.Many_det(size_axis, part_list, 1)
            print(output)

            print('***НИЗ***')
            size_axis1 = int(size_axis[0]) - int(self.etag)
            size_axis2 = int(size_axis[1]) - int(self.etag)
            size_axis3 = [size_axis1, size_axis2, size_axis[2]]
            part_list = ['К-СД10', 'С-СД9', 'С-СД10']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis3[0], size_axis3[1], 0, self.input_data[3])
            output = v.Many_det(size_axis3, part_list, 1)
            print(output)

            part_list = ['Ш-СД11', 'Ш-СД12', 'Ш-СД13', 'Ш-СД14']  #
            v = Welded_part(self.input_data[0], self.ssh, self.ss, size_axis3[1], size_axis3[2], 0, self.input_data[3])
            output = v.Many_det3(size_axis3, part_list, 1)
            print(output)

        elif self.input_data[1] == 'ФБ':

            part_list = ['c', 'k', 's17', 's18']
            v = Welded_part(self.input_data[0], self.ssh, self.ss, 0, 0, 0, self.input_data[3])
            output = v.Many_det2(size_axis, part_list, 2)
            print(output)

        elif self.input_data[1] == '2ФБ':

            part_list = ['kc', 'k']
            v = Welded_part(self.input_data[0], self.ssh, self.ss, 0, 0, 0, self.input_data[3])
            output = v.Many_det2(size_axis, part_list, 1)
            print(output)

            part_list = ['c', 's17', 's18']
            v = Welded_part(self.input_data[0], self.ssh, self.ss, 0, 0, 0, self.input_data[3])
            output = v.Many_det2(size_axis, part_list, 4)
            print(output)

        else:
            return 0