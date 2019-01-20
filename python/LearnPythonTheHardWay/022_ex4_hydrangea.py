# -*- coding: utf-8 -*-

cars = 100  # 자동차수
space_in_a_car = 4  # 자동차 1대 안의 공간. *_: 밑줄(underscore)
drivers = 30  # 운전자 수
passengers = 90  # 승객 수
cars_not_driven = cars-drivers  # 운행되지 않는 차 = 자동차수 - 운전자 수
cars_driven = drivers  # 운행되는 차 = 운전자 수
carpool_capacity = cars_driven * space_in_a_car
# 카풀 정원 = 운행되는 차 * 자동차 1대 안의 공간
average_passengers_per_car = passengers / cars_driven
# 차 1대 당 평균 승객 수 = 승각 수 / 운행되는 차


print "자동차", cars, "대가 있습니다."
print "운전자는", drivers, "명 뿐입니다."
print "오늘은 빈 차가", cars_not_driven, "대일 것입니다."
print "오늘은", carpool_capacity, "명을 태울 수 있습니다."
print "함께 탈 사람은", passengers, "명 있습니다."
print "차마다", average_passengers_per_car, "명 정도씩 타야 합니다."

# (+)더해보기 정답
# carpool_capacity != car_pool_capacity. 토씨 하나라도 틀리면 인식 못함.
# 1. space_in_a_car = 4면, 뒤에 .0이 사라짐.
# 2. 부동소수점 : 컴퓨터가 십진수를 인식하는 방법.
# 10(10)=1010(2): 정수부는 2로 나누어 처리, 10.34375(10)=1010.01011(2): 소수부는 2로 곱하여 처리.
# 그렇다면 0.1(10)은? 0.00011011011011........ ->이 때 부동소수점을 이용해 저장.
# 부동소수점: 컴퓨터에서 실수를 표시하는 방법. 소수점은 자유롭게 놓고, 지수와 가수를 이용해 실수를 표현.
# ex) 1010.01101(2)=1.01001101(2) * 2^3

