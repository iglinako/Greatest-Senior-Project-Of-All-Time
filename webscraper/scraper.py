import urllib2
from xml.etree import ElementTree as et

#url_base="steamcommunity.com/app/{appid}/homecontent/&p={pagenum}&browsefilter=toprated&browsefilter=mostrecent&l=english&appHubSubSection=10"
url_base = "https://steamcommunity.com/app/{appid}/homecontent/?userreviewsoffset={offset}&p={pagenum}&browsefilter=mostrecent&appHubSubSection=10"
class ReviewScraper(object):

    def __init__(self, gameid, startdate):
        self.gameid=gameid

    def __enter__(self):
        pass

    def __exit__(self):
        pass

    def get_reviews(self):
        pass


def parse_review(text):
    tree = et.fromstring("<root>" + text + "<\\root>").root
    output = [element.text for element in tree.findall('div class="apphub_CardTextContent"')]
    return output
    
if __name__=='__main__':
    urlob = urllib2.urlopen(url_base.format(appid=324800, offset=30, pagenum=4))
    reviews = parse_review(urlob.read())
    for review in reviews:
        print review
        print '-'*25
