def vector_length(x1, y1, x2, y2):
    vec = []
    vec.append(x1 - x2)
    vec.append(y1 - y2)
    return vec
# alg przechodzenia po drzewie
# szerokosc komorki / odleglosc
# 1 dla kazdego punktu policzyc
# 2 zaktualizowac pozycje
# 3 zbudowac nowe drzewo


def traverse(root):
    if root._n_kid_one is not None:
        print("n1")
        traverse(root._n_kid_one)
    elif root._n_kid_two is not None:
        print("n2")
        traverse(root._n_kid_two)
    elif root._n_kid_three is not None:
        print("n3")
        traverse(root._n_kid_three)
    elif root.n_kid_four is not None:
        print("n4")
        traverse(root.n_kid_four)
    elif root._s_kid_one is not None:
        print("n1")
        traverse(root._s_kid_one)
    elif root._s_kid_two is not None:
        print("n2")
        traverse(root._s_kid_two)
    elif root._s_kid_three is not None:
        print("n3")
        traverse(root._s_kid_three)
    elif root._s_kid_four is not None:
        print("n4")
        traverse(root._s_kid_four)
    else:
        print("elo")


def calculate(*args):
    pass
