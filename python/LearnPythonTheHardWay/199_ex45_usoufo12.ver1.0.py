# -*- coding:utf-8 -*-

from sys import exit
import random
import time
from datetime import datetime

def record_n_rank(name, time, record):
	
	"""if a 'game_usr_record.txt' file does not exist, create the file. add up the given data with current time information. Then, it reads all data in the file and sort them in increasing order of length of time spend in the game. Storing the data as a form of dictionary and list, it clears the existing file and write down the data in dictionary. it reads the file and show data with the number indicating the ranking of the user."""
	
	with open('game_usr_record.txt','a+') as usr_record:
		date = datetime.today().strftime("%Y/%m/%d-%H:%M:%S")
		line = "%s \t %d \t %d \t %s \n" % (name, time, record, date)
		usr_record.write(line)
	
	with open('game_usr_record.txt','r') as usr_record:
		time_n_rest = {}
		for line in usr_record:
			(name1, record_time1, record1, time1) = line.split(" \t ")
			time_n_rest[record_time1] = [name1, record1, time1]
			print(time_n_rest)				#테스트용
			# 변수이름 중복될까봐 뒤에 1 붙였는데 namespace가 안겹쳐서 상관없으려나?!?!
		lst = sorted(time_n_rest)			
		print(lst, "in the loop")			#테스트용
		print(lst)								#테스트용
			
	with open('game_usr_record.txt','w') as usr_record:
		for i in range(0,len(lst)):
			usr_record.write(time_n_rest[lst[i]][0] + " \t " + lst[i] + " \t " + time_n_rest[lst[i]][1] + " \t " + time_n_rest[lst[i]][2] + "\n")
			

	print("\t  순위 | 이름 | 플레이 시간 | 이동한 방의 개수 | 등록된 일시")
	with open('game_usr_record.txt','r') as usr_record:
		n = 0
		for line in usr_record:
			n += 1
			print("\t[" + str(n) + "]    " + line)

class Engine(object):
	
	def __init__(self, level = 1 ):
		print("게임을 시작합니다!!!!")
		self.scene_map = Map('central_corridor', level)
		# Map 인스턴스의 인자로 초기화면 설정!
			
	def play(self):
		print("우주선에 외계인이 침략했고, 우리 영웅은 방으로 이어진 미로를 통과해 싸워 이겨 나가면서")
		print("행성으로 낙하할 수 있는 구명정으로 탈출해야합니다. 문제들을 풀어서 외계인들에게 이길 수")
		print("있어요. 살아나가기를 기원합니다. 굿 럭.")
		
		record = 0
		start_time = time.time()
		on = True
		
		while on:
			
			print("\n"+"-"*50)
			print("<\t %d번째 방 \t>" % (record + 1))
			self.scene_map.current_scene.print_message()
			
			self.scene_map.current_scene_str = self.scene_map.current_scene.enter()
			# This code execute the characteristic function of each class and get info. to which scene you will move next.
			
			if self.scene_map.current_scene_str == "the_end":
				print("이제 외계인은 그만!!")
				on = False
			else:
				self.scene_map.current_scene = self.scene_map.scene[self.scene_map.current_scene_str]
				print("다음 방은 %s 입니다!" % self.scene_map.current_scene_str)
				print("다음 방으로 이동중입니다" + "\n."*3)
				
			record += 1
				
			time.sleep(random.randint(1,4))
			
		end_time = time.time()
		record_time = int(end_time - start_time)
		#소수점 1자리까지 살리고싶은데 방법이 없을까??
		
		
		print("축하합니다, 탈출하셨군요! \n 당신의 기록은 %d회, %d sec(s) 입니다" % (record, record_time))
		
		self.scene_map.current_scene.initialize()
		# Since the Scene.prob2 might be modified while progressing the program, set the value back to its initial state.
		
		if input("기록을 등록하고 랭킹을 확인하겠습니까? (y/n)") == "y":
			nm = input("이름과 함께 등록하세요")
			
			record_n_rank(nm, record_time, record)
			
			
