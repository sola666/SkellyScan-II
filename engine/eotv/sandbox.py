import re
import sys
import os
import argparse
import time
import hashlib
import random
import multiprocessing
import threading
import socket
import json
from collections import Counter

import dns.resolver
import requests
import urllib.parse as urlparse
import urllib.parse as urllib

from past.types import unicode

G = '\033[92m'  # green
Y = '\033[93m'  # yellow
B = '\033[94m'  # blue
R = '\033[91m'  # red
W = '\033[0m'  # white


class enumratorBase(object):
	def __init__(self, base_url, engine_name, domain, subdomains=None, silent=False, verbose=True):
		subdomains = subdomains or []
		self.domain = urlparse.urlparse(domain).netloc
		self.session = requests.Session()
		self.subdomains = []
		self.timeout = 25
		self.base_url = base_url
		self.engine_name = engine_name
		self.silent = silent
		self.verbose = verbose
		self.headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Accept-Language': 'en-US,en;q=0.8',
			'Accept-Encoding': 'gzip',
		}
		self.print_banner()

	def print_(self, text):
		if not self.silent:
			print(text)
		return

	def print_banner(self):
		""" subclass can override this if they want a fancy banner :)"""
		self.print_(G + "[-] Searching now in %s.." % (self.engine_name) + W)
		return

	def send_req(self, query, page_no=1):

		url = self.base_url.format(query=query, page_no=page_no)
		try:
			resp = self.session.get(url, headers=self.headers, timeout=self.timeout)
		except Exception:
			resp = None
		return self.get_response(resp)

	def get_response(self, response):
		if response is None:
			return 0
		return response.text if hasattr(response, "text") else response.content

	def check_max_subdomains(self, count):
		if self.MAX_DOMAINS == 0:
			return False
		return count >= self.MAX_DOMAINS

	def check_max_pages(self, num):
		if self.MAX_PAGES == 0:
			return False
		return num >= self.MAX_PAGES

	# override
	def extract_domains(self, resp):
		""" chlid class should override this function """
		return

	# override
	def check_response_errors(self, resp):
		""" chlid class should override this function
		The function should return True if there are no errors and False otherwise
		"""
		return True

	def should_sleep(self):
		"""Some enumrators require sleeping to avoid bot detections like Google enumerator"""
		return

	def generate_query(self):
		""" chlid class should override this function """
		return

	def get_page(self, num):
		""" chlid class that user different pagnation counter should override this function """
		return num + 10

	def enumerate(self, altquery=False):
		flag = True
		page_no = 0
		prev_links = []
		retries = 0

		while flag:
			query = self.generate_query()
			count = query.count(self.domain)  # finding the number of subdomains found so far

			# if they we reached the maximum number of subdomains in search query
			# then we should go over the pages
			if self.check_max_subdomains(count):
				page_no = self.get_page(page_no)

			if self.check_max_pages(page_no):  # maximum pages for Google to avoid getting blocked
				return self.subdomains
			resp = self.send_req(query, page_no)

			# check if there is any error occured
			if not self.check_response_errors(resp):
				return self.subdomains
			links = self.extract_domains(resp)

			# if the previous page hyperlinks was the similar to the current one, then maybe we have reached the last page
			if links == prev_links:
				retries += 1
				page_no = self.get_page(page_no)

				# make another retry maybe it isn't the last page
				if retries >= 3:
					return self.subdomains

			prev_links = links
			self.should_sleep()

		return self.subdomains


class enumratorBaseThreaded(multiprocessing.Process, enumratorBase):
	def __init__(self, base_url, engine_name, domain, subdomains=None, q=None, silent=False, verbose=True):
		subdomains = subdomains or []
		enumratorBase.__init__(self, base_url, engine_name, domain, subdomains, silent=silent, verbose=verbose)
		multiprocessing.Process.__init__(self)
		self.q = q
		return

	def run(self):
		domain_list = self.enumerate()
		for domain in domain_list:
			self.q.append(domain)


class GoogleEnum(enumratorBaseThreaded):
	def __init__(self, domain, subdomains=None, q=None, silent=False, verbose=True):
		subdomains = subdomains or []
		base_url = "https://google.com/search?q={query}&btnG=Search&hl=en-US&biw=&bih=&gbv=1&start={page_no}&filter=0"
		self.engine_name = "Google"
		self.MAX_DOMAINS = 11
		self.MAX_PAGES = 200
		super(GoogleEnum, self).__init__(base_url, self.engine_name, domain, subdomains, q=q, silent=silent, verbose=verbose)
		self.q = q
		return

	def extract_domains(self, resp):
		links_list = list()
		link_regx = re.compile('<cite.*?>(.*?)<\/cite>')
		try:
			links_list = link_regx.findall(resp)
			for link in links_list:
				link = re.sub('<span.*>', '', link)
				if not link.startswith('http'):
					link = "http://" + link
				subdomain = urlparse.urlparse(link).netloc
				if subdomain and subdomain not in self.subdomains and subdomain != self.domain:
					if self.verbose:
						self.print_("%s%s: %s%s" % (R, self.engine_name, W, subdomain))
					self.subdomains.append(subdomain.strip())
		except Exception:
			pass
		return links_list

	def check_response_errors(self, resp):
		if (type(resp) is str or type(resp) is unicode) and 'Our systems have detected unusual traffic' in resp:
			self.print_(R + "[!] Error: Google probably now is blocking our requests" + W)
			self.print_(R + "[~] Finished now the Google Enumeration ..." + W)
			return False
		return True

	def should_sleep(self):
		time.sleep(5)
		return

	def generate_query(self):
		if self.subdomains:
			fmt = 'site:{domain} -www.{domain} -{found}'
			found = ' -'.join(self.subdomains[:self.MAX_DOMAINS - 2])
			query = fmt.format(domain=self.domain, found=found)
		else:
			query = "site:{domain} -www.{domain}".format(domain=self.domain)
		return query
