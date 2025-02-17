from abc import ABC


class Renderer(ABC):
    def render_circle(self, radius):
        pass

    # render_square(self, width):
    #   pass


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing a circle of radius {radius}")


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing pixels for a circle of radius {radius}")


class Shape:
    def __init__(self, renderer: Renderer):
        self.renderer: Renderer = renderer

    def draw(self): pass
    def resize(self, factor): pass


class Circle(Shape):
    def __init__(self, renderer: Renderer, radius: int):
        super().__init__(renderer)
        self.radius: int = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


if __name__ == '__main__':
    raster = RasterRenderer()
    vector = VectorRenderer()

    circle = Circle(raster, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()


