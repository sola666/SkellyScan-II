class me:
	import os
	currDir = os.getcwd()
	domain = ''

	def __init__(self, url,preset):
		self.self = self
		self.url = url
		self.scanType = preset
		self.nohttpsUrl = self.url.replace(r"https://", "").replace(r"http://", "")
		self.projectFile = self.url.replace(r"https://", "").replace(r"http://", "").replace(r'.', '').replace('www','')

	def createProjectFile(self):
		import os
		isExist = os.path.exists(self.currDir + "\\projects\\" + self.projectFile)
		if not isExist:
			os.makedirs(self.currDir + "\\projects\\" + self.projectFile)

