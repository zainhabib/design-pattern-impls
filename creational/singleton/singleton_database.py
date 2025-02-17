import random


class Database:
    _instance = None
    rand = 0

    def __new__(cls, *args, **kwargs):
        print("__new__")
        print("cls, type: ", cls, type(cls))
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)

        cls.rand = random.randint(1, 101)

        print("cls._instance, type: ", cls._instance, type(cls._instance))
        return cls._instance

    def __init__(self):
        print("__init__")
        self.randi = random.randint(101, 201)
        print("self, type: ", self, type(self))
