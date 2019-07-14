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

    def insert2(self, data):

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

        if tmp_x >= 0 and tmp_y >= 0 and tmp_z >= 0:  # FIRST
            print("1")
            case = 1
            self._n_kid_one = self.d(data, 1)
            # self.n_first(data)
            # self.d(data, 1)

        elif tmp_x < 0 and tmp_y >= 0 and tmp_z >= 0:  # SECOND
            print("2")
            case = 2
            self._n_kid_two = self.d(data, 2)
            # self.d(data, 2)
            # self.n_second(data)

        elif tmp_x < 0 and tmp_y < 0 and tmp_z >= 0:  # THIRD
            print("3")
            case = 3
            self._n_kid_three = self.d(data, 3)
            # data = self.a(data)
            # self.n_third(data)
            # self.d(data, case)

        elif tmp_x >= 0 and tmp_y < 0 and tmp_z >= 0:  # FOURTH
            # data = self.a(data)
            print("4")
            case = 4
            self._n_kid_four = self.d(data, 4)
            # self.n_fourth(data)
            # self.d(data, case)

        elif tmp_x >= 0 and tmp_y >= 0 and tmp_z < 0:  # FIFTH
            print("5")
            case = 5
            self._s_kid_one = self.d(data, 5)
            # data = self.a(5data)
            # self.s_first(data)
            # self.d(data, case)

        elif tmp_x < 0 and tmp_y >= 0 and tmp_z < 0:  # 6
            print("6")
            case = 6
            self._s_kid_two = self.d(data, 6)
            # self.s_second(data)
            # data = self.a(data)
            # self.d(data, case)

        elif tmp_x < 0 and tmp_y < 0 and tmp_z < 0:  # SEVENTH
            print("7")
            case = 7
            self._s_kid_three = self.d(data, 7)
            # data = self.a(data)
            # self.s_third(data)
            # self.d(data, case)

        elif tmp_x >= 0 and tmp_y < 0 and tmp_z < 0:  # EIGTH
            print("8")
            case = 8
            self._s_kid_four = self.d(data, 8)
            # data = self.a(data)
            # self.s_fourth(data)
            # self.d(data, case)

    def get_coords(self, tmp):
        frame_size = self.frame_size
        tmpx = tmp - frame_size
        if tmpx < -frame_size or tmpx > frame_size:
            tmpx2 = tmp + frame_size
            return tmpx2
        else:
            return tmpx

    def d(self, data, case):
        # print("TMPX: " + str(tmp_x) + "\n\tTMPY: "
        #       + str(tmp_y) + "\n\t\t\tZ: " + str(tmp_z)
        #       + "\n\t\t\tframe: " + str(self.frame_size))
        tmp = self.get_child
        if tmp is None:
            print("przypadek pierwszy\n\n")
            # self.calculate_center_of_mass(self, data)
            self.gravity_score += 1
            return Node(data, self.frame_size/2, 0,
                        data.name, False, self.name, self)
        elif tmp and tmp._is_hub:
            print("przypadek drugi\n\n")
            # self.calculate_center_of_mass(tmp, data)
            self.gravity_score += 1
            tmp.insert2(data)
            return tmp
        else:
            # self.calculate_center_of_mass(data)
            self.gravity_score += 1
            # if self.is_hub:
            #     self.calculate_center_of_mass(self, data)
            print("przypadek trzeci\n\n")
            tmp_data = self.get_child._data
            temp = self.get_child
            temp._is_hub = True
            temp.name = "HUB"
            # temp._data = None
            temp.insert2(tmp_data)
            temp.insert2(data)
            return temp

