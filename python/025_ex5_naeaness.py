# -*- coding: utf-8 -*-

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 188.0 # cm
height_in_inch = (height / 2.54)
weight = 82.0 # kg
weight_in_pound = weight / 0.4536
eyes = 'Blue'
teeth = 'white'
hair = 'brown'

print "%s, talk about this" % name
print "my height is %dcm" % height
print "my weight is %dkg" % weight
print "my eyes is %s hair is %s." %(eyes, hair)
print "teeth is normally %s it changes when drinks coffee" %teeth

# 이 줄은 까다롭지만 정확히 따라 하세요
print "%d, %d, %d를 모두 더하면 %d랍니다." %(
age, height, weight, age + height + weight)

print "height in pound %r, weight in pound %r" %(height_in_inch, round(weight_in_pound))