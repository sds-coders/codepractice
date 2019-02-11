# -*- coding: utf-8 -*-

print("You are in dark room with two doors. Which one do you prefer to enter?(1/2)")

door = int(input(">"))
# 옵션에 없는 인풋 받았을 때 유연하게 대처하기 위해서는 string으로 받는게 더 나을뻔했다
if door == 1:
    print("거대 곰이 치즈 케이크를 먹고 있습니다. 무엇을 할까요?")
    print("1. take the cake away")
    print("2. yell at the bear.")
    
    bear = int(input(">"))
    
    if bear == 1:
        print("The bear ate your head instead. Well done")
    elif bear == 2:
        print("The bear ate your leg instead. Great")
    else:
        print("Well, to take an action'%s' would be better. Bear runs away" % bear)
              
elif door == 2:
    print("You are lookin' in to abysmall C'thulu's 눈동자")
    print("1. Blueberry")
    print("2. Yellow Jacket pins")
    print("3. To understand the meloy a pistol is crying out")
 
    insanity = input(">")
    if insanity == "1" or insanity == "2":
        print("당신의 육체는 젤리푸딩의 마음의 힘으로 살아남습니다. 잘했어요!")
    else:
        print("광기가 당신의 눈을 썩어 문드러진 시궁창으로 만듭니다. 잘했어요!")
 
else:
    print("비틀거리다 발을 헛디뎌 칼날로 떨어져 죽습니다. 잘했어요ㅋ")
    