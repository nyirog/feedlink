from HTMLParser import HTMLParser

class _LinkReader(HTMLParser):
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

def get_links(fh):
    """
    Read the href attributes from link and a tag of fh html file
    
    Args:
        fh: file handle of the html file

    Returns:
        list of the links
    """
    html = fh.read()
    reader = LinkReader()
    reader.feed(html)
    return reader.links
