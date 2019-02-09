# -*- coding: utf-8 -*-

x = "세상에는 %d 종류의 사람이 있어요." %10
# 변수에 문자열을 대입, 문자열 안에 출력할 값을 뒤에 별도로 대입
binary = "'이진수'"
# 따옴표 안에 따옴표를 출력하려면 다른 따옴표를 사용해야 하는가?
do_not = "모르는"
y = "%s를 아는 사람과 %s 사람." % (binary, do_not)
# 변수에 문자열을 대입한다. 안에 출력할 string 값을 따옴표 밖에 변수 형태로 작성
# 문자열 안에 문자열 1
z = 'How fun is it!'


print x
print y
print z

print "'%s'라고 했어요." % x
# 문자열 안에 문자열 2
print "'%s이라고도 했죠." %y
# 문자열 안에 문자열 3
print "So, %r" %z

hilarious = False
joke_evaluation = "웃기는 농담 아니에요?! %r"

print joke_evaluation % hilarious
# joke_evaluation 안에  %r 출력이 포함되어 있으므로 뒤에 % 변수명을 작성하여 hilarious를 출력
w = "이 문자열의 왼쪽 ->"
e = "<- 이 문자열의 오른쪽"

print w + e
# 문자열을 서로 더하면 두 문자열을 연속하여 출력한다.