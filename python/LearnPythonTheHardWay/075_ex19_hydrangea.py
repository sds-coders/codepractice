# -*- coding: utf-8 -*-

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "There are %d slices of cheese!" % cheese_count
    print "There are %d boxes of crackers!" % boxes_of_crackers
    print "It's more than enough to throw a party!"
    print "Please get me a sheet of blanket. \n"
    
print "함수에 그냥 숫자를 직접 줄 수도 있습니다."
cheese_and_crackers(20, 30)

print "스크립트의 변수를 쓸 수도 있고요."
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "안에서 계산을 해도 됩니다."
cheese_and_crackers(10+20, 5+6)

print "합쳐서 변수도 쓰고 계산도 할 수 있습니다."
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# 더해보기.
print "터미널에서 변수 받기"
inputcheese = int(raw_input("치즈 수:"))
inputcrackers = int(raw_input("크래커 수:"))
cheese_and_crackers(inputcheese, inputcrackers)
