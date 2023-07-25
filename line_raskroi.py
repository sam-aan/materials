# coding:utf8
import re
import copy

def techno(array):
    '''модуль для создания маршрутной карты'''
    print('СОЗДАНИЕ МАРШРУТНОЙ КАРТЫ')
    print(array)
    spis = {'000 170': ["15", "30", "35"],
            '000 774-01': ["15", "60"],
            '000 774-02': ["15", "60"],
            'kl': ["30", "50", "55", "60"],
            'klfuv': ["50", "55", "60"],
            'kp': ["30", "50", "55", "60"],
            'kpfuv': ["50", "55", "60"],
            'ksm': ["55", "60"],
            'kcb': ["55", "60"],
            'ksb': ["55", "60"],
            'kz': ["30", "35", "40", "50", "55"],
            'om': ["55", "60"],
            'omf': ["55", "60"],
            'pf': ["55", "60"],
            'pfk': ["55", "60"],
            'pr': ["30", "50", "55", "60"],
            'pr1': ["30", "50", "55", "60"],
            'pr2': ["30", "50", "55", "60"],
            'pr3': ["30", "50", "55", "60"],
            'pr4': ["30", "50", "55", "60"],
            'pr5': ["30", "50", "55", "60"],
            'pr6': ["30", "50", "55", "60"],
            'pt': ["50", "60"],
            'sb': ["55", "60"],
            'sk': ["55", "60"],
            'Ск-Тр': ["35", "45", "55"],
            '000 125': ["55", "60"],
            '000 125-01': ["55", "60"],
            '000 125-02': ["55", "60"],
            '000 125-03': ["55", "60"],
            '000 777': ["55", "60"],
            '000 776': ["55", "60"],
            'ts': ["30", "50", "55", "60"],
            'ts1.1': ["30", "50", "55", "60"],
            'ts1.2': ["30", "50", "55", "60"],
            'ts1.3': ["30", "50", "55", "60"],
            'ts1.4': ["30", "50", "55", "60"],
            'ts2.1': ["30", "50", "55", "60"],
            'ts2.2': ["30", "50", "55", "60"],
            'ts2.3': ["30", "50", "55", "60"],
            'ts2.4': ["30", "50", "55", "60"],
            'ts3.1': ["30", "50", "55", "60"],
            'ts3.2': ["30", "50", "55", "60"],
            'ts3.3': ["30", "50", "55", "60"],
            'ts3.4': ["30", "50", "55", "60"],
            'ts4.1': ["30", "50", "55", "60"],
            'ts4.2': ["30", "50", "55", "60"],
            'ts4.3': ["30", "50", "55", "60"],
            'ts4.4': ["30", "50", "55", "60"],
            'ts5.1': ["30", "50", "55", "60"],
            'ts5.2': ["30", "50", "55", "60"],
            'ts5.3': ["30", "50", "55", "60"],
            'ts5.4': ["30", "50", "55", "60"],
            'ts6.1': ["30", "50", "55", "60"],
            'ts6.2': ["30", "50", "55", "60"],
            'ts6.3': ["30", "50", "55", "60"],
            'ts6.4': ["30", "50", "55", "60"],
            'ts7.1': ["30", "50", "55", "60"],
            'ts7.2': ["30", "50", "55", "60"],
            'ts7.3': ["30", "50", "55", "60"],
            'ts7.4': ["30", "50", "55", "60"],
            'ts8.1': ["30", "50", "55", "60"],
            'ts8.2': ["30", "50", "55", "60"],
            'ts8.3': ["30", "50", "55", "60"],
            'ts8.4': ["30", "50", "55", "60"],
            'tv': ["30", "50", "55", "60"],
            'ug': ["30", "50", "55", "60"],
            'ugf': ["30", "40", "50", "55", "60"],
            'uv': ["30", "50", "55", "60"],
            'uvf': ["30", "50", "55", "60"],
            'zg': ["30", "50", "55", "60"],
            'zgf': ["30", "50", "55", "60"],
            'zv': ["30", "50", "55", "60"],
            'zvf': ["30", "50", "55", "60"],
            'В': ["05", "15", "20"],
            'Д': ["55"],
            'ЗВ': ["30", "50", "55", "60"],
            'ЗВФ': ["30", "50", "55", "60"],
            'ЗГ': ["30", "50", "55", "60"],
            'ЗГФ': ["30", "50", "55", "60"],
            'З-ТС': ["15", "40", "50", "55"],
            'ИК': ["50", "55"],
            'ИС': ["50", "55"],
            'К': ["05", "15", "30", "40", "50", "55"],
            'К1': ["05", "15", "30"],
            'К11': ["05", "15", "30"],
            'К12': ["05", "15", "30"],
            'К13': ["05", "15", "30"],
            'К14': ["05", "15", "30"],
            'К15': ["05", "15", "30"],
            'К16': ["05", "15", "30"],
            'К18': ["05", "15", "30", "35", "55"],
            'К18-01': ["05", "15", "30", "35"],
            'К18-02': ["05", "15", "30", "35"],
            'К19': ["05", "15"],
            'К2': ["05", "15", "30"],
            'К20': ["05", "15"],
            'К21': ["05", "15"],
            'К3': ["05", "15", "30"],
            'К4': ["05", "15", "30"],
            'К5': ["05", "15", "30"],
            'К7': ["05", "15", "30"],
            'К8': ["05", "15", "30"],
            'К9': ["05", "15", "30"],
            'КВ': ["05", "15", "30", "40", "50", "55"],
            'КВ18': ["05", "15", "30", "35", "55"],
            'КВ18-01': ["05", "15", "30", "35", "55"],
            'КВ18-02': ["05", "15", "30", "35", "55"],
            'КВ20': ["05", "15"],
            'КВ21': ["05", "15"],
            'КВ-кр': ["05", "15", "55"],
            'КЗ': ["30", "35", "40", "50", "55"],
            'К-кр': ["05", "15", "55"],
            'КЛ': ["30", "50", "55", "60"],
            'КП': ["30", "50", "55", "60"],
            'КС': ["05", "15", "30"],
            'КС1': ["05", "15", "30"],
            'КС2': ["05", "15", "30"],
            'КС3': ["05", "15", "30"],
            'КС4': ["05", "15", "30"],
            'КС5': ["05", "15", "30"],
            'КС6': ["05", "15", "30"],
            'КС8': ["05", "15", "30"],
            'КС9': ["05", "15", "30"],
            'КСБ': ["55"],
            'К-СД1': ["30", "35", "40", "50", "55"],
            'К-СД10': ["30", "35", "40", "50", "55"],
            'К-СД11': ["30", "35", "40", "50", "55"],
            'КС-СД11': ["30", "35", "40", "50", "55"],
            'К-СД12': ["30", "35", "40", "50", "55"],
            'К-СД13': ["30", "35", "40", "50", "55"],
            'К-СД13ф': ["30", "35", "40", "50", "55"],
            'К-СД14': ["30", "35", "40", "50", "55"],
            'К-СД15': ["30", "35", "40", "50", "55"],
            'К-СД16': ["30", "35", "40", "50", "55"],
            'К-СД1-З': ["30", "35", "40", "50", "55"],
            'К-СД2': ["30", "35", "40", "50", "55"],
            'К-СД2ф': ["30", "35", "40", "50", "55"],
            'К-СД3': ["30", "35", "40", "50", "55"],
            'К-СД3ф': ["30", "35", "40", "50", "55"],
            'К-СД4': ["30", "35", "40", "50", "55"],
            'К-СД4Ф': ["30", "35", "40", "50", "55"],
            'К-СД5': ["30", "35", "40", "50", "55"],
            'К-СД5Ф': ["30", "35", "40", "50", "55"],
            'К-СД6': ["30", "35", "40", "50", "55"],
            'К-СД6-З': ["30", "35", "40", "50", "55"],
            'К-СД7': ["30", "35", "40", "50", "55"],
            'К-СД8': ["30", "35", "40", "50", "55"],
            'К-СД9': ["30", "35", "40", "50", "55"],
            'КС-кр': ["05", "15", "40", "55"],
            'ЛБ': ["15", "30"],
            'ЛВ': ["15", "30"],
            'ЛТ': ["15", "30"],
            'МЦ': ["15"],
            'Н': ["05", "15", "35"],
            'ОМ': ["55", "60"],
            'ОМ1.1': ["30", "50", "55", "60"],
            'ОМ1.2': ["30", "50", "55", "60"],
            'ОМ1.3': ["30", "50", "55", "60"],
            'ОМ1.4': ["30", "50", "55", "60"],
            'ОМ1.5': ["30", "50", "55", "60"],
            'ОМ1.6': ["30", "50", "55", "60"],
            'ОМ2.1': ["30", "50", "55", "60"],
            'ОМ2.2': ["30", "50", "55", "60"],
            'ОМ2.3': ["30", "50", "55", "60"],
            'ОМ2.4': ["30", "50", "55", "60"],
            'ОМ2.5': ["30", "50", "55", "60"],
            'ОМ2.6': ["30", "50", "55", "60"],
            'ОМФ': ["55", "60"],
            'П': ["50", "60"],
            'ПФ': ["55", "60"],
            'ПФК': ["55", "60"],
            'С': ["05", "30"],
            'С-01': ["05", "15", "30"],
            'С1': ["05", "30"],
            'С1-01': ["05", "15", "30"],
            'С11': ["05", "30"],
            'С11-01': ["05", "15", "30"],
            'С12': ["05", "30"],
            'С12-01': ["05", "15", "30"],
            'С13': ["05", "30"],
            'С13-01': ["05", "15", "30"],
            'С14': ["05", "30"],
            'С14-01': ["05", "15", "30"],
            'С15': ["05", "30"],
            'С15-01': ["05", "15", "30"],
            'С16': ["05", "30"],
            'С16-01': ["05", "15", "30"],
            'С2': ["05", "30"],
            'С2-01': ["05", "15", "30"],
            'С3': ["05", "30"],
            'С3-01': ["05", "15", "30"],
            'С4': ["05", "30"],
            'С4-01': ["05", "15", "30"],
            'С5': ["05", "30"],
            'С5-01': ["05", "15", "30"],
            'С7': ["05", "30"],
            'С7-01': ["05", "15", "30"],
            'С8': ["05", "30"],
            'С8-01': ["05", "15", "30"],
            'С9': ["05", "30"],
            'С9-01': ["05", "15", "30"],
            'СБ': ["55", "60"],
            'Ск': ["05", "40", "50", "55"],
            'Ск-01': ["05", "15", "40", "50", "55"],
            'С-кр': ["05", "55"],
            'С-кр-01': ["05", "15", "55"],
            'СС': ["05", "15", "35"],
            'ЛВ/Н': ["45", "40", "50"],
            'КЛБ': ["45", "40", "50"],
            'ЛВБ': ["45", "40", "50"],
            'ЛБМ': ["45", "40", "50"],
            'km': ["45", "30", "35", "55"],
            'kb': ["45", "30", "35", "55"],
            '000 124': ["45", "30", "35", "55"],
            'С-СД1': ["30", "35", "40", "50", "55"],
            'С-СД10': ["30", "35", "40", "50", "55"],
            'С-СД11': ["30", "35", "40", "50", "55"],
            'С-СД12': ["30", "35", "40", "50", "55"],
            'С-СД13': ["30", "35", "40", "50", "55"],
            'С-СД14': ["30", "35", "40", "50", "55"],
            'С-СД15': ["30", "35", "40", "50", "55"],
            'С-СД16': ["30", "35", "40", "50", "55"],
            'С-СД2': ["30", "35", "40", "50", "55"],
            'С-СД3': ["30", "35", "40", "50", "55"],
            'С-СД3-3ф': ["30", "35", "40", "50", "55"],
            'С-СД3-З': ["30", "35", "40", "50", "55"],
            'С-СД3ф': ["30", "35", "40", "50", "55"],
            'С-СД4': ["30", "35", "40", "50", "55"],
            'С-СД4-З': ["30", "35", "40", "50", "55"],
            'С-СД4-ЗФ': ["30", "35", "40", "50", "55"],
            'С-СД4Ф': ["30", "35", "40", "50", "55"],
            'С-СД5': ["30", "35", "40", "50", "55"],
            'С-СД6': ["30", "35", "40", "50", "55"],
            'С-СД7': ["30", "35", "40", "50", "55"],
            'С-СД8': ["30", "35", "40", "50", "55"],
            'С-СД9': ["30", "35", "40", "50", "55"],
            'СТП 026 В': ["05", "25", "30"],
            'СТП 09 В': ["05", "25", "30"],
            'СУ': ["05", "15", "20"],
            'ТВ': ["30", "50", "55", "60"],
            'ТП': ["05", "10", "25", "35", "55"],
            'ТС': ["30", "50", "55", "60"],
            'ТС1.1': ["30", "50", "55", "60"],
            'ТС1.2': ["30", "50", "55", "60"],
            'ТС1.3': ["30", "50", "55", "60"],
            'ТС1.4': ["30", "50", "55", "60"],
            'ТС2.1': ["30", "50", "55", "60"],
            'ТС2.2': ["30", "50", "55", "60"],
            'ТС2.3': ["30", "50", "55", "60"],
            'ТС2.4': ["30", "50", "55", "60"],
            'ТС3.1': ["30", "50", "55", "60"],
            'ТС3.2': ["30", "50", "55", "60"],
            'ТС3.3': ["30", "50", "55", "60"],
            'ТС3.4': ["30", "50", "55", "60"],
            'ТС4.1': ["30", "50", "55", "60"],
            'ТС4.2': ["30", "50", "55", "60"],
            'ТС4.3': ["30", "50", "55", "60"],
            'ТС4.4': ["30", "50", "55", "60"],
            'ТС5.1': ["30", "50", "55", "60"],
            'ТС5.2': ["30", "50", "55", "60"],
            'ТС5.3': ["30", "50", "55", "60"],
            'ТС5.4': ["30", "50", "55", "60"],
            'ТС6.1': ["30", "50", "55", "60"],
            'ТС6.2': ["30", "50", "55", "60"],
            'ТС6.3': ["30", "50", "55", "60"],
            'ТС6.4': ["30", "50", "55", "60"],
            'ТС7.1': ["30", "50", "55", "60"],
            'ТС7.2': ["30", "50", "55", "60"],
            'ТС7.3': ["30", "50", "55", "60"],
            'ТС7.4': ["30", "50", "55", "60"],
            'ТС8.1': ["30", "50", "55", "60"],
            'ТС8.2': ["30", "50", "55", "60"],
            'ТС8.3': ["30", "50", "55", "60"],
            'ТС8.4': ["30", "50", "55", "60"],
            'ТЦ': ["15"],
            'У': ["05", "30"],
            'У2': ["05", "30"],
            'У1': ["05", "30"],
            'У2-З': ["05", "30"],
            'УВ': ["30", "50", "55", "60"],
            'УВФ': ["30", "50", "55", "60"],
            'УГ': ["30", "50", "55", "60"],
            'УГФ': ["30", "50", "55", "60"],
            '000 120': ["05", "10", "25", "40", "50", "55"],
            '000 119': ["05", "10", "25", "40", "50", "55"],
            '000 128': ["05", "10", "15", "25"],
            '000 108': ["45"],
            'Ш': ["05", "25", "30"],
            'Ш-01': ["05", "25", "40", "50", "55"],
            'Ш1': ["05", "10", "25", "40", "50", "55"],
            'Ш10': ["05", "10", "25", "30"],
            'Ш1-01': ["05", "10", "25", "30"],
            'Ш11': ["05", "10", "25", "30"],
            'Ш12': ["05", "10", "25", "30"],
            'Ш13': ["05", "10", "25", "40", "50", "55"],
            'Ш14': ["05", "10", "25", "40", "50", "55"],
            'Ш15': ["05", "10", "25", "40", "50", "55"],
            'Ш16': ["05", "10", "25", "40", "50", "55"],
            'Ш17': ["05", "10", "15", "25", "40", "50", "55"],
            'Ш18': ["05", "10", "15", "25", "40", "50", "55"],
            'Ш19': ["05", "10", "15", "25", "40", "50", "55"],
            'Ш2': ["05", "10", "25", "40", "50", "55"],
            'Ш20': ["05", "10", "15", "25", "40", "50", "55"],
            'Ш2-01': ["05", "10", "25", "30"],
            'Ш21': ["05", "10", "15", "25", "40", "50", "55"],
            'Ш22': ["05", "10", "15", "25", "40", "50", "55"],
            'Ш23': ["05", "10", "25", "40", "50", "55"],
            'Ш24': ["05", "10", "25", "40", "50", "55"],
            'Ш25': ["05", "10", "25", "40", "50", "55"],
            'Ш26': ["05", "10", "25", "40", "50", "55"],
            'Ш27': ["05", "10", "25", "40", "50", "55"],
            'Ш28': ["05", "10", "25", "40", "50", "55"],
            'Ш29': ["05", "10", "25", "40", "50", "55"],
            'Ш3': ["05", "10", "25", "30"],
            'Ш30': ["05", "10", "25", "40", "50", "55"],
            'Ш33': ["05", "15", "25", "30"],
            'Ш36': ["05", "10", "15", "25", "30", "40", "50", "55"],
            'Ш37': ["05", "10", "15", "25", "30", "40", "50", "55"],
            'Ш38': ["05", "10", "25", "40", "50", "55"],
            'Ш46': ["05", "10", "25", "40", "50", "55"],
            'Ш4': ["05", "10", "25", "30"],
            'Ш41': ["10", "40", "50", "55"],
            'Ш5': ["05", "10", "25", "40", "50", "55"],
            'Ш6': ["05", "10", "25", "40", "50", "55"],
            'Ш7': ["05", "10", "25", "40", "50", "55"],
            'Ш8': ["05", "10", "25", "40", "50", "55"],
            'Ш9': ["05", "10", "25", "30"],
            'k_pe': ["30", "35", "40", "50", "55"],
            'Ш-СД1': ["30", "35", "40", "50", "55"],
            'Ш-СД1-З (Зеркальная)': ["30", "35", "40", "50", "55"],
            'Ш-СД10': ["30", "35", "40", "50", "55"],
            'Ш-СД11': ["30", "35", "40", "50", "55"],
            'Ш-СД12': ["30", "35", "40", "50", "55"],
            'Ш-СД13': ["30", "35", "40", "50", "55"],
            'Ш-СД14': ["30", "35", "40", "50", "55"],
            'Ш-СД15': ["30", "35", "40", "50", "55"],
            'Ш-СД15-З': ["30", "35", "40", "50", "55"],
            'Ш-СД15-З (Зеркальная)': ["30", "35", "40", "50", "55"],
            'Ш-СД16': ["30", "35", "40", "50", "55"],
            'Ш-СД16-З': ["30", "35", "40", "50", "55"],
            'Ш-СД16-З (Зеркальная)': ["30", "35", "40", "50", "55"],
            'Ш-СД17': ["30", "35", "40", "50", "55"],
            'Ш-СД17-З': ["30", "35", "40", "50", "55"],
            'Ш-СД17-З (Зеркальная)': ["30", "35", "40", "50", "55"],
            'Ш-СД18': ["30", "35", "40", "50", "55"],
            'Ш-СД18-З': ["30", "35", "40", "50", "55"],
            'Ш-СД18-З (Зеркальная)': ["30", "35", "40", "50", "55"],
            'Ш-СД19': ["30", "35", "40", "50", "55"],
            'Ш-СД19-З': ["30", "35", "40", "50", "55"],
            'Ш-СД19-З (Зеркальная)': ["30", "35", "40", "50", "55"],
            'Ш-СД1-З': ["30", "35", "40", "50", "55"],
            'Ш-СД2': ["30", "35", "40", "50", "55"],
            'Ш-СД2-З (Зеркальная)': ["30", "35", "40", "50", "55"],
            'Ш-СД20': ["30", "35", "40", "50", "55"],
            'Ш-СД20-З': ["30", "35", "40", "50", "55"],
            'Ш-СД21': ["30", "35", "40", "50", "55"],
            'Ш-СД21-З': ["30", "35", "40", "50", "55"],
            'Ш-СД21-З (Зеркальная)': ["30", "35", "40", "50", "55"],
            'Ш-СД22': ["30", "35", "40", "50", "55"],
            'Ш-СД22-З': ["30", "35", "40", "50", "55"],
            'Ш-СД22-З (Зеркальная)': ["30", "35", "40", "50", "55"],
            'Ш-СД25': ["30", "35", "40", "50", "55"],
            'Ш-СД26': ["30", "35", "40", "50", "55"],
            'Ш-СД27': ["30", "35", "40", "50", "55"],
            'Ш-СД28': ["30", "35", "40", "50", "55"],
            'Ш-СД29': ["30", "35", "40", "50", "55"],
            'Ш-СД2-З': ["30", "35", "40", "50", "55"],
            'Ш-СД3': ["30", "35", "40", "50", "55"],
            'Ш-СД3-З (Зеркальная)': ["30", "35", "40", "50", "55"],
            'Ш-СД30': ["30", "35", "40", "50", "55"],
            'Ш-СД31': ["30", "35", "40", "50", "55"],
            'Ш-СД32': ["30", "35", "40", "50", "55"],
            'Ш-СД33': ["10", "30", "35", "40", "50", "55"],
            'Ш-СД33-01': ["10", "30", "35", "40", "50", "55"],
            'Ш-СД33-02': ["10", "30", "35", "40", "50", "55"],
            'Ш-СД33-03': ["10", "30", "35", "40", "50", "55"],
            'Ш-СД33-04': ["10", "30", "35", "40", "50", "55"],
            'Ш-СД33-05': ["10", "30", "35", "40", "50", "55"],
            'Ш-СД34': ["10", "30", "35", "40", "50", "55"],
            'Ш-СД34-02': ["10", "30", "35", "40", "50", "55"],
            'Ш-СД34-03': ["10", "30", "35", "40", "50", "55"],
            'Ш-СД34-04': ["10", "30", "35", "40", "50", "55"],
            'Ш-СД34-05': ["10", "30", "35", "40", "50", "55"],
            'Ш-СД35': ["30", "35", "40", "50", "55"],
            'Ш-СД35-З': ["30", "35", "40", "50", "55"],
            'Ш-СД36': ["30", "35", "40", "50", "55"],
            'Ш-СД36-З': ["30", "35", "40", "50", "55"],
            'Ш-СД37': ["30", "35", "40", "50", "55"],
            'Ш-СД38': ["30", "35", "40", "50", "55"],
            'Ш-СД39': ["30", "35", "40", "50", "55"],
            'Ш-СД3-З': ["30", "35", "40", "50", "55"],
            'Ш-СД4': ["30", "35", "40", "50", "55"],
            'Ш-СД4-З (Зеркальная)': ["30", "35", "40", "50", "55"],
            'Ш-СД40': ["30", "35", "40", "50", "55"],
            'Ш-СД41': ["30", "35", "40", "50", "55"],
            'Ш-СД42': ["30", "35", "40", "50", "55"],
            'Ш-СД4-З': ["30", "35", "40", "50", "55"],
            'Ш-СД7': ["30", "35", "40", "50", "55"],
            'Ш-СД8': ["30", "35", "40", "50", "55"],
            'Ш-СД9': ["30", "35", "40", "50", "55"]
            }
    spisok_nazvanii = {'пила': '05', 'гибка': '10', 'фрезер': '15', 'сверловка': '20', 'напыление': '25', 'сварка': '30',
                       'зачистка': '35', 'шлифовка': '40', 'лаз.резка': '45', 'покраска': '50', 'предсборка': '55',
                       'сборка_заливка': '60'}

    for i in array:     # берем строку
        oper = spis[array[i]['Обозначение']]        # список с операциями [1, 0, 0...]

        for j in spisok_nazvanii:

            if spisok_nazvanii[j] in oper:
                array[i][j] = spisok_nazvanii[j]
            else:
                array[i][j] = '0'

    return array


