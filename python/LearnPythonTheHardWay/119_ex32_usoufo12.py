# -*- coding: utf-8 -*-

the_count = [1, 2, 3, 4, 5]
fruits = ['사과','귤','배','살구']
change = [1, 'ten', 2, 'hundred', 3, 'five hundreds']

# First for statement loops following lists
for number in the_count:
    print("This is %d" % number)
    
# Similar to above
for fruit in fruits:
    print("Fruits: %s" % fruit)
    
# Can mix them up
for i in change:
    print("Changes %s" % i)
    
# Can build up the list, starting from empty list.
elements = []

# Use range function to count from 0 to 5
for i in range(0,6):
    print("append %d to the list." % i)
    #list can understand append
    elements.append(i)
    
# Also print this out
for i in elements:
    print("Element is %d" % i)
    
# range :
# range(start,stop,step) return a list of sequence of integers from start(inclusive) to stop(exclusively) by step

# |  __add__(...)
# |      x.__add__(y) <==> x+y
# |
# |  __contains__(...)
# |      x.__contains__(y) <==> y in x
# |
# |  __delitem__(...)
# |      x.__delitem__(y) <==> del x[y]
# |
# |  __delslice__(...)
# |      x.__delslice__(i, j) <==> del x[i:j]
# |  __eq__(...)
# |      x.__eq__(y) <==> x==y
# |
# |  __ge__(...)
# |      x.__ge__(y) <==> x>=y
# |
# |  __getattribute__(...)
# |      x.__getattribute__('name') <==> x.name
# |
# |  __getitem__(...)
# |      x.__getitem__(y) <==> x[y]
# |  append(...)
# |      L.append(object) -- append object to end
# |
# |  count(...)
# |      L.count(value) -> integer -- return number of occurrences of value
#|
#|  extend(...)
# |      L.extend(iterable) -- extend list by appending elements from the iterable
# |
# |  index(...)
# |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
# |      Raises ValueError if the value is not present.
# |
# |  insert(...)
# |      L.insert(index, object) -- insert object before index
# |
# |  pop(...)
# |      L.pop([index]) -> item -- remove and return item at index #(default last).