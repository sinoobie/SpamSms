import mechanize,time,os
from bs4 import BeautifulSoup as BS

class Payu:
	def __init__(self):
		#install browser
		self.br = mechanize.Browser()
		self.br.set_handle_equiv(True)
		self.br.set_handle_gzip(True)
		self.br.set_handle_redirect(True)
		self.br.set_handle_referer(True)
		self.br.set_handle_robots(False)
		self.br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
		self.br.addheaders =[('Connection','keep-alive'),
		('Pragma','no-cache'),
		('Cache-Control','no-cache'),
		('Origin','http://sms.payuterus.biz'),
		('Upgrade-Insecure-Requests','1'),
		('Content-Type','application/x-www-form-urlencoded'),
		('User-Agent','Opera/9.80 (Android; Opera Mini/8.0.1807/36.1609; U; en) Presto/2.12.423 Version/12.16'),
		('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'),
		('Referer','http://sms.payuterus.biz/alpha/'),
		('Accept-Encoding','gzip, deflate'),
		('Accept-Language','id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'),
		('Cookie','_ga=GA1.2.131924726.1560439960; PHPSESSID=jjrqqaakmfcgfgbtjt8tve5595; _gid=GA1.2.1969561921.1561024035; _gat=1')
		]
		self.u='http://sms.payuterus.biz/alpha/'
		self.banner()

	def banner(self):
#		os.system('clear')
		print("""
		;;;;;;;;;;;;;;;;;;;;;;;;
		; SMS Gratis PayuTerus ;
		;      - noobie -      ;
		;;;;;;;;;;;;;;;;;;;;;;;;
		""")
		no=input('[?] Nomor Target: ')
		psn=input('[info] ketik "\\n" untuk garis baru pada pesan\n[?] Pesan: ')
		self.main(no,psn)

	def main(self,no,msg):
		o=[]
		bs=BS(self.br.open(self.u),features="html.parser")
		for x in bs.find_all("span"):
			o.append(x.text)
		capt=int(str(o)[2])+int(str(o)[6])
		self.br.select_form(nr=0)
		self.br.form['nohp']=no
		self.br.form['pesan']=msg
		self.br.form['captcha']=str(capt)
		sub=self.br.submit().read()
		if 'SMS Gratis Telah Dikirim' in str(sub):
			print('[+] Sukses mengirim sms ke',no)
		elif 'Mohon Tunggu' in str(sub):
			print('[!] Tunggu beberapa saat untuk mengirim sms yang sama')
		else:
			print('[-] Gagal mengirim sms ke',no)

try:
	Payu()
	while True:
		plh=input("\n[?] coba lagi (y/n) ")
		if plh.lower() == 'y':
			Payu()
		elif plh.lower() == 'n':
			exit('sampai jumpa lagi...')
except KeyboardInterrupt:
	print('\nErr: KeyboardInterrupt')
except Exception as E:
	print(f'Err: {E}')
