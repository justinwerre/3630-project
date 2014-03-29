from WebCrawler import WebCrawler

crawler = WebCrawler("Protocol", "http://en.wikipedia.org/wiki/Robots_exclusion_standard")
print "geting the webpage, please wait"
crawler.getCurrentPage()
crawler.findKeyword()