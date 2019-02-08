# -*- coding: utf-8 -*-

from sys import argv
# argv 모듈 불러오기
script, filename = argv
# argv에 두 개의 항목 지정. 하나는 스크립트 이름, 하나는 터미널 변수인 'filename'
txt = open(filename)
# txt 변수는 filename 파일을 여는 변수로 정함.
print "파일 %r의 내용:" % filename
print txt.read()
# 단순 프린팅 및, open한 파일의 내용을 읽음.
# !!! txt.read()를 하려면 txt의 filename이 열려있어야함. 7번 줄에서 open했지?
print "파일 이름을 다시 입력해 주세요."
file_again = raw_input(">")
# 터미널에서 받는 raw_input은 문자열 형태로 file_again이 받음.
txt_again = open(file_again)
# txt_again은 raw_input을 통해 받은 제목의 파일을 여는 변수.
print txt_again.read()
# raw_input을 통해 받은 제목의 파일을 열어 읽음.
