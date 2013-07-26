
###testing xlwt
import xlwt
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('sheet 1')

#Now that the sheet is created, it’s very easy to write data to it.
# indexing is zero based, row then column
sheet.write(0,1,'test text')  

#When you’re done, save the workbook (you don’t have to close it like you do with a file object)
wbk.save('test.xls')
