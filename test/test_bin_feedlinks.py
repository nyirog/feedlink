#!/usr/bin/env python
from sys import path
from unittest import TestCase, main
from os.path import dirname, realpath
from imp import load_source

basedir = realpath(dirname(__file__)+'/..')
feedlinks = None

def setUpModule():
    global feedlinks

    path.append(basedir+'/bin')
    feedlinks = load_source('feedlinks', basedir+'/bin/feedlinks')
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


if __name__ == '__main__':
    main()
