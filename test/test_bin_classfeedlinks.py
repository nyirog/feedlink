#!/usr/bin/env python
from sys import path
from unittest import TestCase, main
from os.path import dirname, realpath
from imp import load_source
from StringIO import StringIO
from json import load

basedir = realpath(dirname(__file__)+'/..')
feedlinks = None

def setUpModule():
    global feedlinks

    path.append(basedir+'/src')
    path.append(basedir+'/bin')
    feedlinks = load_source('feedlinks', basedir+'/bin/classfeedlinks')
    return

class TestGetOptions(TestCase):
    def test_get_options(self):
        options = feedlinks.get_options([
            basedir+'/test/data/feeds.html',
            '--json', basedir+'/test/data/feeds.json'
        ])
        self.assertIsInstance(options['html'], file)
        self.assertIsInstance(options['json'], file)
        return

    def test_get_options_defaults(self):
        options = feedlinks.get_options([])
        self.assertIsInstance(options['html'], file)
        self.assertIsInstance(options['json'], file)
        return

class TestMain(TestCase):
    def setUp(self):
        self.stdin = StringIO("""
        <a href="http://feeds.feedburner.com/codinghorror"/>
        <br/>
        <link href="http://www.hwsw.hu/xml/latest_news_rss.xml"/>
        <link href="http://comment.blog.hu/atom"
              type="application/atom+xml"/>
        """)
        return

    def test_main(self):
        stdout = StringIO()
        feedlinks.main(self.stdin, stdout)
        stdout.seek(0)
        feeds = load(stdout)
        self.assertDictEqual(feeds,
            {
                'rss': [
                    "http://feeds.feedburner.com/codinghorror",
                    "http://www.hwsw.hu/xml/latest_news_rss.xml",
                ],
                'atom': [
                    'http://comment.blog.hu/atom',
                ],
            }
        )
        return

class TestBuild(TestCase):
    def setUp(self):
        self.links = [
            "http://feeds.feedburner.com/codinghorror",
            "http://www.hwsw.hu/xml/latest_news_rss.xml",
            "http://comment.blog.hu/atom",
        ]
        return

    def test(self):
        feeds = feedlinks.build(self.links)
        self.assertDictEqual(feeds,
            {
                'rss': [
                    "http://feeds.feedburner.com/codinghorror",
                    "http://www.hwsw.hu/xml/latest_news_rss.xml",
                ],
                'atom': [
                    'http://comment.blog.hu/atom',
                ],
            }
        )
        return

if __name__ == '__main__':
    main()
