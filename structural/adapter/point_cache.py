class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def draw_point(p):
    print(".", end=" ")

# ^^ Yuo are given this API

# VV


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end



class Rectagle(list):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x+width, y)))
        self.append(Line(Point(x+width, y), Point(x+width, y+height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y+height), Point(x+width, y+height)))


class LineToPointAdapter:
    cache = {}

    def __init__(self, line):
        self.h = hash(line)
        if self.h in self.cache:
            return

        super().__init__()

        print(f"Generating point for line"
              f"[{line.start.x}, {line.start.y}]"
              f"[{line.end.x}, {line.end.y}]")

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = max(line.start.y, line.end.y)
        bottom = min(line.start.y, line.end.y)

        points = []

        if right - left == 0:
            for y in range(top, bottom):
                points.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                points.append(Point(x, top))

        self.cache[self.h] = points

    def __iter__(self):
        return iter(self.cache[self.h])

def draw(rcs):
    print("\n\n --- Drawing some stuff ---\n")
    for rc in rcs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            # print("for p in adapter")
            for p in adapter:
                # print("p: ", p)
                draw_point(p)


if __name__ == '__main__':
    rcs = [
        Rectagle(1, 1, 10, 10),
        Rectagle(3, 3, 6, 6)
    ]
    draw(rcs)
