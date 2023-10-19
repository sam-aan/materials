# coding^utf8
import re
class calc():
    def __init__(self, input_data, Proizv):
        print(input_data)
        self.a = {'Серия': input_data[0],
                  'ip': input_data[1],
                  'Материал': input_data[2],
                  'Кол. пров.': int(input_data[3]),
                  'In': input_data[4],
                  'Наименование': input_data[5],
                  'Обозначение': str(input_data[6]).lower(),
                  'тип': input_data[7],
                  'размер': input_data[8],
                  'Производство': str(Proizv),
                  'количество': int(input_data[9]),
                  'стандарт': 'стандарт'}

    def isFloat(self, value):
        """Проверяем, является ли значение числом"""
        try:
            float(value)
            return True
        except ValueError:
            return False

    def calc_nom(self):        # размер фланца

        if self.a['Серия'] in ['Е3', 'E3']:
            self.a['толщина стенки'] = 25
            self.a['толщина изоляции'] = 0.5
            self.a['ширина крышки'] = 125
            self.a['толщина крышки'] = 33
            self.a['толщина крышки средней'] = 40
            self.a['расстояние от оси до шины'] = 20.5
            self.a['расстояние от оси до корпуса'] = 118.5
        elif self.a['Серия'] in ['CR1', 'CR', 'CRM']:
            self.a['толщина стенки'] = 25
            self.a['ширина крышки'] = 125
            self.a['толщина крышки'] = 33
            self.a['толщина крышки средней'] = 40
            self.a['расстояние от оси до шины'] = 17.5
            self.a['расстояние от оси до корпуса'] = 127.5
        elif self.a['Серия'] in ['CR2']:    # CR1 в корпусе
            self.a['толщина стенки'] = 25
            self.a['ширина крышки'] = 125
            self.a['толщина крышки'] = 33
            self.a['толщина крышки средней'] = 40
            self.a['расстояние от оси до шины'] = 17.5
            self.a['расстояние от оси до корпуса'] = 127.5


        spisok_oboznachenii = {"pt": "Прямая секция",
                               "pf": "Прямая секция с фланцем",
                               "pfk": "Прямая секция с закрытым фланцем",
                               "prf": "Прямая распределительная секция с фикс. Выводом",
                               "pr": "Прямая распределительная секция с розеткой",
                               "ug": "Угловая горизонтальная секция",
                               "ugf": "Угловая горизонтальная секция c фланцем",
                               "uv": "Угловая вертикальная секция",
                               "uvf": "Угловая вертикальная секция с фланцем",
                               "kp": "Правая комбинированная секция",
                               "kpfug": "Правая комбинированная секция с фланцем уг",
                               "kpfuv": "Правая комбинированная секция с фланцем ув",
                               "kl": "Левая комбинированная секция",
                               "klfug": "Левая комбинированная секция с фланцем уг",
                               "klfuv": "Левая комбинированная секция с фланцем ув",
                               "zvf": "z-образная вертикальная секция с фланцем",
                               "zv": "z-образная вертикальная секция",
                               "zgf": "z-образная горизонтальная с фланцем",
                               "zg": "z-образная горизонтальная",
                               "tv": "Тройник вертикальный",
                               "tvf": "Тройник вертикальный с фланцем",
                               "tg": "Тройник горизонтальный",
                               "tgf": "Тройник горизонтальный с флацем",
                               "sk": "Секция компенсации",
                               "spf": "Секция перевода фаз",
                               "pn": "Секция перевода нейтрали",
                               "om": "Блок отбора мощности",
                               "omf": "Блок отбора мощности фикированный",
                               "tsv": "Трансформаторная секция вертикальная",
                               "tsvuv": "Трансформаторная секция вертикальная с углом вертикальным",
                               "tsvug": "Трансформаторная секция вертикальная с углом горизонтальным",
                               "tsvt": "Трансформаторная секция вертикальная с тройником",
                               "tsg": "Трансформаторная секция горизонтальная",
                               "tsguv": "Трансформаторная секция горизонтальная с углом вертикальным",
                               "tsgug": "Трансформаторная секция горизонтальная с углом горизонтальным",
                               "tsgt": "Трансформаторная секция горизонтальная с тройником",
                               "kz": "Концевая заглушка",
                               "sb": "Стыковочный блок",
                               "op": "Огнепожарная проходка",
                               "ks": "Крепежная скоба",
                               "pp": "Пружинный подвес",
                               "gp": "Жесткий подвес",
                               "ad": "Адаптер",
                               "ksb": "Крышка стыка",
                               "sux": "Сухарь",
                               "n": "Направляющая",
                               "fl": "Фланец",
                               "ops": "Опалубка для стыка",
                               "п": "Прямая секция",
                               "пф": "Прямая секция с фланцем",
                               "пфк": "Прямая секция с закрытым фланцем",
                               "омф": "Прямая распределительная секция с фикс. Выводом",
                               "ом": "Прямая распределительная секция с розеткой",
                               "уг": "Угловая горизонтальная секция",
                               "угф": "Угловая горизонтальная секция c фланцем",
                               "ув": "Угловая вертикальная секция",
                               "увф": "Угловая вертикальная секция с фланцем",
                               "кп": "Правая комбинированная секция",
                               "кпфуг": "Правая комбинированная секция с фланцем уг",
                               "кпфув": "Правая комбинированная секция с фланцем ув",
                               "кл": "Левая комбинированная секция",
                               "клфуг": "Левая комбинированная секция с фланцем уг",
                               "клфув": "Левая комбинированная секция с фланцем ув",
                               "звф": "z-образная вертикальная секция с фланцем",
                               "зв": "z-образная вертикальная секция",
                               "згф": "z-образная горизонтальная с фланцем",
                               "зг": "z-образная горизонтальная",
                               "тв": "Тройник вертикальный",
                               "твф": "Тройник вертикальный с фланцем",
                               "тг": "Тройник горизонтальный",
                               "тгф": "Тройник горизонтальный с флацем",
                               "ск": "Секция компенсации",
                               "спф": "Секция перевода фаз",
                               "спн": "Секция перевода нейтрали",
                               "бом": "Блок отбора мощности",
                               "бомф": "Блок отбора мощности фикированный",
                               "тсв": "Трансформаторная секция вертикальная",
                               "тсвув": "Трансформаторная секция вертикальная с углом вертикальным",
                               "тсвуг": "Трансформаторная секция вертикальная с углом горизонтальным",
                               "тсвт": "Трансформаторная секция вертикальная с тройником",
                               "тсг": "Трансформаторная секция горизонтальная",
                               "тсгув": "Трансформаторная секция горизонтальная с углом вертикальным",
                               "тсгуг": "Трансформаторная секция горизонтальная с углом горизонтальным",
                               "тсгт": "Трансформаторная секция горизонтальная с тройником",
                               "кз": "Концевая заглушка",
                               "сб": "Стыковочный блок",
                               "оп": "Огнепожарная проходка",
                               "пп": "Пружинный подвес",
                               "жпп": "Жесткий подвес",
                               "ад": "Адаптер",
                               "кс": "Крепежная скоба",
                               "ксб": "Крышка стыка"
                               }

        if self.isFloat(self.a['In']):
            self.a['In'] = int(self.a['In'])
        else:
            self.a['In'] = 0

        if self.a['тип'] == 'None':
            self.a['тип'] = ''

        if self.a['размер'] == 'None':
            self.a['размер'] = ''


        if self.a['Обозначение'] in spisok_oboznachenii:
            print(self.a['Обозначение'])

            if self.a['Наименование'] == spisok_oboznachenii[self.a['Обозначение']]:

                if self.a['Наименование'] in ["Крышка стыка", "Крепежная скоба"]:
                    self.a['In'] = 630

                print('все верно!')

            else:
                print('ошибка в Наименовании. Исправили на ', spisok_oboznachenii[self.a['Обозначение']])
                self.a['Наименование'] = spisok_oboznachenii[self.a['Обозначение']]

        else:
            print('ошибка в обозначении')
            self.a['стандарт'] = 'нестандарт'

        if self.a['Материал'] in ['а', 'А', 'a', 'A', 'Al']:
            self.a['Материал'] = 'Al'
            self.a['K'] = 0.45
            #self.a['R'] = 10

            if self.a['Серия'] in ['Е3', 'E3']:
                rS = {250: {'ширина шины': 40, 'толщина шины': 6, 'количество этажей': 1,
                            'межфазное расстояние фланца': 100, 'количество втулок': 1},
                      400: {'ширина шины': 40, 'толщина шины': 6, 'количество этажей': 1,
                            'межфазное расстояние фланца': 100, 'количество втулок': 1},
                      630: {'ширина шины': 40, 'толщина шины': 6, 'количество этажей': 1,
                            'межфазное расстояние фланца': 100, 'количество втулок': 1},
                      800: {'ширина шины': 55, 'толщина шины': 6, 'количество этажей': 1,
                            'межфазное расстояние фланца': 100, 'количество втулок': 1},
                      1000: {'ширина шины': 80, 'толщина шины': 6, 'количество этажей': 1,
                             'межфазное расстояние фланца': 100, 'количество втулок': 1},
                      1250: {'ширина шины': 110, 'толщина шины': 6, 'количество этажей': 1,
                             'межфазное расстояние фланца': 100, 'количество втулок': 1},
                      1600: {'ширина шины': 160, 'толщина шины': 6, 'количество этажей': 1,
                             'межфазное расстояние фланца': 100, 'количество втулок': 2},
                      2000: {'ширина шины': 200, 'толщина шины': 6, 'количество этажей': 1,
                             'межфазное расстояние фланца': 100, 'количество втулок': 2},
                      2500: {'ширина шины': 200, 'толщина шины': 8, 'количество этажей': 1,
                             'межфазное расстояние фланца': 130, 'количество втулок': 2},
                      2501: {'ширина шины': 110, 'толщина шины': 6, 'количество этажей': 2,
                             'межфазное расстояние фланца': 130, 'количество втулок': 4},
                      3200: {'ширина шины': 160, 'толщина шины': 6, 'количество этажей': 2,
                             'межфазное расстояние фланца': 130, 'количество втулок': 4},
                      4000: {'ширина шины': 200, 'толщина шины': 6, 'количество этажей': 2,
                             'межфазное расстояние фланца': 130, 'количество втулок': 4},
                      5000: {'ширина шины': 200, 'толщина шины': 8, 'количество этажей': 2,
                             'межфазное расстояние фланца': 130, 'количество втулок': 4},
                      6400: {'ширина шины': 200, 'толщина шины': 8, 'количество этажей': 3,
                             'межфазное расстояние фланца': 130, 'количество втулок': 6}}

            elif self.a['Серия'] in ['CR1', 'CR', 'CRM', 'CR2']:
                rS = {250: {'ширина шины': 40, 'толщина шины': 6, 'количество этажей': 1,
                            'межфазное расстояние фланца': 100, 'количество втулок': 1},
                      400: {'ширина шины': 40, 'толщина шины': 6, 'количество этажей': 1,
                            'межфазное расстояние фланца': 100, 'количество втулок': 1},
                      630: {'ширина шины': 40, 'толщина шины': 6, 'количество этажей': 1,
                            'межфазное расстояние фланца': 100, 'количество втулок': 1},
                      800: {'ширина шины': 55, 'толщина шины': 6, 'количество этажей': 1,
                            'межфазное расстояние фланца': 100, 'количество втулок': 1},
                      1000: {'ширина шины': 80, 'толщина шины': 6, 'количество этажей': 1,
                             'межфазное расстояние фланца': 100, 'количество втулок': 1},
                      1250: {'ширина шины': 110, 'толщина шины': 6, 'количество этажей': 1,
                             'межфазное расстояние фланца': 100, 'количество втулок': 1},
                      1600: {'ширина шины': 160, 'толщина шины': 6, 'количество этажей': 1,
                             'межфазное расстояние фланца': 100, 'количество втулок': 2},
                      1601: {'ширина шины': 160, 'толщина шины': 6, 'количество этажей': 1,
                             'межфазное расстояние фланца': 100, 'количество втулок': 2},
                      2000: {'ширина шины': 200, 'толщина шины': 6, 'количество этажей': 1,
                             'межфазное расстояние фланца': 100, 'количество втулок': 2},
                      2500: {'ширина шины': 110, 'толщина шины': 6, 'количество этажей': 2,
                             'межфазное расстояние фланца': 130, 'количество втулок': 4},
                      3200: {'ширина шины': 160, 'толщина шины': 6, 'количество этажей': 2,
                             'межфазное расстояние фланца': 130, 'количество втулок': 4},
                      4000: {'ширина шины': 200, 'толщина шины': 6, 'количество этажей': 2,
                             'межфазное расстояние фланца': 130, 'количество втулок': 4},
                      5000: {'ширина шины': 200, 'толщина шины': 8, 'количество этажей': 2,
                             'межфазное расстояние фланца': 130, 'количество втулок': 4},
                      6400: {'ширина шины': 200, 'толщина шины': 8, 'количество этажей': 3,
                             'межфазное расстояние фланца': 130, 'количество втулок': 6}}

                if self.a['In'] in [5000, 6400]:
                    self.a['толщина изоляции'] = 11.5 / 2
                else:
                    self.a['толщина изоляции'] = 9.5 / 2

        elif self.a['Материал'] in ['м', 'М', 'm', 'M', 'Cu']:
            self.a['Материал'] = 'Cu'
            self.a['K'] = 0.7
            #self.a['R'] = 7

            if self.a['Серия'] in ['Е3', 'E3']:
                rS = {630: {'ширина шины': 40, 'толщина шины': 6, 'количество этажей': 1,
                            'межфазное расстояние фланца': 100, 'количество втулок': 1},
                      800: {'ширина шины': 40, 'толщина шины': 6, 'количество этажей': 1,
                            'межфазное расстояние фланца': 100, 'количество втулок': 1},
                      1000: {'ширина шины': 55, 'толщина шины': 6, 'количество этажей': 1,
                             'межфазное расстояние фланца': 100, 'количество втулок': 1},
                      1250: {'ширина шины': 80, 'толщина шины': 6, 'количество этажей': 1,
                             'межфазное расстояние фланца': 100, 'количество втулок': 1},
                      1600: {'ширина шины': 110, 'толщина шины': 6, 'количество этажей': 1,
                             'межфазное расстояние фланца': 100, 'количество втулок': 1},
                      2000: {'ширина шины': 160, 'толщина шины': 6, 'количество этажей': 1,
                             'межфазное расстояние фланца': 100, 'количество втулок': 2},
                      2500: {'ширина шины': 160, 'толщина шины': 8, 'количество этажей': 1,
                             'межфазное расстояние фланца': 130, 'количество втулок': 2},
                      2600: {'ширина шины': 110, 'толщина шины': 6, 'количество этажей': 2,
                             'межфазное расстояние фланца': 100, 'количество втулок': 2},
                      3200: {'ширина шины': 110, 'толщина шины': 6, 'количество этажей': 2,
                             'межфазное расстояние фланца': 130, 'количество втулок': 4},
                      4000: {'ширина шины': 160, 'толщина шины': 6, 'количество этажей': 2,
                             'межфазное расстояние фланца': 130, 'количество втулок': 4},
                      5000: {'ширина шины': 160, 'толщина шины': 8, 'количество этажей': 2,
                             'межфазное расстояние фланца': 130, 'количество втулок': 4},
                      6400: {'ширина шины': 160, 'толщина шины': 8, 'количество этажей': 3,
                             'межфазное расстояние фланца': 130, 'количество втулок': 6}}

            if self.a['Серия'] in ['CR1', 'CR', 'CRM', 'CR2']:
                rS = {250: {'ширина шины': 30, 'толщина шины': 6, 'количество этажей': 1,
                            'межфазное расстояние фланца': 100, 'количество втулок': 1},
                      400: {'ширина шины': 30, 'толщина шины': 6, 'количество этажей': 1,
                            'межфазное расстояние фланца': 100, 'количество втулок': 1},
                      630: {'ширина шины': 30, 'толщина шины': 6, 'количество этажей': 1,
                            'межфазное расстояние фланца': 100, 'количество втулок': 1},
                      800: {'ширина шины': 40, 'толщина шины': 6, 'количество этажей': 1,
                            'межфазное расстояние фланца': 100, 'количество втулок': 1},
                      1000: {'ширина шины': 55, 'толщина шины': 6, 'количество этажей': 1,
                             'межфазное расстояние фланца': 100, 'количество втулок': 1},
                      1250: {'ширина шины': 80, 'толщина шины': 6, 'количество этажей': 1,
                             'межфазное расстояние фланца': 100, 'количество втулок': 1},
                      1600: {'ширина шины': 110, 'толщина шины': 6, 'количество этажей': 1,
                             'межфазное расстояние фланца': 100, 'количество втулок': 2},
                      2000: {'ширина шины': 160, 'толщина шины': 6, 'количество этажей': 1,
                             'межфазное расстояние фланца': 100, 'количество втулок': 2},
                      2500: {'ширина шины': 80, 'толщина шины': 6, 'количество этажей': 2,
                             'межфазное расстояние фланца': 130, 'количество втулок': 4},
                      3200: {'ширина шины': 110, 'толщина шины': 6, 'количество этажей': 2,
                             'межфазное расстояние фланца': 130, 'количество втулок': 4},
                      4000: {'ширина шины': 160, 'толщина шины': 6, 'количество этажей': 2,
                             'межфазное расстояние фланца': 130, 'количество втулок': 4},
                      5000: {'ширина шины': 160, 'толщина шины': 8, 'количество этажей': 2,
                             'межфазное расстояние фланца': 130, 'количество втулок': 4},
                      6400: {'ширина шины': 160, 'толщина шины': 8, 'количество этажей': 3,
                             'межфазное расстояние фланца': 130, 'количество втулок': 6}}

                if self.a['In'] in [5000, 6400]:
                    self.a['толщина изоляции'] = 11.5 / 2
                else:
                    self.a['толщина изоляции'] = 9.5 / 2

        else:
            print('Неверно указан Материал ', self.a['Материал'])
            self.a['стандарт'] = 'нестандарт'



        if int(self.a['In']) not in rS:
            print("Не указан номинальный ток")
            self.a['стандарт'] = 'нестандарт'
            s = rS[630]
        else:
            s = rS[int(self.a['In'])]

        for i in s:
            self.a[i] = s[i]



        # Кама Алюминий 6мм
        if self.a['Производство'] == 'Kama' and self.a['Материал'] == 'Al' and self.a['толщина шины'] == 6:
            self.a['R'] = 15
        # Кама Алюминий 8мм
        elif self.a['Производство'] == 'Kama' and self.a['Материал'] == 'Al' and self.a['толщина шины'] == 8:
            self.a['R'] = 16
        # Кама Медь 6мм
        elif self.a['Производство'] == 'Kama' and self.a['Материал'] == 'Cu' and self.a['толщина шины'] == 6:
            self.a['R'] = 5
        # Кама Медь 8мм
        elif self.a['Производство'] == 'Kama' and self.a['Материал'] == 'Cu' and self.a['толщина шины'] == 8:
            self.a['R'] = 12
        # Солярис Алюминий 6мм
        elif self.a['Производство'] == 'Solaris' and self.a['Материал'] == 'Al' and self.a['толщина шины'] == 6:
            self.a['R'] = 13
        # Солярис Алюминий 8мм
        elif self.a['Производство'] == 'Solaris' and self.a['Материал'] == 'Al' and self.a['толщина шины'] == 8:
            self.a['R'] = 14
        # Солярис Медь 6мм
        elif self.a['Производство'] == 'Solaris' and self.a['Материал'] == 'Cu' and self.a['толщина шины'] == 6:
            self.a['R'] = 6.5
        # Солярис Медь 8мм
        elif self.a['Производство'] == 'Solaris' and self.a['Материал'] == 'Cu' and self.a['толщина шины'] == 8:
            self.a['R'] = 7     # Вот это не точно!!!!!!!!!!!!!!!!!!!!!
        else:
            print('КАКАЯ ТО ХУЕТА' * 50)
            print(self.a['Производство'], self.a['Материал'], self.a['толщина шины'])

        self.a['ширина стенки'] = int(self.a['ширина шины']) + 3


        # размер между этажами
        if self.a['количество этажей'] == 2:
            self.a['разница между этажами'] = self.a['ширина шины'] / 2 + 3
        elif self.a['количество этажей'] == 3:
            self.a['разница между этажами'] = self.a['ширина шины'] + 6
        else:
            self.a['разница между этажами'] = 0


        # перечисляем стп для разных выводов
        if self.a['Обозначение'] in ['pf', 'pfk', 'ugf', 'uvf', 'zgf', 'zvf', 'kpuvf', 'kpugf', 'kluvf', 'klugf'] \
                and len(re.split(r'[*+-]', self.a['размер'])) > 1:

            if self.a['Обозначение'] in ['pf', 'pfk']:
                razmer = str(re.split(r'[*+-]', self.a['размер'])[1])
            elif self.a['Обозначение'] in ['ugf', 'uvf']:
                razmer = str(re.split(r'[*+-]', self.a['размер'])[2])
            else:
                razmer = str(re.split(r'[*+-]', self.a['размер'])[3])

            if razmer == '130':
                print("Нестандартная секция!\nМеняем межфазное расстояние на 130 мм.")
                self.a['межфазное расстояние фланца'] = '130'
            elif razmer == '100':
                print("Нестандартная секция!\nМеняем межфазное расстояние на 100 мм.")
                self.a['межфазное расстояние фланца'] = '100'
        else:
            self.a['фланец край'] = 0
            self.a['фланец центр'] = 0
            self.a['СТП край'] = ''
            self.a['СТП центр'] = ''

        # 3 проводника
        if str(self.a['Кол. пров.']) in ['3']:
            self.a['количество токопроводящих пластин'] = 6
            self.a['количество демпферов'] = 3
            self.a['количество средних изоляторов'] = 2
            self.a['длина вывода фланца'] = 210

            # 130 mm bus-6 mm    3200/4000А
            if str(self.a['межфазное расстояние фланца']) == '130' and self.a['толщина шины'] == 6:
                self.a['СТП край'] = 'СТП 035'                          # край
                self.a['СТП центр'] = ' '                               # центр (прямая)
                self.a['фланец край'] = 328.2                           # край
                self.a['фланец центр'] = self.a['длина вывода фланца']  # центр (прямая)
            # 100 mm bus-8 mm 2500/5000/6400A
            elif str(self.a['межфазное расстояние фланца']) == '100' and self.a['толщина шины'] == 8:
                self.a['СТП край'] = 'СТП 037'                          # край
                self.a['СТП центр'] = '???'                             # центр (прямая)
                self.a['фланец край'] = 269.6                           # край
                self.a['фланец центр'] = self.a['длина вывода фланца']  # центр (прямая)
            else:
                self.a['СТП край'] = '???'                              # край 100 mm bus-6 mm
                self.a['СТП центр'] = ' '                               # центр (прямая)
                self.a['фланец край'] = 289                             # край
                self.a['фланец центр'] = self.a['длина вывода фланца']  # центр (прямая)

            # bus-8 mm СТП 036
            if self.a['толщина шины'] == 8:
                self.a['большой гиб'] = 1.9                             # большой гиб
                self.a['малый гиб'] = 0                                 # малый гиб (прямая)
                self.a['СТП край вывод'] = 'СТП 036'
                self.a['СТП центр вывод'] = ''
                self.a['толщина пакета'] = 30
            # bus-6 mm СТП 034
            else:
                self.a['большой гиб'] = 1.1                             # большой гиб
                self.a['малый гиб'] = 0                                 # малый гиб (прямая)
                self.a['СТП край вывод'] = 'СТП 034'
                self.a['СТП центр вывод'] = ''
                self.a['толщина пакета'] = 22

        # 4 проводника (стандарт)
        if str(self.a['Кол. пров.']) in ['4']:
            self.a['количество токопроводящих пластин'] = 8
            self.a['количество демпферов'] = 4
            self.a['количество средних изоляторов'] = 3
            self.a['длина вывода фланца'] = 210

            if self.a['Производство'] in ['Солярис', 'Solaris']:
                if self.a['Материал'] in ['Al', 'AL', 'Ал', 'АЛ']:

                    if str(self.a['межфазное расстояние фланца']) in ['130', 130]:
                        # 130 mm 6 mm    3200/4000
                        if self.a['толщина шины'] == 6:
                            print("Межфазное расстояние фланца", self.a['межфазное расстояние фланца'])
                            self.a['СТП край'] = 'СТП 066Ф-02'                         # край
                            self.a['СТП центр'] = 'СТП 066Ф-01'                        # центр (прямая)
                            self.a['фланец край'] = 379.8                              # край
                            self.a['фланец центр'] = 241.4                             # центр (прямая)
                        # 130 mm 8 mm    2500/5000/6400
                        elif self.a['толщина шины'] == 8:
                            self.a['СТП край'] = 'СТП 066Ф-06'                         # край
                            self.a['СТП центр'] = 'СТП 066Ф-05'                        # центр (прямая)
                            self.a['фланец край'] = 376                                # край
                            self.a['фланец центр'] = 240.2                             # центр (прямая)
                        else:
                            print('Нестандартный фланец')
                            self.a['стандарт'] = 'нестандарт'

                    elif str(self.a['межфазное расстояние фланца']) in ['100', 100]:

                        # 100 mm 8 mm    2500/5000/6400 (Исключительные случаи)
                        if self.a['толщина шины'] == 6:
                            self.a['СТП край'] = 'СТП 066Ф-04'                        # край
                            self.a['СТП центр'] = 'СТП 066Ф-03'                       # центр (прямая)
                            self.a['фланец край'] = 334.8                             # край
                            self.a['фланец центр'] = 232.8                            # центр (прямая)
                        # 100 mm 6 mm   (большая часть заказа)
                        elif self.a['толщина шины'] == 8:
                            self.a['СТП край'] = 'СТП 066Ф-08'                        # край
                            self.a['СТП центр'] = 'СТП 066Ф-07'                       # центр (прямая)
                            self.a['фланец край'] = 329.8                             # край
                            self.a['фланец центр'] = 231.6                            # центр (прямая)
                        else:
                            print('Нестандартный фланец')
                            self.a['стандарт'] = 'нестандарт'
                    else:
                        print('Нестандартный фланец')
                        self.a['стандарт'] = 'нестандарт'
                elif self.a['Материал'] in ['Cu', 'CU', 'Ме', 'МЕ', 'М', 'м']:
                    if str(self.a['межфазное расстояние фланца']) in ['130', 130]:
                        # 130 mm 6 mm    3200/4000
                        if self.a['толщина шины'] == 6:
                            print("Межфазное расстояние фланца", self.a['межфазное расстояние фланца'])
                            self.a['СТП край'] = 'СТП 066Ф-12'  # край
                            self.a['СТП центр'] = 'СТП 066Ф-11'  # центр (прямая)
                            self.a['фланец край'] = 377.8  # край
                            self.a['фланец центр'] = 245.9  # центр (прямая)
                        # 130 mm 8 mm    2500/5000/6400
                        elif self.a['толщина шины'] == 8:
                            self.a['СТП край'] = 'СТП 066Ф-16'  # край
                            self.a['СТП центр'] = 'СТП 066Ф-15'  # центр (прямая)
                            self.a['фланец край'] = 387.1  # край
                            self.a['фланец центр'] = 245.9  # центр (прямая)
                        else:
                            print('Нестандартный фланец')
                            self.a['стандарт'] = 'нестандарт'
                    elif str(self.a['межфазное расстояние фланца']) in ['100', 100]:

                        # 100 mm 8 mm    2500/5000/6400 (Исключительные случаи)
                        if self.a['толщина шины'] == 6:
                            self.a['СТП край'] = 'СТП 066Ф-14'  # край
                            self.a['СТП центр'] = 'СТП 066Ф-13'  # центр (прямая)
                            self.a['фланец край'] = 344.7  # край
                            self.a['фланец центр'] = 237.2  # центр (прямая)
                        # 100 mm 6 mm   (большая часть заказа)
                        elif self.a['толщина шины'] == 8:
                            self.a['СТП край'] = 'СТП 066Ф-18'  # край
                            self.a['СТП центр'] = 'СТП 066Ф-17'  # центр (прямая)
                            self.a['фланец край'] = 342.1  # край
                            self.a['фланец центр'] = 237.3  # центр (прямая)
                        else:
                            print('Нестандартный фланец')
                            self.a['стандарт'] = 'нестандарт'
                    else:
                        print('Нестандартный фланец')
                        self.a['стандарт'] = 'нестандарт'
                else:
                    print('Нестандартный фланец')
                    self.a['стандарт'] = 'нестандарт'
            elif self.a['Производство'] in ['Кама', 'Kama']:
                print(self.a['Материал'])
                if self.a['Материал'] in ['Al', 'AL', 'Ал', 'АЛ']:
                    if str(self.a['межфазное расстояние фланца']) in ['130', 130]:
                        # 130 mm 6 mm    3200/4000
                        if self.a['толщина шины'] == 6:
                            print("Межфазное расстояние фланца", self.a['межфазное расстояние фланца'])
                            self.a['СТП край'] = 'СТП 067Ф-02'                         # край
                            self.a['СТП центр'] = 'СТП 067Ф-01'                        # центр (прямая)
                            self.a['фланец край'] = 378.1                              # край
                            self.a['фланец центр'] = 241                               # центр (прямая)
                        # 130 mm 8 mm    2500/5000/6400
                        elif self.a['толщина шины'] == 8:
                            self.a['СТП край'] = 'СТП 067Ф-06'                         # край
                            self.a['СТП центр'] = 'СТП 067Ф-05'                        # центр (прямая)
                            self.a['фланец край'] = 376                                # край
                            self.a['фланец центр'] = 239.8                             # центр (прямая)
                        else:
                            print('Нестандартный фланец')
                            self.a['стандарт'] = 'нестандарт'

                    elif str(self.a['межфазное расстояние фланца']) == '100':

                        # 100 mm 8 mm    2500/5000/6400 (Исключительные случаи)
                        if self.a['толщина шины'] == 6:
                            self.a['СТП край'] = 'СТП 067Ф-04'                        # край
                            self.a['СТП центр'] = 'СТП 067Ф-03'                       # центр (прямая)
                            self.a['фланец край'] = 333.1                             # край
                            self.a['фланец центр'] = 232.3                            # центр (прямая)
                        # 100 mm 6 mm   (большая часть заказа)
                        elif self.a['толщина шины'] == 8:
                            self.a['СТП край'] = 'СТП 067Ф-08'                        # край
                            self.a['СТП центр'] = 'СТП 067Ф-07'                       # центр (прямая)
                            self.a['фланец край'] = 328.1                             # край
                            self.a['фланец центр'] = 231.1                            # центр (прямая)
                        else:
                            print('Нестандартный фланец')
                            self.a['стандарт'] = 'нестандарт'
                    else:
                        print('Нестандартный фланец')
                        self.a['стандарт'] = 'нестандарт'
                elif self.a['Материал'] in ['Cu', 'CU', 'Ме', 'МЕ', 'М', 'м']:
                    if str(self.a['межфазное расстояние фланца']) in ['130', 130]:
                        # 130 mm 6 mm    3200/4000
                        if self.a['толщина шины'] == 6:
                            print("Межфазное расстояние фланца", self.a['межфазное расстояние фланца'])
                            self.a['СТП край'] = 'СТП 067Ф-12'  # край
                            self.a['СТП центр'] = 'СТП 067Ф-11'  # центр (прямая)
                            self.a['фланец край'] = 379.5  # край
                            self.a['фланец центр'] = 246.3  # центр (прямая)
                        # 130 mm 8 mm    2500/5000/6400
                        elif self.a['толщина шины'] == 8:
                            self.a['СТП край'] = 'СТП 067Ф-16'  # край
                            self.a['СТП центр'] = 'СТП 067Ф-15'  # центр (прямая)
                            self.a['фланец край'] = 382.8  # край
                            self.a['фланец центр'] = 244.8  # центр (прямая)
                        else:
                            print('Нестандартный фланец')
                            self.a['стандарт'] = 'нестандарт'
                    elif str(self.a['межфазное расстояние фланца']) in ['100', 100]:

                        # 100 mm 8 mm    2500/5000/6400 (Исключительные случаи)
                        if self.a['толщина шины'] == 6:
                            self.a['СТП край'] = 'СТП 067Ф-14'  # край
                            self.a['СТП центр'] = 'СТП 067Ф-13'  # центр (прямая)
                            self.a['фланец край'] = 346.4  # край
                            self.a['фланец центр'] = 237.6  # центр (прямая)
                        # 100 mm 6 mm   (большая часть заказа)
                        elif self.a['толщина шины'] == 8:
                            self.a['СТП край'] = 'СТП 067Ф-18'  # край
                            self.a['СТП центр'] = 'СТП 067Ф-17'  # центр (прямая)
                            self.a['фланец край'] = 337.8  # край
                            self.a['фланец центр'] = 236.2  # центр (прямая)
                        else:
                            print('Нестандартный фланец')
                            self.a['стандарт'] = 'нестандарт'
                    else:
                        print('Нестандартный фланец')
                        self.a['стандарт'] = 'нестандарт'
                else:
                    print('Нестандартный фланец')
                    self.a['стандарт'] = 'нестандарт'
            else:
                print('Нестандартный фланец')
                self.a['стандарт'] = 'нестандарт'



            # bus-8 mm
            if self.a['толщина шины'] == 8:
                self.a['большой гиб'] = 3.7  # большой гиб
                self.a['малый гиб'] = 0.4  # малый гиб (прямая)
                self.a['СТП край вывод'] = 'СТП 014'
                self.a['СТП центр вывод'] = 'СТП 015'
                self.a['толщина пакета'] = 38
            # bus-6 mm
            else:
                self.a['большой гиб'] = 2.5  # большой гиб
                self.a['малый гиб'] = 0.2  # малый гиб (прямая)
                self.a['СТП край вывод'] = 'СТП 05'
                self.a['СТП центр вывод'] = 'СТП 06'
                self.a['толщина пакета'] = 30

            if self.a['Серия'] in ['CR1', 'CR', 'CRM', 'CR2']:
                self.a['большой гиб'] = 0  # большой гиб
                self.a['малый гиб'] = 0  # малый гиб
        else:
            print('ошибка в количестве проводников')
            self.a['стандарт'] = 'нестандарт'

        return self.a

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    print(1)