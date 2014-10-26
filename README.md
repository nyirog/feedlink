feedlink
========

rss/atom feed classifier

Usage
-----

You can try feedlink before install if the PYTHONPATH is extended with the 
lib directory

```bash
$ PYTHONPATH=./lib:$PYTHONPATH
```

```bash
$ cat test/data/feeds.html
<a href="http://feeds.feedburner.com/codinghorror"/>
<br/>
<link href="http://www.hwsw.hu/xml/latest_news_rss.xml">
<link href="http://comment.blog.hu/atom" type="application/atom+xml">

$ ./bin/classfeedlinks test/data/feeds.html
{
    "atom": [
            "http://comment.blog.hu/atom"
    ],
    "rss": [
            "http://feeds.feedburner.com/codinghorror",
            "http://www.hwsw.hu/xml/latest_news_rss.xml"
    ]
}
```
classfeedlinks can be used in pipeline process

```bash
$ cat test/data/feeds.html | ./bin/classfeedlinks > feeds.json
$ ./bin/classfeedlinks < test/data/feeds.html > feeds.json
```

or with named files
```bash
$ ./bin/classfeedlinks --json feeds.json test/data/feeds.html
```

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

