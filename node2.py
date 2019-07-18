import sys
from data import GravityObject

G = 6.67e-11


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

        if self.frame_size < 0.00000000000000000000001:
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

        print(data.tmp_x)
        print(data.tmp_y)
        print(data.tmp_z)
        data.meh = True
        data.tmp_x = tmp_x
        data.tmp_y = tmp_y
        data.tmp_z = tmp_z

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
        if tmpx < - frame_size or tmpx > frame_size:
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
            self.gravity_score += data._mass
            # self.calculate_center_of_mass(self, data)
            # if data._is_in_tree is False:
            return Node(data, self.frame_size/2.0, 0.0,
                        data.name, False, self.name, self)
        elif tmp and tmp._is_hub:
            print("przypadek drugi\n\n")
            self.gravity_score += data._mass
            # self.calculate_center_of_mass(self, data)
            tmp.insert2(data)
            return tmp
        else:
            self.gravity_score += data._mass
            # self.calc_case_3(data)
            # self.calculate_center_of_mass(self, data)
            # if self.is_hub:
            #     self.calculate_center_of_mass(self, data)
            print("przypadek trzeci\n\n")
            # if data._is_in_tree is False:s
            # self.calculate_center_of_mass(tmp, data)
            tmp_data = GravityObject(
                tmp.data.x, tmp.data.y, tmp.data.z,
                tmp.data.tmp_x, tmp.data.tmp_y, tmp.data.tmp_z, tmp.data._L, 10.0, "pierwszy")
            tmp_data.meh = True
            tmp._is_hub = True
            tmp.name = "HUB " + str(case)

            # tmp.data.x = 0.0
            # tmp.data.y = 0.0
            # tmp.data.z = 0.0

            # temp._data = None
            tmp.insert2(tmp_data)
            tmp.insert2(data)
            return tmp

    def calc_force(self, root):

        pass

    #jezeli ramka jest mniejsza niz N polaczyc dwie kulki

    def calculate_EHHHHHHHHHHHHHH(self, root):
        x = 0.0
        y = 0.0
        z = 0.0
        m = 0.0
        print("LECI")
        if root._n_kid_one is not None:
            print("1 jest")
            x += root._n_kid_one._data._x * root._n_kid_one._data._mass
            y += root._n_kid_one._data._y * root._n_kid_one._data._mass
            z += root._n_kid_one._data._z * root._n_kid_one._data._mass
            m += root._n_kid_one._data._mass
        if root._n_kid_two is not None:
            print("2 jest")
            x += root._n_kid_two._data._x * root._n_kid_two._data._mass
            y += root._n_kid_two._data._y * root._n_kid_two._data._mass
            z += root._n_kid_two._data._z * root._n_kid_two._data._mass
            m += root._n_kid_two._data._mass
        if root._n_kid_three is not None:
            print("3 jest")
            x += root._n_kid_three._data._x * root._n_kid_three._data._mass
            y += root._n_kid_three._data._y * root._n_kid_three._data._mass
            z += root._n_kid_three._data._z * root._n_kid_three._data._mass
            m += root._n_kid_three._data._mass
        if root._n_kid_four is not None:
            print("4 jest")
            x += root._n_kid_four._data._x * root._n_kid_four._data._mass
            y += root._n_kid_four._data._y * root._n_kid_four._data._mass
            z += root._n_kid_four._data._z * root._n_kid_four._data._mass
            m += root._n_kid_four._data._mass
        if root._s_kid_one is not None:
            print("5 jest")
            x += root._s_kid_one._data._x * root._s_kid_one._data._mass
            y += root._s_kid_one._data._y * root._s_kid_one._data._mass
            z += root._s_kid_one._data._z * root._s_kid_one._data._mass
            m += root._s_kid_one._data._mass
        if root._s_kid_two is not None:
            print("6 jest")
            x += root._s_kid_two._data._x * root._s_kid_two._data._mass
            y += root._s_kid_two._data._y * root._s_kid_two._data._mass
            z += root._s_kid_two._data._z * root._s_kid_two._data._mass
            m += root._s_kid_two._data._mass
        if root._s_kid_three is not None:
            print("7 jest")
            print(root._s_kid_three._data._x)
            print(root._s_kid_three._data._mass)
            x += root._s_kid_three._data._x * root._s_kid_three._data._mass
            y += root._s_kid_three._data._y * root._s_kid_three._data._mass
            z += root._s_kid_three._data._z * root._s_kid_three._data._mass
            m += root._s_kid_three._data._mass
        if root._s_kid_four is not None:
            print("8 jest")
            x += root._s_kid_four._data._x * root._s_kid_four._data._mass
            y += root._s_kid_four._data._y * root._s_kid_four._data._mass
            z += root._s_kid_four._data._z * root._s_kid_four._data._mass
            m += root._s_kid_four._data._mass
        if root._data is not None:
            print(x)
            print(m)
            if m == 0:
                return root
            print("save jest")
            root._data._x = x / m
            root._data._y = y / m
            root._data._z = z / m
            root._data._mass = m
        return root

    def in_order_traversal(self, root):
        res = []
        if root:
            print("JD")
            if root._n_kid_one is not None:
                res = self.in_order_traversal(root._n_kid_one)
            if root._n_kid_two is not None:
                res = self.in_order_traversal(root._n_kid_two)
            if root._n_kid_three is not None:
                res = self.in_order_traversal(root._n_kid_three)
            if root._n_kid_four is not None:
                res = self.in_order_traversal(root._n_kid_four)
            if root._s_kid_one is not None:
                res = self.in_order_traversal(root._s_kid_one)
            if root._s_kid_two is not None:
                res = self.in_order_traversal(root._s_kid_two)
            if root._s_kid_three is not None:
                res = self.in_order_traversal(root._s_kid_three)
            if root._s_kid_four is not None:
                res = self.in_order_traversal(root._s_kid_four)
            if root._data is not None:
                self.calculate_EHHHHHHHHHHHHHH(root)
                print(root.name, root.is_hub, "\t\tX: ", root._data._x, "\n\t\t\tY: ",
                      root._data._y, "\n\t\t\t\tZ: ", root._data._z)
        return res

    def pre_order_traversal(self, root):
        res = []
        if root:
            if root._data is not None:
                print(root.name, root.is_hub, "\t\tX: ", root._data.x, "\n\t\t\tY: ",
                      root._data.y, "\n\t\t\t\tZ: ", root._data.z, "\n\t\t\t\tframe: ", root.frame_size)

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

        # def print2DUtil(self, space):
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

    # trzeba to skomplikowac na kilka funkcji

    # PRZESLAC JAKO ROOOOOOOT
    #
    # def calc(self, son):
    #     pass
    #
    # def calc_case_3(self, data):
    #     x, y, z, m = 0
    #     if self._n_kid_one.data is not None:
    #         x, y, z, m = self.calc(self._n_kid_one.data)
    #         pass
    #
    # def calculate_center_of_mass(self, root, data):
    #     # if root is None:
    #     #     return
    #     # if root._data is None:
    #     #     return
    #     if self._data is None:
    #         return
    #     if self.gravity_score == 0.0:
    #         return
    #     if data is None:
    #         return
    #     # print(self._data)
    #     if self.data.x == data.x:
    #         return
    #     # print(data._mass)
    #     # print(self.name, "\t\tX: ", self._data._x, "\n\t\t\tY: ", self.is_hub,
    #     #       self._data._y, "\n\t\t\t\tZ: ", self._data._z)
    #     # print("mass: ", self.gravity_score)
    #     # print("TEST")
    #     # print("framesize: ", self.frame_size)
    #     # print(self.name, self.is_hub, "\t\tX: ", self._data.calc_x, "\n\t\t\tY: ",
    #     #       self._data.calc_y, "\n\t\t\t\tZ: ", self._data.calc_z, "\n")
    #
    #     self._data.x = (root._data.x * root._data._mass
    #                     + data.x * data._mass) / self.gravity_score
    #
    #     self._data.y = (root._data.y * root._data._mass
    #                     + data.y * data._mass) / self.gravity_score
    #
    #     self._data.z = (root._data.z * root._data._mass
    #                     + data.z * data._mass) / self.gravity_score
    #     print("\n\t\t\t\tX: ", self.data.x)
    #     print("\n\t\t\t\t\tmass: ", self.data.mass)
    #     print("\n\t\t\t\t\t\tData X: ", data.x)
    #     print("\n\t\t\t\t\t\t\tdata mass: ", data.mass)
    #     print("\n\t\t\t\t\t\t\t\tgravity score: ", self.gravity_score)
    #
    #     # self.data.x = self.data.x * self.data.mass + data.x * data._mass
    #     # self.data.x /= self.gravity_score
    #
    #     # print("X: ", x, "\n\tY: ", y, "\n\t\tZ: ", z)
    #     # div = 1_000_000_000
    #     # print(self.name, self.is_hub, "\t\tX: ", self._data._x, "\n\t\t\tY: ",
    #     #       self._data._y, "\n\t\t\t\tZ: ", self._data._z)
