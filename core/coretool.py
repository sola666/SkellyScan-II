import subprocess


class tool:

	def __init__(self, name, path):
		import urllib.parse
		self.self = self
		self.name = name.upper()
		self.path = urllib.parse.unquote(urllib.parse.quote(f'{path}'), 'utf8')

	def run(self, command, verboseflag):
		import os
		import sys

		from subprocess import DEVNULL, STDOUT, check_call, run
		if verboseflag is True:
			if '.py' in self.path:
				subprocess.run(f'py {self.path} {command}', stdout=sys.stdout, stderr=sys.stderr)
			else:
				subprocess.run(f'{self.path} {command}', stdout=sys.stdout, stderr=sys.stderr)
		else:
			if '.py' in self.path:
				subprocess.run(f'py {self.path} {command}', stdout=DEVNULL, stderr=STDOUT)
			else:
				subprocess.run(f'{self.path} {command}', stdout=DEVNULL, stderr=STDOUT)
