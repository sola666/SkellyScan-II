from core import splash, projectmanager, workflow
import argparse
import sys
from core import wsrunner
from colorama import Fore, init


def runworkflow(preset, projectfile, domain):
	workflow.instruction(preset, projectfile, domain)


def main():
	init(autoreset=True)
	args = parse_args()
	domain = args.domain if args.domain is not None else input('Attack URL : ')
	preset = args.preset if args.preset is not None else input('Workflow Preset: ')
	verbosity = args.verbose if args.verbose is True else False

	if domain[-1] == '/':
		domain = domain[:-1]
	thisProject = projectmanager.me(domain, preset)
	thisProject.createProjectFile()

	if args.vpn >= 15:
		print(f'{Fore.MAGENTA}Starting Windscribe VPN cycle...')
		wsrunner.wsrunner(args.vpn)
	elif 15 > args.vpn > 0:
		print('Aborted - Set VPN toggle >= 15 or leave off')

	workflow.instruction(preset, thisProject.projectFile, domain,verbosity)


def parser_error(errmsg):
	print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
	print("Error: " + errmsg)
	sys.exit()


def parse_args():
	# parse the arguments
	parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -d google.com -p basicscan")
	parser.error = parser_error
	parser._optionals.title = "OPTIONS"
	parser.add_argument('-d', '--domain', help="Domain name to enumerate it's subdomains", required=False)
	parser.add_argument('-p', '--preset', help="Preset scan .ini you would like to run", required=False)
	parser.add_argument('-vpn', '--vpn', help="Cycle through Windscribe VPN servers", required=False, default=0)
	parser.add_argument('-v', '--verbose', help="Verbose printing results of workflow items", required=False, action='store_true')
	return parser.parse_args()


if __name__ == '__main__':
	splash.doSplash()
	main()
