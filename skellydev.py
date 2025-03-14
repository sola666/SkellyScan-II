from core import splash, projectmanager, workflow
import argparse
import threading
import sys


# thread_local = threading.local()
# def vpncycle():
# 	import subprocess
# 	cmd = r"pythonw core\wsrunner.py"
# 	process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# 	print('vpn started')

# def vpncycle():
# 	from core import wsrunner
# 	wsrunner.cyclevpn(5.0)


def runworkflow(preset, projectfile, domain):
	workflow.instruction(preset, projectfile, domain)


def main():
	from core import wsrunner
	args = parse_args()
	domain = args.domain
	preset = args.preset

	thisProject = projectmanager.me(domain, preset)
	thisProject.createProjectFile()

	if args.vpn > 0:
		print('Starting Windscribe VPN cycle...')
		wsrunner.wsrunner(args.vpn)

	workflow.instruction(preset, thisProject.projectFile, domain)


def parser_error(errmsg):
	print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
	print("Error: " + errmsg)
	sys.exit()


def parse_args():
	# parse the arguments
	parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -d google.com -p basicscan")
	parser.error = parser_error
	parser._optionals.title = "OPTIONS"
	parser.add_argument('-d', '--domain', help="Domain name to enumerate it's subdomains", required=False, default=input('Attack URL : '))
	parser.add_argument('-p', '--preset', help="Preset scan .ini you would like to run", required=False, default=input('Workflow Preset: '))
	parser.add_argument('-vpn', '--vpn', help="Cycle through Windscribe VPN servers", required=False, default=0)
	return parser.parse_args()


if __name__ == '__main__':
	splash.doSplash()
	main()
