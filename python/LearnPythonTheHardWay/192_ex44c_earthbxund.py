# -*- coding: utf-8 -*-


class Parent(object):

    def altered(self):
        print "부모 altered()"


class Child(Parent):

    def altered(self):
        print "자식, 부모 altered() 호출 전"
        # super를 Child와 self 실행인자로 호출하고, 무엇이 나왔든 그 값에서 altered 함수를 호출한다.
        super(Child, self).altered()
        print "자식, 부모 altered() 호출 후"


dad = Parent()
son = Child()

dad.altered()
son.altered()
