import xlrd

workbook = xlrd.open_workbook('../data/example_09.xls')
worksheet = workbook.sheet_by_name('Questionnaire')

for row in worksheet.get_rows():
    for col in row:
        print(col)