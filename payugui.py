try:
	from tkinter import *
	from tkinter import messagebox
	from bs4 import BeautifulSoup as BS
	import mechanize,time,random,os,requests,re
except ModuleNotFoundError as mdl:
	exit('Module Err: %s'%(mdl))

class Main:
	def __init__(self):
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
		('User-Agent','Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36'),
		('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'),
		('Referer','http://sms.payuterus.biz/alpha/'),
		('Accept-Encoding','gzip, deflate'),
		('Accept-Language','id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'),
		('Cookie','_ga=GA1.2.131924726.1560439960; PHPSESSID=jjrqqaakmfcgfgbtjt8tve5595; _gid=GA1.2.1969561921.1561024035; _gat=1')
		]
		self.u='http://sms.payuterus.biz/alpha/'
		self.tkmain()

	def tkmain(self):
		global Tex
		root = Tk()
		root.title("SMS GRATIS [GUI]")
		root.geometry('500x500')
		root.configure(bg='black')
		fram=Frame(root)

		messagebox.showinfo('PAYU SMS GRATIS','Author: KANG-NEWBIE\nContact: https://t.me/kang_nuubi\nGithub: https://github.com/kang-newbie\nTeam: CRABS_ID')
		bn = Label(root, text="[ PAYU SMS GRATIS ]\n[ GUI VERSION ]\n",font=("Arial",10),fg="blue",bg='black')
		bn.config(font=('High Tower Text', 14))
		bn.pack()

		lbl = Label(root,text="Nomor:",fg='white',bg='black')
		lbl.pack()

		self.no = Entry(root,width=20,bd=3)
		self.no.pack()

		lbl2 = Label(root, text="Pesan:",fg='white',bg='black')
		lbl2.pack()

		self.msg = Entry(root,width=50,bd=3)
		self.msg.pack()

		Sid = Scrollbar(fram, width=12)
		Tex = Text(fram, height=12, width=55, fg='white', bg='black')
		Sid.pack(side=RIGHT, fill=Y)
		Tex.pack(side=BOTTOM, fill=BOTH, expand=1)
		Sid.config(command=Tex.yview)
		Tex.config(yscrollcommand=Sid.set)	

		fram2=Frame(root)
		blk= Label(root, text="",bg='black')
		btn = Button(fram2, text="   SEND   ",bg="blue",fg="white",command=self.spam)
		btn2 = Button(fram2, text="    EXIT    ",bg="red",fg="white",command=self.keluar)
		blk.pack()
		btn.pack(side=RIGHT)
		btn2.pack(side=LEFT)
		fram2.pack()

		stus=Label(root,text="\nRESULT :",fg='white',bg='black')
		stus.pack()
		fram.pack()
		root.mainloop()

	def spam(self):
		T=True
		try:
			if self.no.get() == '':
				messagebox.showwarning('Masukan Nomor','Kalo ngak ada tujuannya pesannya mau dikirim kemana bosqu?')
				T=False
			elif len(self.msg.get()) > 150:
				messagebox.showwarning('Pesan Error','Pesan maksimal 150 karakter')
				T=False
			o=[]
			bs=BS(self.br.open(self.u),features="html.parser")
			for x in bs.find_all("span"):
				o.append(x.text)
			capt=int(o[0].split(' ')[0])+int(o[0].split(' ')[2])
			self.br.select_form(nr=0)
			self.br.form['nohp']=self.no.get()
			self.br.form['pesan']=self.msg.get()
			self.br.form['captcha']=str(capt)
			if T == True:
				sub=self.br.submit().read()
				#print(sub)
				if 'SMS Gratis Telah Dikirim' in str(sub):
					stat=f"[+] Terkirim ke {self.no.get()}\n"
				elif 'Mohon Tunggu' in str(sub):
					stat="[!] Tunggu beberapa saat untuk mengirim sms yang sama\n"
				else:
					stat=f"[-] Gagal Terkirim ke {self.no.get()}\n"
				Tex.insert(END, stat)
		except:
			messagebox.showerror('Error','Sepertinya ada yang salah. coba:\nPriksa koneksi internet anda atau\nLaporkan ke author')

	def keluar(self):
		res=messagebox.askyesno("Exit","Kamu yakin mau ninggalin aku?'-'",default='no')
		if res == True:
			print("Terima Kasih telah menggunakan tools saya\n-Kang_Newbie-")
			exit()

try:
	Main()
except Exception as Err:
	print("[Err] %s"%(Err))