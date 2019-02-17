# -*- coding: utf-8 -*-

## Animal 'is-an' object. Let's see extrapoint part.

##Dog 'is-an' Animal
class Dog(Animal):
	
	def __init__(self,name):
		##Dog 'has-an' __init__/name
		self.name = name

##Cat 'is-an' Animal
class Cat(Animal):
	
	def __init__(self, name):
		##Cat 'has-an' __init__/name
		self.name = name
		
##Person 'is-an' object
class Person(object):
	
	def __init__(self, name):
		## Person 'has-an' __init__/name
		self.name = name
		
		##Person 'has-a' pet
		self.pet = None
		
##Employee 'is-a' Person
class Employee(Person):
	
	def __init__(self, name, salary):
		##Employee has a name???????????????????????????
		super(Employee, self).__init__(name) # 음 이거 Person의 함수 불러오는거일탠데 왜 Employee지 뭐지왜지
		##Employee 'has-a' salary
		self.salary = salary
		
##Fish 'is-an' object
class Fish(object):
	pass

##Salmon 'is-a' Fish
class Salmon(Fish):
	pass

##Halibut 'is-a' Fish, 큰 넙치/광어
class Halibut(Fish):
	pass


##rover 'is-a' Dog 띠용?
rover = Dog("Rover")

##satan 'is-a' Cat
satan = Cat("Satan")

##mary 'is-a' Person
mary = Person("Mary")

##frank 'is-a' Employee who 'has' name, Frank, and salary, 120000
frank = Employee("Frank", 120000)

##frank 'has-a' pet, rover
frank.pet = rover

##flipper 'is-a' Fish
flipper = Fish()

##crouse 'is-a' Salmon
crouse = Salmon()

##harry 'is-a' Halibut()
harry = Halibut()

# Python 3.x : class Myclass(object): - New-style class
#			   class Myclass:		  - New-style class
# Python 2.x : class Myclass(object): - New-style class
# 			 : class Myclass:  		  - Old-style class (Problem!!)
# => Python 3 or higher ver. does not need '(object)' in structure, but recommended to include for compatibility with Python 2.x