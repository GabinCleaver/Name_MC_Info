import requests, json, logging
from colorama import Fore, init

init()

minecraft_name = input(Fore.LIGHTCYAN_EX + "[>] Saisissez un nom d'utilisateur MC : ")

def converttostr(input_seq, seperator):
   final_str = seperator.join(input_seq)
   return final_str

def req(name):
	try:
		resp = requests.get("https://api.ashcon.app/mojang/v2/user/" + name)
		data = json.loads(resp.text)

		print(Fore.GREEN + "[+] Nom: " + data["username"])
		print(Fore.GREEN + "[+] UUID: " + data["uuid"])
		if data["created_at"] == None:
			print(Fore.RED + "[-] Crée le: Non Trouvé")
		else:
			print(Fore.GREEN + "[+] Crée le: " + data["created_at"])
		print(Fore.GREEN + "\n[+] Nom Historique: ")

		# Checking for username history
		for names in data["username_history"]:
			try:
				print(Fore.YELLOW + "   - " + names["username"] + f"(Changed {data['changed_at']})")
			except:
				print(Fore.YELLOW + "   - " + names["username"])
	
	except Exception as x:
		logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
		logging.critical(x)

req(minecraft_name)