# Implements
# LSP: Liskov Substitution Principle
from shape import Rectangle, Square


def use_it(shape: Rectangle):
    w = shape.width
    shape.height = 10
    expected_area = int(w * 10)
    print(f"Expected an area of {expected_area}, got {shape.area}")


if __name__ == '__main__':
    rc = Rectangle(2, 3)
    use_it(rc)

    # Having Square breaks the Liskov Substitution Principle
    sq = Square(5)
    use_it(sq)
