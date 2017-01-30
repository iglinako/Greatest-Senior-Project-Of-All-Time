from sys import argv
import urllib2
from xml.etree import ElementTree as et


url_base = "https://steamcommunity.com/app/{appid}/homecontent/?userreviewsoffset={offset}&p={pagenum}&browsefilter=mostrecent&appHubSubSection=10"

content_start = '<div class="apphub_CardTextContent">'
content_end = '<div class="UserReviewCardContent_Footer">'

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
    output = []
    start = 0
    try:
        while(True):
            start = text.index(content_start, start+len(content_start)-1)
            end = text.index(content_end, start)
            output.append(text[start:text.rindex('</div>', start, end)-10])

    except:
        pass
    
    return map(clean_review_text, output)
    

def clean_review_text(review_text):
    if '</div>' in review_text:
        return review_text[review_text.rindex('</div>')+7:].strip()
    return review_text.strip()

if __name__=='__main__':
    urlob = urllib2.urlopen(url_base.format(appid=324800, offset=(int(argv[1])-1)*10, pagenum=int(argv[1])))
    reviews = parse_review(urlob.read())
    for review in reviews:
        print review
        print '-'*25
