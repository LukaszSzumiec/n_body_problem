from vpython import scene
from vpython import vec
from data import GravityObject
from node import Node
import random


global L
L = 2e7
scene.height = scene.width = 600
scene.range = L
scene.title = "witam serdecznie"
scene.center = vec(0, 0, 0)

balls = []


def generate_points(amount):
    for i in range(0, amount):
        x = random.randrange(-1_000_000, 1_000_000) / 1_000_000
        y = random.randrange(-1_000_000, 1_000_000) / 1_000_000
        z = random.randrange(-1_000_000, 1_000_000) / 1_000_000
        objects.append(GravityObject(x, y, z, L))


objects = []
root = Node(None, 1, 0, "root", True, "none", None)

generate_points(100)
for _object in objects:
    print("test")
    root.insert2(_object)
