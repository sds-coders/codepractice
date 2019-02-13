# class X(Y) : X is a Y ( X 클래스라는 Y의 일종을 만든다.)
# class X(object): def__init__(self,J): X 클래스는 self와 J 매개변수를 받는 __init__을 가졌다
# class X(obejct): def M(self,J): X 클래스는 self와 J 매개변수를 받는 M을 가진다. X has a M
# foo = x() : foo 변수를 X클래스의 인슷턴스 하나로 정한다
# foo.M(J) : foo 변수에서 M함수를 받아 self, J매개변수를 넣어 호출한다
# foo.K = Q : foo 변수에서 K속성을 받아 Q 값으로 정한다.

# -*- coding: utf-8 -*-

import random
from urllib import urlopen
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

# 문장을 먼저 연습하고 싶은가
if len(sys.argv) == 2 and sys.argv[1] == "한국어":
	PHRASE_FIRST = True
else:
	PHRASE_FIRST = False

# 웹사이트에서 단어를 불러온다
for word in urlopen(WORD_URL).readlines():
	WORDS.append(word.strip()) # what does .strip() do? It probably remove the blank space at the both sides of the word.
	
def convert(snippet, phrase):
	class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []
	
	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1,3)
		param_names.append(', '.join(random.sample(WORDS,param_count)))
		
	for sentence in snippet, phrase:
		result = sentence[:]
		
		# 가짜 클래스 이름
		for word in class_names:
			result = result.replace("%%%", word, 1)
			
		# 가짜 나머지 이름
		for word in other_names:
			result = result.replace("***",word, 1)
		
		# 가짜 매개변수 목록
		for word in param_names:
			result = result.replace("@@@", word, 1)
			
		results.append(result)
		
	return results

# CTRL-D를 누를 때까지 계속한다
try:
	while True:
		snippets = PHRASES.keys()
		random.shuffle(snippets)
		
		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer = answer, question
				
			print(question)
			
			input(">")
			print("답: %s\n\n" % answer)

except E0FError:
	print("\nBye")