from HTMLParser import HTMLParser

class WebCrawlerHTMLParser(HTMLParser):
	def __init__(self, keyword):
		HTMLParser.__init__(self)
		self.keyword = keyword.lower()
		self.found = False;

	def handle_data(self, data):
		words = data.split()
		for word in words:
			if word.lower() == self.keyword:
				self.found = True

	def keywordFound(self):
		return self.found