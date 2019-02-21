# -*- coding: utf-8 -*-

## Animal은 object의 일종이다 (is-a) (네, 조금 헷갈리죠) 추가 점수 부분을 살펴보세요
class Animal(object):
	pass

## Dog 클래스는 self와 name 매개변수를 받는 __init__을 가졌다 (has-a)
class Dog(Animal)
	def __init__(self, name):
		## self 변수에서 name 속성을 받아 name 값으로 정한다
		self.name = name

## Cat 클래스는 self와 name 매개변수를 받는 __init__을 가졌다 (is-a)
class Cat(Animal):
	
	def __init__(self, name):
		## self 변수에서 name 속성을 받아 name 값으로 정한다
		self.name = name

## Person은 object의 일종이다 (is-a)
class Person(object):

	def __init__(self, name):
		## self 변수에서 name 속성을 받아 name 값으로 정한다
		self.name = name

		## Person은 어떤 종류의 pet을 갖고 있다 (has-a)
		self.pet = None

## Employee 클래스는 self와 name, salary 매개변수를 받는 __init__을 가졌다 (has-a)
class Employee(Person):
	
	def __init__(self, name, salary):
		## ?? 음 이 마법은 뭐죠?
		super(Employee, self).__init__(name)
		## self 변수에서 salary 속성을 받아 salary 값으로 정한다
		self.salary = salary

## Fish는 object의 일종이다 (is-a)
class Fish(object):
	pass

## Salmon은 Fish의 일종이다 (is-a)
class Salmon(Fish):
	pass

## Halibut은 Fish의 일종이다 (is-a)
class Halibut(Fish):
	pass


## rover는 Dog의 일종이다(is-a)
rover = Dog("Rover")

## satan은 Cat의 일종이다(is-a)
satan = Cat("Satan")

## mary는 Mary의 일종이다
mary = Person("Mary")

## mary 변수에서 pet 속성을 받아 satan 값으로 정한다
mary.pet = satan

## frank 변수에서 Employee 함수를 받아 self, Frank, 120000 매개변수를 넣어 호출한다
frank = Employee("Frank", 120000)

## frank 변수에서 pet 속성을 받아 rover 값으로 정한다
frank.pet = rover

## flipper 변수를 Fish 클래스의 인스턴스 하나로 정한다
flipper = Fish()

## crouse 변수를 Salmon 클래스의 인스턴스 하나로 정한다
crouse = Salmon()

## harry 변수를 Halibut 클래스의 인스턴스 하나로 정한다
harry = Halibut()
