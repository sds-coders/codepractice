# -*- coding: utf-8 -*-

print("몇 살이죠?"),
age = int(input())
print("키는 얼마죠?"),
height = int(input())
print("몸무게는 얼마죠?"),
weight = int(input())

print("네, 나이는%r 살, 키는%r, 몸무게는%r이네요." % (age, height, weight))
print("뜬금없지만, 태양의 각지름은%r 정도입니다."% '''32'10"''')


# raw_input () & input() for python2, which returns string and integer, respectively.
# input() for python3 and it returns string only, possibly converted to desired data type.
# %r regard ' in '32'10' as \' and, in turn, backslash is printed together.
