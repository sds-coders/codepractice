# -*- coding: utf-8 -*-

formatter = "%s %s %s %s"

print formatter % (1, 2, 3, 4)
print formatter % ("하나", "둘", "셋", "넷")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "난 이게 있죠.",
    "지금 막 써주신 그것.",
    "하지만 '노래'하진 않아요.",
    "그러니까 잘 자요."
)

formatter2 = "%r %r %r %r"
print formatter2 % (
    "I had this thing.",
    "That you coudl type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

# Mistakes I've done
# 1. Omitted quotationmark so that string is not perceived

# Guess what
# The string corresponding to the third formatter of variable formatter2 is printed with double quotation marks to distinguish a single quotationmark in it.