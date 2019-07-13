import sys


class Node:
    def __init__(self, *args, **kwargs):
        self.parent = args[6]
        self._n_kid_one = None  # First quarter of coord system UP
        self._n_kid_two = None  # Second
        self._n_kid_three = None  # Third
        self._n_kid_four = None  # Forth

        self._s_kid_one = None  # First quarter of coord system DOWN
        self._s_kid_two = None  # Second
        self._s_kid_three = None  # Third
        self._s_kid_four = None  # Forth

        self._is_hub = args[4]
        self.parent_name = args[5]
        self._data = args[0]  # Data of node

        self._gravity_score = args[2]  # Wage
        self.frame_size = args[1]
        self.name = args[3]

    def insert1(self, data):

        if self.frame_size < 0.000000001:
            print("ERROR" + self.name)
            sys.exit(0)

        global tmp_x
        global tmp_y
        global tmp_z
        global case

        if data.meh:
            tmp_x = self.get_coords(data.tmp_x)
            tmp_y = self.get_coords(data.tmp_y)
            tmp_z = self.get_coords(data.tmp_z)
        else:
            tmp_x = data.tmp_x
            tmp_y = data.tmp_y
            tmp_z = data.tmp_z
        data.meh = True

        data.tmp_x = tmp_x
        data.tmp_y = tmp_y
        data.tmp_z = tmp_z

        if self._n_kid_one is None:
            print("kid one is none")
        # print("\n\nTMPX: " + str(tmp_x) + "\n\tTMPY: "
        #       + str(tmp_y) + "\n\t\t\tZ: " + str(tmp_z)
        #       + "\n\t\t\tframe: " + str(sel5f.frame_size))
            # print("\n\n\n")

        if tmp_x >= 0 and tmp_y >= 0 and tmp_z >= 0:  # FIRST
            print("1")
            case = 1
            self._n_kid_one = self.d(data, 1)
            # self.n_first(data)

        elif tmp_x < 0 and tmp_y >= 0 and tmp_z >= 0:  # SECOND
            print("2")
            case = 2
            self._n_kid_two = self.d(data, 2)
            # self.n_second(data)

        elif tmp_x < 0 and tmp_y < 0 and tmp_z >= 0:  # THIRD
            print("3")
            case = 3
            self._n_kid_three = self.d(data, 3)
            # data = self.a(data)
            # self.n_third(data)

        elif tmp_x >= 0 and tmp_y < 0 and tmp_z >= 0:  # FOURTH
            # data = self.a(data)
            print("4")
            case = 4
            self._n_kid_four = self.d(data, 4)
            # self.n_fourth(data)

        elif tmp_x >= 0 and tmp_y >= 0 and tmp_z < 0:  # FIFTH
            print("5")
            case = 5
            self._s_kid_one = self.d(data, 5)

            # data = self.a(5data)
            # self.s_first(data)

        elif tmp_x < 0 and tmp_y >= 0 and tmp_z < 0:  # 6
            print("6")
            case = 6
            self._s_kid_two = self.d(data, 6)
            # self.s_second(data)
            # data = self.a(data)

        elif tmp_x < 0 and tmp_y < 0 and tmp_z < 0:  # SEVENTH
            print("7")
            case = 7
            self._s_kid_three = self.d(data, 7)
            # data = self.a(data)
            # self.s_third(data)

        elif tmp_x >= 0 and tmp_y < 0 and tmp_z < 0:  # EIGTH
            print("8")
            case = 8
            self._s_kid_four = self.d(data, 8)
            # data = self.a(data)
            # self.s_fourth(data)

    def get_coords(self, tmp):
        frame_size = self.frame_size
        tmpx = tmp - frame_size
        if tmpx < -frame_size or tmpx > frame_size:
            tmpx2 = tmp + frame_size
            return tmpx2
        else:
            return tmpx

    @property
    def get_child(self):
        if case == 1:
            return self._n_kid_one
        elif case == 2:
            return self._n_kid_two
        elif case == 3:
            return self._n_kid_three
        elif case == 4:
            return self._n_kid_four
        elif case == 5:
            return self._s_kid_one
        elif case == 6:
            return self._s_kid_two
        elif case == 7:
            return self._s_kid_three
        elif case == 8:
            return self._s_kid_four
        else:
            print("\n\nINVALID ARG\n\n")

    def d(self, data, case):
        print("TMPX: " + str(tmp_x) + "\n\tTMPY: "
              + str(tmp_y) + "\n\t\t\tZ: " + str(tmp_z)
              + "\n\t\t\tframe: " + str(self.frame_size))
        if self.get_child is None:
            print("przypadek pierwszy\n\n")
            return Node(data, self.frame_size/2, self.gravity_score, data.name,
                        False, self.name, self)

        elif self.get_child and self.get_child.is_hub:
            print("przypadek drugi\n\n")
            return self.get_child.insert1(data)
        else:
            print("przypadek trzeci\n\n")
            tmp = self.get_child._data
            print(self.get_child.name)
            return self.get_child.insert1(tmp), self.get_child.insert1(data)

    @property
    def gravity_score(self):
        return self._gravity_score

    @gravity_score.setter
    def gravity_score(self, value):
        self._gravity_score = value

    @property
    def is_hub(self):
        return self._is_hub

    @is_hub.setter
    def is_hub(self, value):
        self._is_hub = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
