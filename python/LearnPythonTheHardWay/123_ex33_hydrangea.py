# -*- coding: utf-8 -*-

# 더 해보기 1 & 3
numbers = []

# j는 더 해보기 1, k는 더 해보기 3의 산물.
def number_from_zero(j, k):
    i = 0
    while i < j:
        numbers.append(i)
        i = i + k
    return numbers

        
print number_from_zero(9, 2)

print "숫자 :"

for num in numbers:
    print num,
    
    
# 원문
# i = 0
# numbers = []

# def number_from_zero(j):
#     while i < j:
#         print "꼭대기에서 i는 %d" % i
#         numbers.append(i)

#         i = i + 1
#         print "숫자는 이제: ", numbers
#         print "바닥에서 i는 %d" % i

        
# print "숫자: "

# print number_from_zero(6)

# for num in numbers:
#     print num

# 더 해보기 5.
once = []

def one_more_time(j, k):
    i = 0
    for j in range(0, j):
        if i < j:
            once.append(i)
            i += k
    return once

print one_more_time(11,2)
