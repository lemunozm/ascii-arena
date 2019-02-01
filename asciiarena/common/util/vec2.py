import enum
import math

class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self, v):
        return Vec2(self.x + v.x, self.y + v.y)


    def __sub__(self, v):
        return Vec2(self.x - v.x, self.y - v.y)


    def __iadd__(self, v):
        self.x = self.x + v.x
        self.y = self.y + v.y
        return self


    def __isub__(self, v):
        self.x = self.x - v.x
        self.y = self.y - v.y
        return self


    def length(self):
        return math.sqrt(self.x**2 + self.y**2)


    @staticmethod
    def distance(v1, v2):
        return (v1 - v2).length()


    @staticmethod
    def empty():
        return Vec2(0, 0)


    @staticmethod
    def up():
        return Vec2(0, 1)


    @staticmethod
    def down():
        return Vec2(0, -1)


    @staticmethod
    def right():
        return Vec2(1, 0)


    @staticmethod
    def left():
        return Vec2(-1, 0)