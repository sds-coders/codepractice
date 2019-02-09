# -*-coding: utf-8 -*-

cars = 100
# 차라는 변수를 선언하고 값을 대입
space_in_a_car = 4.0
# 차에 남은 공간 변수를 선언하고 소수점을 기입하여 부동소수점을 표시
drivers = 30
# 운전자 변수 선언 및 값 대입
passengers = 90
# 승객 변수 선언 및 값 대입
cars_not_driven = cars - drivers
# 운전되지 않는 차 변수 선언 및 값 정의(변수간의 차잇값)
cars_driven = drivers
# 값 선언, 운전되는 차의 대수는 운전자의 수와 같다.
carpool_capacity = cars_driven * space_in_a_car
# 차에 남은 공간 곱하기 운행중인 차량 대수를 하여 카풀 용량을 표시
average_passengers_per_car = passengers / cars_driven
# 차마다 타야 하는 사람의 숫자는 승객 수 나누기 운행중인 차량의 수

print "자동차", cars, "대가 있습니다."
print "운전자는", drivers, "명 뿐입니다."
print "오늘은 빈 차가", cars_not_driven, "대일 것입니다."
print "오늘은", carpool_capacity, "명을 태울 수 있습니다."
print "함께 탈 사람은", passengers, "명 있습니다."
print "차마다", average_passengers_per_car, "명 정도씩 타야 합니다."

# 값의 출력

# 이 아래는 더 해보기와 자주 묻는 질문의 테스트입니다.
test = cars_driven == drivers
print test
print"여러분 %s 안녕" % "모두"


