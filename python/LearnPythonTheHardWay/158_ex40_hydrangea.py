# -*- coding: utf-8 -*-

# 클래스 정의. 하나의 작은 모듈을 생성.
class Song(object):
    # init__(self, input)에는 반드시 self.input = input를 해 줘야 하는듯.
    # 안그러면 NameError, AttributeError뜸.
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for lines in self.lyrics:
            print lines

# 음...어렵다.
# thing = Class(object) 형식. '인스턴스화' (소형 클래스 모듈 임포트)
# 그 결과 '객체'가 만들어짐.
happy_bday = Song(["생일 축하합니다",
                   "고소 당하기는 싫으니까",
                   "여기서 이만 할게요."])

bulls_on_parade = Song(["조개로 가득 찬 주머니 차고",
                        "가족 주위에 모여든 그들"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

undongsong = Song(["언동이가 제일 좋아",
                   "친구들 모여라",
                   "언제나 ~"])

undongsong.sing_me_a_song()

mysong = Song("love")
mysong.sing_me_a_song()
