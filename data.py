from vpython import vec
from vpython import sphere


class GravityObject:
    # def __init__(self, Window, x, y, z, frame_size, name):
    def __init__(self, *args, **kwargs):
        self._mass = 5.972 * 1e24
        self._radius = 6.371 * 1e6
        self._x = args[0]
        self._y = args[1]
        self._z = args[2]
        self._L = args[3]
        self.frame_size = 1
        self.name = "asdf"
        self.ball = sphere(
            pos=self._L*vec(args[0], args[1], args[2]),
            size=vec(self._L/200, self._L/200, self._L/200))
        print("Point created")
        self.tmp_x = args[0]
        self.tmp_y = args[1]
        self.tmp_z = args[2]
        self.meh = False

    def decrementCoordinates(self):
        self.tmp_x /= 2
        self.tmp_y /= 2
        self.tmp_z /= 2

    # @staticmethod
    # def update(*pts):
    #     for i in range(len(pts)):
    #         x = pts[i].x
    #         y = pts[i].y
    #         z = pts[i].z
    #         # print(z)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, z):
        self._z = z
