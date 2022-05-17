# simple_table.py
# coding^utf8

from fpdf import FPDF

def simple_table(spis):
    spacing = 1

    # Колонтитул
    class CustomPDF(FPDF):

        def header(self):
            # Устанавливаем лого
            #self.image('snakehead.jpg', 10, 8, 33)
            self.set_font('Arial', 'B', 15)
            # Добавляем адрес
            self.cell(40, 5, 'ООО "ПИК "Солярис"')
            # Разрыв линии
            self.ln(20)

        def footer(self):
            self.set_y(-10)
            self.set_font('Arial', 'I', 8)
            # Добавляем номер страницы
            page = 'Page ' + str(self.page_no()) + '/{nb}'
            self.cell(0, 10, page, 0, 0, 'C')

    #pdf = CustomPDF('P', 'mm', (100, 50)).header()
    pdf = FPDF('P', 'mm', (100, 50))
    pdf.alias_nb_pages()
    pdf.add_page()
    # Add a DejaVu Unicode font (uses UTF-8)
    # Supports more than 200 languages. For a coverage status see:
    # http://dejavu.svn.sourceforge.net/viewvc/dejavu/trunk/dejavu-fonts/langcover.txt
    pdf.add_font('DejaVu-bolt', '', 'PFDinDisplayPro-Bold.ttf', uni=True)
    pdf.add_font('DejaVu', '', 'PF DinDisplay Pro.ttf', uni=True)
    pdf.add_font('gothic', '', 'GOTHIC.ttf', uni=True)
    pdf.set_font('DejaVu', '', 8)

    width_ = {0: 3, 1: 3, 2: 3, }
    # записываем первую строчку вне таблицы
    #pdf.cell(0, -10, txt='Спецификация', ln=0.5, align="C")
    #row_height = pdf.w / 4
    zag = ['Артикул', 'Сер.ном.', 'Наимен-е',  'Размер, мм', 'Ном.элем.', 'Масса, кг.']

    for i in spis:

        for s in zag:
            pdf.set_font('DejaVu-bolt', '', 3)
            pdf.cell(16, -5, txt=str(s), border=1, ln=0, align='C')

        pdf.cell(0, 0, txt='', border=0, ln=1)

        for j in i:
            pdf.set_font('DejaVu-bolt', '', 3)      # выбираем шрифт
            pdf.cell(16, 18, txt=str(j), border=1, ln=0, align='C')   # записываем ячейку

        pdf.ln(30)
    pdf.output('simple_table.pdf')
    print('konec')


if __name__ == '__main__':
    simple_table([['E3-55-Al-4-4000-uv', '1-1-0001', 'угловая вертикальная секция', '450*450', 'A1', 34.47]])

