# -*- coding: utf-8 -*-

print "몇 살이죠?",
age =raw_input()
print "키는 얼마죠?",
height = raw_input()
print "몸무게는 얼마죠?",
weight = raw_input()

print "네, 나이는 %r살, 키는 %r, 몸무게는 %r이네요." %(
age, height, weight)
print "뜬금없지만, 태양의 각지름은 %r 정도입니다." % '''32'10"'''

# 이 아래는 더 해보기의 내용

 
test_name = raw_input("이름은 무엇이죠?")
print test_name
test_multiplier = int(raw_input("배수를 입력받습니다."))
test_multiplier = test_multiplier*int(age)

print test_multiplier
