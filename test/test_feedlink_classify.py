#!/usr/bin/env python
from os.path import dirname, realpath
from sys import path
from unittest import TestCase, main
from urllib2 import urlopen

basedir = realpath(dirname(__file__)+'/..')
path.append(basedir + '/lib')
from feedlink.classify import classify, get_feed_types, rss, atom

class TestClassify(TestCase):
    def test_feed_types(self):
        self.assertListEqual(get_feed_types(), ['atom', 'rss'])
        return

class TestRss(TestCase):
    def test_valid(self):
        self.assertTrue(rss.check('<rss type="2.0"></rss>'))
        return

    def test_invalid(self):
        self.assertFalse(rss.check('<rss type="2.0"></rss'))
        return

    def test_link(self):
        fh = urlopen('http://comment.blog.hu/rss')
        self.assertEqual(classify(fh), 'rss')
        return

class TestAtom(TestCase):
    def test_valid(self):
        feed = '<feed xmlns="%s"></feed>' % atom.xmlns
        self.assertTrue(atom.check(feed))
        return

    def test_link(self):
        fh = urlopen('http://comment.blog.hu/atom')
        self.assertEqual(classify(fh), 'atom')
        return

if __name__ == '__main__':
    main()
