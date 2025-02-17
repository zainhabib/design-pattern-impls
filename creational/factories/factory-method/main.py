#from points import Point
from points_with_factory import PointsFactory

if __name__ == '__main__':
    # p = Point(1, 2)
    # p = Point.new_cartesian_point(1, 2)
    # print(p)
    # pp = Point.new_polar_point(2, 3)
    # print(pp)
    p = PointsFactory.new_cartesian_point(1, 2)
    print(p)
    pp = PointsFactory.new_polar_point(4, 7)
    print(pp)
