def httpcode(find):
	httplib = [{'Code': '1××', 'Description': 'Informational'}, {'Code': '100', 'Description': 'Continue'}, {'Code': '101', 'Description': 'Switching Protocols'}, {'Code': '102', 'Description': 'Processing'}, {'Code': '2××', 'Description': 'Success'}, {'Code': '200', 'Description': 'OK'},
	           {'Code': '201', 'Description': 'Created'}, {'Code': '202', 'Description': 'Accepted'}, {'Code': '203', 'Description': 'Non-authoritative Information'}, {'Code': '204', 'Description': 'No Content'}, {'Code': '205', 'Description': 'Reset Content'},
	           {'Code': '206', 'Description': 'Partial Content'}, {'Code': '207', 'Description': 'Multi-Status'}, {'Code': '208', 'Description': 'Already Reported'}, {'Code': '226', 'Description': 'IM Used'}, {'Code': '3××', 'Description': 'Redirection'},
	           {'Code': '300', 'Description': 'Multiple Choices'}, {'Code': '301', 'Description': 'Moved Permanently'}, {'Code': '302', 'Description': 'Found'}, {'Code': '303', 'Description': 'See Other'}, {'Code': '304', 'Description': 'Not Modified'}, {'Code': '305', 'Description': 'Use Proxy'},
	           {'Code': '307', 'Description': 'Temporary Redirect'}, {'Code': '308', 'Description': 'Permanent Redirect'}, {'Code': '4××', 'Description': 'Client Error'}, {'Code': '400', 'Description': 'Bad Request'}, {'Code': '401', 'Description': 'Unauthorized'},
	           {'Code': '402', 'Description': 'Payment Required'}, {'Code': '403', 'Description': 'Forbidden'}, {'Code': '404', 'Description': 'Not Found'}, {'Code': '405', 'Description': 'Method Not Allowed'}, {'Code': '406', 'Description': 'Not Acceptable'},
	           {'Code': '407', 'Description': 'Proxy Authentication Required'}, {'Code': '408', 'Description': 'Request Timeout'}, {'Code': '409', 'Description': 'Conflict'}, {'Code': '410', 'Description': 'Gone'}, {'Code': '411', 'Description': 'Length Required'},
	           {'Code': '412', 'Description': 'Precondition Failed'}, {'Code': '413', 'Description': 'Payload Too Large'}, {'Code': '414', 'Description': 'Request-URI Too Long'}, {'Code': '415', 'Description': 'Unsupported Media Type'},
	           {'Code': '416', 'Description': 'Requested Range Not Satisfiable'}, {'Code': '417', 'Description': 'Expectation Failed'}, {'Code': '418', 'Description': 'Im a teapot'}, {'Code': '421', 'Description': 'Misdirected Request'}, {'Code': '422', 'Description': 'Unprocessable Entity'},
	           {'Code': '423', 'Description': 'Locked'}, {'Code': '424', 'Description': 'Failed Dependency'}, {'Code': '426', 'Description': 'Upgrade Required'}, {'Code': '428', 'Description': 'Precondition Required'},
	           {'Code': '429', 'Description': 'Too Many Requests'}, {'Code': '431', 'Description': 'Request Header Fields Too Large'}, {'Code': '444', 'Description': 'Connection Closed Without Response'}, {'Code': '451', 'Description': 'Unavailable For Legal Reasons'},
	           {'Code': '499', 'Description': 'Client Closed Request'}, {'Code': '5××', 'Description': 'Server Error'}, {'Code': '500', 'Description': 'Internal Server Error'}, {'Code': '501', 'Description': 'Not Implemented'},
	           {'Code': '502', 'Description': 'Bad Gateway'}, {'Code': '503', 'Description': 'Service Unavailable'}, {'Code': '504', 'Description': 'Gateway Timeout'}, {'Code': '505', 'Description': 'HTTP Version Not Supported'}, {'Code': '506', 'Description': 'Variant Also Negotiates'},
	           {'Code': '507', 'Description': 'Insufficient Storage'}, {'Code': '508', 'Description': 'Loop Detected'}, {'Code': '510', 'Description': 'Not Extended'},
	           {'Code': '511', 'Description': 'Network Authentication Required'}, {'Code': '599', 'Description': 'Network Connect Timeout Error'}]

	for hl in httplib:
		if hl['Code'] == find:
			return 'HTTP Response ' + hl['Code'] + ' - ' + hl['Description']


a = httpcode('404')
print(a)