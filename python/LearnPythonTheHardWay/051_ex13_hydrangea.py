# -*- coding: utf-8 -*-

from sys import argv
# import한 기능: '모듈'이라고 부름.
script, first, second, third = argv
# script: 파일(스크립트)이름, first~third: 터미널 명령 시 입력하는 변수.
# 변수는 파일 내에 정한 개수와 터미널에서 입력하는 수가 같아야 함.
print "스크립트 이름:", script
print "첫 번째 변수:", first
print "두 번째 변수:", second
print "세 번째 변수:", third
