import argparse
import sys
import pandas as pd
from core import toolmanager
import time
toolkit = toolmanager.toolmanager()


class loopit:

	def __init__(self, loopinput, tool, toolargs, field=None):
		self.field = field
		self.loopinput = loopinput
		self.tool = tool
		self.toolargs = toolargs

		if '.txt' in loopinput:
			self.fromtxt()

		elif '.csv' in loopinput:
			self.fromcsv()

		elif '.json' in loopinput:
			self.fromjson()
		else:
			print('File type not supported...')
			exit()
		pass

	def fromtxt(self):
		with open(self.loopinput, "r") as fd:
			loopval = fd.read().splitlines()

		for lv in loopval:
			if len(lv) == 0:
				pass
			else:
				if lv[-1] == '/':
					lv = lv[:-1]
				feixdyfile = lv.replace(r"https://", "").replace(r"http://", "").replace(r'.', '').replace('www', '')
				print(f"running {self.tool} with parameters {self.toolargs.replace('feixdy', lv)}")
				toolkit[self.tool].run(self.toolargs.replace('feixdy', lv).replace('_TIMESTAMP_', time.strftime("%Y%m%d-%H%M%S")).replace('_FEIXDYFILE_', feixdyfile),"Y")

	def fromcsv(self):
		loopval = pd.read_csv(self.loopinput)

		for lv in loopval[self.field]:
			if len(lv) == 0:
				pass
			else:
				if lv[-1] == '/':
					lv = lv[:-1]
				feixdyfile = lv.replace(r"https://", "").replace(r"http://", "").replace(r'.', '').replace('www', '')
				print(f"running {self.tool} with parameters {self.toolargs.replace('feixdy', lv)}")
				toolkit[self.tool].feixdyind = 1
				toolkit[self.tool].run(self.toolargs.replace('feixdy', lv).replace('_TIMESTAMP_', time.strftime("%Y%m%d-%H%M%S")).replace('_FXDFILE_', feixdyfile), "Y")

	def fromjson(self):
		print('.json not yet supported...')
		pass



def main():
	args = parse_args()
	inputfile = args.inputfile
	field = args.field
	tool = args.tool
	toolargs = args.toolargs
	li = loopit(loopinput=inputfile,tool=tool,toolargs=toolargs,field=field)

def parser_error(errmsg):
	print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
	print("Error: " + errmsg)
	sys.exit()


def parse_args():
	# parse the arguments
	parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -d google.com -p basicscan")
	parser.error = parser_error
	parser._optionals.title = "OPTIONS"
	parser.add_argument('-i', '--inputfile', help="Input file to iterate through", required=True)
	parser.add_argument('-f', '--field', help="The field of the file to iterate (if .csv)", default=None)
	parser.add_argument('-t', '--tool', help="The tool you want to run", required=True)
	parser.add_argument('-ta', '--toolargs', help="The args of the tool you want to run", required=True)
	return parser.parse_args()


if __name__ == '__main__':
	main()
