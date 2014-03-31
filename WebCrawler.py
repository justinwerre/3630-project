import urllib2 
import robotparser
from collections import deque
from Parser import WebCrawlerHTMLParser

class WebCrawler:
	def __init__(self, keyWord, webAddress):
		self.keyWord = keyWord
		self.currentWebAddress = webAddress
		self.links = deque()
		self.robotParser = robotparser.RobotFileParser()
		self.robotParser.set_url("http://en.wikipedia.org/robots.txt")
		self.robotParser.read()


	def getCurrentPage(self):
		self.currentPage = urllib2.urlopen(self.currentWebAddress)

	def findKeyword(self):
		parser = WebCrawlerHTMLParser(self.keyWord)
		encoding = self.currentPage.headers.getparam('charset')
		page = self.currentPage.read().decode(encoding)
		parser.feed(page)
		self.links.extend(parser.linksFound())
		return parser.keywordFound()

	def nextPage(self):
		foundNextPage = False
		while not foundNextPage:
			#extend adds elements to the right, so the next element is in the left
			self.currentWebAddress = "http://en.wikipedia.org" + self.links.popleft();
			if self.robotParser.can_fetch("*", self.currentWebAddress):
				foundNextPage = True