def material(name_file):
    spis = ['Токопроводящая пластина', 'Стенка стыка', 'Сухарь', 'Направляющая', 'Крышка', 'Крышка с выступом',
            'Уголок_25х25х3', 'Стенка', 'Крышка средняя', 'Шина']
    f = open('techno.txt', 'w')
    with open(name_file) as file:
        array = [row.strip() for row in
                 file]  # переписываем все строки в список ['первая строка', 'вторая строка', ...]
        array2 = []
        # print(array)
        kol_str = len(array)  # записываем клличесвто элементов в списке, оно же
        # print('всего строк ', kol_str)
    n_poz = 0
    for x in array:
        q = re.findall(r'[^;\s]+', x)  # список строки КОТОРУЮ НУЖНО СРАВНИТЬ
        # print('количество элементов в списке атрибутов строки ', len(q))
        w9 = q[-1]

        # начинаем проверять на совпадение
        # print('\nстрока которую сравниваем ', x)
        y = array.index(x) + 1  # нам нужна следующая строка
        sov = 0  # это счетчик совпадений
        while y <= kol_str - 1:  # начинаем сравнивать со следующей строкой
            line = array[y]  # строка с которой сравниваем это следующая строка
            w = re.findall(r'[^;\s]+', line)  # список строки С КОТОРОЙ СРАВНИВАЕМ
            if q[1] == w[1] and q[2] in spis and q[2] == w[2]:  # если значения строк совпадают, то
                w9 = str(int(w9) + int(w[9]))  # складываем количество
                sov = sov + 1  # сообщаем что были совпадения
                # print('совпадение в', y, 'строке +', str(w[9]))
                # print('строка которую удаляем', array[y])
                del array[y]
                kol_str = len(array)
                # print('итого строк осталось: ', kol_str)
                # print(y)
                # print(line)
            else:
                # print('нет совпадений в ', y, ' строке')
                y = y + 1

        # проверяем есть ли совпадения
        if sov == 0:
            array2.append(x)
        else:
            in_spis = [q[0], q[1], q[2], w9]
            in_dat2 = (' '.join(in_spis))
            # print('Записываем в список ', in_dat2)
            array2.append(in_dat2)

    # записываем результат в файл
    # print(array2)
    for i in array2:
        # print(i)
        f = open('techno.txt', 'a')
        f.write(i + '\n')
        f.close()

