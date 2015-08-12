'''lab5 2h: Create a boids class with the 
following member variables. velocity, position, speed, direction. 
It should have the ability to print each value as a method of the object. 
For Example: b = Boid() then b.printVelocity() will display [1,1]'''
import math

class Boid:
	def __init__(self, vlc, pos) :
		self.vlc = vlc
		self.pos = pos
	def printVelocity(self):
		return self.vlc
	def printPos(self) :
		return self.pos
	def printDir(self) :
		temp = 0
		temp2 = []
		for v in self.vlc:
			temp += eval("v*v")
		for v in self.vlc:
			temp2.append('v / math.sqr(temp)')
		return temp2
	def newPos(self) :
		temp = []
		for p in self.pos:
			temp.append(eval(self.vlc[(p.count() - 1)])
		return temp
		
	
a = [5,5]
c = [0,0]

b = Boid(a,c)
print b.printPos()
print b.printVelocity()
print b.printDir()
print b.newPos()


