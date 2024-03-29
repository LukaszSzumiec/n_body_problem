from vpython import vec
from vpython import sphere


class GravityObject:
    # def __init__(self, Window, x, y, z, frame_size, name):
    def __init__(self, *args, **kwargs):
        # self._radius = 6.371 * 1e6
        self._x = args[0]
        self._y = args[1]
        self._z = args[2]
        self.tmp_x = args[3]
        self.tmp_y = args[4]
        self.tmp_z = args[5]
        self.calc_x = self.tmp_x
        self.calc_y = self.tmp_y
        self.calc_z = self.tmp_z
        self._L = args[6]
        self._is_in_tree = False
        self._mass = args[7]
        self.frame_size = 1
        self.name = args[8]
        if args[7] != 0:
            self.ball = sphere(
                pos=self._L*vec(args[0], args[1], args[2]),
                size=vec(self._L/200, self._L/200, self._L/200))
        print("Point created")
        self.meh = False

    @property
    def mass(self):
        return self._mass

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
