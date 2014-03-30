import urllib2 
from collections import deque
from Parser import WebCrawlerHTMLParser

class WebCrawler:
	def __init__(self, keyWord, webAddress):
		self.keyWord = keyWord
		self.currentWebAddress = webAddress
		self.links = deque()

	def getCurrentPage(self):
		self.currentPage = urllib2.urlopen(self.currentWebAddress)

	def findKeyword(self):
		parser = WebCrawlerHTMLParser(self.keyWord)
		parser.feed(self.currentPage.read())
		self.links.extend(parser.linksFound())
		return parser.keywordFound()

	def nextPage(self):
		#extend adds elements to the right, so the next element is in the left
		self.currentWebAddress = "http://en.wikipedia.org" + self.links.popleft();