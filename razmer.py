# coding^utf8
import re


class razmer_sekc:
    def __init__(self, razmer):
        self.razmer = razmer
        self.osx = 0
        self.osy = 0
        self.osz = 0

    def os(self):
        q = re.findall(r'[^хХxX*]+', self.razmer)  # разделяем размер на составные размеры x y z
        self.osx = q[0]
        self.osy = q[1]
        self.osz = q[2]
        return [self.osx, self.osy, self.osz]