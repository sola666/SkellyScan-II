class wsvpn:

	def __init__(self):
		self.self = self
		self.servers = self.getservers()
		self.location = None

	def rand(self):
		import os
		import subprocess
		import random
		from subprocess import DEVNULL, STDOUT, check_call, run
		randomserver = random.choice(self.servers)
		self.location = randomserver[0]
		subprocess.run(f'C:\Program Files (x86)\Windscribe\windscribe-cli.exe connect "{randomserver[1]}', stdout=DEVNULL, stderr=STDOUT)

	def close(self):
		import os
		import subprocess
		import random
		from subprocess import DEVNULL, STDOUT, check_call, run
		randomserver = random.choice(self.servers)
		subprocess.run(f'C:\Program Files (x86)\Windscribe\windscribe-cli.exe disconnect', stdout=DEVNULL, stderr=STDOUT)

	def best(self):
		import os
		import subprocess
		import random
		from subprocess import DEVNULL, STDOUT, check_call, run
		randomserver = random.choice(self.servers)
		subprocess.run(f'C:\Program Files (x86)\Windscribe\windscribe-cli.exe connect best', stdout=DEVNULL, stderr=STDOUT)

	def getservers(self):
		import requests
		from bs4 import BeautifulSoup
		import re
		vpnservers = []
		URL = "https://res.windscribe.com/res/status"
		page = requests.post(URL)
		soup = BeautifulSoup(page.content, "html.parser")
		serverlist = soup.find_all("span", class_="stats-pop-name")
		for sl in serverlist:
			sl = str(sl)
			sl = sl.replace(r'<span class="stats-pop-name">', '').replace(r'</span>', '')
			nickname = sl.split(' - ')[0]
			location = sl.split(' - ')[1]
			aa = [nickname, location]
			vpnservers.append(aa)
		return vpnservers
