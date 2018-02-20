class Director (object):

	chipmunks = []

	def __init__(self):
		pass

	def append(self,chipmunk):
		self.chipmunks.append(chipmunk)
	
	def conduct(self):
		print("conducting")
		for chipmunk in self.chipmunks:
			chipmunk.play()
