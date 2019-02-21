# -*- coding: utf-8 -*-

## Animal은 object의 일종이다(is-a) (네, 조금 헷갈리죠) 추가 점수 부분을 살펴보세요
class Animal(object):
    pass

## Dog는 Animal을 상속했다. Dog는 Animal의 일종이다. is-a
class Dog(Animal):
    
    def __init__(self, name):
        ## Dog는 name을 받는 __init__라는 특성을 가진다. has-a
        self.name = name
        
## Cat는 Animal을 상속했다. Cat는 Animal의 일종이다. is-a
class Cat(Animal):
    
    def __init__(self, name):
        ## Cat는 name을 받는 __init__라는 특성을 가진다. has-a
        self.name = name
        
## Person은 Object의 일종이다. is-a
class Person(object):
    
    def __init__(self, name):
        ## has-a. Person은 name을 받는 __init__이라는 특성을 가진다.
        self.name = name
    
        ## Person은 어떤 종류의 pet을 갖고 있다. (has-a)
        self.pet = None
    
## Employee는 Person의 일종이다. is-a
class Employee(Person):

# 여기랑 73번째 줄 주목해서 볼 것.
    def __init__(self, name, salary):
        ## has-a. 음? 이 마법은 뭐죠? 
        # Person의 Subclass인 Employee에서, super를 사용하면 상위 클라스 Person에서 정보 불러올 수 있음.
        # super를 사용함으로서 class Person에 있던 self.name = name을 안 해도 name입력이 가능.
        # 근데 그럼 Person을 상속하지 않는 건가...? 아.......모르겟다....
        super(Employee, self).__init__(name)
        ## has-a. Employee는 어떤 종류의 salary를 가지고 있다.
        self.salary = salary
    def printer(self):
        print self.name, self.salary


## is-a. Fish는 Object의 일종이다.
class Fish(object):
    pass

## is-a. Salmon은 Fish의 일종이다.
class Salmon(Fish):
    pass

## is-a. Halibut은 Fish의 일종이다.
class Halibut(Fish):
    pass

## rover는 Dog의 일종이다(is-a)
rover = Dog("Rover")

## satan은 Cat의 일종이다(is-a)
satan = Cat("Satan")

## mary는 Person의 일종이다(is-a)
mary = Person("Mary")

## mary는 satan이라는 pet을 가지고 있다(has-a)
mary.pet = satan

## frank는 Employee의 일종이다(is-a). frank는 월급 120000을 갖는다(has-a)
frank = Employee("Frank", 120000)
frank.printer()
print frank.pet

## frank는 rover라는 pet을 가지고 있다(has-a)
frank.pet = rover

## filpper는 fish의 일종이다(is-a)
flipper = Fish()

## crouse는 salmon의 일종이다(is-a)
crouse = Salmon()

## harry는 halibut의 일종이다(is-a)
harry = Halibut()
