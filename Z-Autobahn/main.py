import os
import sys
import xlrd
import logo

logo.printLogo()

print("[1] Cymru")
print("[2] Nmap")
print("[3] DNSenum")
num = input(": ")

if num == '1':
  	excel = input("Enter in a bind file: ")
  	book = xlrd.open_workbook(excel)
  	sheet = book.sheet_by_name('Sheet1')
  	data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
  	i = 0
  	while i < len(data):
  		os.system('whois -h whois.cymru.com " -w ' + ''.join(data[i]) + '"' + ' | tee -a output.txt')
  		i += 1
#print('\n')
elif num == '2':
	logo.printNmap()
	excel = input("Enter in an IP list file: ")
	book = xlrd.open_workbook(excel)
	sheet = book.sheet_by_name('Sheet1')
	data = [[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
	i = 0
	while i < len(data):
		os.system('nmap ' + ''.join(data[i]))
	#print('\n')
		i += 1

elif num == '3':
	logo.printDNSenum()
	excel = input("Enter in a bind file: IN PROG")
	book = xlrd.open_workbook(excel)
	sheet = book.sheet_by_name('Sheet1')
	data = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
	i = 0
	while i < len(data):
		os.system('whois -h whois.cymru.com " -w ' + ''.join(data[i]) + '"')
	#print('\n')
		i += 1