class Scene(object):
	prob1 = 3	#30
	prob2 = 5	#45
	prob3 = 100	#40
	def __init__(self,level = 1):
		"""Given level value, __init__ form the question set and adjust probabilities used in game in accordance to the level"""
		self.qna = {
		"1번 문제" : "1번 답",
		"2번 문제" : "2번 답",
		"3번 문제" : "3번 답",
		"4번 문제" : "4번 답",
		"5번 문제" : "5번 답",
		}
		self.qna1 = {
				"5번 문제" : "5번 답",
				"6번 문제" : "6번 답",
				"7번 문제" : "7번 답",
				"8번 문제" : "8번 답",
				"9번 문제" : "9번 답",
				"10번 문제" : "10번 답"
			}
		self.qna2 ={
				"11번 문제" : "11번 답",
				"12번 문제" : "12번 답",
				"13번 문제" : "13번 답",
				"14번 문제" : "14번 답",
				"15번 문제" : "15번 답",
				"16번 문제" : "16번 답",
				"17번 문제" : "17번 답",
				"18번 문제" : "18번 답"
			}
			
		if level == 2:
			Scene.prob1 = 40
			Scene.prob3 = 30
			
			self.qna.update(self.qna1)
			
		elif level == 3:
			Scene.prob1 = 50
			Scene.prob3 = 20
			self.qna.update(self.qna1)
			self.qna.update(self.qna2)
		
		# 테스트용
		print(level)
		print(Scene.prob1, " ", Scene.prob2, " ", Scene.prob3)
		print(self.qna)
		# 테스트
		
	def initialize(self):
		Scene.prob2 = 45
		print(Scene.prob2)
		
	def next(self,val):
		if val <= Scene.prob1:
			return "central_corridor"
		elif val <= Scene.prob2 + Scene.prob1 :
			return "the_bridge"
		elif val <= 98 :
			return "laser_weapon_armory"
		else:
			return "escape_pod"
		
	def enter(self):
		pass
	
	message = " "
	def print_message(self):
		print("와우, %s" % self.message)


class CentralCorridor(Scene):
	num_of_aliens = random.randint(1,4)
	message = "당신은 지금 중앙복도에 있습니다. 외계인이" + str(num_of_aliens) + "마리 있네요.\n외계인들을 전부 물리쳐야 다음방으로 넘어갈 수 있습니다.\n외계인은 자신이 낸 문제를 맞추는 사람이 있으면 화가나서 죽습니다.\n외계인이 내는 문제들을 맞춰 무사히 다음방으로 넘어가세요!"
	line_aliens = ["뀨","규","뀨뀨"]
	
	def enter(self):
		for i in range(0, self.num_of_aliens):
			
			qst = random.sample(self.qna.keys(), 1)[0]		# random.sample() returns list, so indexing is needed here.
			print(qst)
			ansr = self.qna[qst]
			usr_ansr = input(random.sample(self.line_aliens, 1)[0] + "! " + qst  + "\n >")
			
			if usr_ansr != ansr:
				death()
			
		next_scene = self.next(random.randint(1,100))
		self.num_of_aliens = random.randint(1,4)
		# 다음번 화면 호출 때는 외계인의 수가 바뀌도록..
		# 없으면 계속 똑같은 수만 나옴!
		#instance variable이든, class variable이든 상관없을것같으니 안헷갈리게 instance variable로 쓰자. 
		return next_scene

	
class TheBridge(Scene):
	
	message = "외계인이 다리를 막고있네요. \n \
	외계인을 물리치고 다리를 건너야 계속 진행할 수 있습니다. \n \
	다리를 지나갈 때 폭탄을 설치해서 다리를 폭파시킬 수 있습니다. \n \
	폭파시킨 다리는 더이상 쓰이지 않기때문에 당신이 길을 찾고 탈출할 확률이 올라갑니다."
	line_aliens = ["뀨","규","뀨뀨"]
	
	def enter(self):
		qst = random.sample(self.qna.keys(), 1)[0]
		ansr = self.qna[qst]
		usr_ansr = input(random.sample(self.line_aliens, 1)[0] + "!" + qst + "\n>")
			
		if usr_ansr != ansr:
			death()
		else:
			next_scene = self.next(random.randint(1,100))
		
		if input("다리에 폭탄을 설치하여 파괴하겠습니까? (y/n)") == "y":
			print(Scene.prob2)	#테스트용
			if Scene.prob2 > 0 :
				Scene.prob2 -= 2
				print(Scene.prob2)	#테스트용
		# prob2는 TheBridge가 호출될 확률을 나타내고, 폭탄을 설치할때마다 줄여서 게임이 너무 오래걸리지 않을 수 있도록!
		# 다음 방을 결정하는 next함수는 Scene을 상속한 모든 인스턴스에서 호출되니까, next 함수에서 중요한 변수인 prob2의 변경이 모든 인스턴스에 적용될 수 있게
		# class variable 을 선언해주자!
		return next_scene
			
	
