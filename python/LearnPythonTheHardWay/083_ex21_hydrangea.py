# -*- coding: utf-8 -*-

def add(a, b):
    print "덧셈 %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "뺄셈 %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "곱셈 %d X %d" % (a, b)
    return a * b

def divide(a, b):
    print "나눗셈 %d %% %d" % (a, b)
    return a / b

print "함수만으로 계산해 봅시다!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "나이: %d, 키: %d, 몸무게: %d, IQ: %d" % (age, height, weight, iq)

# 추가 점수 문제. 일단 써 보세요.
print "문제가 있어요."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "결과:", what, "손으로 계산할 수 있나요?"

# return이 있냐 없냐의 차이는 여기서 나타남. 잘 볼 것!
def add2(a, b):
    print a + b
    
def subtract2(a, b):
    print a - b
# 여기까지는 똑같이 덧셈과 뺄셈의 기능을 지니는 것 같이 보임. 하지만...
## l = add2(1, 2)
## p = subtract2(2, 1)
## print "결과: ", l + p
# 함숫값을 출력할 수만 있고, 파이썬 내부에서 가지고 있지는 않음.
# 따라서 l과 p는 아무 정보도 가지지 않음.

# 응용2. what2
print "===========응용문제: what2=========="
(30 + 78 * 45) / 300 - 40
what2 = divide((add(30, multiply(78, 45))), subtract(300, 40))
print what2, ">> return이라는 기능이 있기 때문에 함수에 변수만 잘 넣어주면 알아서 결과를 출력함!"