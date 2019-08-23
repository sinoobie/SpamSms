#!/usr/bin/python
# -*- coding: utf-8 -*-
# Coded by KANG-NEWBIE
"""
ngapai bosq? mau recode?
tinggal pake aja susah amat sih?!
"""
from multiprocessing.pool import ThreadPool
try:
	import os, random
	from time import sleep as turu
	import subprocess as sp
	import requests
except ModuleNotFoundError:
	print("\nSepertinya module requests BELUM Di Install")
	print("$ pip install requests\n")
	exit()

try:
	os.system('clear')
	print("""\033[1;32m
   _  _     \033[1;36mSPAM SMS (GRAB) UNLIMITED\033[1;32m
 _| || |_   \033[1;31mAuthor : KANG-NEWBIE\033[1;32m
|_  ..  _|  \033[1;31mContact : https://t.me/kang_nuubi\033[1;32m
|_      _|  \033[1;31mgithub : https://github.com/KANG-NRWBIE\033[1;32m
  |_||_| 
""")
	no = input("\033[1;37m[?] NOMOR (Pakai 62 Gan) =>\033[1;36m ")
	jum=int(input("\033[1;37m[?] Jumlah => \033[1;36m"))
except KeyboardInterrupt:
	print("\nKey interrupt")
	exit()
print()
print("[*] RESULT:")
def main(arg):
	try:
		idk=('phoneNumber')
		r = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber':no, 'countryCode': 'ID', 'name': 'nuubi', 'email': 'nuubi@mail.com', 'deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
#		print(r.text)
		if str(idk) in str(r.text):
			print("\033[1;32m[+] SUKSES")
		else:
			print("\033[1;31m[-] GAGAL")
	except: pass

jobs = []
for x in range(jum):
    jobs.append(x)
p=ThreadPool(5)
p.map(main,jobs)
print("done ^•^")
