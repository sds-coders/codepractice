# -*- coding: utf-8 -*-

from sys import argv

script, first, second, third = argv

fourth = input("Type the fourth argument: ")

print("스크립트 이름:"), script
print("첫 번째 변수:"), first
print("두 번째 변수:"), second
print("세 번째 변수:"), third
print("네 번째 변수:"), fourth

# argv : argument variable/ it contains transmitted 
# information(argument variable) when a script is executed:
# when user typed python ex13.py 1 2 3 , it returns argv as ('ex13.py', '1', '2', '3')

# Python 3, like Python2, does not require a command 'print' paranthesis when its argument is variable.