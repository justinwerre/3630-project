from HTMLParser import HTMLParser

class WebCrawlerHTMLParser(HTMLParser):
	def __init__(self, keyword):
		HTMLParser.__init__(self)
		self.keyword = keyword.lower()
		self.found = False;
		self.links = list()

	def handle_starttag(self, tag, attrs):
		#make sure the tag is a anchor element
		if tag == "a":
			for attr in attrs:
				#find the href
				if attr[0] == "href":
					link = attr[1].split("/")
					if len(link) > 2 and link[1] == "wiki":
						self.links.append(attr[1])
						#print len(self.links), attr[1]

	#look for the keyword in the content of a tag
	def handle_data(self, data):
		words = data.split()
		for word in words:
			if word.lower() == self.keyword:
				self.found = True

	def keywordFound(self):
		return self.found

	def linksFound(self):
		return self.links