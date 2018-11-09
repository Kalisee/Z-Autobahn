import os
import xlrd
import logo
import cymru_auto
import nmap_auto
import dnsenum_auto

logo.printLogo()

print("[1] Cymru")
print("[2] Nmap")
print("[3] DNSenum")
num = input(": ")

if num == '1':
    cymru_auto.cymru()
elif num == '2':
    nmap_auto.nmap()
elif num == '3':
    dnsenum_auto.dnsenum()