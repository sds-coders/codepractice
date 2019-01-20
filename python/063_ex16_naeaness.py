# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print "%r 파일을 지우려 합니다." % filename
print "취소하려면 CTRL-C(^C)를 누르세요."
print "진행하려면 리턴을 누르세요."

raw_input("?")

print "파일 여는 중..."
target = open(filename, 'a')
# w는 쓰기 a는 이어쓰기

print "파일 내용을 지웁니다. 안녕히!"
target.truncate()
# 얘는 뭐하는 놈?

print "이제 새 줄에 들어갈 내용을 묻겠습니다."

line1 = raw_input("1줄: ")
line2 = raw_input("2줄: ")
line3 = raw_input("3줄: ")

print "이 내용을 파일에 씁니다."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# print target.read()
# 문서를 다시 열지 않고 한번에 읽는 방법은?

print "마지막으로 파일을 닫습니다."
target.close()

target = open(filename)
print target.read()

