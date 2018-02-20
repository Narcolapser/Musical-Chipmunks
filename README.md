# Musical Chipmunks!

A small and simple library for monitoring your local network. This program was created in response to a problem with existing monitoring applications being a bit to intense. If you want to setup a monitoring system to monitor your 100s or 1000s  of computers and appliancs, try Nagios or Shinken. However if you are trying to monitor 3 computers and a handful of IoT appliances, then this is the program for you!

### Name:

A group of chipmunks is called a band. (Actually, it sounds like it's actually a scurry, but I saw it was a band once and so the name stuck) The nodes of the network are your chipmunks, the system is the director. The director conducts and you make sweet music, assuming everything is going fine.


## Usage

The usage of this was designed to be as simple as possible using a cute analogy of chipmunks and music. No NRPE to install on all your nodes. No complex configuration files. Not sure how to use cron or start Musical Chipmunks as a service? That's fine, this is meant to meet you at your skill level. This program does not have a single executable that you provide a configuration for. Instead the "configuration" so to speak is just a python script.

The first step is to import the parts that you need/want:

    from musicalchipmunks.chipmunk import Chipmunk
    from musicalchipmunks.director import Director
    from musicalchipmunks.notes import ssh, http

You will need the chipmunk and the director in all cases. Notes are your tests. Import the ones that you need. 

Next step is to create your chipmunks:

    node1 = Chipmunk("Kitchen Lights", "192.168.0.101")
    node2 = Chipmunk("Garage Door", "192.168.0.102")
    carbon = Chipmunk(name="Carbon", ip="192.168.0.103", user="user", password="password")
    mycroft = Chipmunk(name="Mycroft", ip="192.168.0.104", user="user", password="password")
    oxygen = Chipmunk(name="Oxygen", ip="192.168.0.105", user="user", password="password")

the chipmunk contains the information unique to the chipmunk. Most of the tests will probably ssh so you probably will just need the user name and password. 

Next step is to prepare the music notes (test):

    basic = http.Basic()
    ssh_test = ssh.Ssh()
    disk = ssh.Disk()
    proc = ssh.Proc()

This is where you will give test specific configurations.

Next you provide your chipmunks with music:

    node1.set_music(basic)
    node2.set_music(basic)

    carbon.set_music([ssh_test,disk,proc])
    mycroft.set_music([ssh_test,disk,proc])
    oxygen.set_music([ssh_test,disk,proc])

Whether you have a single note or a list of notes you can send it to the chipmunk and it will dig it.

Next prepare the director:

    director = Director()

    director.append(node1)
    director.append(node2)
    director.append(carbon)
    director.append(mycroft)
    director.append(oxygen)

Just add the chipmunks to the band and you are ready to go.

Finally you need to ask the director to conduct:

    director.conduct()

This will run all the tests and spit out the results. 
