# -*- coding: utf-8 -*-

class Parent(object):
	
	def altered(self):
		print("Parent altered()")
		
class Child(Parent):
	
	def altered(self):
		print("Child, before calling Parent's altered()")
		super(Child, self).altered()
		print("Child, after calling Parent's altered()")
		# super(Child, self): allows you to call methods of the superclass(Parents here) in your subclass(Child here).
		# can also take two parameters: 
		# the first is the subclass - it clarifies the subclass, at the class hierarchy, just below the superclass that has the function you want to take.
		# the second parameter is an object that is an instance of that subclass
		# By including second parameter, super() returns bound method: a method that is bound to the object, which gives the method the object’s context such as any instance attributes. If this parameter is not included, the method returned is just a function, unassociated with an object’s context.
		# super() without any parameter is equivalent to the super function here.
		# The parameterless call to super() is recommended and sufficient for most use cases, and needing to change the search hierarchy regularly could be indicative of a larger design issue.
		# Ref. from < https://realpython.com/python-super/ >

dad = Parent()
son = Child()

dad.altered()
son.altered()