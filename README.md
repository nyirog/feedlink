feedlink
========

rss/atom feed classifier

Usage
-----

You can try feedlink before install if the PYTHONPATH is extended with the 
lib directory

```bash
$ cat test/data/feeds.html
<a href="http://feeds.feedburner.com/codinghorror"/>
<br/>
<link href="http://www.hwsw.hu/xml/latest_news_rss.xml">
<link href="http://comment.blog.hu/atom" type="application/atom+xml">

$ PYTHONPATH=./lib:$PYTHONPATH ./bin/classfeedlinks test/data/feeds.html
{
    "atom": [
            "http://comment.blog.hu/atom"
    ],
    "rss": [
            "http://feeds.feedburner.com/codinghorror",
            "http://www.hwsw.hu/xml/latest_news_rss.xml"
    ]
}

Install
-------

feedlink depends on the lxml third party python package.

```bash
sudo apt-get install python-lxml
sudo python setup.py install
```

Test
----

Run all the test

```bash
python -m unittest discover -s test -p test_*.py
```

