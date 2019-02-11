# -*- coding: utf-8 -*-

people = 30
cars = 40
buses = 15


if cars > people:
    print("Should get on cars")
elif cars < people:
    print("Shouldn't take cars")
else:
    print("What you gonna do?")
    
if buses > cars:
    print("Too many buses")
elif buses< cars:
    print("Possibly take the buses instead")
else:
    print("still cannot decide")

if people > buses:
    print("Right, Let's take a bus")
else:
    print("Good, then let's stay in home")
    
    
    
# elif : Activated after upper conditional statement turns out to be False, suggests another condition and execute its code if it's true.