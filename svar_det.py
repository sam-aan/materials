# coding: utf8
import math
import re

class Detali:
    def __init__(self, os, input_data, name, coating, kol, tip, ABC):
        print(input_data)
        self.name = name    # Обозначение
        self.os = os  # Размер по осям
        self.material = input_data['материал']
        self.nominal = int(input_data['номинал'])  # вычислили номинал
        self.H_stenka = input_data['ширина стенки']  # ширина стенки
        self.H = input_data['ширина шины']  # ширина шины
        self.H_paketa = input_data['толщина пакета']  # толщина пакета
        self.S_sh = input_data['толщина шины']  # Толщина шины по умолчанию 6 мм.
        # расстояние развертки двойного гиба
        self.L1_sh_m = input_data['малый гиб']  # развертка малого гиба
        self.L1_sh_b = input_data['большой гиб']  # развертка большого гиба
        self.stp_L1 = input_data['СТП край вывод']
        self.stp_L2 = input_data['СТП центр вывод']
        self.L1Edge = input_data['фланец край']  # развертка крайней шины фланца
        self.L1Centre = input_data['фланец центр']  # развертка средней шины гиба
        self.StpEdge = input_data['СТП край']
        self.SptCentre = input_data['СТП центр']
        self.S_stenka = input_data['толщина стенки']
        self.S_sh_izol = input_data['толщина изоляции']
        self.H_krishka = input_data['ширина крышки']
        self.S_krishka = input_data['толщина крышки']
        self.S_krishka_sred = input_data['толщина крышки средней']
        self.R_sh = input_data['расстояние от оси до шины']
        self.R_kor = input_data['расстояние от оси до корпуса']
        # переменные для работы
        self.oboznachenie = ''
        self.naimenovanie = ''
        self.L = '-'
        self.L1 = '-'
        self.A = ABC[0]  #
        self.B = ABC[1]  #
        self.C = ABC[2]  #
        self.a = []  # Возврать результата
        self.Nprov = input_data['кол-во проводников']
        self.Ka = input_data['K']       # К-фактор для гибов
        self.R = input_data['R']
        self.coating = coating          # цвет открашивания профиля
        self.kolN = kol                  # количество деталей в расчете
        self.tip = tip

