#!/usr/bin/env python
from sys import path
from unittest import TestCase, main
from os.path import dirname, realpath

basedir = realpath(dirname(__file__)+'/..')
path.append(basedir + '/src')
from feedlink.classify import classify, get_feed_types, rss, atom

class TestClassify(TestCase):
    def test_feed_types(self):
        self.assertListEqual(get_feed_types(), ['atom', 'rss'])
        return

class TestRss(TestCase):
    def test_valid_rss(self):
        self.assertTrue(rss.check('<rss type="2.0"></rss>'))
        return

    def test_invalid_xml(self):
        self.assertFalse(rss.check('<rss type="2.0"></rss'))
        return

if __name__ == '__main__':
    main()
