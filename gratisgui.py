try:
	from tkinter import *
	from tkinter import messagebox
	from bs4 import BeautifulSoup as BS
	import mechanize,time,random,os,requests,re
except ModuleNotFoundError as mdl:
	exit('Module Err: %s'%(mdl))

ua = ['Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1', 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0', 'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0', 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0', 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko', 'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko', 'Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 7.0; InfoPath.3; .NET CLR 3.1.40767; Trident/6.0; en-IN)', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)', 'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)', 'Mozilla/4.0 (Compatible; MSIE 8.0; Windows NT 5.2; Trident/6.0)', 'Mozilla/4.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)', 'Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))', 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7)', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; InfoPath.3; MS-RTC LM 8; .NET4.0C; .NET4.0E)', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; chromeframe/12.0.742.112)', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; Tablet PC 2.0; InfoPath.3; .NET4.0C; .NET4.0E)', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; yie8)', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.8.36217; WOW64; en-US)', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; .NET CLR 2.7.58687; SLCC2; Media Center PC 5.0; Zune 3.4; Tablet PC 3.6; InfoPath.3)', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; Media Center PC 4.0; SLCC1; .NET CLR 3.0.04320)', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322)', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; SLCC1; .NET CLR 1.1.4322)', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 3.0.04506.30)', 'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.0; Trident/4.0; FBSMTWB; .NET CLR 2.0.34861; .NET CLR 3.0.3746.3218; .NET CLR 3.5.33652; msn OptimizedIE8;ENUS)', 'Mozilla/4.0(compatible; MSIE 7.0b; Windows NT 6.0)', 'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)', 'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)', 'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; Media Center PC 3.0; .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.1)', 'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; FDM; .NET CLR 1.1.4322)', 'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)', 'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; el-GR)', 'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 5.2)', 'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; .NET CLR 2.0.50727)', 'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)', 'Mozilla/4.0 (compatible; MSIE 6.01; Windows NT 6.0)', 'Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.1; DigExt)', 'Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.1)',"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36"]

br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [("User-Agent",random.choice(ua))]

root = Tk()
root.title("SMS GRATIS [GUI]")
root.geometry('500x500')
root.configure(bg='black')
fram=Frame(root)
try:
	html=requests.get('https://www.sms-gratis.xyz').text
	tes=re.findall(r'</b><br>(.*?)</center>',html)
	tess=str(tes).replace('<font color=green>','').replace('</font>','').replace('<font color=red>','').replace('<br><br>\\t','')
except:
	sts='[Error]'
	print("connection Error")

messagebox.showinfo('SMS GRATIS','Author: KANG-NEWBIE\nContact: https://t.me/kang_nuubi\nGithub: https://github.com/kang-newbie\nTeam: CRABS_ID')
bn = Label(root, text="[ SMS GRATIS ]\n[ GUI VERSION ]\n",font=("Arial",10),fg="blue",bg='black')
bn.config(font=('High Tower Text', 14))
bn.pack()
status=Label(root,text="Status Server: "+str(tess),fg='magenta',bg='black')
status.config(font=("Times New Roman", 11))
status.pack()
lbl = Label(root,text="Nomor:",fg='white',bg='black')
lbl.pack()
no = Entry(root,width=20,bd=3)
no.pack()
lbl2 = Label(root, text="Pesan:",fg='white',bg='black')
lbl2.pack()
msg = Entry(root,width=50,bd=3)
msg.pack()
Sid = Scrollbar(fram, width=12)
Tex = Text(fram, height=12, width=55, fg='white', bg='black')
Sid.pack(side=RIGHT, fill=Y)
Tex.pack(side=BOTTOM, fill=BOTH, expand=1)
Sid.config(command=Tex.yview)
Tex.config(yscrollcommand=Sid.set)

def clicked():
	T=True
	try:
		if no.get() == '':
			messagebox.showwarning('Masukan Nomor','Kalo ngak ada tujuannya pesannya mau dikirim kemana bosqu?')
			T=False
		elif len(msg.get()) < 5:
			messagebox.showwarning('Pesan Error','Pesan harus minimal 5 karakter')
			T=False
		elif len(msg.get()) > 100:
			messagebox.showwarning('Pesan Error','Pesan maksimal 100 karakter')
			T=False
		o=[]
		bs=BS(br.open('https://www.sms-gratis.xyz'),features="html.parser")
		for x in bs.find_all("b"):
			o.append(x.text)
		ja=o[0].split(' ')
		a=int(ja[0])
		x=ja[1]
		b=int(ja[2])
		if '+' in x:
			jawab=a+b
		elif '-' in x:
			jawab=a-b
		elif 'x' in x:
			jawab=a*b
		elif '/' in x:
			jawab=a/b
		br.select_form(nr=0)
		br.form['nomor']=no.get()
		br.form['pesan']=msg.get()
		br.form['jawaban']=str(jawab)
		if T == True:
			br.submit()
			br._factory.is_html=True
			br.select_form(nr=0)
			sub=br.submit().read()
			#print(sub)
			if 'SMS Berhasil Dikirim' in str(sub):
				stat=f"[+] Terkirim ke {no.get()}\n"
			elif 'Limit Telah Tercapai' in str(sub):
				stat="[!] Nomor terkena limit. Silahkan kembali beberapa saat lagi\n"
			else:
				stat=f"[-] Gagal Terkirim ke {no.get()}\n"
			Tex.insert(END, stat)
	except:
		messagebox.showerror('Error','Sepertinya ada yang salah. coba:\nPriksa koneksi internet anda atau\nLaporkan ke author')
	
def keluar():
	res=messagebox.askyesno("Exit","Kamu yakin mau ninggalin aku?'-'",default='no')
	if res == True:
		print("Terima Kasih telah menggunakan tools saya\n-Kang_Newbie-")
		exit()
	
fram2=Frame(root)
blk= Label(root, text="",bg='black')
btn = Button(fram2, text="   SEND   ",bg="blue",fg="white",command=clicked)
btn2 = Button(fram2, text="    EXIT    ",bg="red",fg="white",command=keluar)
blk.pack()
btn.pack(side=RIGHT)
btn2.pack(side=LEFT)
fram2.pack()
stus=Label(root,text="\nRESULT :",fg='white',bg='black')
stus.pack()
fram.pack()
root.mainloop()
