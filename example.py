from musicalchipmunks.chipmunk import Chipmunk
from musicalchipmunks.director import Director
from musicalchipmunks.notes import ssh, http
import time

node1 = Chipmunk("Kitchen Lights","192.168.0.101")
node2 = Chipmunk("Garage Door","192.168.0.102")
carbon = Chipmunk(name="Carbon", ip="192.168.0.103", user="uzar", password="passw0rd")
mycroft = Chipmunk(name="Mycroft", ip="192.168.0.104", user="uzar", password="passw0rd")
oxygen = Chipmunk(name="Oxygen", ip="192.168.0.105", user="uzar", password="passw0rd")
helium = Chipmunk(name="Helium", ip="192.168.1.106", user='uzar', password='passw0rd')

basic = http.Basic()
ssh_test = ssh.Ssh()
disk = ssh.Disk()
proc = ssh.Proc()

node1.set_music(basic)
node2.set_music(basic)

carbon.set_music([ssh_test,disk,proc])
mycroft.set_music([ssh_test,disk,proc])
oxygen.set_music([ssh_test,disk,proc])
helium.set_music([ssh_test,disk,proc])

director = Director()

director.append(node1)
director.append(node2)
director.append(helium)
director.append(carbon)
director.append(mycroft)
director.append(oxygen)

while 1:
director.conduct()
	time.sleep(5)

