def replacetokens(inputstr):
	tokens = {"a": "b", "1": "2"}
	for t in tokens:
		inputstr = inputstr.replace(t, tokens[f'{t}'])
	return inputstr


def urlparse(inputstr):
	import urllib.parse
	return urllib.parse.quote(f'{inputstr}')


def urlunparse(inputstr):
	import urllib.parse
	return urllib.parse.unquote(urllib.parse.quote(f'{inputstr}'), 'utf8')


a = urlunparse('www.google.com/this is a test')
print(a)
