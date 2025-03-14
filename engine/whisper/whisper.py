import argparse
import concurrent.futures
import os
import sys
import time
import pandas as pd
import requests
import urllib3
from colorama import Fore, Back, init
from urllib3.exceptions import InsecureRequestWarning

init(autoreset=True)


class crystalball:

	def __init__(self, threadcount, urlinput, outputfile):
		self.self = self
		self.start = time.time()
		self.threadcount = threadcount
		self.collection = pd.DataFrame()
		self.outputfile = outputfile
		self.urlinput = urlinput
		self.allurls = []
		self.scanned = 0
		self.responses = 0
		self.head = []
		try:
			with open(r"wordlists\fingerprinting\interestingtext.txt", "r") as fd:
				self.fingerprints = fd.read().splitlines()
		except:
			with open(r"fingerprints.txt", "r") as fd:
				self.fingerprints = fd.read().splitlines()
				pass

	def checkurl(self, url):
		fpresult = ""
		if len(url) > 0:
			if url[:4] != 'http':
				url = 'https://' + url
			try:
				r = requests.get(url, verify=False, timeout=10)
				f = r.text
				for fp in self.fingerprints:
					if fp in f:
						fpresult = f'{fp}'
						break
					else:
						fpresult = ""

				result = pd.DataFrame({'URL': url, 'Response': r.status_code, 'Fingerprint': fpresult}, index=[0])
				pr = {'URL': url, 'Response': r.status_code, 'Fingerprint': fpresult}
				self.scanned += 1
				self.responses += 1
			except requests.ReadTimeout as e:
				result = pd.DataFrame({'URL': url, 'Response': 'No Response', 'Fingerprint': fpresult}, index=[0])
				pr = {'URL': url, 'Response': 'No Response', 'Fingerprint': fpresult}
				self.scanned += 1
			except requests.exceptions.ConnectionError as e:
				result = pd.DataFrame({'URL': url, 'Response': 'No Response', 'Fingerprint': fpresult}, index=[0])
				pr = {'URL': url, 'Response': 'No Response', 'Fingerprint': fpresult}
				self.scanned += 1

			self.collection = pd.concat([self.collection, result])
			return pr

	def printresult(self, thisresult):
		okresponse = [401, 402, 403, 404, 405, 501, 502, 503, 504, 505]
		badresponse = ['No Response']
		printurl = thisresult['URL'] if len(thisresult['URL']) <= 50 else thisresult['URL'][50:]
		printurl = "{:<50}".format(printurl)
		backcol = Back.LIGHTRED_EX if thisresult['Response'] in badresponse else Back.LIGHTYELLOW_EX if thisresult['Response'] in okresponse else Back.LIGHTGREEN_EX
		fontcol = Fore.LIGHTWHITE_EX if thisresult['Response'] in badresponse else Fore.BLACK  # if thisresult['Response'] in okresponse else Fore.RESET
		fpstring = Fore.MAGENTA + tco.LightYellow + '[!!!]' + tco.LightMagenta + ' Interesting Text ' + tco.LightYellow + '[!!!]' + tco.LightMagenta + '  -- "' + thisresult['Fingerprint'] + '"' if len(thisresult['Fingerprint']) > 0 else ''
		strtoprint = backcol + fontcol + str(thisresult['Response']) + Back.RESET + Fore.RESET + ' - ' + printurl + ' ' + fpstring
		print(strtoprint)

	def scan(self):
		urllib3.disable_warnings()
		requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

		if '.txt' in self.urlinput:
			try:
				with open(self.urlinput, "r") as fd:
					self.allurls = fd.read().splitlines()
			except FileExistsError:
				'File does not exist...'
		else:
			self.allurls = self.urlinput

		with concurrent.futures.ThreadPoolExecutor(max_workers=int(self.threadcount)) as executor:
			checks = {executor.submit(self.checkurl, line): line for line in self.allurls}
			for future in concurrent.futures.as_completed(checks):
				url = checks[future]
				try:
					self.printresult(future.result())
				# self.updateui(future.result())
				# data = future.result()
				# print(data)
				except Exception as e:
					print(e)
					executor.shutdown()
					pass
		executor.shutdown()

		if len(self.outputfile) > 0:
			self.exportcsv()

	def exportcsv(self):
		import time
		timestr = time.strftime("%Y%m%d-%H%M%S")
		self.collection.to_csv(f"{self.outputfile.replace('.csv', '')}_{timestr}.csv", encoding='utf-8', index=False)

	def updateui(self, pr):
		# os.system('cls||clear')
		# splash()
		updatestr = f'''
{tco.White}----------------------------------------------------------------------
{tco.LightYellow}Responses  : {tco.Green}{self.responses}{tco.LightYellow}     Scanned  : {tco.Green}{self.scanned}
{tco.White}----------------------------------------------------------------------
{tco.LightYellow}Input  : {tco.LightGreen}{self.urlinput}
{tco.LightYellow}Threads: {tco.LightGreen}{self.threadcount}
{tco.LightYellow}Output : {tco.LightGreen}{self.outputfile}'
{tco.White}----------------------------------------------------------------------
{tco.Red}HTTP  Scanned URL                                        Text Flag
		'''
		sys.stdout.write("\r" + updatestr)
		if len(self.head) == 20:
			try:
				self.head.pop(0)
			except:
				pass
		self.head.append(pr)
		for cr in self.head:
			self.printresult(cr)


def parser_error(errmsg):
	print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
	print("Error: " + errmsg)
	sys.exit()


def parse_args():
	# parse the arguments
	parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -d google.com -p basicscan")
	parser.error = parser_error
	parser._optionals.title = "OPTIONS"
	parser.add_argument('-t', '--threads', help="Threads to use for this scan", required=False, default=150)
	parser.add_argument('-o', '--output', help="Name of the output file (csv)", required=False, default='crystalball.txt')
	parser.add_argument('-w', '--wordlist', help="The list of URLs to cycle through", required=False, default='scan.txt')
	return parser.parse_args()


def main():
	args = parse_args()
	threadarg = args.threads
	outputarg = args.output
	wordlistarg = args.wordlist
	ts = crystalball(threadarg, wordlistarg, outputarg)
	ts.scan()
	ts.exportcsv()

def splash():
	from pyfiglet import Figlet
	f = Figlet(font='larry3d')
	print(tco.White + '----------------------------------------------------------------')
	print(tco.LightMagenta + f.renderText('w h i s p e r'))
	print(tco.White + '----------------------------------------------------------------')

if __name__ == '__main__':
	from core import tco
	tco = tco.tco
	splash()
	main()
