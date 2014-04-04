from WebCrawler import WebCrawler

startLink = "http://en.wikipedia.org/wiki/House_of_Wessex"
# startLink = "http://en.wikipedia.org/wiki/%C3%86thelred_the_Unready"
keyword = "mage"
print "Setting up crawler, please wait"
crawler = WebCrawler(keyword, startLink)

# print "Getting a web page, please wait: ", crawler.currentWebAddress
# crawler.getCurrentPage()
# crawler.findKeyword()

while True:
	print "Getting a web page, please wait: ", crawler.currentWebAddress
	crawler.getCurrentPage()
	if crawler.findKeyword():
		break
	crawler.nextPage()
print "Keyword found on page: ", crawler.currentWebAddress