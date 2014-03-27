import urllib2 

class WebCrawler:
	def __init__(self, keyWord, webAddress):
		self.keyWord = keyWord
		self.currentWebAddress = webAddress

	def getCurrentPage(self):
		self.currentPage = urllib2.urlopen(self.currentWebAddress)