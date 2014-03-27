import unittest
from WebCrawler import WebCrawler

class TestWebCrawler(unittest.TestCase):
	def testInstantiateKeyWord(self):
		self.spider = WebCrawler("robot", "")
		self.assertEquals(self.spider.keyWord, "robot")

	def testInstantiateWebAddress(self):
		self.spider = WebCrawler("robot", "http://en.wikipedia.org/wiki/Robots_exclusion_standard")
		self.assertEquals(self.spider.currentWebAddress, "http://en.wikipedia.org/wiki/Robots_exclusion_standard")

suite = unittest.TestLoader().loadTestsFromTestCase(TestWebCrawler)
unittest.TextTestRunner(verbosity=2).run(suite)