# PRZESLAC JAKO ROOOOOOOT
    def calculate_center_of_mass(self, root, data):
        if root._data is None:
            return
        # print(self._data._mass)
        # print(data._mass)
        # print(self.name, "\t\tX: ", self._data._x, "\n\t\t\tY: ", self.is_hub,
        #       self._data._y, "\n\t\t\t\tZ: ", self._data._z)
        m = root._data._mass + data._mass
        print("TEST")

        self._data._x = (root._data._x * root._data._mass
                         + data._x * data._mass) / m
        self._data._y = (root._data._y * root._data._mass
                         + data._y * data._mass) / m
        self._data._z = (root._data._z * root._data._mass
                         + data._z * data._mass) / m

        # print("X: ", x, "\n\tY: ", y, "\n\t\tZ: ", z)
        print(self.name, self.is_hub, "\t\tX: ", self._data._x, "\n\t\t\tY: ",
              self._data._y, "\n\t\t\t\tZ: ", self._data._z)

    def pre_order_traversal(self, root):
        res = []
        if root:
            if root._data is not None:
                print(root.name, root.is_hub, "\t\tX: ", root._data._x, "\n\t\t\tY: ",
                      root._data._y, "\n\t\t\t\tZ: ", root._data._z)
            if root._n_kid_one is not None:
                res = res + self.pre_order_traversal(root._n_kid_one)
            if root._n_kid_two is not None:
                res = res + self.pre_order_traversal(root._n_kid_two)
            if root._n_kid_three is not None:
                res = res + self.pre_order_traversal(root._n_kid_three)
            if root._n_kid_four is not None:
                res = res + self.pre_order_traversal(root._n_kid_four)
            if root._s_kid_one is not None:
                res = res + self.pre_order_traversal(root._s_kid_one)
            if root._s_kid_two is not None:
                res = res + self.pre_order_traversal(root._s_kid_two)
            if root._s_kid_three is not None:
                res = res + self.pre_order_traversal(root._s_kid_three)
            if root._s_kid_four is not None:
                res = res + self.pre_order_traversal(root._s_kid_four)
        return res

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

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

        # def traverse(self):
        #     if self._n_kid_one is not None:
        #         print("n1", self.gravity_score)
        #         self._n_kid_one.traverse()
        #     elif self._n_kid_two is not None:
        #         print("n2", self.gravity_score)
        #         self._n_kid_two.traverse()
        #     elif self._n_kid_three is not None:
        #         print("n3", self.gravity_score)
        #         self._n_kid_three.traverse()
        #     elif self._n_kid_four is not None:
        #         print("n4", self.gravity_score)
        #         self._n_kid_four.traverse()
        #     elif self._s_kid_one is not None:
        #         print("s1", self.gravity_score)
        #         self._s_kid_one.traverse()
        #     elif self._s_kid_two is not None:
        #         print("s2", self.gravity_score)
        #         self._s_kid_two.traverse()
        #     elif self._s_kid_three is not None:
        #         print("s3", self.gravity_score)
        #         self._s_kid_three.traverse()
        #     elif self._s_kid_four is not None:
        #         print("s4", self.gravity_score)
        #         self._s_kid_four.traverse()
        #     else:
        #         print("elo", self.gravity_score)

        # def print2DUtil(self, space):
        #
        #     # if self:
        #     #     arrow = "|\n" \
        #     #         "L>>" + str(self.name)
        #     # # Base case
        #     if self is None:
        #         return
        #     # gap = ''
        #     # for i in range (0, Node.counter):
        #     #     gap = gap.join("\t")
        #     # print(gap.join(self.name))
        #       str(tmpx_plus) + "\n\t\t\tTMPYPLUS: " + str(tmpy_plus) + "\n\t\t\t\tFRAME: " + str(self.frame_size))
        #     #
        # print("TMPXMIN: " + str(tmpx_minus) + "\n\tTMPYMINUS: " + str(tmpy_minus) + "\n\t\tTMPXPLUS: " +
        #     # if self._n_kid_one or self._n_kid_two or self._n_kid_three or self._
        #     # n_kid_four:
        #     #     Node.counter += 1
        #
        #     print(self.name + "\t\t" + self.parent_name)
        #     # Increase distance between levels
        #     space += self.COUNT[0]
        #     self.print2DUtil(self._n_kid_one, space)
        #     self.print2DUtil(self._n_kid_two, space)
        #     self.print2DUtil(self._n_kid_three, space)
        #     self.print2DUtil(self._n_kid_four, space)
        #
        # def display(self):
        #
        #     # space=[0]
        #     # Pass initial space count as 0
        #     self.print2DUtil(self, 0)
    # COUNT = [15]
    #
    # counter = 0
    #
    # @staticmethod
    # def print2DUtil(self, space):
    #
    #     # if self:
    #     #     arrow = "|\n" \
    #     #         "L>>" + str(self.name)
    #     # # Base case
    #     if self is None:
    #         return
    #     # gap = ''
    #     # for i in range (0, Node.counter):
    #     #     gap = gap.join("\t")
    #     # print(gap.join(self.name))
    #     #
    #     # if self._n_kid_one or self._n_kid_two or self._n_kid_three or self._
    #     # n_kid_four:
    #     #     Node.counter += 1
    #
    #     print(self.name + "\t\t" + self.parent_name)
    #     # Increase distance between levels
    #     space += self.COUNT[0]
    #     self.print2DUtil(self._n_kid_one, space)
    #     self.print2DUtil(self._n_kid_two, space)
    #     self.print2DUtil(self._n_kid_three, space)
    #     self.print2DUtil(self._n_kid_four, space)
    #
    # def display(self):
    #
    #     # space=[0]
    #     # Pass initial space count as 0
    #     self.print2DUtil(self, 0)
