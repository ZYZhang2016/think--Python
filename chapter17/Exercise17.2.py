# coding:utf-8


class Point():
    '''a 2-d point
    '''

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '{},{}'.format(self.x, self.y)

    def __add__(self, other):
        if isinstance(other, tuple):
            return self.x + other[0], self.y + other[1]
        if isinstance(other, Point):
            return self.x + other.x, self.y + other.y


def main():
    point1 = Point(3)
    print(point1)
    point2 = (41, 5)
    print(point2)
    print(point1 + point2)


if __name__ == '__main__':
    main()
