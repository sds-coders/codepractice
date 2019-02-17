# -*- coding: utf-8 -*-
from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)
# seek(offset) -> Move to new file position.
#       Note that not all file objects are seekable.

def print_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(input_file)

print("파일 전체를 출력해 봅시다.\n")

print_all(current_file)

print("이번에는 테이프처럼 되감아 봅시다.")

rewind(current_file)

print("세 줄을 출력해 봅시다.")

for i in range(0,2):
    print_a_line(i, current_file)