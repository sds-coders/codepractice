# -*- coding: utf-8 -*-

class Other(object):
	
	def override(self):
		print("다른 override()")
		
	def implicit(self):
		print("Different implicit()")
		
	def altered(self):
		print("Diff. altered()")
		

class Child(object):
	
	def __init__(self):
		self.other = Other()
	# Class(child) 'has-a'nother Class(other)
	
	def implicit(self):
		self.other.implicit()
		
	def override(self):
		print("Child override()")
		
	def altered(self):
		print("Child, before calling diff. altered()")
		self.other.altered()
		print("Child, after calling diff. altered()")
		
son = Child()

son.implicit()
son.override()
son.altered()
