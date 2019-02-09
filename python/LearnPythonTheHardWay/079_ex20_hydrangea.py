# -*- coding: utf-8 -*-

from sys import argv

script, input_file = argv


# print_all(f)함수의 정의: f파일을 읽음. *1
def print_all(f):
    print f.read()


# seek: 파일 내에서 읽고 있는 위치를 변경. tell()으로 위치 확인 가능.
def rewind(f):
    f.seek(0)


# line_count는 밑에 1로 정의됨. 만약, seek(0)이 되어있지 않으면 아무것도 읽지 않겠지?
# readline()에 대한 추가정보: 파일에서 바이트를 읽다가 \n문자를 찾으면 멈추고, 그동안 찾은 값을 반환.
def print_a_line(line_count, f):
    print line_count, f.readline()


# *1 print_all함수를 실행하기 전, 터미널에 변수로 입력한 파일을 input_file으로 지정해서 open후 시작.
current_file = open(input_file)

print "파일 전체를 출력해 봅시다.\n"

print_all(current_file)
print '파일 현재 위치: %r' % current_file.tell()

print "이번에는 테이프처럼 되감아 봅시다."
# 이 바로 밑에 줄을 비활성화 한 뒤 실행해 볼 것. seek함수의 역할을 알게 될 것!
rewind(current_file)
print '파일 현재 위치: %r' % current_file.tell()

print "세 줄을 출력해 봅시다."

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
# +=단축표기를 이용한 표현 개선
current_line += 1
print_a_line(current_line, current_file)
