# -*- coding: utf-8 -*-

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'My project',
	'author': 'My Name',
	'url': 'Project Url',
	'download_url': 'from which one would downloadd',
	'author_email': 'My e-mail.',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'Project Name'
}

setup(**config)