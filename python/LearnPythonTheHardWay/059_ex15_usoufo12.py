# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

txt = open(filename)
# open() : open a file using the file() type, returns a file object.
# Preferred way to open a file

print("파일 %r의 내용" % filename)
print(txt.read())
# call the function(method) 'read' in the file object, 'txt', and print the result.

close()
# One should close files before a script ends.

print("파일 이름을 다시 입력해주세요.")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())
close()

# close
# read : read content of the file and can possibly assign the content to the variable
# readline : read a line from the file
# truncate : empty the file
# write(contents) : write a content on the file, It takes string as its argument