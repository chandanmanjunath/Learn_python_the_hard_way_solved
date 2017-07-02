from sys import exit
class Red():
    def start_method(self):
        print "red"
        return 'green'

class Green():
    def start_method(self):
        print "green"
        return 'yellow'

class Yellow():
    def start_method(self):
        print "yellow"
        exit(1)
class Engine(object):
    def __init__(self,directions_obj):
        self.directions_obj=directions_obj
        #print self.directions_obj.test()

    def play_drive(self):
        present_scene=self.directions_obj.start_room()
        print "present scene",present_scene

        while(True):
           next_scene=present_scene.start_method()
           present_scene=self.directions_obj.next_room_name(next_scene)

class Direction():
    rooms={'red':Red(),
           'green':Green(),
           'yellow':Yellow()}
    def test(self):
        print "hello"

    def __init__(self,start_room_name):
        self.start_room_name=start_room_name

    def next_room_name(self,room_name):
        print "inside next room",room_name
        print  Direction.rooms.get(room_name)
        return Direction.rooms.get(room_name)

    def start_room(self):
        print "inside start_room_name debug",self.next_room_name(self.start_room_name)
        return self.next_room_name(self.start_room_name)



start= Direction('red')
drive= Engine(start)
drive.play_drive()
