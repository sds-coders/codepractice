# -*- coding: utf-8 -*-

my_name = 'Zed A. Shaw'
my_age = 35  # not a lie
my_height = 188  # cm
my_weight = 82  # kg
my_eyes = '파랑'
my_teeth = '하양'
my_hair = '갈색'

print "%s에 대해 이야기해 보죠." % my_name
print "키는 %d 센티미터고요." % my_height
print "몸무게는 %d 킬로그램이예요." % my_weight
print "사실 아주 많이 나가는 건 아니죠."
print "눈은 %s이고 머리는 %s이예요." % (my_eyes, my_hair)
print "이는 보통 %s이고 커피를 먹으면 달라져요." % my_teeth

# 이 줄은 까다롭지만 정확히 따라 하세요.
print "%d, %d, %d를 모두 더하면 %d 랍니다." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)


# 더 해보기 과제.
name = '김준식'
age = 35  # not a lie
height = 188  # cm
weight = 82  # kg
eyes = '파랑'
teeth = '하양'
hair = '갈색'

print "%s에 대해 이야기해 보죠." % name
print "키는 %d 인치고요." % (height / 2.54)
print "몸무게는 %r 파운드예요." % (weight / 0.4536)
print "사실 아주 많이 나가는 건 아니죠."
print "눈은 %s이고 머리는 %s이예요." % (eyes, hair)
print "이는 보통 %s이고 커피를 먹으면 달라져요." % teeth

# 이 줄은 까다롭지만 정확히 따라 하세요.
print "%d, %d, %d를 모두 더하면 %d 랍니다." % (
    age, height, weight, age + height + weight)
