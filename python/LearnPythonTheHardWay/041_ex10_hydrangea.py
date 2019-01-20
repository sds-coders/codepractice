# -*- coding: utf-8 -*-

tabby_cat = "\t난 탭이 됨."
persian_cat = "나는\n분리됨"
backslash_cat = "나는 \\ 고 \\ 양이."

fat_cat = """
할 일 목록:
\t* 고양이 밥
\t* 물고기
\t* 개박하\n\t* 오리새
  """

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# 10_2. 뭐야이게! 실행하지 말 것. ㅅㅂ...
#while True:
#    for i in ["/","-","|","\\","|"]:
#        print "%s\r" % i,

fat_cat2 = '''
할 일 목록:
\t* 고양이 밥
\t* 물고기
\t* 개박하\n\t* 오리새
  '''

print fat_cat2

# 10_3. 3/4
# 
a = "ducks"
b = "언동아"
c = "언동안"
d = "金"

print d
print "%r" % d
count_animals = "\n%s\n%s\n%s" % (a, b, c)
print count_animals
count_animals2 = "\n%r\n%r\n%r" % (a, b, c)
print count_animals2
print a
print b
print c
print "%s, %r, %s" % (a, b, c)
