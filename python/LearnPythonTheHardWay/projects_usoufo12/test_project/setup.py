# -*- coding: utf-8 -*-

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'this project is for test operation as an exercises of LTPHW ex 46',
	'author': 'usoufo12',
	'url': 'does not have Project Url yet',
	'download_url': 'does not have download_url yet',
	'author_email': 'usoufo12@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['test_project'],
	'scripts': [],
	'name': 'test_project'
}

setup(**config)