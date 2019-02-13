# -*- coding: utf-8 -*-

class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def ext(self, a):
		self.lyrics = self.lyrics.extend(a)
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)
			
happy_bday = Song(["Happy B-day!",
				   "Don't wanna be accused",
				   "I'm done here"])
	
bulls_on_parade = Song(["w/ mini sack full of shell",
					   "가족 주위에 모여든 그들"])

dalla = Song(["People look at me",
			"And they tell me,",
			"얼굴만 보고 날라리 같대요"])

lyric_dalla = ["I love myself",
			  "난 뭔가 달라 달라 yeah"]

dalla2 = Song(lyric_dalla)

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
dalla.sing_me_a_song()
dalla2.sing_me_a_song()

print(dalla.lyrics)
dalla.ext(['1','2'])
print(dalla.lyrics) # Check!
#dalla.sing_me_a_song()