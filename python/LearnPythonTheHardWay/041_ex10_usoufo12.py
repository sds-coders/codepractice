# -*- coding: utf-8 -*-

tabby_cat = "\t난 탭이 됨."
persian_cat = "나는\n분리됨."
backslash_cat = "나는 \\ 고 \\ 양이."

fat_cat = '''
할 일 목록:
\t* 고양이 밥
\t* 물고기
\t* 개박하\n\t* 오리새
'''
# Nothing happens to replace double quotation mark to single quotation mark

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

n = 0
while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print("%s\r" % i),
    n += 1
    if n == 5:
        break

while n > 0:
    for i in ["<", ">"]:
        print("%s\r" % i,)
    n -= 1
    