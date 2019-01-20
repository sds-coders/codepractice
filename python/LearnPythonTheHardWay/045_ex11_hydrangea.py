# -*- coding: utf-8 -*-

print "몇 살이죠?",
age = raw_input()
print "키는 얼마죠?",
height = raw_input()
print "몸무게는 얼마죠?",
weight = raw_input()

print "네, 나이는%s 살, 키는%r, 몸무게는%r이네요." % (
    age, height, weight)
print "뜬금없지만, 태양의 각지름은%r 정도입니다." % '''32'10"'''
# 12번 줄의 결과물 : '32\'10"'
# 32\를 32로 띄우려면???
print "뜬금없지만, 태양의 각지름은%s 정도입니다." % '''32'10"'''
# 정답 : %r을 %s로 바꿔 주면 됨. %r은 디버그를 위한 출력법. 따라서 따옴표 안의 '를 \'로 인식.

# 11_2 더해보기
# raw_input(): 문자형 데이터를 입력받을 때 사용(숫자를 넣어도 문자형으로 인식. 1 = '1')
# input(): 숫자형 데이터를 입력받을 때 사용.
# 단, python3에서는 input()이 문자형 데이터를 받는 것으로 통폐합. int()나 float()를 사용해야 함.

# raw_input을 쓰는 다른 방법!
age2 = raw_input("여자친구는 몇 살이죠? ")
height2 = raw_input("여자친구 키는 얼마죠? ")
weight2 = raw_input("그녀 몸무게는 얼마죠? ")
print "네, 그녀 나이는 %r살, 키는 %r, 몸무게는 %r이라고요. 있긴 있어요?" % (
    age2, height2, weight2)
