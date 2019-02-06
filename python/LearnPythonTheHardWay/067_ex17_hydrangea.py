# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file = argv

in_file = open(from_file)
in_file.read()
out_file = open(to_file, 'w')
out_file.write(in_file.read())


# open(to_file, 'w').write(open(from_file).read())
