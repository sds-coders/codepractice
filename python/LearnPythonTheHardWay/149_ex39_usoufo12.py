# -*- coding: utf-8 -*-

# 도 이름에서 약자로의 매핑(mapping)을 만듭니다
states = {
    '충청북도': '충북',
    '경상북도': '경북',
    '전라남도': '전남',
    '경기도': '경기',
    '강원도': '강원'
}

# 기본적인 도와 도시 묶음을 만듭니다.
cities = {
    '전남': '광주',
    '강원': '원주',
    '경북': '대구'
}

# 도시 몇 개를 더 씁니다
cities['경기'] = '수원'
cities['충북'] = '충주'

# 도시를 출력합니다
print('-' * 10)
print("경기도에는", cities['경기'])
print("충청북도에는", cities['충북'])

# 도를 출력합니다
print('-' * 10)
print("강원도의 약자는", states['강원도'])
print("경상북도의 약자는", states['경상북도'])

# 도 이름 사전과 돗 ㅣ사전을 차례로 써 봅니다
print('-' * 10)
print("강원도에는", cities[states['강원도']])
print("경상북도에는", cities[states['경상북도']])

# 도 이름 약자를 모두 출력해 봅니다
print('-' * 10)
for state, abbrev in states.items():
    print("%s의 줄임말은 %s입니다" % (state, abbrev))
#.items() return lists of tuples which consist of key and value.
    
# 도에 있는 도시를 모두 출력해 봅니다
print('-' * 10)
for abbrev, city in cities.items():
    print("%s에는 %s시가 있습니다" % (abbrev, city))
    
# 둘을 한 번에 해봅니다
print('-' * 10)
for state, abbrev in states.items():
    print("%s의 줄임말은 %s이고 %s시가 있습니다" % (state, abbrev, cities[abbrev]))
    
print('-' * 10)
# 없을 수도 있는 도 이름 약자를 안전하게 받아 옵니다
state = states.get('제주도', None) # D.get(k,d) -> D[k] of k in D, else d. d defaults to None.

if not state:
    print("제주도는 없습니다.")

# 도시를 기본값을 넣고 가져 옵니다
city = cities.get('제주', '없습니다')
print("'제주'의 시는 %s" % city)

# 불--편
# Ordered dictionaries are just like regular dictionaries but they remember the order that items were inserted. When iterating over an ordered dictionary, the items are returned in the order their keys were first added
#  class collections.OrderedDict([items])

#    Return an instance of a dict subclass, supporting the usual dict methods. An OrderedDict is a dict that remembers the order that keys were first inserted. If a new entry overwrites an existing entry, the original insertion position is left unchanged. Deleting an entry and reinserting it will move it to the end.

# from https://docs.python.org/3.4/library/collections.html?highlight=ordereddict#collections.OrderedDict