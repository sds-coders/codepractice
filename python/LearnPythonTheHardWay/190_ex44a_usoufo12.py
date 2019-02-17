# -*- coding: utf-8 -*-

class Parent(object):
	
	def implicit(self):
		print("Parent implicit()")
		
class Child(Parent):
	pass  # Python grammar, which declares the usage of empty block.

dad = Parent()
son = Child()

dad.implicit()
son.implicit()