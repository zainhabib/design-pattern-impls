from math import sin, cos


# class CoordinateSystem(Enum):
#     CARTESIAN = 1
#     POLAR = 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"(x:{self.x}, y:{self.y})"

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))
