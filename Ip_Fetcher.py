try:
	import os
	import time
	import requests
	from colorama import Fore, Back, Style
	import sys
except ImportError as ie:
	print("[!] You Have Missing Modules")
	print("[!] " + ie)


os.system("clear")



def getUserIpAddressVersion4():
	os.system("clear")
	print(Fore.GREEN + "[+] Fetching Binary Resources...")
	time.sleep(3)
	print(Fore.GREEN + "[+] 1010100101010110110101010101010010000101110101010101000100101101010101101010001010")
	print(Fore.GREEN + "[+] 0101001010000101011010101101010101001010101010010100101010111010100100010101001010")
	print("")
	print(Fore.BLUE + "[*[ Converting Fetched Binary Resources To User IP Address....")
	time.sleep(2)
	print(Fore.BLUE + "[*] Fetching Ip Address.....")
	time.sleep(1)
	User_IpAddressv4 = requests.get("https://api.ipify.org")
	User_IpAddress_text = User_IpAddressv4.text
	time.sleep(2)
	print(Fore.GREEN + "[+] Your Ip Is: " + User_IpAddress_text)
	return


print(Fore.RED + """

		==========================================================
		#		    [1] To Fetch IPV4			 #
		#=========================================================
		#		      	+Enjoy+				 #
		==========================================================
""")

choice = input(Fore.BLUE + "[*] Select Option To Fetch Your Ip: ")

if (choice == "1"):
	getUserIpAddressVersion4()

else:
	print("[!] Invalid Option!")
