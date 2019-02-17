# -*- coding: utf-8 -*-

the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'orange', 'pear', 'salgoo~']
change = [1, 'ten cents', 2 ,'hundred cents', 3, 'Oh Dalla~']

# 첫 번째 for문은 list를 따라 돕니다.
for number in the_count:
    print "이 수는 %d" % number
    
# 위와 같아요.
for fruit in fruits:
    print "과일 종류: %s" % fruit

# 섞어 만든 list도 돌 수 있어요.
for i in change:
    print "받은 잔돈 %s" % i

# list를 만들 수도 있는데, 먼저 빈 것으로 시작합시다.
elements = []

# 그리고 0에서 5까지 세는 range 함수를 써요.
for i in range(0, 6):
    print "list에 %d 숫자를 더합니다." % i
    # append는 list가 알아듣는 함수입니다.
    elements.append(i)
    
# 이것도 출력할 수 있습니다.
for i in elements:
    print "원소는 %d" % i

element = [0, 0, 1, 1, 2, 3, 6]
print element

# count(오쇼) : list내에 (요소)가 몇 개 있는지
print element.count(0)

# insert(요소, 위치) : list내에 (요소) 삽입. 삽입위치는 (위치)로 정함.
element.insert(1, "Get a piece of me bastard")
print element

# index(요소) : list내에 (요소)가 처음으로 나오는 위치
print element.index(1)
index = element.index(1, 2)
print "index of 1 in list:", index

# extend(리스트) : list 뒤에 (리스트)를 append하는 기능.
dongun = []
dongun2 = [0, 1, 2, 3, 4, 5]
dongun.extend(dongun2)
print dongun
# 이런 방법도 있다. extend랑 이 방법이 바로 32.2-2의 해결책.
dongun += element
print dongun

# pop(인덱스) : list의 (인덱스)에 있는 요소를 제거.
dongun.pop(0)
print dongun

# remove(요소) : list의 (요소)중 첫 번쨰로 등장하는 놈 제거.
dongun.remove(2)
print dongun

# reverse(): list 거꾸로 뒤집음.
dongun.reverse()
print dongun

# sort(): list 정렬. int 다음 str 순으로 정리함.
dongun.sort()
print dongun
