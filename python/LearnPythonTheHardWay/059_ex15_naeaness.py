# coding: utf-8 -*-

from sys import argv
# 모듈의 임포트

script, filename = argv
# 실행인자 한개를 받음

txt = open(filename)
# txt란 변수에 open pydoc open 명령 (filename) 입력

print "파일 %r의 내용:" % filename
print txt.read()
# txt 변수에 입력되어 있는 파일을 읽도록 명령
print filename.read()
# open처리 하지 않으면 되지 않는다

# print "파일 이름을 다시 입력해 주세요."
# file_again = raw_input(">")
# 파일 이름을 프로그램 내에서 입력받는다.

file_again = raw_input(
    "파일 이름을 다시 입력해 주세요 \n>")

txt_again = open(file_again)
# 입력받은 이름을 open처리

print txt_again.read()
# open한 파일을 읽기

