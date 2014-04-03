from WebCrawler import WebCrawler

startLink = raw_input("Please enter a starting web address: ")
keyword = raw_input("Please enter a keyword to search for: ")
crawler = WebCrawler(keyword, startLink)

while True:
	print "Getting a web page, please wait: ", crawler.currentWebAddress
	crawler.getCurrentPage()
	if crawler.findKeyword():
		break
	crawler.nextPage()

print "Keyword found on the following page:", crawler.currentWebAddress