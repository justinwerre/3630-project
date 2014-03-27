import unittest
from WebCrawler import WebCrawler

class TestWebCrawler(unittest.TestCase):
	def testInstantiateKeyWord(self):
		self.spider = WebCrawler("robot")
		self.assertEquals(self.spider.keyWord, "robot")

suite = unittest.TestLoader().loadTestsFromTestCase(TestWebCrawler)
unittest.TextTestRunner(verbosity=2).run(suite)