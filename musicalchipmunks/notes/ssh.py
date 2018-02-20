#import paramiko
import subprocess

class Ssh (object):
	'''
	Tests if ssh is open and working. 
	'''
	def __init__(self):
		pass

	def play(self,chipmunk):
		print("Playing ssh for chipmunk " + chipmunk.name)
		try:
			con = paramiko.SSHClient()
			con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			con.connect(chipmunk.ip,
				username=chipmunk.user,
				password=chipmunk.password,
				look_for_keys=False)
			return True
		except (BadHostKeyException, AuthenticationException, SSHException, socket.error) as e:
			print(e)
		return False


class Disk (object):

	def __init__(self):
		pass

	def play(self,chipmunk):
		print("Playing disk for chipmunk " + chipmunk.name)

class Proc (object):

	def __init__(self):
		pass

	def play(self,chipmunk):
		print("Playing proc for chipmunk " + chipmunk.name)

