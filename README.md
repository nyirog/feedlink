feedlink
========

rss/atom feed classifier

Usage
-----

You can try feedlink before install if the PYTHONPATH is extended with the 
lib directory

```bash
PYTHONPATH=./lib:$PYTHONPATH ./bin/feedlink < doc.html > link.json
```

Install
-------

classfeedlink depends on the lxml third party python package.

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

