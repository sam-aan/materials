# coding^utf8
import re
print ( "                                                  Расчет секций корпус детали\n" )
opa = open('det.txt', 'w')
def P (pr, pr1, pr2):#это для записи в текстовый файл новой строки
    pri = open('det.txt', 'a')
    pri.write(str(pr) + ';' + str(pr1) + ';' + str(pr2) + '\n')
    pri.close()


class raz_det:
    S = 33  # высота крышки
    H = 125  # ширина крышки
    s1 = 25  # высота стенки
    h_shina = 27  # ширина пакета шин
    korpus = 118.5
    shina = 20.5
    def __init__(self, nam, L):
        self.nam = nam
        self.L = L


    def k(N):  # N это длина по оси КРЫШКИ
        nam = 'Крышка прямая'
        L = N - korpus * 2
        return raz_det(nam, L)


    def k1(N):
        nam = 'Крышка с верхним левым срезом'
        L = N - korpus + H / 2
        return raz_det(nam, L)


    def k2(N):
        nam = 'Крышка с верхним правым срезом'
        L = float(N) - float(korpus) + float(H) / 2
        return raz_det(nam, L)


    def k3(N):
        nam = 'Крышка с боковым срезом вниз'
        L = float(N) - float(korpus) + float(h1) / 2 + float(S)
        return raz_det(nam, L)


    def k4(N):
        nam = 'Крышка с боковым срезом вверх'
        L = N - korpus + h1 / 2 + S
        return raz_det(nam, L)


    def k5(N):
        nam = 'Крышка с двумя срезами влево вправо'
        L = N + H
        return raz_det(nam, L)


    def k7(N):
        nam = 'Крышка с двумя срезами влево'
        L = N + H
        return raz_det(nam, L)


    def k8(N):
        nam = 'Крышка с двумя срезами вправо'
        L = N + H
        return raz_det(nam, L)


    def k9(N):
        nam = 'Крышка с двумя боковыми срезами вверх вниз'
        L = N + h1 + S
        return raz_det(nam, L)


    def k11(N):
        nam = 'Крышка с двумя боковыми срезами вниз'
        L = N + h1 + S * 2 + h1
        return raz_det(nam, L)


    def k12(N):
        nam = 'Крышка с двумя боковыми срезами вверх'
        L = N + h1
        return raz_det(nam, L)


    def k13(N):
        nam = 'Крышка с верхним срезом влево и боковым вниз'
        L = N + H / 2 + S + h1 / 2
        return raz_det(nam, L)


    def k14(N):
        nam = 'Крышка с верхним срезом вправо и боковым вниз'
        L = N + H / 2 - S + h1 / 2
        return raz_det(nam, L)


    def k15(N):
        nam = 'Крышка с верхним срезом влево и боковым вверх'
        L = N + H / 2 - h1 / 2
        return raz_det(nam, L)


    def k16(N):
        nam = 'Крышка с верхним срезом вправо и боковым вверх'
        L = N + H / 2 - h1 / 2
        return raz_det(nam, L)


    def C(N):  # СТЕНКА
        nam = 'Стенка прямая'
        L = N - korpus * 2
        return raz_det(nam, L)


    def C1(N):
        nam = 'Стенка с верхним левым срезом'
        L = N - korpus + h1 / 2
        return raz_det(nam, L)


    def C2(N):
        nam = 'Стенка с верхним правым срезом'
        L = N - korpus + h1 / 2
        return raz_det(nam, L)


    def C3(N):
        nam = 'Стенка с боковым срезом вниз'
        L = N - korpus + h_shina / 2 + s1
        return raz_det(nam, L)


    def C4(N):
        nam = 'Стенка с боковым срезом вверх'
        L = N - korpus - h_shina / 2
        return raz_det(nam, L)


    def C5(N):
        nam = 'Стенка с двумя срезами верхний влево нижний влево'
        L = N + h1
        return raz_det(nam, L)


    def C7(N):
        nam = 'Стенка с двумя срезами верхний влево нижний вправо'
        L = N + h1
        return raz_det(nam, L)


    def C8(N):
        nam = 'Стенка с двумя срезами верхним вправо нижним влево'
        L = N + h1
        return raz_det(nam, L)


    def C9():
        nam = 'Стенка с двумя боковыми срезами вверх вниз'
        L = N + s1 + h_shina
        return raz_det(nam, L)


    def C11(N):
        nam = 'Стенка с двумя боковыми срезами вниз'
        L = N + s1 * 2 + h_shina
        return raz_det(nam, L)


    def C12(N):
        nam = 'Стенка с двумя боковыми срезами вверх'
        L = N - h_shina
        return raz_det(nam, L)


    def C13(N):
        nam = 'Стенка с верхним срезом влево и боковым вниз'
        L = N + h1 / 2 + h_shina / 2 + s1
        return raz_det(nam, L)


    def C14(N):
        nam = 'Стенка с верхним срезом вправо и боковым вниз'
        L = N + h1 / 2 + h_shina / 2 + s1
        return raz_det(nam, L)


    def C15(N):
        nam = 'Стенка с верхним срезом влево и боковым вверх'
        L = N + h1 / 2 - h_shina / 2
        return raz_det(nam, L)


    def C16(N):
        nam = 'Стенка с верхним срезом вправо и боковым вверх'
        L = N + h1 / 2 - h_shina / 2
        return raz_det(nam, L)
