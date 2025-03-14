def instruction(preset, projectlib, attackurl, verboseflag=None):
	import time
	from core import toolmanager
	from colorama import Fore, init
	import configparser
	init(autoreset=True)
	toolkit = toolmanager.toolmanager()
	config = configparser.ConfigParser()
	config.sections()
	config.read('presets/' + preset.replace('.ini', '') + '.ini')
	attackurl = attackurl.lower()
	for a in config:
		runtool = ''
		runtask = ''
		for b in config[a]:
			if b == 'tool':
				runtool = config[a][b]
			if b == 'task':
				runtask = config[a][b]
		if a != 'DEFAULT':
			tokens = {
				"_PROJECTLIB_": projectlib
				, "_NOHTTPDOMAINNAME_": attackurl.replace('https://www.', '').replace('http://www.', '').replace('https://', '').replace('http://', '')
				, "_DOMAINNAME_": attackurl
				, "_TIMESTAMP_": time.strftime("%Y%m%d-%H%M%S")
			}
			feixdytokens = {
				"_PROJECTLIB_": projectlib
				, "_NOHTTPDOMAINNAME_": attackurl.replace('https://www.', '').replace('http://www.', '').replace('https://', '').replace('http://', '')
				, "_DOMAINNAME_": attackurl
			}

			if runtool == 'feixdy':
				for t in feixdytokens:
					runtask = runtask.replace(t, feixdytokens[f'{t}'])
			else:
				for t in tokens:
					runtask = runtask.replace(t, tokens[f'{t}'])
			print(f'{Fore.LIGHTYELLOW_EX}Step {a} - Running {runtool} ...')
			print(f'{Fore.LIGHTMAGENTA_EX}Parameters - {runtask}')
			toolkit[runtool].run(runtask, verboseflag)
			print(f'{runtool} complete!')
