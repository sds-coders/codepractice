# -*- coding: utf-8 -*-

class Parent(object):
	
	def override(self):
		print("Parent override()")
		
class Child(Parent):
	
	def override(self):
		print("Child override()")
	# Child overrides 'override()' of Parent!
	
dad = Parent()
son = Child()

dad.override()  # execute Parent.override()
son.override()  # present Child.override()