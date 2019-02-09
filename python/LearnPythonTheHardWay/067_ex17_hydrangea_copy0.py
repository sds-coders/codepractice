# -*- coding: utf-8 -*-

# ex17을 한 줄로 줄이기.
from sys import argv
from os.path import exists

script, from_file, to_file = argv

# 일단 17단원에서 필수적인 요인들은 모두 여기에 있음.

# 1. 복사의 대상인 from_file을 열고 읽음
## in_file = open(from_file)
## indata = in_file.read()

# 2. 붙여넣기의 대상인 to_file을 '쓰기 모드'로 열고 읽음
## out_file = open(to_file, 'w')
## out_file.write(indata)

# 3. to_file과 from_file을 닫음.
# 근데 to_file의 open상태를 닫네? 여기 좀 헷갈림.
## out_file.close()
## in_file.close()

# 일단 이걸 한 줄로 정리해보자. 

# indata = open(from_file).read()
# open(to_file, 'w').write(indata)

open(to_file, 'w').write(open(from_file).read())
