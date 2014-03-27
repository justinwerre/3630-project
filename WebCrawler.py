import urllib2 

class WebCrawler:
	def __init__(self, keyWord, webAddress):
		self.keyWord = keyWord
		self.currentWebAddress = webAddress