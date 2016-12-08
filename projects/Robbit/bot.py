class Robot():
	def __init__(self, head, body):
		self.head = head
		self.body = body

class Head(Robot):
	def __init__(self, brain, eyes, mouth, ears):
		Robot.__init__(self, head, body)
		self.brain = brain
		self.eyes = eyes
		self.mouth = mouth
		self.ears = ears

	def talkHead(self):
		print "My eyes are made of " + self.eyes
		print "My mouth, brought to you by " + self.mouth

class Body(Robot):
	def __init__(self, computer, arms, wheels):
		self.computer = computer
		self.arms = arms
		self.wheels = wheels

	def feelBody(self):
		print "This is my body. I feel it with my arms."


