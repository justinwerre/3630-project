import urllib2 
from Parser import WebCrawlerHTMLParser

class WebCrawler:
	def __init__(self, keyWord, webAddress):
		self.keyWord = keyWord
		self.currentWebAddress = webAddress

	def getCurrentPage(self):
		self.currentPage = urllib2.urlopen(self.currentWebAddress)

	def findKeyword(self):
		parser = WebCrawlerHTMLParser(self.keyWord)
		parser.feed(self.currentPage.read())
		return parser.keywordFound()