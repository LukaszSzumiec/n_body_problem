from vpython import vec
from vpython import sphere


class GravityObject:
    # def __init__(self, Window, x, y, z, frame_size, name):
    def __init__(self, *args, **kwargs):
        # self._radius = 6.371 * 1e6
        self._x = args[0]
        self._y = args[1]
        self._z = args[2]
        self._L = args[3]
        self._mass = args[4]
        self.frame_size = 1
        self.name = args[5]
        self.ball = sphere(
            pos=self._L*vec(args[0], args[1], args[2]),
            size=vec(self._L/200, self._L/200, self._L/200))
        print("Point created")
        self.tmp_x = args[0]
        self.tmp_y = args[1]
        self.tmp_z = args[2]
        self.meh = False

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