class komlektuyushie:
    '''модуль для создания ведомости комплектующих'''
    def __init__(self, data, length_OS, spis_kompl):
        self.data = data
        self.length_OS = length_OS
        self.spis_kompl = spis_kompl

    def print_data(self, data):

        for i in data:
            self.spis_kompl['st_izd'].append([str(i[0]) + ';' + str(i[1]) + ';' + str(i[2]) + ';' + str(i[3] * self.kol)])

    def standart_izdel(self):
        kol_bolt_M6x30 = {'630': 10, '800': 10, '1000': 10, '1250': 10, '1600': 10, '2000': 10, '2500': 12, '2600': 14,
                          '3200': 14, '3201': 14, '4000': 14, '5000': 14, '6400': 14}

        if self.data['Обозначение'] in ['пф', 'угф', 'увф', 'звф', 'згф', 'тс', 'pf', 'pfk', 'ugf', 'uvf', 'zvf', 'zgf']:
            self.kol = 1
            spis_st_izd = ['стандартный вывод', 'заклепка', 'флнцевый вывод']
            self.length_OS = self.length_OS - self.data['расстояние от оси до корпуса']
        elif self.data['Обозначение'] in ['п', 'уг', 'ув', 'зв', 'зг', 'кп', 'кл', 'ом', 'омф', 'pr', 'ug', 'uv', 'zv',
                                          'zg', 'kp', 'kl', 'pr', 'prf']:
            self.kol = 2
            spis_st_izd = ['стандартный вывод', 'заклепка']
            self.length_OS = self.length_OS - self.data['расстояние от оси до корпуса'] * 2
        elif self.data['Обозначение'] in ['тв', 'тг', 'tv', 'tg']:
            self.kol = 3
            spis_st_izd = ['стандартный вывод', 'заклепка']
            self.length_OS = self.length_OS - self.data['расстояние от оси до корпуса'] * 3
        else:
            return False

        if self.length_OS <= 1000:
            kol_zakl = int(self.length_OS / 100) * 4
        elif self.length_OS > 1000 and self.length_OS < 1500:
            kol_zakl = int(self.length_OS / 150) * 4
        else:
            kol_zakl = int(self.length_OS / 200) * 4

        for i in spis_st_izd:
            if i == 'стандартный вывод':
                s = [['стд. изд', 'Винт самонарезной М6х12 DIN7500C полуцилиндр гол. оцинк. TORX',
                      'Пи-Ст-В.сам.пцг.torx.М6х12', 12 * self.kol],
                     ['стд. изд', 'Винт самонарезной М6х12 DIN7500М потай гол. оцинк. TORX',
                      'Пи-Ст-В.сам.пг.torx.М6х12', 4 * self.kol]]
            elif i == 'флнцевый вывод':
                s = [['стд. изд', 'Винт самонарезной М6х12 DIN7500C полуцилиндр гол. оцинк. TORX',
                      'Пи-Ст-В.сам.пцг.torx.М6х12', 8 * self.kol],
                     ['стд. изд', 'Винт самонарезной М6х12 DIN7500М потай гол. оцинк. TORX',
                      'Пи-Ст-В.сам.пг.torx.М6х12', 4 * self.kol],  # крепление фланца к шкафу и РЕ
                     ['стд. изд', 'Болт шестигранный М8х30 8.8 DIN933', 'Пи-Ст-Б.шг.М8х30',
                      kol_bolt_M6x30[str(self.data['In'])] * self.kol],  # крепление шин ушами
                     ['стд. изд', 'Болт шестигранный М8х65 8.8 DIN 933', 'Пи-Ст-Б.шг.М8х65', 2 * self.kol]]
            elif i == 'заклепка':
                s = [['стд. изд', 'Заклепка вытяжная AFT 4,8х12 мм Алюм/Сталь станд.бортик (0,5/5,0zac) ZAC',
                      'Пи-Ст-Зк.выт.4.8х12', kol_zakl]]
            else:
                s = [['', '', '', 0]]
            self.print_data(s)

