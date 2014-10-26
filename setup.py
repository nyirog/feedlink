#!/usr/bin/env python

from distutils.core import setup
from os.path import dirname

setup(name='feedlink',
      version='0.1.0',
      description='feed classifier script',
      author='Nyiro, Gergo',
      author_email='gergo.nyiro@gmail.com',
      packages=['feedlink'],
      package_dir = {'': 'lib'},
      scripts=['bin/classfeedlinks'],
      requires=['lxml', 'jsonschema'],
      license=open(dirname(__file__)+'/LICENSE').read()
 )
