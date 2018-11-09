import os
import xlrd
import logo

def nmap():
	logo.printNmap()
	excel = input("Enter in an IPs file: ")
	book = xlrd.open_workbook(excel)
	sheet = book.sheet_by_name('Sheet1')
	data = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
	i = 0
	while i < len(data):
		os.system('nmap ' + ''.join(data[i]))
	i += 1
