# -*- coding: utf-8 -*-

ten_things = "Apples Oranges Corws Telephone Light Sugar"

print "잠깐, 아직 목록에 10개가 들어있지 않으니 한 번 고쳐 봅시다."

# stuff 리스트는 ten_things 스트링의 ' '를 기준으로 형성됨.
stuff = ten_things.split(' ')  # = split(ten_things, ' ')
more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']

# len을 리스트 대상으로 돌리면 리스트 뜸.
while len(stuff) != 10:
    next_one = more_stuff.pop()  # = pop(more_stuff)
    print "추가: ", next_one
    stuff.append(next_one)  # = append(stuff, next_one)
    print "이제 %d 항목이 있습니다." % len(stuff)
    
print "한 번 볼까요!", stuff

print "이걸로 무언가 해 봅시다."

# stuff[1]이면 'Apples'가 아닌 'Oranges'!
print stuff[1]
# stuff[0]은 'Apples', 거기서 -1하면 맨 끝으로 돌아가서 'Corn'
print stuff[-1]  # 워어, 복잡해?
# 리스트 맨 끝 요소 뽑아버리기~
print stuff.pop()  # = pop(stuff)
# 모든 요소에 스페이스바 끼워넣고 프린트하기~
# 참고로 맨 끝에 corn은 pop되어서 나가리~
print ' '.join(stuff)  # = join(' ', stuff)
# 3에서 '6-1' 사이의 요소들 사이에 #를 끼워버리기~ '분할(slice)' 이라고 합니당.
print '#'.join(stuff[3:6])  # = join('#', stuff[3:6])
