# -*- coding: utf-8 -*-

# 처음 보는 낯선 내용이 있으니, 정확히 입력하도록 주의하세요.

days = "월 화 수 목 금 토 일"
months = "\n1월\n2월\n3월\n4월\n5월\n6월\n7월\n8월"

print "요일 목록: ", days
print "월 목록: ", months

print """
여기 무언가가 있어요.
세 개의 큰따옴표 안에요.
쓰고 싶은 만큼 쓸 수 있어요.
4줄이든, 5줄이든, 6줄이든 원하는 만큼.
"""

print "요일 목록: %s" % days
# 윗 예제에서의 출력물과 무엇이 다른가?

formatter = "%r, %r, %r, %r, %r, %r, %r"
formatter = days
formatter2 = "%r, %r, %r, %r, %r, %r, %r"
formatter2 = days+months


print "포메터의 테스트", formatter
print "포메터2의 테스트", formatter2