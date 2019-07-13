from vpython import scene
from vpython import vec
from data import GravityObject
from node import Node
import lets_calculate_this
import random


theta = 1
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
generate_points(10000)
# objects.append(GravityObject(0.001, 0.001, 0.001, L))
# objects.append(GravityObject(0.200, 0.001, 0.001, L))
# objects.append(GravityObject(0.030, 0.001, 0.001, L))
# objects.append(GravityObject(0.1, 0.001, 0.001, L))
# objects.append(GravityObject(0.5, 0.001, 0.001, L))

for _object in objects:
    root.insert2(_object)

# root.traverse()