class LaserWeaponArmory(Scene):
	
	message = "무기고.비밀번호를 맞춰서 무기를 꺼낼 수 있습니다. \n \
	비밀번호는 세자리의 자연수이고 중복되는 숫자는 없습니다. \n \
	룰은 숫자야구와 같으며, 추가적으로 10번 이내로 맞춰야합니다. \n \
	10번 초과시 무기고의 보안시스템이 발동하여 더이상 입력할 수 없게되고 다른 방으로 이동합니다. \n \
	< B는 볼, S는 스트라이크 >"
	
	def __init__(self,level):
		"""랜덤한 비밀번호 생성, 이 함수는 게임도중에 다시 호출되지 않으므로 비밀번호는 그대로 간다."""
		super().__init__(level)
		self.factor = random.sample(range(0,10),3)
		self.password = "%d%d%d" % (self.factor[0], self.factor[1], self.factor[2])
		# when an integer needed, ( 100 * self.factor[0] ) + ( 10* self.factor[1]) + self.factor[2]
				
	def enter(self):
		n = 0
		print(self.password)														# 테스트용
		while n<10:
			n += 1
			usr_ansr = input("Password : _ _ _" + " \t < %d번째 시도>" % n + "\n > ")
			#이게 스트링으로 반환되던가 정수로 반환되던가,, 에 따라서 else 안의 코드스위트값에  str함수 필요없음!
			
			if usr_ansr == self.password:
				print("축하- 무기 획득-! 외계선들을 다 부수고 구명정으로 이동합니다")
				next_scene = "escape_pod"
				break
			else:
				
				S = 0
				B = 0
				
				for i in usr_ansr:
					if i in self.password:
						if usr_ansr.index(i) == self.password.index(i):
							S += 1
						else:
							B += 1
				# 입력한 숫자가 비밀번호에 존재하는지 확인하고, 인덱싱으로 확인한 위치까지 일치하면 S증가, 위치가 일치하지않으면 B증가.	
				print("땡! " + usr_ansr + "  < B: %d, S: %d > " % (B,S))
		
		if n == 10:
			print("으억 외계인이 너무 가까이왔어요, 이제 도망가야해용")
			next_scene = self.next(random.randint(1,100))
				
		return next_scene
		
		
class EscapePod(Scene):
	
	message = "구명정을 선택하세요. 고장난 구명정으로는 탈출할 수 없습니다.\n \
	외계인들의 훼손으로 구명정의 " + str(Scene.prob3) + "% 만이 멀쩡합니다. \n \
	아니, 뒤에서 외계인들이 쫓아오고있네요! 구명정 한대의 시동을 걸 시간밖에 없습니다. \n \
	서둘러서 고르세요!"
	
	def enter(self):
		input("몇 번 구명정을 고르시겠습니까?(001~100번) > ")
		
		if random.randint(1,100) < Scene.prob3:
			next_scene = "the_end"
			
		else:
			print("오 이런,, 고장난 구명정이에요,, ㅋ,, 외계인에게 붙잡히기 전에 빠르게 다음 방으로 이동하세요!")
			next_scene = self.next(random.randint(1,100))
			
		return next_scene
			
	
def death():
	
	"""랜덤한 메세지 출력"""
	
	message_list = ["앙","앙앙","%깃"]
	message = random.sample(message_list,1)[0]
	print(message)
	exit(1)

				
class Map(object):
	
	def __init__(self, initial_scene, level):
		
		self.scene = {
		'central_corridor' : CentralCorridor(level),
		'laser_weapon_armory' : LaserWeaponArmory(level),
		'the_bridge' : TheBridge(level),
		'escape_pod' : EscapePod(level),
		}
		
		self.current_scene_str = initial_scene
		print(initial_scene)
		self.current_scene = self.scene[initial_scene]
		print("지도 생성중 \n. \n. \n.")
	
	def next_scene(self, scene_name):
		pass
	
	
a_game = Engine(1)
a_game.play()
	