# coding^utf8
import nominal


def kol_naprav():
    # кол-во стандартных выводов\ кол-во фланцевых выводов\ количество стыков
    slovar_vivodov = {'П': [2, 0, 1],
                      'УГ': [2, 0, 1],
                      'УВ': [2, 0, 1],
                      'Z-Г': [2, 0, 1],
                      'Z-В': [2, 0, 1],
                      'К-П': [2, 0, 1],
                      'К-Л': [2, 0, 1],
                      'ZГ': [2, 0, 1],
                      'ZВ': [2, 0, 1],
                      'КП': [2, 0, 1],
                      'КЛ': [2, 0, 1],
                      'ОМ': [2, 0, 1],
                      'ПФ': [1, 1, 1],
                      'ПФК': [1, 1, 1],
                      'Т-В': [3, 0, 2],
                      'Т-Г': [3, 0, 2],
                      '2П': [2, 0, 1],
                      '2УГ': [2, 0, 1],
                      '2УВ': [2, 0, 1],
                      '2Z-Г': [2, 0, 1],
                      '2Z-В': [2, 0, 1],
                      '2К-П': [2, 0, 1],
                      '2К-Л': [2, 0, 1],
                      '2ZГ': [2, 0, 1],
                      '2ZВ': [2, 0, 1],
                      '2КП': [2, 0, 1],
                      '2КЛ': [2, 0, 1],
                      '2ОМ': [2, 0, 1],
                      '2ПФ': [1, 1, 1],
                      '2ПФ100': [1, 1, 1],
                      '2ПФК': [1, 1, 1],
                      '2Т-В': [3, 0, 2],
                      '2Т-Г': [3, 0, 2],
                      '3УВ': [2, 0, 1],
                      '3П': [2, 0, 1],
                      '3УГ': [2, 0, 1]}

#расписываем выводы подетально
def vivodi(i):
    slovar_izd_standart = {'Направляющая': 2, 'Сухарь': 2, 'Винт М6х16 DIN912': 8, 'Шайба плоская 6': 8,  'Шайба гровер 6': 8}
    slovar_izd_flanec = {'Фланец': 2, 'Сухарь': 2, 'Трубка 10 30мм': 2, 'Винт М6х16 DIN912': 8, 'Шайба плоская 6': 8,
                         'Шайба гровер': 8, 'Болт М8х60': 2, 'Гайка с фланцем М8': 2, 'Шайба плоская 8': 2}
    if i == 1:
        j = slovar_izd_standart
    else:
        j = slovar_izd_flanec
    return j

# габариты для  EPDM
def gab_epdm(nom):
    raz_shirina = nominal.vvod_znach(nom)
    razmer = [25, raz_shirina.calc_nom()[0], 3]
    vivod = 'x'.join(map(str, razmer))
    #print(vivod)
    return vivod

if __name__ == '__main__':
    gab_epdm(630)