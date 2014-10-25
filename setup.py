#!/usr/bin/env python

from distutils.core import setup

setup(name='feedlink',
      version='0.1.0',
      description='feed classifier script',
      author='Nyiro, Gergo',
      author_email='gergo.nyiro@gmail.com',
      packages=['feedlink'],
      package_dir = {'': 'lib'},
      scripts=['bin/classfeedlinks'],
      requires=['lxml'],
 )
