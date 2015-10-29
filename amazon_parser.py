import urllib.request
import json
from bs4 import BeautifulSoup, SoupStrainer

to_crawl=[]
crawled=[]
l='http://www.amazon.com'
to_crawl.append(s)
h=urllib.request.urlopen(l)
crawled.append(s)

alinks=BeautifulSoup(h, parse_only=SoupStrainer('a', href=True))
for tags in alinks:
	if tags.has_attr('href'):
		li=tags['href']
		if li.find('http://www.amazon.com')==0 and li not in crawled:
			to_crawl.append(li)

# product=BeautifulSoup(h, parse_only=SoupStrainer('title'))
name=soup.title.contents.split(':')
product=name[0]
category=name[-1]

