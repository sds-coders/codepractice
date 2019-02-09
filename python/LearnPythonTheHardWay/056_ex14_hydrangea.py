# -*- coding: utf-8 -*-

# 시작 전에 한 가지 알아낸 점!
# 터미널로 파이썬을 제대로 실행하려면, 먼저 저장을 한 뒤에 실행해야 함.
# 아주 중요!!!!!!!

from sys import argv

script, user_name, user_age = argv
prompt = 'Your Answers = '  # 이렇게 쓰면, raw_input 안의 프롬프트를 일괄적으로 변경 가능. YAY!

print "안녕 %s, 나는 %s 스크립트야." % (user_name, script)
print "너는 %s살이구나. 나보다 훨씬 젊어." % (user_age)
print "몇 가지 질문을 할게."
print "%s, 나를 좋아해?" % user_name
likes = raw_input(prompt)

print "%s, 어디에 살아?" % user_name
lives = raw_input(prompt)

print "무슨 종류의 컴퓨터를 갖고 있어?"
computer = raw_input(prompt)

print """
좋아, 나를 좋아하냐는 질문에는 '%s'.
'%s'에 살아. 헐... 그게 어디야? 듣기만 해도 소름이야...
그리고 '%s' 컴퓨터를 가졌어. 설마 군인은 아니지? 으!
""" % (likes, lives, computer)
