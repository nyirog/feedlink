from urllib2 import urlopen
from lxml import etree

def classify(link):
    fh = urlopen(link)
    feed = fh.read()

    for subclass in FeedClassifier.__subclasses__():
        if subclass.check(feed):
            return subclass.__name__
    raise UnknownFeedError()

def get_feed_types():
    types = [subcls.__name__ for subcls in FeedClassifier.__subclasses__()]
    return types

class FeedClassifier(object):
    @classmethod
    def check(cls, feed):
        return False

class atom(FeedClassifier):
    pass

class rss(FeedClassifier):
    @classmethod
    def check(cls, feed):
        try:
            root = etree.fromstring(feed)
        except etree.XMLSyntaxError, error:
            return False
        return root.tag == cls.__name__
    pass

class UnknownFeedError(Exception):
    pass

