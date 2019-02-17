# -*- coding: utf-8 -*-

# class X(Y) : X is a Y ( X 클래스라는 Y의 일종을 만든다.)
# class X(object): def__init__(self,J): X 클래스는 self와 J 매개변수를 받는 __init__을 가졌다
# class X(obejct): def M(self,J): X 클래스는 self와 J 매개변수를 받는 M을 가진다. X has a M
# foo = x() : foo 변수를 X클래스의 인슷턴스 하나로 정한다
# foo.M(J) : foo 변수에서 M함수를 받아 self, J매개변수를 넣어 호출한다
# foo.K = Q : foo 변수에서 K속성을 받아 Q 값으로 정한다.

import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES ={"class %%%(%%%):":
			"%%% 클래스라는 %%%의 일종을 만든다.", #is-a
			"class %%%(object):\n\tdef __init__(self, ***)" :
			"%%% 클래스는 self와 ***매개변수를 받는 __init__을 가졌다.",#has-a
			"class %%%(object):\n\tdef ***(self,@@@)":
			"%%%클래스는 self와 @@@매개변수를 받는 ***를 가졌다.",
			"*** = %%%()" : 
			"***변수를 %%%클래스의 인스턴스 하나로 정한다",
			"***.***(@@@)":
			"%%% 변수에서 *** 함수를 받아 @@@ 매개변수를 넣어 호출한다.",
			"***.*** = '***'":
			"*** 변수에서 *** 속성을 받아 *** 값으로 정한다."
			}

# 문장을 먼저 연습하고 싶은지 확인
if len(sys.argv) == 2 and sys.argv[1] == "한국어":  # sys.argv에 할당된 리스트의 길이 확인, 2번째 항목값 확인
	PHRASE_FIRST = True
else:
	PHRASE_FIRST = False


for word in urlopen(WORD_URL).readlines():		  
	WORDS.append(word.strip().decode("utf-8")) 
# 사이트의 각 문장들을 항목으로 가지는 리스트의 각 항목들에 대하여 블록코드 실행.
# 블록코드는 각 문장들을 스페이스 단위로 잘라서 나오는 단어들을 WORDS 리스트에 항목추가.
# read() returns a string as a whole, while readlines() returns list that has strings corresponding to each line. It's why this code uses readlines() instead of read()
# strip(char) return a copy of string which is deprived of char. It defaults blankspace(' ').
# It seems better to use split() since the line could consist of more than one word.

def convert(snippet, phrase):
	class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
	other_names = random.sample(WORDS, snippet.count("***"))
	#snippet에 "%%%"가 몇개인지 확인하고, 그 값만큼  words에서 샘플을 뽑고 capitalize해서 리스트로 반환]
	
	results = []
	param_names = []
	
	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1, 3)
		param_names.append(', '.join(random.sample(WORDS,param_count)))
	# snippet의 "@@@"개수 확인하고 블록코드 실행
	# 블록코드는 WORDS에서 1개 또는 2개를 임의로 샘플링하고 ', ' 로 하나의 항목으로 연결시키고, param_names에 추가한다.
	
	for sentence in snippet, phrase: #??
		result = sentence[:]
		# sentence를 복사하여 추가
		
		# 가짜 클래스 이름
		for word in class_names:
			result = result.replace("%%%", word, 1)
			
		# 가짜 나머지 이름
		for word in other_names:
			result = result.replace("***", word, 1)
		
		# 가짜 매개변수 목록
		for word in param_names:
			result = result.replace("@@@", word, 1)
		# result의 "@@@"를 word로 변경.
		# str.replace(old,new,count) : It substitute 'old' in the string with 'new', optionally limited by count.
		results.append(result)
		
	return results
	# %,@,*가 word in given url site로 변경된 result를 results에 저장.
	
# CTRL-D를 누를 때까지 계속한다
try:
	while True:
		snippets = list(PHRASES.keys())
		##Python 3!! dict.keys() method returns 'dict_keys'type result, which is required to trnasformed into list or another datatype according to needs.
		#Returns keys from PHRASE dict.
		
		random.shuffle(snippets)
		#Return shuffled lst
		
		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer = answer, question
				
			print(question)
			
			input(">")
			print("답: %s\n\n" % answer)
	#PHRASES에서 random한 순서로 key-value쌍을 호출, 내부의 @%*를 urlsite의 random word로 바꾸고 값 저장. Q-value, A-key, 정답출력
	#snippet의 항목개수만큼 출력
			
except EOFError:
	print("\nBye")
				  
	# EOFerror : End Of File Error,which occurs when built-in function like input() or raw_input() do not read any data before encountering the end of their input stream.