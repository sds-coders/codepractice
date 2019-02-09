# -*- coding: utf-8 -*-

formatter = "%s %s %s %s"

print formatter % (1, 2, 3, 4)
print formatter % ("하나", "둘", "셋", "넷")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "난 이게 있죠.",
    "지금 막 써 주신 그것.",
    "하지만 '노래'하진 않아요.",
    "그러니까 잘 자요."
)  # 반점 빼먹지 않기. 안그러면 TypeError 발생

formatter2 = "%r %r %r %r"
print formatter2 % (  # 'formatter' 오타 주의!
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

# %s와 %r에 따라 결과가 다름. 
# %s는 문자열을 출력. %r은 무엇이든 모두 출력.
# 책에선, %r은 디버그 정보를 얻기 위해서만 써야 한다고 함. 
# '프로그래머를 위한 그대로인' 버전으로 보여줌. ...뭐 그렇대. 알아만두자
