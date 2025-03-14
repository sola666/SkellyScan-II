import threading
from colorama import Fore,init

class wsrunner:
	def __init__(self, frequency):
		self.self = self
		self.frequency = frequency
		self.running = True
		self.vthread = threading.Thread(target=self.cyclevpn, daemon=True)
		self.vthread.start()

	def cyclevpn(self):
		import time
		import requests
		from core import wswrapper
		init(autoreset=True)
		thisvpn = wswrapper.wsvpn()
		starttime = time.time()
		while self.running is True:
			thisvpn.rand()
			r = requests.get('https://api.ipify.org')
			print(f'{Fore.MAGENTA}VPN Switched: {Fore.LIGHTYELLOW_EX}{r.text}{Fore.MAGENTA} - {Fore.WHITE}{thisvpn.location}')
			time.sleep(self.frequency - ((time.time() - starttime) % self.frequency))

	def stopvpn(self):
		self.running = False

