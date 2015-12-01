class Fighter:
	def __init__(self, arr, name):
		self.superPower = False;
		self.nickname = name;
		self.shots = arr;
		self.lives = 1000;

	def setSuperPower(self):
		if self.shots[9] == 0 and len(self.shots[10]) > 9 and self.shots[10][:9][::-1] == 'mygonhcet':
			self.superPower = True;
		else:
			self.superPower = False;

class Battlefield:
	def __init__(self, Fighter0, Fighter1, Fighter2, Fighter3):
		self.fighters = ([Fighter0, Fighter1, Fighter2, Fighter3])
		
	def fight(self):
		for fighter in self.fighters:
			fighter.setSuperPower()
			if fighter.superPower == True:
				fighter.lives += 100
				print fighter.nickname, ' got SUPER POWER!'
			else:
				print fighter.nickname, ' will fight without super power!'

		round = 0
		while self.fighters[0].lives > 0 or self.fighters[1].lives > 0 or self.fighters[2].lives > 0 or self.fighters[3].lives > 0:
			self.fighters[0].lives -= self.fighters[0].shots[1] + self.fighters[1].shots[1] + self.fighters[2].shots[1] + self.fighters[3].shots[1]
			self.fighters[1].lives -= self.fighters[0].shots[2] + self.fighters[1].shots[2] + self.fighters[2].shots[2] + self.fighters[3].shots[2]
			self.fighters[2].lives -= self.fighters[0].shots[3] + self.fighters[1].shots[3] + self.fighters[2].shots[3] + self.fighters[3].shots[3]
			self.fighters[3].lives -= self.fighters[0].shots[4] + self.fighters[1].shots[4] + self.fighters[2].shots[4] + self.fighters[3].shots[4]

			round += 1
			
			print 'Round #',round, 'score:'
			for fighter in self.fighters:
				 print '\t', fighter.nickname, '\t', fighter.lives
			print '\n'

def display(array):
	for element in array:
		print element

def main():
	antonio = Fighter([6,1,9,8,7,4,3,2,5,0, 'technogym0'], 'antonio')
	paolo = Fighter(  [2,1,9,3,4,7,6,8,5,0, 'technogymLOL'], 'montesel')
	jessica = Fighter([5,1,2,9,3,2,9,0,4,6, ''], 'jessica')
	gomiero = Fighter([5,1,2,3,9,1,7,6,9,0, ''], 'gomiero')
	battle = Battlefield(antonio, paolo, jessica, gomiero)
	battle.fight()

if __name__ == '__main__':
	 main()
