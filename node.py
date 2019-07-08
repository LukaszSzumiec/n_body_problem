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

        self.is_hub = args[4]
        self.parent_name = args[5]
        self._data = args[0]  # Data of node
        self._gravity_score = args[2]  # Wage
        self.frame_size = args[1]
        self.name = args[3]

    def insert2(self, data):

        if self.frame_size < 0.001:
            print("ERROR" + self.name)
            sys.exit(0)

        if data.meh:
            tmp_x = self.get_coords(data.tmp_x)
            tmp_y = self.get_coords(data.tmp_y)
            tmp_z = self.get_coords(data.tmp_z)
        else:
            tmp_x = data.tmp_x
            tmp_y = data.tmp_y
            tmp_z = data.tmp_z
        data.meh = True
        self.gravity_score += 1
        # print("TMPXMIN: " + str(tmp_x) + "\n\tTMPYMINUS: " + str(tmp_y) + "\n\t\t\t\tFRAME: " + str(self.frame_size))

        # print("TMPXMIN: " + str(tmpx_minus) + "\n\tTMPYMINUS: " + str(tmpy_minus) + "\n\t\tTMPXPLUS: " +
        #       str(tmpx_plus) + "\n\t\t\tTMPYPLUS: " + str(tmpy_plus) + "\n\t\t\t\tFRAME: " + str(self.frame_size))

        if tmp_x >= 0 and tmp_y >= 0 and tmp_z >= 0:  # FIRST
            data.tmp_x = tmp_x
            data.tmp_y = tmp_y
            data.tmp_z = tmp_z
            self.n_first(data)

        elif tmp_x < 0 and tmp_y >= 0 and tmp_z >= 0:  # SECOND
            data.tmp_x = tmp_x
            data.tmp_y = tmp_y
            self.n_second(data)

        elif tmp_x < 0 and tmp_y < 0 and tmp_z >= 0:  # THIRD
            data.tmp_x = tmp_x
            data.tmp_y = tmp_y
            data.tmp_z = tmp_z
            self.n_third(data)

        elif tmp_x >= 0 and tmp_y < 0 and tmp_z >= 0:  # FOURTH
            data.tmp_x = tmp_x
            data.tmp_y = tmp_y
            data.tmp_z = tmp_z
            self.n_fourth(data)

        if tmp_x >= 0 and tmp_y >= 0 and tmp_z < 0:  # FIFTH
            print("5")
            data.tmp_x = tmp_x
            data.tmp_y = tmp_y
            data.tmp_z = tmp_z
            self.s_first(data)

        elif tmp_x < 0 and tmp_y >= 0 and tmp_z < 0:  # 6
            print("6")
            data.tmp_x = tmp_x
            data.tmp_y = tmp_y
            data.tmp_z = tmp_z
            self.s_second(data)

        elif tmp_x < 0 and tmp_y < 0 and tmp_z < 0:  # SEVENTH
            print("7")
            data.tmp_x = tmp_x
            data.tmp_y = tmp_y
            data.tmp_z = tmp_z
            self.s_third(data)

        elif tmp_x >= 0 and tmp_y < 0 and tmp_z < 0:  # EIGTH
            print("8")
            data.tmp_x = tmp_x
            data.tmp_y = tmp_y
            data.tmp_z = tmp_z
            self.s_fourth(data)

    def n_first(self, data):
        # print("FIRS   TTTTTTTTTTTTTTT")
        if self._n_kid_one is None:
            # print("new node")
            self._n_kid_one = Node(
                data, self.frame_size / 2, self._gravity_score, data.name,
                False, self.name, self)

        elif self._n_kid_one and self._n_kid_one.is_hub:
            self._n_kid_one.insert2(data)

        else:
            # print("asdf")
            tmp = self._n_kid_one._data
            self._n_kid_one = Node(
                tmp, self.frame_size / 2, self._gravity_score - 1, "HUB -1",
                True, self.name, self)
            self._n_kid_one.insert2(tmp)
            # print("test")
            self._n_kid_one.insert2(data)
            # print("2test")

    def n_second(self, data):
        # print("SECONDDDDDDDDDDDD")

        if self._n_kid_two is None:
            self._n_kid_two = Node(
                data, self.frame_size / 2, self._gravity_score, data.name,
                False, self.name, self)

        elif self._n_kid_two and self._n_kid_two.is_hub:
            self._n_kid_two.insert2(data)
        else:
            tmp = self._n_kid_two._data
            self._n_kid_two = Node(
                tmp, self.frame_size / 2, self._gravity_score, "HUB-2", True,
                self.name, self)
            self._n_kid_two.insert2(tmp)
            self._n_kid_two.insert2(data)

    def n_third(self, data):
        # print("THIRDDDDDDDDDD")

        if self._n_kid_three is None:
            self._n_kid_three = Node(
                data, self.frame_size / 2, self._gravity_score, data.name,
                False, self.name, self)

        elif self._n_kid_three and self._n_kid_three.is_hub:
            self._n_kid_three.insert2(data)

        else:
            tmp = self._n_kid_three._data
            self._n_kid_three = Node(
                tmp, self.frame_size / 2, self._gravity_score - 1, "HUB-3",
                True, self.name, self)
            self._n_kid_three.insert2(tmp)
            self._n_kid_three.insert2(data)

    def n_fourth(self, data):
        # print("FOURTHHHHHHHHHH")

        if self._n_kid_four is None:
            self._n_kid_four = Node(
                data, self.frame_size / 2, self._gravity_score, data.name,
                False, self.name, self)

        elif self._n_kid_four and self._n_kid_four.is_hub:
            self._n_kid_four.insert2(data)

        else:
            tmp = self._n_kid_four._data
            self._n_kid_four = Node(
                tmp, self.frame_size / 2, self._gravity_score, "HUB-4", True,
                self.name, self)
            self._n_kid_four.insert2(tmp)
            self._n_kid_four.insert2(data)

    def s_first(self, data):
        if self._s_kid_one is None:
            self._s_kid_one = Node(
                data, self.frame_size / 2, self.gravity_score, data.name,
                False, self.name, self)
        elif self._s_kid_one and self._s_kid_one.is_hub:
            self._s_kid_one.insert2(data)
        else:
            tmp = self._s_kid_one.data
            self._s_kid_one = Node(
                tmp, self.frame_size / 2, self.gravity_score, "HUB-5", True,
                self.name, self
            )

    def s_second(self, data):
        if self._s_kid_two is None:
            self._s_kid_two = Node(
                data, self.frame_size / 2, self.gravity_score, data.name,
                False, self.name, self
                )
        elif self._s_kid_two and self._s_kid_two.is_hub:
            self._s_kid_two.insert2(data)
        else:
            tmp = self._s_kid_two.data
            self._s_kid_two = Node(
                tmp, self.frame_size / 2, self.gravity_score, "HUB-6", True,
                self.name, self
            )

    def s_third(self, data):
        if self._s_kid_three is None:
            self._s_kid_three = Node(
                data, self.frame_size / 2, self.gravity_score, data.name,
                False, self.name, self
            )
        elif self._s_kid_three and self._s_kid_three.is_hub:
            self._s_kid_three.insert2(data)
        else:
            tmp = self._s_kid_three.data
            self._s_kid_three = Node(
                tmp, self.frame_size / 2, self.gravity_score, "HUB-7", True,
                self.name, self)

    def s_fourth(self, data):
            if self._s_kid_four is None:
                self._s_kid_four = Node(
                    data, self.frame_size / 2, self.gravity_score, data.name,
                    False, self.name, self
                )
            elif self._s_kid_four and self._s_kid_one.is_hub:
                self._s_kid_four.insert2(data)
            else:
                tmp = self._s_kid_four._data
                self.skidfour = Node(
                    tmp, self.frame_size / 2, self.gravity_score, "HUB-8", True,
                    self.name, self)

    def get_coords(self, tmp):
        frame_size = self.frame_size
        tmpx = tmp - frame_size
        if tmpx < -frame_size or tmpx > frame_size:
            tmpx2 = tmp + frame_size
            return tmpx2
        else:
            return tmpx

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

    def traverse():
        pass

    @property
    def gravity_score(self):
        return self._gravity_score

    @gravity_score.setter
    def gravity_score(self, value):
        self._gravity_score = value