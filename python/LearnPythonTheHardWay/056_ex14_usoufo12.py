# -*- coding: utf-8 -*-

from sys import argv

script, user_name = argv
prompt = '>_ '

print("안녕 %s, 나는 %s 스크립트야." % (user_name, script))
print("몇 가지 질문을 할게.")
print("%s, 나를 좋아해?" % user_name)
likes = input(prompt)

print("%s, 어디에 살아?" % user_name)
lives = input(prompt)

print("무슨 종류의 컴퓨터를 갖고 있어?")
computer = input(prompt)

print("어떤 맥주를 좋아하니, %s?" % user_name)
beer = input(prompt)

print("""
좋아, 나를 좋아하냐는 질문에는 '%s'.
'%s'에 살아. 어딘지는 모르겠지만.
그리고 '%s' 컴퓨터를 가졌어. 멋져
무엇보다도, '%s'를 가장 즐겨마셔.
""" % (likes, lives, computer, beer))
