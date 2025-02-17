class Bitmap:
    def __init__(self, filename):
        self.filename = filename
        print(f"Loading image from {self.filename}")

    def draw(self):
        print(f"Drawing image {self.filename}")


class LazyBitmap:
    def __init__(self, filename: str):
        self.filename = filename
        self._bitmap = None

    def draw(self):
        if not self._bitmap:
            self._bitmap = Bitmap(self.filename)
        self._bitmap.draw()


def draw_image(image: Bitmap):
    print("About to draw image.")
    image.draw()
    print("Done drawing image.")


def main():
    bmp = Bitmap("facepalm.jpg")
    draw_image(bmp)

    print("------------------------")

    bmp = LazyBitmap("facepalm.jpg")
    draw_image(bmp)
    print("------------------------")
    draw_image(bmp)


if __name__ == "__main__":
    main()
