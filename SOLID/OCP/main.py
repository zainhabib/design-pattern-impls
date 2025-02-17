# Implements
# Open Close Principle

from product import Product, Color, Size, ProductFilter
from specification import Specification, Filter, ColorSpecification, SizeSpecification, AndSpecification, BetterFilter

if __name__ == '__main__':
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    # OLD (WRONG) Way
    # pf = ProductFilter()
    # print("Green Products (Old/Wrong):")
    # for p in pf.filter_by_color(products, Color.GREEN):
    #     print(f" - {p.name} is green")

    bf = BetterFilter()
    print("Green products in new(Good) way:")
    greenSpec = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, greenSpec):
        print(f" - {p.name} is green")

    print("Large products:")
    large_spec = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large_spec):
        print(f" - {p.name} is large")

    print(f"Large Blue products:")
    large_blue = AndSpecification(large_spec, ColorSpecification(Color.BLUE))
    for p in bf.filter(products, large_blue):
        print(f" - {p.name} is large and blue")

    # Using syntactic sugar
    print(f"Large Blue products (Same with 'and' syntactic sugar")
    large_blue = large_spec and ColorSpecification(Color.BLUE)
    for p in bf.filter(products, large_blue):
        print(f" - {p.name} is large and blue")