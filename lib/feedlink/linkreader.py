from HTMLParser import HTMLParser

class _LinkReader(HTMLParser):
    """html parser to retriev the link attributes"""
    _link_tags = {'link', 'a'}
    _link_attr = 'href'
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
        return

    def handle_starttag(self, tag, attrs):
        if tag not in self._link_tags:
            return
        attrs = dict(attrs)
        if self._link_attr in attrs:
            self.links.append(attrs[self._link_attr])
        return

def get_links(html):
    """
    Read the href attributes from link and a tag of *html* document
    
    Args:
        html: html document

    Returns:
        list of the links
    """
    reader = _LinkReader()
    reader.feed(html)
    return reader.links
