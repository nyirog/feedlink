#!/usr/bin/env python
import sys

from unittest import TestCase, main
from os.path import dirname, realpath

basedir = realpath(dirname(__file__)+'/../..')
sys.path.append(basedir + '/src')
from feedlink.linkreader import _LinkReader, get_links

class TestLinkReader(TestCase):
    def setUp(self):
        self.reader = _LinkReader()
        return

    def test_LinkReader_feeding(self):
        html = '''
        <a href="foo/bar">
        <link href="spam/egg">
        '''
        self.reader.feed(html)
        self.assertListEqual(self.reader.links, ['foo/bar', 'spam/egg'])
        return

class TestGetLinks
    def test_get_links(self):
        with open(basedir+'/test/data/feeds.html') as fh:
            links = get_links(fh)
        return

if __name__ == '__main__':
    main()

