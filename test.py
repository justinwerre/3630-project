import robotparser
robotParser = robotparser.RobotFileParser()
robotParser.set_url("http://en.wikipedia.org/robots.txt")
robotParser.read()
print robotParser.can_fetch("*", "http://en.wikipedia.org/wiki/Special:Search")