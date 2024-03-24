class Square:
    def __init__(self, a):
        self.a = a

    def get_perimetr(self):
        return 4 * self.a


if __name__ == '__main__':
    s1 = Square(10)
    s2 = Square(20)
    print("Периметр квадрата 1", s1.get_perimetr())
    print("Периметр квадрата 2", s2.get_perimetr())
