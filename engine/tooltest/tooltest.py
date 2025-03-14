import argparse
import sys

def main():
	print('TEST STARTED...')
	args = parse_args()
	a = args.testa
	b = args.testb
	c = args.testc
	print(f'a = {a}, b = {b} - done!')
	with open(c, 'w') as f:
		f.write(f'a = {a}, b = {b} - done!')


def parser_error(errmsg):
	print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
	print("Error: " + errmsg)
	sys.exit()


def parse_args():
	# parse the arguments
	parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -d google.com -p basicscan")
	parser.error = parser_error
	parser._optionals.title = "OPTIONS"
	parser.add_argument('-a', '--testa', help="test param a", required=True)
	parser.add_argument('-b', '--testb', help="test param b", required=False)
	parser.add_argument('-c', '--testc', help="fileoutput test", required=False)
	return parser.parse_args()


if __name__ == '__main__':
	main()
