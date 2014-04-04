import unittest
from WebCrawler import WebCrawler

class TestWebCrawler(unittest.TestCase):
	def setUp(self):
		self.spider = WebCrawler("robot", "http://en.wikipedia.org/wiki/Robots_exclusion_standard")

	def tearDown(self):
		del self.spider

	def testInstantiateKeyWord(self):
		self.assertEquals(self.spider.keyWord, "robot")

	def testInstantiateWebAddress(self):
		self.assertEquals(self.spider.currentWebAddress, "http://en.wikipedia.org/wiki/Robots_exclusion_standard")

	def testGetCurrentPage(self):
		self.spider.getCurrentPage()
		self.assertEquals(self.spider.currentPage.getcode(), 200)

	def testFindKeyWord(self):
		self.spider.getCurrentPage()
		self.assertEquals(self.spider.findKeyword(), True)

	def testParseLinks(self):
		self.spider.getCurrentPage()
		self.spider.findKeyword()
		self.assertEquals(len(self.spider.links), 98)

	def testGetNextWebpage(self):
		self.spider.getCurrentPage()
		self.spider.findKeyword()
		self.spider.nextPage()
		self.assertEquals(self.spider.currentWebAddress, "http://en.wikipedia.org/wiki/MediaWiki:Robots.txt")
		self.assertEquals(len(self.spider.links), 97	)
		self.spider.getCurrentPage()
		self.assertEquals(self.spider.currentPage.getcode(), 200)

	def testParstInternetArchive(self):
		self.spider = WebCrawler("robot", "http://en.wikipedia.org/wiki/internet_archive")
		self.spider.getCurrentPage()
		self.spider.findKeyword()

	def testFollowRobotDotTxt(self):
		testLinks = list()
		testLinks.append("/wiki/Special:Search")
		testLinks.append("/wiki/computers")
		self.spider.links.extend(testLinks)
		self.spider.nextPage()
		self.assertEquals(self.spider.currentWebAddress, "http://en.wikipedia.org/wiki/computers")

	def testDontParseDuplicatPage(self):	
		testLinks = list()
		testLinks.append("/wiki/computers")
		testLinks.append("/wiki/computers")
		testLinks.append("/wiki/computers_hard_drives")
		self.spider.links.extend(testLinks)
		self.spider.nextPage()
		self.spider.nextPage()
		self.assertEquals(self.spider.currentWebAddress, "http://en.wikipedia.org/wiki/computers_hard_drives")

	def testParseTheUnready(self): 
		testLinks = list()
		testLinks.append("/wiki/%C3%86thelred_the_Unready")
		self.spider.links.extend(testLinks)
		self.spider.nextPage()
		self.assertEquals(self.spider.currentWebAddress, "http://en.wikipedia.org/wiki/%C3%86thelred_the_Unready")



suite = unittest.TestLoader().loadTestsFromTestCase(TestWebCrawler)
unittest.TextTestRunner(verbosity=2).run(suite)