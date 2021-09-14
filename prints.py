# coding^utf8

class prints:
    def __init__(self, P_sek, P_sborka, P_detal ):
        self.P_sek = P_sek
        self.P_sborka = P_sborka
        self.P_detal = P_detal

    def print_det(self):
        q = open('spisok_det.txt', 'a') # создаем новй пустой файл для деталей
        q.write(str(self.P_detal) + '\n')
        q.close()

    def print_sborka(self):
        q = open('spisok_sborok.txt', 'a') # создаем новй пустой файл для деталей
        q.write(str(self.P_sborka) + '\n')
        q.close()

    def print_sek(self):
        q = open('spisok_sekcii.txt', 'a') # создаем новй пустой файл для деталей
        q.write(str(self.P_sek) + '\n')
        q.close()