import os,time,sys,shutil

class Main:

	def __init__(self):
		self.detekos()

	def menu(self):
		print("""
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
		;       S P A M  S M S      ;
		;---------------------------;
		; Author : Kang-newbie      ;
		; Contact : t.me/kang_nuubi ;
		;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

1. Spam TRI
2. Spam Grab
3. Spam HooqTV
4. Spam HooqTv (GUI)
5. Spam OYOROOMS
6. Spam TelkomNyet
7. Spam Sms Gratis
8. Spam Sms Gratis (GUI)
9. Sms Gratis PayuTerus
10. Sms Gratis PayuTerus (GUI)
""")
		pilih=int(input('/Kang-newbie: '))
		if pilih == 1:
			import src.sms
		elif pilih == 2:
			import src.grab
		elif pilih == 3:
			import src.hooq
		elif pilih == 4:
			import src.hooqgui
		elif pilih == 5:
			import src.oyo
		elif pilih == 6:
			print("""
		;;;;;;;;;;;;;;;;;;;
		; Spam TelkomNyet ;
		;;;;;;;;;;;;;;;;;;;

1. Spam TelkomNyet-v1
2. Spam TelkomNyet-v2
""")
			pilihlagi=int(input('/Kang-newbie: '))
			if pilihlagi == 1:
				import src.telnyet
			elif pilihlagi == 2:
				import src.telnyet2
			else: print("[!] lihat menu dong(o)");self.menu()
		elif pilih == 7:
			import src.gratis
		elif pilih == 8:
			import src.gratisgui
		elif pilih == 9:
			import src.payu
		elif pilih == 10:
			import src.payugui
		else: print("[!] lihat menu dong(o)");self.menu()

	def detekos(self):
		#remove cache
		try:
			shutil.rmtree("src/__pycache__")
		except: pass

		if os.name in ['nt','win32']:
			os.system('cls')
		else: os.system('clear')
		self.menu()

try:
	Main()
except KeyboardInterrupt:
	exit('[Exit] Key interrupt')
except Exception as F:
	print('Err: %s'%(F))