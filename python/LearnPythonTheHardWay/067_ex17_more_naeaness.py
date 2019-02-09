# -*- coding: utf-8 -*- 

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "%s에서 %s로 복사합니다." %(from_file, to_file)

indata = open(from_file).read()
out_file = open(to_file, 'w').write(indata)

print "좋습니다. 모두 완료되었습니다."
