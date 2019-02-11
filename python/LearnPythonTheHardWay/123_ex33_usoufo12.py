# -*- coding: utf-8 -*-
    
i=0
numbers = []

while i < 6:
    print("꼭대기에서 i는 %d" % i)
    numbers.append(i)
    
    i += 1
    print("숫자는 이제: ", numbers)
    print("바닥에서 i는 %d" % i)

    
print("Numbers: ")

for num in numbers:
    print(num)
    
def num_tree(n,step):
    
    i=0
    numbers = []
    
    while i < n:
        print("꼭대기에서 i는 %d" % i)
        numbers.append(i)
    
        i += step
        print("숫자는 이제: ", numbers)
        print("바닥에서 i는 %d" % i)
    
print(num_tree(8,2)) # 왜 None 이 나오지???

def num_tree_2(n,step):
    numbers = []
    
    for i in range(0,n,step):
        print("꼭대기에서 i는 %d" % i)
        numbers.append(i)
        
        print("숫자는 이제: ",numbers)
        
        
print(num_tree_2(8,2))
