#!/usr/bin/env python
from sys import path
from unittest import TestCase, main
from os.path import dirname, realpath

basedir = realpath(dirname(__file__)+'/..')
path.append(basedir + '/src')
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

class TestGetLinks:
    def test_get_links(self):
        html = '''
        <a href="foo/bar">
        <link href="spam/egg">
        '''
        links = get_links(html)
        self.assertListEqual(self.reader.links, ['foo/bar', 'spam/egg'])
        return

if __name__ == '__main__':
    main()

