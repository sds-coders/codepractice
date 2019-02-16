# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print("%r 파일을 지우려 합니다." % filename)
print("취소하려면 CTRL-C(^C)를 누르세요.")  # ^C causes'Keyboard Interrupt'
print("진행하려면 리턴을 누르세요.")

input("?")  # presents the string on the shell, while returns nothing.

print("파일 여는 중...")
target = open(filename, 'w')

print("파일 내용을 지웁니다. 안녕히!")
target.truncate() 
# doc.python.org : truncate() which are less frequently used
# its existence does not affect the result, indeed.
print("이제 세 줄에 들어갈 내용을 묻겠습니다.")

line1 = input("1줄: ")
line2 = input("2줄: ")
line3 = input("3줄: ")

print("이 내용을 파일에 씁니다.")

target.write(line1 + '\n' + line2 + '\n' + line3)
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print("마지막으로 닫습니다.")
target.close() # f.close()는 열려 있는 파일 객체를 닫아 주는 역할을 한다. 사실 이 문장은 생략해도 된다. 프로그램을 종료할 때 파이썬 프로그램이 열려 있는 파일의 객체를 자동으로 닫아주기 때문이다. 하지만 close()를 사용해서 열려 있는 파일을 직접 닫아 주는 것이 좋다. 쓰기모드로 열었던 파일을 닫지 않고 다시 사용하려고 하면 오류가 발생.

print("\n 파일에 다음과 같이 입력되었습니다.")
target = open(filename, 'r')
print(target.read())



#                   | r   r+   w   w+   a   a+
# ------------------|--------------------------
# read              | +   +        +        +
# write             |     +    +   +    +   +
# write after seek  |     +    +   +
# create            |          +   +    +   +
# truncate          |          +   +
# position at start | +   +    +   +
# position at end   |                   +   +