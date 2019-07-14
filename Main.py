from vpython import scene
from vpython import vec
from data import GravityObject
from node2 import Node
import lets_calculate_this
import random


theta = 0.5
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
        objects.append(GravityObject(x, y, z, L, "."))


# empty_point = GravityObject(0, 0, 0, L, 0, "pusty")
objects = []
root = Node(None, 1, 0, "root", True, "none", None)
# generate_points(10)
objects.append(GravityObject(0.1, 0.001, 0.001, L, 10, "pierwszy"))
objects.append(GravityObject(0.2, 0.001, 0.001, L, 10, "drugi"))
objects.append(GravityObject(0.3, 0.001, 0.001, L, 10, "trzeci"))
# objects.append(GravityObject(0.1, 0.001, 0.001, L, 1e20, "czwarty"))
# objects.append(GravityObject(0.5, 0.001, -0.001, L, 1e20, "piaty"))

for _object in objects:
    root.insert2(_object)

# root.traverse()
root.pre_order_traversal(root)
