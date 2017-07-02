from sys import exit
from random import randint
class Scene(object):
    def __init__(self):
        pass

    def enter(self):
        pass
class Engine(object):
    def __init__(self,scene_map):
        self.scene_map=scene_map

    def play(self):
        current_scene

class Death(Scene):
    def __init__(self):
        pass
    def enter(self):
        pass

class CentralCorridor(Scene):
    def __init__(self):
        pass
    def enter(self):
        pass

class LaserWeaponArmory(Scene):
    def __init__(self):
        pass
    def enter(self):
        pass

class TheBridge(Scene):
    def __init__(self):
        pass
    def enter(self):
        pass

class EscapePod(Scene):
    def __init__(self):
        pass
    def enter(self):
        pass

class Map(object):
    def __init__(self,start_scene):
        pass

    def next_scene(self,scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
