# -*- coding: utf-8 -*-

from sys import exit

def gold_room():
    """it requires you to input any number containing 0 or 1 and you should enter less than 50 in order to win the game"""
    print("황금으로 가득 찬 방입니다. 얼마나 가져갈까요?")
    
    next = input(">")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("인간이여, 숫자 쓰는 법부터 배우세요.")
        # It may quit the function with the message?
    if how_much < 50:
        print("좋아, 욕심부리지 않는군요. 당신이 이겼습니다!")
        exit(0)
    else:
        dead("욕심쟁이 얼간이 같으니!")
        
def bear_room():
    print("Here is a bear")
    print("with large amount of honey")
    print("There is another fat bear in front of the door")
    print("How could you move the bears?")
    bear_moved = False
    
    while True:
        next = input("(꿀 뺏기/ 곰 놀리기/ 문 열기)>")
        
        if next == "꿀 뺏기":
            dead("The bear look at you and chop your cheek badly")
        elif next == "곰 놀리기" and not bear_moved:
            print("The bear get away from the door. You may leave safely")
            bear_moved = True
        elif next == "곰 놀리기" and bear_moved:
            dead("You just exasperated the bear and it ate your leg away")
            # Executed when you keep "곰 놀리기" twice.
        elif next == "문 열기" and bear_moved:
            gold_room()
        else:
            print("무슨 말인지 모르겠네요. 선택지 중에 고르세요")
            
def cthulhu_room():
    print("여기에서는 대악마 크툴루를 봅니다.")
    print("He, it, anyway gazes at you and you are getting crazy")
    print("Run away, or I would tear your head apart")
    
    next = input("(달아나기/ 먹기)>")
    
    if "달아나기" in next:
        start()
    elif "먹기" in next:
        dead("음, 맛이 좋군요!")
    else:
        cthulhu_room()
        

def dead(why):
    """It prints out the given message and turn off the game"""
    print(why, "ㅋ")
    exit(0)
# Shouldn't it be defined previously, preceding at least 'gold room'?


def start():
    print("You're in dark, dark room.")
    print("At right side and left side are doors")
    print("Which one would you select?")
    
    next = input("(왼쪽/ 오른쪽)>")
    
    if next == "왼쪽":
        bear_room()
    elif next == "오른쪽":
        cthulhu_room()
    else:
        dead("문 주위에서 맴돌기만하다 굶어 죽었습니다.")
        
start()


# 프로그램 강재종료/ 인자에 따라서 오류여부/종류 특정가능