def linear_cutting(IN_name_file, OUT_name_file):
    '''Очередная сортировка хз зачем она нужна'''
    print('ЛИНЕЙНЫЙ РАСКРОЙ')
    open(OUT_name_file, 'w').close()
    with open(IN_name_file) as file:
        array = [row.strip() for row in file]   # переписываем все строки в список ['первая строка', 'вторая строка', ...]
        array2 = []
        kol_str = len(array)    #   записываем клличесвто элементов в списке, оно же
    for x in array:
        q = re.findall(r'[^;]+', x)  # список строки КОТОРУЮ НУЖНО СРАВНИТЬ
        #print('список который сравниваем', q)
        qN = q[-1]  # присваиваем значение количества строки которую нужно сравнить
        del q[-1]   # удаляем значение количества строки которую нужно сравнить
        # начинаем проверять на совпадение
        y = array.index(x) + 1  # нам нужна следующая строка
        sov = 0                 # это счетчик совпадений
        while y <= kol_str-1:   #начинаем сравнивать со следующей строкой
            i = 0
            s = True
            line = array[y]     #строка с которой сравниваем это следующая строка
            w = re.findall(r'[^;]+', line)  # список строки С КОТОРОЙ СРАВНИВАЕМ
            #print('список с которым сравниваем', w)
            wN = w[-1]
            del w[-1]
            if q == w:
                print(q[i], w[i])
                i += 1
                s = True
            else:
                s = False
                #print('элемент не похож')
            if s == True:
                qN = str(float(wN) + float(qN))  # складываем количество
                sov = sov + 1  # сообщаем что были совпадения
                del array[y]
                kol_str = len(array)
            else:
                y = y + 1
        # проверяем есть ли совпадения
        if sov == 0:
            array2.append(x)
        else:
            in_spis = q
            in_spis.append(qN)
            in_dat2 = (';' .join(in_spis))
            array2.append(in_dat2)

#записываем результат в файл
    for i in array2:
        f = open(OUT_name_file, 'a')
        f.write(i + '\n')
        f.close()

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    print(techno({1: {'Серия': 'E3', 'ip': '55', 'Материал': 'Al', 'In': 2000, 'Кол. пров.': 4, 'Наименование': 'Прямая секция', 'Обозначение': 'pt', 'Разм.L': '3000', 'Разм.L1': '-', 'Разм.A': '-', 'Разм.B': '-', 'Разм.C': '-', 'количество': 1, 'тип': 3.0, 'стандарт': 'стандарт', 'категория': 'спецификация', 'пила': '50', 'гибка': '60'}}))