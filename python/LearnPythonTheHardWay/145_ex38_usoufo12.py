# -*- coding: utf-8 -*-

ten_things = " Apples Oranges Crows Telephone Light Sugar"

print("Moment, there are less than 10 things in the list. Let's add up.")

stuff = ten_things.split() # split() takes the default argument as "' '"
more_stuff = ["Day", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Add up: ", next_one)
    stuff.append(next_one)
    print("%d components now." % len(stuff))
    
print("Now see! ", stuff)

print("이걸로 무언가 해 봅시다.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop()) # pop() takes the default as -1
print(' '.join(stuff)) # It does connect each component in the list orderly by 'self'.
print('#'.join(stuff[3:5]))

# dir() : 인자가 없으면, 현재 지역 스코프에 있는 이름들의 리스트를 돌려줍니다. 인자가 있으면, 해당 객체에 유효한 어트리뷰트들의 리스트를 돌려주려고 시도합니다.