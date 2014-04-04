import urllib
import robotparser
rb = robotparser.RobotFileParser("http://en.wikipedia.org/robots.txt")
rb.read()
print rb
print rb.can_fetch("*", "http://en.wikipedia.org/wiki/%C3%86thelred_the_Unready")