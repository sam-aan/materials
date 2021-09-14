# coding^utf8
import xlrd


def exl_TO_list(FilePath):
    ''' вначале читаем файл и переписываем его в список списков '''
    print(FilePath)
    rb = xlrd.open_workbook(FilePath, formatting_info=True)
    sheet = rb.sheet_by_index(0)
    vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
    return  vals


if __name__ == '__main__':
    print(exl_TO_list('D:/временная/Загрузки/2020/03/31/example.xls'))
