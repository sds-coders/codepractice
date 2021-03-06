# -*- coding: utf-8 -*-

# 도 이름에서 약자로의 매핑(mapping)을 만듭니다.
states = {
    '충청북도': '충북',
    '경상북도': '경북',
    '전라남도': '전남',
    '경기도': '경기',
    '강원도': '강원'
}

# 기본적인 도와 도시 묶음을 만듭시다.
cities = {
    '전남': '광주',
    '강원': '원주',
    '경북': '대구'
}

# 도시 몇 개를 더 씁니다.
cities['경기'] = '수원'
cities['충북'] = '충주'

# 도시를 출력합니다.
print '-' * 10
print "경기도에는", cities['경기']
print "충청북도에는", cities['충북']

# 도를 출력합니다.
print '-' * 10
print "강원도의 약자는", states['강원도']
print "경상북도의 약자는", states['경상북도']

# 도 이름 사전과 도시 사전을 차례로 써 봅시다.
print '-' * 10
print "강원도에는", cities[states['강원도']]
print "경상북도에는", cities[states['경상북도']]

# 도 이름 약자를 모두 출력해 봅시다.
print '-' * 10
for state, abbrev in states.items():
    print "%s의 줄임말은 %s입니다." % (state, abbrev)

# 도에 있는 도시를 모두 출력해 봅시다.
print '-' * 10
for abbrev, city in cities.items():
    print "%s에는 %s시가 있습니다." % (abbrev, city)

# 둘을 한 번에 해봅시다.
print '-' * 10
for state, abbrev in states.items():
    # list.items(): list of D's (key, value) pairs as 2-tuples
    print "%s의 줄임말은 %s이고 %s시가 있습니다." % (
        state, abbrev, cities[abbrev])

print '-' * 10
# 없을 수도 있는 도 이름 약자를 안전하게 받아 옵니다.
state = states.get('제주도', None)

if not state:
    print "제주도는 없습니다."

# 도시를 기본값을 넣고 가져 옵니다.
city = cities.get('제주', '없습니다')
# D.get(k, [d]) -> D[k] if k in D, else d(default:None)
print "'제주'의 시는 %s" % city

# 좀 더 알아보자.
mydic = {
    '1': 'a',
    '2': 'b',
    '3': 'c'
}  # key : value 형식.

# dic에 key와 value 추가하는 법. dict[k] = v 형식.
mydic[4] = 'd'
print mydic
# items(): dict안의 key-value쌍을 tuple형식으로 묶어서 보여줌.
print mydic.items()
# dict.keys() and dict.values()
print mydic.keys()
print mydic.values()
# dict.get(). key로 value 뽑아내기. 없으면 None 보여줌. 2차 변수로 넣으면 그걸 대신 보여줌.
print mydic.get('1')
print mydic.get('5', 'nothing~')
