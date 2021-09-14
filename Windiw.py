from tkinter import *
from tkinter import messagebox
# from CW import ChildWindow
import openpyxl


class Window:
    def __init__(self, width, height, title="Расчеты",
                 x=800, y=300, resizable=(False, False), icon=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)
        self.rasch_entry = Entry(self.root, font="TimesNewRoman, 16")

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        Label(self.root, text="Введите расчетную мощность", font="TimesNewRoman, 16").pack(padx=0, pady=0)
        self.rasch_entry.pack(padx=0, pady=0)
        Button(self.root, text="Рассчитать", font="TimesNewRoman, 16", command=self.entry_check).pack(padx=0, pady=0)

    def entry_check(self):
        try:
            cek = int(self.rasch_entry.get())
        except ValueError:
            messagebox.showerror('Ошибка', 'Вы ввели не цифры')
        else:
            self.button_action()

    def button_action(self):
        book = openpyxl.load_workbook(r'AObject\Shini.xlsx')
        sheet = book['Shini']
        col = sheet.max_row
        raschety = int(self.rasch_entry.get())
        for row in range(2, col+1):
            WbIda = int(sheet[row][0].value)
            Plosh = int(sheet[row][1].value)
            KolVit = int(sheet[row][2].value)
            PerTok = int(sheet[row][3].value)
            KolShi = int(sheet[row][4].value)
            Metall = str(sheet[row][5].value)
            Price = int(sheet[row][6].value)
            print(WbIda)
            if raschety <= PerTok:
                QualitySize = PerTok / (Plosh * KolVit)
                QualityPrice = PerTok / (KolShi * Price)
                QualityAll = QualitySize * QualityPrice
                sheet[row][0].value = WbIda
                sheet[row][1].value = Plosh
                sheet[row][2].value = KolVit
                sheet[row][3].value = PerTok
                sheet[row][4].value = KolShi
                sheet[row][5].value = Metall
                sheet[row][6].value = Price
                sheet[row][7].value = QualitySize
                sheet[row][8].value = QualityPrice
                sheet[row][9].value = QualityAll
        book.save('ShiniDone.xlsx')
        choice = messagebox.askyesno("Выход", "Произвести новый расчет?")
        if not choice:
            self.root.destroy()

    # def create_child(self, width, height, title="Завершение",
    #                  x=800, y=300, resizable=(False, False), icon=None):
    #     ChildWindow(self.root, width, height, title, x, y, resizable, icon)


if __name__ == "__main__":
    window = Window(300, 100)
    # window.create_child(400, 400)
    window.run()
