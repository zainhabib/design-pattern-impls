class FileWithLogging:
    def __init__(self, file):
        self.file = file

    def writelines(self, lines: list[str]):
        self.file.writelines(lines)
        print(f"wrote {len(lines)} lines")

    def __iter__(self):
        self.file.__iter__()

    def __next__(self):
        self.file.__next__()

    def __getattr__(self, item):
        print(f"------ getttr called, {item=}")
        return getattr(self.__dict__["file"], item)

    def __setattr__(self, key, value):
        if key == 'file':
            self.__dict__["file"] = value
        else:
            setattr(self.__dict__["file"], key, value)

    def __delitem__(self, item):
        delattr(self.__dict__["file"], item)


if __name__ == '__main__':
    file = FileWithLogging(open("hello.txt", "w"))
    file.writelines(["hello", "world"])
    file.write("testing")
    closer = file.close
    closer()
