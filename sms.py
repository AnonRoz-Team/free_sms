#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5
#Maklum kalo berantakan ster
G = '\033[0;32m'
C = '\033[0;36m'
W = '\033[0;37m'
R = '\033[0;31m'
Y = '\033[0;33m'
import requests,os,time
from bs4 import BeautifulSoup as bs
def logo():
	os.system('clear')
	print '''%s
___________  %sCoded by D4RKSH4D0WS%s
\_   _____/______   ____   ____      ______ _____   ______
 |    __) \_  __ \_/ __ \_/ __ \    /  ___//     \ /  ___/
 |     \   |  | \/\  ___/\  ___/    \___ \|  Y Y  \\\___ \ 
 \___  /   |__|    \___  >\___  >  /____  >__|_|  /____  >
     \/                \/     \/        \/      \/     \/
'''%(C,W,C)
def sms(nomer,pesan):
	r=requests.Session()
	scrape=r.get('https://alpha.payuterus.biz/index.php',headers={'user-agent': 'Mozilla/5.0 (Linux; Android 10; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}).text
	sms=r.post('https://alpha.payuterus.biz/send.php',headers={'origin': 'https://alpha.payuterus.biz','content-type': 'application/x-www-form-urlencoded','user-agent': 'Mozilla/5.0 (Linux; Android 10; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','referer': 'https://alpha.payuterus.biz/','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data={'nohp':nomer,'pesan':pesan,'captcha':eval(bs(scrape,'html.parser').find_all('span')[0].text.replace('=','')),'key':bs(scrape,'html.parser').find_all('input',attrs={'name':'key'})[0]['value']}).text
	if 'SMS Gratis Telah Dikirim' in sms:exit('%s[%s*%s] Successful sms sent'%(W,G,W))
	elif 'MAAF....!' in sms:exit('%s[%s!%s] Wait 15 minutes for the same message'%(W,R,W))
	else:exit('%s[%s!%s] Failed'%(W,R,W))
def main():
	logo()
	nomer=raw_input('%s[%s?%s] Input number : '%(W,Y,W))
	if nomer=='':print '%s[%s!%s] Invalid input'%(W,R,W);time.sleep(1);main()
	pesan=raw_input('%s[%s?%s] Input message : '%(W,Y,W))
	if pesan=='':print '%s[%s!%s] Invalid input'%(W,R,W);time.sleep(1);main()
	sms(nomer,pesan)
if __name__=='__main__':
	try:
		main()
	except requests.exceptions.ConnectionError:
		exit('%s[%s!%s] Check internet'%(W,R,W))
	except KeyboardInterrupt:
		exit('%s[%s!%s] Exit'%(W,R,W))
