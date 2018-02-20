class Chipmunk (object):

	def __init__(self,name,ip,**kwargs):
		self.name = name
		self.ip = ip
		if kwargs is not None:
			for key, value in kwargs.iteritems():
#				print "%s == %s" %(key,value)
				setattr(self,key,value)
#		for item in dir(self):
#			print(item,getattr(self,item))

	def set_music(self,notes):
		if isinstance(notes,list):
			self.notes = notes
		else:
			self.notes = [notes]
	
	def play(self):
		for note in self.notes:
			print("Testing: " + str(type(note)) + " for " + self.name + " is: " + str(note.play(self)))
