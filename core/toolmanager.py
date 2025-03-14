def toolmanager():
	toolkit = {}
	import configparser
	from core import coretool
	config = configparser.ConfigParser()
	config.sections()
	config.read('toolkit.ini')
	for a in config['tools']:
		toolkit[a] = coretool.tool(a, config['tools'][a])
	return toolkit


if __name__ == '__main__':
	toolmanager()
