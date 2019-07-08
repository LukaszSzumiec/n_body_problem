import pyglet
from pyglet.gl import *
from pyglet.window import key
from node import Node
from data import Data
import random


class Window(pyglet.window.Window):

        def update(self, time):
            self.clear()
            self.rot_y += 1

        def generate_points(self, amount):

            for i in range(0, amount):
                x = random.randint(0, 600) - 300
                y = random.randint(0, 600) - 300
                z = random.randint(0, 600) - 300
                self.points.append(Data(x, y, z, 300, "jd"))

        def push(self, pos, rot):
            glPushMatrix()

            glRotatef(-rot[0], 1, 0, 0)
            glRotatef(irot[1], 0, 1, 0)
            glTranslatef(-pos[0], -pos[1], -pos[2])

        def Projection(self):
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()

        def Model(self):
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()

        def set3d(self):
            self.Projection()
            gluPerspective(70, self.width/self.height, 0.05, 1000)
            self.Model()

        def set_lock(self, state):
            self.lock = state

        lock = False
        mouse_lock = property(lambda self: self.lock, set_lock)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.points = []
            self.generate_points(5)
            self.set_minimum_size(300, 200)
            self.keys = key.KeyStateHandler()
            self.push_handlers(self.keys)
            pyglet.clock.schedule_interval(self.update, 1/20)
            # self.model = Mod5el
            self.root = Node(None, 300, 0, "root", True, "none", None)
            # if KEY == key.ESCAPE:
            #     self.close()
            # elif KEY == key.E:
            #     self.mouse_lock = not self.mouse_lock
            self.rot_y = 0

        def on_draw(self):
            # self.clear()
            # self.set3d()
            # self.push(asdfsdfasfweafnwerfno)
            # self.model.draw()
            # glPopMatrix()
            pos = [0, 0, -30]

            glPointSize(5)
            self.clear()
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            gluPerspective(90, 10, 0.1, 100)

            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()

            glTranslatef(*pos)
            glRotatef(self.rot_y, 0, 1, 0)

            glBegin(GL_POINTS)
            glVertex3f(-5, -100, 0)
            glVertex3f(5, -5, 0)
            glVertex3f(0, 5, 0)
            glEnd()
            # glBegin(GL_POINTS)
            # Data.update(*self.points)
            # glVertex3f(self.points[0].x, self.points[0].y, self.points[0].z)
            # print("update")
            # glEnd()

            glFlush()
