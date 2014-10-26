from lxml import etree

def classify(fh):
    """
    Classify the feed type of the *link*

    Args:
        fh: url handler

    Returns:
        feed type: 'atom' or 'rss'

    Raises:
        UnknownFeedError: if the *link* does not point to a valid feed
    """
    feed = fh.read()
    for subclass in FeedClassifier.__subclasses__():
        if subclass.check(feed):
            return subclass.__name__
    raise UnknownFeedError()

def get_feed_types():
    """List the available feed types by this feed classifier module."""
    types = [subcls.__name__ for subcls in FeedClassifier.__subclasses__()]
    return types


class FeedClassifier(object):
    """
    Super class of the feed classifiers. The check class method has to be
    overwritten by the descendant classes.

    The name of the descendant class will be its feed type.
    """
    @classmethod
    def check(cls, feed):
        """Validate the *feed* content"""
        return False


class atom(FeedClassifier):
    """atom feed classifier"""
    xmlns = 'http://www.w3.org/2005/Atom'
    @classmethod
    def check(cls, feed):
        try:
            root = etree.fromstring(feed)
        except etree.XMLSyntaxError, error:
            return False
        else:
            if root.nsmap.get(None) == cls.xmlns:
                return True
        return False


class rss(FeedClassifier):
    """rss feed classifier"""
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

