#-*- coding:utf-8 -*-

age = input("몇 살이죠? ")
height = input("키는 얼마죠 ?")
weight = input("몸무게는 얼마죠? ")

print("네, 나이는 %r살, 키는 %r, 몸무게는 %r이네요." % (
age, height, weight))
print("뜬금없지만, 태양의 각지름은 %r입니다." % '''32'10"''')

# 코딩할 때는 %s보단 %r 쓰자.